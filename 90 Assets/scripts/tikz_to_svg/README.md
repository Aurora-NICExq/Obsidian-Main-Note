# TikZ → SVG converter

Converts Obsidian ` ```tikz ` fences into SVG, then replaces each fence with `![[tikz-….svg]]`.

**Engine:** TeX Live `latexmk -xelatex` / `xelatex` (preferred), fallback `tectonic`.  
**SVG:** `pdftocairo -svg` (poppler).

Outputs: `90 Assets/diagrams/<area>/`

## Prerequisites

```bash
which xelatex    # TeX Live 2026+
which pdftocairo # brew install poppler
# optional fallback:
which tectonic
```

CJK labels: `xeCJK` + PingFang SC (macOS).

## Usage

```bash
python3 "90 Assets/scripts/tikz_to_svg/convert_all.py" --dry-run
python3 "90 Assets/scripts/tikz_to_svg/convert_all.py" --only FreeRTOS
python3 "90 Assets/scripts/tikz_to_svg/convert_all.py"
```

Intermediate files in `_work/` — safe to delete; regenerated as needed.
