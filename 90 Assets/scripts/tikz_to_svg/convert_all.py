#!/usr/bin/env python3
"""Convert all ```tikz blocks in the vault to SVG via local TeX + pdftocairo.

Prefers TeX Live `xelatex` (or `latexmk -xelatex`); falls back to `tectonic`.
Then `pdftocairo -svg`.

Usage:
  python3 convert_all.py
  python3 convert_all.py --dry-run
  python3 convert_all.py --only FreeRTOS
"""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

VAULT = Path(__file__).resolve().parents[3]
DIAGRAMS = VAULT / "90 Assets" / "diagrams"
WORK = VAULT / "90 Assets" / "scripts" / "tikz_to_svg" / "_work"
TIKZ_RE = re.compile(r"```tikz\n(.*?)```", re.DOTALL)

# Ensure TeX Live binaries are visible when launched from GUI/agents
TEXBIN = Path("/Library/TeX/texbin")
if TEXBIN.is_dir():
    os.environ["PATH"] = f"{TEXBIN}{os.pathsep}{os.environ.get('PATH', '')}"

PREAMBLE = r"""
\documentclass[border=4pt]{standalone}
\usepackage{fontspec}
\usepackage{xeCJK}
\setCJKmainfont{PingFang SC}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,arrows,positioning,calc,shapes.geometric,shapes.misc,fit,backgrounds,patterns,decorations.pathmorphing,decorations.pathreplacing}
\begin{document}
"""

POSTAMBLE = r"""
\end{document}
"""


def area_for(path: Path) -> str:
    parts = path.parts
    # map to short area folder names
    s = str(path)
    if "Signals and Systems" in s:
        return "signals-and-systems"
    if "FreeRTOS" in s:
        return "freertos"
    if "stm32" in s:
        return "stm32"
    if "Circuit Theory" in s:
        return "circuit-theory"
    if "Electronics Circuits" in s:
        return "electronic-circuits"
    if "Digital Electronics" in s:
        return "digital-electronics"
    if "Data Structures" in s:
        return "data-structures"
    if "Linear Algebra" in s:
        return "linear-algebra"
    if "Multivariable Calculus" in s:
        return "multivariable-calculus"
    if "Calculus" in s:
        return "calculus"
    if "Linux" in s:
        return "linux"
    if "C Programming" in s:
        return "c-programming"
    if "算法" in s or "Embedded Systems" in s:
        return "embedded"
    return "misc"


def slugify(name: str) -> str:
    base = Path(name).stem
    base = re.sub(r"[^\w\-]+", "-", base, flags=re.UNICODE)
    base = re.sub(r"-+", "-", base).strip("-").lower()
    return base[:50] or "note"


def extract_body(raw: str) -> str:
    body = raw.strip()
    body = re.sub(r"\\begin\{document\}", "", body)
    body = re.sub(r"\\end\{document\}", "", body)
    return body.strip() + "\n"


