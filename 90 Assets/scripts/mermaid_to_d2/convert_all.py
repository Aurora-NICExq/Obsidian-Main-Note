#!/usr/bin/env python3
"""Convert ```mermaid blocks to D2, render SVG with `d2`, embed ![[…]].

Usage:
  python3 convert_all.py
  python3 convert_all.py --only FreeRTOS
  python3 convert_all.py --dry-run
"""

from __future__ import annotations

import argparse
import hashlib
import re
import shutil
import subprocess
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
DIAGRAMS = VAULT / "90 Assets" / "diagrams"
SRC_DIR = VAULT / "90 Assets" / "scripts" / "mermaid_to_d2" / "sources"
MERMAID_RE = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)

DIRECTION = {
    "TB": "down",
    "TD": "down",
    "BT": "up",
    "LR": "right",
    "RL": "left",
}


def area_for(path: Path) -> str:
    s = str(path)
    mapping = [
        ("FreeRTOS", "freertos"),
        ("stm32", "stm32"),
        ("Digital Electronics", "digital-electronics"),
        ("Book Notes", "book-notes"),
        ("Rust", "rust"),
        ("Linux", "linux"),
        ("Data Structures", "data-structures"),
        ("Signals and Systems", "signals-and-systems"),
    ]
    for key, area in mapping:
        if key in s:
            return area
    return "misc"


def slugify(name: str) -> str:
    base = Path(name).stem
    base = re.sub(r"[^\w\-]+", "-", base, flags=re.UNICODE)
    base = re.sub(r"-+", "-", base).strip("-").lower()
    return base[:50] or "note"


def clean_label(s: str) -> str:
    s = s.strip().strip('"').strip("'")
    s = s.replace("<br/>", "\\n").replace("<br>", "\\n").replace("<br />", "\\n")
    s = s.replace('"', '\\"')
    return s


def parse_node_decl(token: str) -> tuple[str, str | None]:
    token = token.strip()
    m = re.match(r'^([A-Za-z_][\w-]*)\s*\[\s*"([^"]*)"\s*\]$', token)
    if m:
        return m.group(1), clean_label(m.group(2))
    m = re.match(r"^([A-Za-z_][\w-]*)\s*\[\s*([^\]]*)\s*\]$", token)
    if m:
        return m.group(1), clean_label(m.group(2))
    m = re.match(r'^([A-Za-z_][\w-]*)\s*\(\s*"([^"]*)"\s*\)$', token)
    if m:
        return m.group(1), clean_label(m.group(2))
    m = re.match(r"^([A-Za-z_][\w-]*)$", token)
    if m:
        return m.group(1), None
    safe = re.sub(r"[^\w\-]", "_", token) or "n"
    return safe, clean_label(token)


