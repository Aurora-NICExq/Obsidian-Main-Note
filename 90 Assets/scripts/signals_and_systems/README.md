# Signals and Systems diagram scripts

Generate SVGs used by notes under `30 Electrical & Computer Engineering/Signals and Systems/`.

Output for both generators: `90 Assets/diagrams/signals-and-systems/*.svg`.
Notes embed them as `![[ss-….svg]]`.

## generate_tikz.py — TikZ/pgfplots, fully offline (preferred for new figures)

Sources are editable TeX fragments in `sources_tikz/ss-<note-slug>-NN.tex`
(a bare `tikzpicture`, no preamble). Needs only the local TeX Live, so it runs
with no network at all — deliberately **not** tectonic, which downloads packages
on first use.

```bash
cd "90 Assets/scripts/signals_and_systems"
python3 generate_tikz.py            # only rebuilds what changed
python3 generate_tikz.py --only sampling
python3 generate_tikz.py --force
```

Prerequisites: `/Library/TeX/texbin/xelatex` (TeX Live 2026+) and `pdftocairo`
(`brew install poppler`). Intermediates land in `_work/` (gitignored).

Covers the 18 figures added 2026-08-12 for lectures 6 and 9–26.

## generate_all.py — matplotlib (the original 20 figures)

Produced the older `ss-<topic>.svg` files. Needs matplotlib in a venv:

```bash
cd "90 Assets/scripts/signals_and_systems"
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt   # needs network
.venv/bin/python generate_all.py
```

Kept for provenance and for regenerating those 20 figures. New figures should
go through `generate_tikz.py` instead, so the whole pipeline stays offline.

## Gotchas when writing TikZ sources

- Don't `\def` names that collide with TeX primitives (`\dp`, `\wd`, `\ht`) —
  the failure shows up as a baffling "You can't use `\fontchardp' in math mode".
- pgfmath's `?:` evaluates **both** branches, and plain pgfmath overflows above
  ~16384. The `\bwmag{u}{N}` helper in the preamble computes the Butterworth
  magnitude with both branches clamped; use it instead of writing `(x/a)^(2N)`.
- Coordinate arithmetic inside `\foreach` needs the math parser: use the
  `\stemat` helper, or brace the component as `({expr},0)`.
