# Electronic Circuits I diagram scripts

Generate the SVGs used by notes under
`30 Electrical & Computer Engineering/Electronics Circuits/`.

Each figure is an editable TeX fragment in `sources/` — a bare `circuitikz` or
`tikzpicture` environment, no preamble. `generate_all.py` wraps it in a shared
standalone preamble (xeCJK + PingFang SC, circuitikz, a small colour/style set),
compiles it, and writes the SVG.

```bash
cd "90 Assets/scripts/electronic_circuits"
python3 generate_all.py            # only rebuilds what changed
python3 generate_all.py --only common-emitter
python3 generate_all.py --force    # rebuild everything
```

**Engine:** TeX Live `xelatex` at `/Library/TeX/texbin` → `pdftocairo -svg` (poppler).
Deliberately **not** `tectonic` — it downloads packages on first use, which breaks
the vault's offline-first rule.

Prerequisites:

```bash
ls /Library/TeX/texbin/xelatex   # TeX Live 2026+, ships circuitikz
which pdftocairo                 # brew install poppler
```

Output: `90 Assets/diagrams/electronic-circuits/ec-*.svg`
Notes embed them as `![[ec-….svg]]`.

Source stem == output stem: `sources/ec-common-emitter-stage-01.tex` →
`ec-common-emitter-stage-01.svg`. Intermediate files land in `_work/` (gitignored,
safe to delete).
