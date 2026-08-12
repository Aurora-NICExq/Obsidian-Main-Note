#!/usr/bin/env python3
"""Generate SVGs for the Electronic Circuits I notes.

Each figure lives as an editable TeX fragment in `sources/ec-<slug>-NN.tex`
(a bare `tikzpicture` / `circuitikz` environment, no preamble). This script
wraps each one in a shared standalone preamble, compiles with local TeX Live
`xelatex`, and converts the PDF to SVG with `pdftocairo`.

Fully offline: uses `/Library/TeX/texbin` only — never `tectonic`, which
fetches packages over the network.

Usage:
  python3 generate_all.py
  python3 generate_all.py --only common-emitter
  python3 generate_all.py --force        # ignore the up-to-date check

Outputs to: 90 Assets/diagrams/electronic-circuits/
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
VAULT = HERE.parents[2]  # …/90 Assets/scripts/electronic_circuits -> vault root
SOURCES = HERE / "sources"
OUT = VAULT / "90 Assets" / "diagrams" / "electronic-circuits"
WORK = HERE / "_work"

# Make TeX Live visible when launched from a GUI/agent shell
TEXBIN = Path("/Library/TeX/texbin")
if TEXBIN.is_dir():
    os.environ["PATH"] = f"{TEXBIN}{os.pathsep}{os.environ.get('PATH', '')}"

PREAMBLE = r"""
\documentclass[border=4pt]{standalone}
\usepackage{fontspec}
\usepackage{xeCJK}
\setCJKmainfont{PingFang SC}
\usepackage{amsmath,amssymb}
\usepackage[siunitx, RPvoltages]{circuitikz}
\usetikzlibrary{arrows.meta,arrows,positioning,calc,shapes.geometric,shapes.misc,fit,backgrounds,patterns,decorations.pathmorphing,decorations.pathreplacing,intersections}

% Shared palette — matches the Signals and Systems matplotlib generator
\definecolor{ecblue}{HTML}{2F5F8F}
\definecolor{ecteal}{HTML}{2A7A6B}
\definecolor{ecred}{HTML}{A33B3B}
\definecolor{ecgray}{HTML}{666666}
\definecolor{eclight}{HTML}{AAAAAA}

\ctikzset{bipoles/length=1.0cm, font=\small}
\tikzset{
  ax/.style={ecgray, -{Stealth[length=5pt]}, line width=0.7pt},
  curve/.style={ecblue, line width=1.1pt},
  curve2/.style={ecred, line width=1.1pt},
  curve3/.style={ecteal, line width=1.1pt},
  helper/.style={eclight, dashed, line width=0.6pt},
  note/.style={ecgray, font=\footnotesize},
}
\begin{document}
"""

POSTAMBLE = "\n\\end{document}\n"


def compile_one(tex_src: Path, out_svg: Path, force: bool) -> tuple[bool, str]:
    if (
        not force
        and out_svg.exists()
        and out_svg.stat().st_mtime >= tex_src.stat().st_mtime
    ):
        return True, "up-to-date"

    WORK.mkdir(parents=True, exist_ok=True)
    stem = tex_src.stem
    job = WORK / f"{stem}.tex"
    job.write_text(
        PREAMBLE + tex_src.read_text(encoding="utf-8").strip() + POSTAMBLE,
        encoding="utf-8",
    )

    pdf = WORK / f"{stem}.pdf"
    if pdf.exists():
        pdf.unlink()

    log = ""
    try:
        for _ in range(2):  # second pass settles circuitikz label positions
            r = subprocess.run(
                [
                    "xelatex",
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    f"-output-directory={WORK}",
                    str(job),
                ],
                capture_output=True,
                text=True,
                timeout=180,
                cwd=str(WORK),
            )
            log = r.stdout or r.stderr
    except subprocess.TimeoutExpired:
        return False, "xelatex timeout"

    if not pdf.exists():
        # surface the first real TeX error rather than the whole log
        lines = [ln for ln in log.splitlines() if ln.startswith("!")]
        return False, "\n".join(lines[:5]) or log[-800:]

    out_svg.parent.mkdir(parents=True, exist_ok=True)
    r2 = subprocess.run(
        ["pdftocairo", "-svg", str(pdf), str(out_svg)],
        capture_output=True,
        text=True,
        timeout=60,
    )
    if not out_svg.exists():
        return False, (r2.stderr or r2.stdout or "pdftocairo produced no svg")[-500:]
    return True, "ok"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--only", default="", help="substring filter on the source stem")
    ap.add_argument("--force", action="store_true", help="rebuild even if up to date")
    args = ap.parse_args()

    for tool in ("xelatex", "pdftocairo"):
        if not shutil.which(tool):
            print(
                f"need {tool} on PATH "
                f"({'TeX Live' if tool == 'xelatex' else 'brew install poppler'})",
                file=sys.stderr,
            )
            sys.exit(1)

    srcs = sorted(SOURCES.glob("*.tex"))
    if args.only:
        srcs = [p for p in srcs if args.only in p.stem]
    if not srcs:
        print("no sources matched", file=sys.stderr)
        sys.exit(1)

    ok = skipped = 0
    failures: list[tuple[str, str]] = []
    for src in srcs:
        out_svg = OUT / f"{src.stem}.svg"
        good, info = compile_one(src, out_svg, args.force)
        if good and info == "up-to-date":
            skipped += 1
            continue
        if good:
            ok += 1
            print(f"  ok      {src.stem}.svg")
        else:
            failures.append((src.stem, info))
            print(f"  FAIL    {src.stem}: {info.splitlines()[0] if info else ''}")

    print(f"\nbuilt={ok} up-to-date={skipped} failed={len(failures)}")
    if failures:
        print("\n--- failures ---")
        for stem, info in failures:
            print(f"\n[{stem}]\n{info}")
        sys.exit(2)


if __name__ == "__main__":
    main()