def convert_flowchart(src: str) -> str:
    lines = [ln.rstrip() for ln in src.strip().splitlines() if ln.strip()]
    header = lines[0]
    m = re.match(r"^(?:flowchart|graph)\s+(TB|TD|BT|LR|RL)\b", header, re.I)
    if not m:
        raise ValueError(f"not a flowchart: {header}")
    direction = DIRECTION[m.group(1).upper()]

    # First pass: collect structure
    stack: list[tuple[str, str]] = []  # (id, title)
    containers: dict[str, tuple[str | None, str]] = {}  # id -> (parent, title)
    node_parent: dict[str, str | None] = {}
    node_label: dict[str, str] = {}
    edges: list[tuple[list[str], list[str], str | None, bool]] = []

    def cur_parent() -> str | None:
        return stack[-1][0] if stack else None

    def remember(nid: str, lab: str | None):
        if lab is not None:
            node_label[nid] = lab
        elif nid not in node_label:
            node_label[nid] = nid
        # first declaration wins for parent
        if nid not in node_parent:
            node_parent[nid] = cur_parent()

    for ln in lines[1:]:
        ln = ln.strip()
        if ln.startswith("%%"):
            continue
        sm = re.match(r'^subgraph\s+([A-Za-z_][\w-]*)\s*\[\s*"([^"]*)"\s*\]', ln)
        if sm:
            cid, title = sm.group(1), clean_label(sm.group(2))
            containers[cid] = (cur_parent(), title)
            stack.append((cid, title))
            continue
        sm = re.match(r"^subgraph\s+(.+)$", ln)
        if sm:
            title = clean_label(sm.group(1).strip().strip('"'))
            cid = re.sub(r"[^\w\-]", "_", title) or f"g{len(containers)}"
            containers[cid] = (cur_parent(), title)
            stack.append((cid, title))
            continue
        if ln == "end":
            if stack:
                stack.pop()
            continue

        em = re.match(
            r"^(.+?)\s*(-->|---|-\.-+|==>|-.->)\s*(?:\|([^|]*)\|\s*)?(.+)$",
            ln,
        )
        if em:
            left, arrow, elabel, right = em.group(1), em.group(2), em.group(3), em.group(4)
            dashed = arrow in ("-.->", "-.-+")

            def split_ids(side: str) -> list[str]:
                ids = []
                for p in [x.strip() for x in side.split("&")]:
                    nid, lab = parse_node_decl(p)
                    remember(nid, lab)
                    ids.append(nid)
                return ids

            edges.append((split_ids(left), split_ids(right), clean_label(elabel) if elabel else None, dashed))
            continue

        nid, lab = parse_node_decl(ln)
        if re.match(r"^[A-Za-z_]", ln):
            remember(nid, lab if lab is not None else nid)
            continue

    def ref(nid: str) -> str:
        parent = node_parent.get(nid)
        return f"{parent}.{nid}" if parent else nid

    out: list[str] = [f"direction: {direction}", ""]

    # emit containers nested — only top-level first, children inside
    children: dict[str | None, list[str]] = {}
    for cid, (parent, _) in containers.items():
        children.setdefault(parent, []).append(cid)

    def emit_container(cid: str, indent: int):
        parent, title = containers[cid]
        pad = "  " * indent
        out.append(f'{pad}{cid}: {{')
        out.append(f'{pad}  label: "{title}"')
        # nodes directly in this container
        for nid, p in node_parent.items():
            if p == cid:
                out.append(f'{pad}  {nid}: "{node_label.get(nid, nid)}"')
        for child in children.get(cid, []):
            emit_container(child, indent + 1)
        out.append(f"{pad}}}")

    for cid in children.get(None, []):
        emit_container(cid, 0)

    out.append("")
    # top-level nodes
    for nid, p in node_parent.items():
        if p is None:
            out.append(f'{nid}: "{node_label.get(nid, nid)}"')
    out.append("")

    for left_ids, right_ids, elabel, dashed in edges:
        style = " {style.stroke-dash: 3}" if dashed else ""
        for a in left_ids:
            for b in right_ids:
                if elabel:
                    out.append(f'{ref(a)} -> {ref(b)}: "{elabel}"{style}')
                else:
                    out.append(f"{ref(a)} -> {ref(b)}{style}")

    out.append("")
    return "\n".join(out)


def convert_state_diagram(src: str) -> str:
    shapes: set[str] = set()
    edges: list[str] = []
    for ln in src.splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("stateDiagram") or ln.startswith("%%"):
            continue
        m = re.match(r"^(\[\*\]|[\w]+)\s*-->\s*(\[\*\]|[\w]+)\s*(?::\s*(.*))?$", ln)
        if not m:
            continue
        a, b, lab = m.group(1), m.group(2), m.group(3)
        a = "Start" if a == "[*]" else a
        b = "End" if b == "[*]" else b
        shapes.add(a)
        shapes.add(b)
        if lab:
            edges.append(f'{a} -> {b}: "{clean_label(lab)}"')
        else:
            edges.append(f"{a} -> {b}")
    out = ["direction: down", ""]
    for s in sorted(shapes):
        if s in ("Start", "End"):
            out.append(f'{s}: {{shape: circle; width: 28; height: 28; label: ""}}')
        else:
            out.append(f"{s}: {s}")
    out.append("")
    out.extend(edges)
    out.append("")
    return "\n".join(out)


