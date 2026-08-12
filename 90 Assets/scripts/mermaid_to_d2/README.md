# Mermaid → D2 → SVG

Converts Obsidian ` ```mermaid ` fences to **D2**, renders with `d2`, embeds `![[d2-….svg]]`.

## Prerequisites

```bash
brew install d2
# optional better layout:
# d2 uses ELK when available via --layout=elk
```

## Usage

```bash
python3 "90 Assets/scripts/mermaid_to_d2/convert_all.py" --dry-run
python3 "90 Assets/scripts/mermaid_to_d2/convert_all.py" --only FreeRTOS
python3 "90 Assets/scripts/mermaid_to_d2/convert_all.py"
```

Generated `.d2` sources (for tweaking): `sources/`  
SVG output: `90 Assets/diagrams/<area>/d2-*.svg`

Supports: `flowchart` / `graph`, `stateDiagram-v2`, `sequenceDiagram` (best-effort).
