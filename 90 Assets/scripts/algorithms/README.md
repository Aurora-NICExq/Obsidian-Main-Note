# Algorithms (MIT 6.006) diagram scripts

Generate the SVGs used by notes under `10 Computer Science/Algorithms (CLRS)/`.

Each figure is an editable TeX fragment in `sources/alg-<note-slug>-NN.tex` (a bare
`tikzpicture`, no preamble). `generate_all.py` wraps it in a shared standalone
preamble (xeCJK + PingFang SC, Menlo for `\texttt`, a small palette and node/edge
style set), compiles it, and writes the SVG.

```bash
cd "90 Assets/scripts/algorithms"
python3 generate_all.py            # only rebuilds what changed
python3 generate_all.py --only dijkstra
python3 generate_all.py --force    # rebuild everything
```

**Engine:** TeX Live `xelatex` at `/Library/TeX/texbin` → `pdftocairo -svg` (poppler).
Deliberately **not** `tectonic` — it downloads packages on first use, which breaks
the vault's offline-first rule.

Prerequisites:

```bash
ls /Library/TeX/texbin/xelatex   # TeX Live 2026+
which pdftocairo                 # brew install poppler
```

Output: `90 Assets/diagrams/algorithms/alg-*.svg`
Source stem == output stem. Intermediates land in `_work/` (gitignored).

## Gotchas when writing TikZ sources

- **`\foreach` variable names**: `\a \b \c \d \i \r \t \v \u \H \L \O` and friends are
  TeX accent/primitive commands. Binding them in `\foreach` clobbers the primitives and
  produces errors far from the real cause ("Extra }, or forgotten $"). Use `\va`, `\rw`,
  `\lbl`, `\vv` … instead.
- **No `\\` inside `$…$`**: a line break must sit between two separate math groups —
  `$a=b,$\\$\quad c=d$`, not `$a=b,\\ \quad c=d$`.
- **Don't name a tikz style `node`** — it collides with the path-syntax keyword. The
  vertex style here is `vtx`.
- **No Obsidian syntax in sources**: `[[Foo]]` renders literally into the SVG.
- Table columns whose text can be long need an explicit `text width=…`; otherwise the
  cell grows and overlaps its neighbour.
