#!/usr/bin/env python3
"""Generate the TikZ/pgfplots SVGs for the Signals and Systems notes.

Companion to `generate_all.py` (matplotlib). That script produced the original
20 `ss-<topic>.svg` figures but needs matplotlib installed; this one needs only
the local TeX Live, so it works with no network at all — which is why every
figure added from 2026-08-12 on lives here.

Each figure is an editable TeX fragment in `sources_tikz/ss-<slug>-NN.tex`
(a bare `tikzpicture` / `axis` environment, no preamble). This script wraps it
in a shared standalone preamble, compiles with `xelatex`, and converts to SVG
with `pdftocairo`.

Usage:
  python3 generate_tikz.py
  python3 generate_tikz.py --only sampling
  python3 generate_tikz.py --force

Outputs to: 90 Assets/diagrams/signals-and-systems/
"""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
VAULT = HERE.parents[2]
SOURCES = HERE / "sources_tikz"
OUT = VAULT / "90 Assets" / "diagrams" / "signals-and-systems"
WORK = HERE / "_work"

TEXBIN = Path("/Library/TeX/texbin")
if TEXBIN.is_dir():
    os.environ["PATH"] = f"{TEXBIN}{os.pathsep}{os.environ.get('PATH', '')}"

# Palette matches generate_all.py so the two generators are visually indistinguishable
PREAMBLE = r"""
\documentclass[border=4pt]{standalone}
\usepackage{fontspec}
\usepackage{xeCJK}
\setCJKmainfont{PingFang SC}
\usepackage{amsmath,amssymb}
\usepackage{tikz}
\usepackage{pgfplots}
\pgfplotsset{compat=1.18}
\usetikzlibrary{arrows.meta,arrows,positioning,calc,shapes.geometric,shapes.misc,fit,
                backgrounds,patterns,decorations.pathmorphing,decorations.pathreplacing,
                decorations.markings,intersections}

\definecolor{ssblue}{HTML}{2F5F8F}
\definecolor{ssteal}{HTML}{2A7A6B}
\definecolor{ssred}{HTML}{A33B3B}
\definecolor{ssgray}{HTML}{666666}
\definecolor{sslight}{HTML}{AAAAAA}

\tikzset{
  ax/.style={ssgray, -{Stealth[length=5pt]}, line width=0.8pt},
  curve/.style={ssblue, line width=1.5pt},
  curve2/.style={ssred, line width=1.5pt},
  curve3/.style={ssteal, line width=1.5pt},
  helper/.style={sslight, dashed, line width=0.7pt},
  note/.style={ssgray, font=\footnotesize},
  blk/.style={draw=ssgray, line width=1.0pt, rounded corners=2pt, fill=white,
              minimum width=1.5cm, minimum height=0.9cm, align=center, font=\small},
  sig/.style={-{Stealth[length=5pt]}, ssgray, line width=1.0pt},
}

% One stem of a stem plot: \stemat{color}{x}{height}.
% x and height go through the math parser, so arithmetic like (\k*4+\n)*0.5 works.
\newcommand{\stemat}[3]{%
  \pgfmathsetmacro\stemx{#2}%
  \pgfmathsetmacro\stemy{#3}%
  \draw[#1, line width=1.4pt] (\stemx,0) -- (\stemx,\stemy);
  \filldraw[#1] (\stemx,\stemy) circle (2.1pt);
}

% Butterworth magnitude 1/sqrt(1+u^(2N)) without pgfmath overflow.
% Plain pgfmath tops out near 16384, and u^(2N) blows past that for N>=4.
% For u>1 we use the algebraically identical u^-N/sqrt(1+u^-2N), so no
% intermediate ever exceeds 1.  #1 = u (>=0), #2 = order N.
% pgfmath's ?: evaluates BOTH branches, so each one is clamped to a base in
% [0,1] — otherwise u=0 divides by zero and u>1 overflows.
\newcommand{\bwmag}[2]{%
  ((#1)<1
    ? 1/sqrt(1+pow(min((#1),1),2*(#2)))
    : pow(1/max((#1),1),(#2))/sqrt(1+pow(1/max((#1),1),2*(#2))))%
}

\pgfplotsset{
  ssaxis/.style={
    axis lines=middle,
    axis line style={ssgray, -{Stealth[length=5pt]}, line width=0.8pt},
    tick style={ssgray},
    label style={ssgray, font=\footnotesize},
    tick label style={ssgray, font=\scriptsize},
    every axis plot/.append style={line width=1.4pt},
    clip=false,
  },
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
        for _ in range(2):  # second pass settles pgfplots label positions
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
                timeout=240,
                cwd=str(WORK),
            )
            log = r.stdout or r.stderr
    except subprocess.TimeoutExpired:
        return False, "xelatex timeout"

    if not pdf.exists():
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