def compile_tikz(body: str, out_svg: Path) -> tuple[bool, str]:
    WORK.mkdir(parents=True, exist_ok=True)
    key = hashlib.sha1(body.encode("utf-8")).hexdigest()[:12]
    tex_path = WORK / f"{key}.tex"
    pdf_path = WORK / f"{key}.pdf"
    tex_path.write_text(PREAMBLE + body + POSTAMBLE, encoding="utf-8")

    err_log = ""
    compiled = False

    # Prefer local TeX Live
    if shutil.which("latexmk"):
        try:
            r = subprocess.run(
                [
                    "latexmk",
                    "-xelatex",
                    "-interaction=nonstopmode",
                    f"-outdir={WORK}",
                    str(tex_path),
                ],
                capture_output=True,
                text=True,
                timeout=180,
                cwd=str(WORK),
            )
            err_log = r.stderr or r.stdout
            compiled = pdf_path.exists()
        except subprocess.TimeoutExpired:
            err_log = "latexmk timeout"
    elif shutil.which("xelatex"):
        try:
            for _ in range(2):
                r = subprocess.run(
                    [
                        "xelatex",
                        "-interaction=nonstopmode",
                        f"-output-directory={WORK}",
                        str(tex_path),
                    ],
                    capture_output=True,
                    text=True,
                    timeout=180,
                )
                err_log = r.stderr or r.stdout
            compiled = pdf_path.exists()
        except subprocess.TimeoutExpired:
            err_log = "xelatex timeout"

    # Fallback: tectonic
    if not compiled and shutil.which("tectonic"):
        try:
            r = subprocess.run(
                ["tectonic", "-X", "compile", "--outdir", str(WORK), str(tex_path)],
                capture_output=True,
                text=True,
                timeout=180,
            )
            err_log = r.stderr or r.stdout
            compiled = pdf_path.exists()
        except subprocess.TimeoutExpired:
            return False, "timeout"

    if not compiled:
        return False, (err_log or "pdf not produced")[-2000:]

    out_svg.parent.mkdir(parents=True, exist_ok=True)
    tmp_svg = WORK / f"{key}.svg"
    r2 = subprocess.run(
        ["pdftocairo", "-svg", str(pdf_path), str(tmp_svg)],
        capture_output=True,
        text=True,
        timeout=60,
    )
    produced = tmp_svg
    if not produced.exists():
        candidates = sorted(WORK.glob(f"{key}*.svg"))
        if not candidates:
            return False, (r2.stderr or r2.stdout or "no svg")[-2000:]
        produced = candidates[0]

    shutil.copy2(produced, out_svg)
    return True, "ok"


def process_file(path: Path, dry_run: bool = False) -> tuple[int, int]:
    text = path.read_text(encoding="utf-8")
    matches = list(TIKZ_RE.finditer(text))
    if not matches:
        return 0, 0

    area = area_for(path)
    slug = slugify(path.name)
    out_dir = DIAGRAMS / area
    ok = fail = 0
    # replace from end so indices stay valid
    new_text = text
    indexed = list(enumerate(matches, 1))
    for block_index, m in reversed(indexed):
        body = extract_body(m.group(1))
        fname = f"tikz-{slug}-{block_index:02d}.svg"
        out_svg = out_dir / fname
        embed = f"![[{fname}]]"

        if dry_run:
            print(f"  would convert block {block_index} -> {area}/{fname}")
            ok += 1
            continue

        print(f"  [{path.relative_to(VAULT)}] block {block_index} -> {fname} ...", flush=True)
        success, info = compile_tikz(body, out_svg)
        if success:
            new_text = new_text[: m.start()] + embed + new_text[m.end() :]
            ok += 1
            print("    ok")
        else:
            fail += 1
            print(f"    FAIL: {info[:300]}")

    if not dry_run and ok and new_text != text:
        # Only write if we replaced something — but if some failed, still write successful replacements
        path.write_text(new_text, encoding="utf-8")
    return ok, fail


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--only", type=str, default="", help="substring filter on path")
    args = ap.parse_args()

    if not shutil.which("pdftocairo"):
        print("need pdftocairo on PATH (brew install poppler)", file=sys.stderr)
        sys.exit(1)
    if not (shutil.which("xelatex") or shutil.which("latexmk") or shutil.which("tectonic")):
        print("need xelatex/latexmk (TeX Live) or tectonic on PATH", file=sys.stderr)
        sys.exit(1)

    md_files = sorted(VAULT.rglob("*.md"))
    total_ok = total_fail = 0
    for p in md_files:
        if any(x in p.parts for x in (".obsidian", ".venv", "node_modules", "_work")):
            continue
        if args.only and args.only not in str(p):
            continue
        text = p.read_text(encoding="utf-8", errors="ignore")
        if "```tikz" not in text:
            continue
        print(f"## {p.relative_to(VAULT)}")
        o, f = process_file(p, dry_run=args.dry_run)
        total_ok += o
        total_fail += f

    print(f"\nDone. ok={total_ok} fail={total_fail}")
    if total_fail:
        sys.exit(2)


if __name__ == "__main__":
    main()