def convert_sequence(src: str) -> str:
    participants: list[str] = []
    aliases: dict[str, str] = {}
    messages: list[str] = []

    for ln in src.splitlines():
        ln = ln.strip()
        if not ln or ln.startswith("sequenceDiagram") or ln.startswith("%%"):
            continue
        m = re.match(r"^participant\s+(\w+)(?:\s+as\s+(.+))?$", ln)
        if m:
            pid, alias = m.group(1), m.group(2)
            aliases[pid] = clean_label(alias) if alias else pid
            participants.append(pid)
            continue
        if ln.lower().startswith("note "):
            continue
        m = re.match(r"^(\w+)\s*(-->>|->>|--x|->x|-->|->)\s*(\w+)\s*:\s*(.*)$", ln)
        if m:
            a, _arrow, b, msg = m.group(1), m.group(2), m.group(3), clean_label(m.group(4))
            for p in (a, b):
                if p not in aliases:
                    aliases[p] = p
                    participants.append(p)
            messages.append(f'{a} -> {b}: "{msg}"')

    out = ["shape: sequence_diagram", ""]
    for p in participants:
        out.append(f'{p}: "{aliases[p]}"')
    out.append("")
    out.extend(messages)
    out.append("")
    return "\n".join(out)


def mermaid_to_d2(src: str) -> str:
    head = src.strip().splitlines()[0].strip() if src.strip() else ""
    if re.match(r"^(flowchart|graph)\b", head, re.I):
        return convert_flowchart(src)
    if head.startswith("stateDiagram"):
        return convert_state_diagram(src)
    if head.startswith("sequenceDiagram"):
        return convert_sequence(src)
    raise ValueError(f"unsupported mermaid type: {head}")


def render_d2(d2_text: str, out_svg: Path) -> tuple[bool, str]:
    SRC_DIR.mkdir(parents=True, exist_ok=True)
    out_svg.parent.mkdir(parents=True, exist_ok=True)
    key = hashlib.sha1(d2_text.encode()).hexdigest()[:12]
    d2_path = SRC_DIR / f"{key}.d2"
    d2_path.write_text(d2_text, encoding="utf-8")
    for args in (
        ["d2", "--layout=elk", str(d2_path), str(out_svg)],
        ["d2", str(d2_path), str(out_svg)],
    ):
        try:
            r = subprocess.run(args, capture_output=True, text=True, timeout=120)
        except subprocess.TimeoutExpired:
            continue
        if r.returncode == 0 and out_svg.exists():
            return True, "ok"
        err = r.stderr or r.stdout
    return False, (err or "render failed")[-2500:]


def process_file(path: Path, dry_run: bool = False) -> tuple[int, int]:
    text = path.read_text(encoding="utf-8")
    matches = list(MERMAID_RE.finditer(text))
    if not matches:
        return 0, 0
    area = area_for(path)
    slug = slugify(path.name)
    out_dir = DIAGRAMS / area
    ok = fail = 0
    new_text = text
    for block_index, m in reversed(list(enumerate(matches, 1))):
        src = m.group(1)
        fname = f"d2-{slug}-{block_index:02d}.svg"
        out_svg = out_dir / fname
        if dry_run:
            try:
                mermaid_to_d2(src)
                print(f"  would ok block {block_index} -> {area}/{fname}")
                ok += 1
            except Exception as e:
                print(f"  would FAIL block {block_index}: {e}")
                fail += 1
            continue
        print(f"  [{path.relative_to(VAULT)}] #{block_index} -> {fname}", flush=True)
        try:
            d2_text = mermaid_to_d2(src)
        except Exception as e:
            print(f"    CONVERT FAIL: {e}")
            fail += 1
            continue
        success, info = render_d2(d2_text, out_svg)
        if success:
            new_text = new_text[: m.start()] + f"![[{fname}]]" + new_text[m.end() :]
            ok += 1
            print("    ok")
        else:
            fail += 1
            print(f"    RENDER FAIL: {info[:500]}")
    if not dry_run and ok and new_text != text:
        path.write_text(new_text, encoding="utf-8")
    return ok, fail


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", default="")
    args = ap.parse_args()
    if not shutil.which("d2"):
        print("d2 not found; brew install d2", file=sys.stderr)
        sys.exit(1)

    total_ok = total_fail = 0
    for p in sorted(VAULT.rglob("*.md")):
        if any(x in p.parts for x in (".obsidian", ".venv", "node_modules", "_work")):
            continue
        if p.name in ("CLAUDE.md", "README.md"):
            continue
        if args.only and args.only not in str(p):
            continue
        if "```mermaid" not in p.read_text(encoding="utf-8", errors="ignore"):
            continue
        print(f"## {p.relative_to(VAULT)}")
        o, f = process_file(p, dry_run=args.dry_run)
        total_ok += o
        total_fail += f
    print(f"\nDone. ok={total_ok} fail={total_fail}")
    sys.exit(2 if total_fail else 0)


if __name__ == "__main__":
    main()
