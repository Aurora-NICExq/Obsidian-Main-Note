#!/usr/bin/env python3
"""Generate SVGs for Computer Organization and Architecture (MIT 6.004)."""

from __future__ import annotations

from pathlib import Path
from math import comb

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import (
    Circle,
    FancyBboxPatch,
    FancyArrowPatch,
    Rectangle,
    FancyBboxPatch as FBox,
    Arc,
    Polygon,
)

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "90 Assets" / "diagrams" / "computer-architecture"
BLUE, TEAL, RED, ORANGE, GRAY, LIGHT = "#2f5f8f", "#2a7a6b", "#a33b3b", "#c47a2c", "#666666", "#aaaaaa"
SHADE, SHADE2 = "#d6e4f0", "#f0e6d6"


def setup():
    plt.rcParams.update(
        {
            "font.size": 11,
            "axes.unicode_minus": False,
            "mathtext.fontset": "dejavusans",
            "svg.fonttype": "none",
            "axes.linewidth": 1.1,
        }
    )
    OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name: str):
    fig.savefig(OUT / name, format="svg", bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    print("wrote", name)


def box(ax, x, y, w, h, text, fc=SHADE, ec=BLUE, fs=10):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08", facecolor=fc, edgecolor=ec, lw=1.3))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=ec)


def arrow(ax, x0, y0, x1, y1, c=ORANGE, lw=1.4):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0), arrowprops=dict(arrowstyle="-|>", color=c, lw=lw, mutation_scale=11))


def fig_moc():
    fig, ax = plt.subplots(figsize=(9.6, 3.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3.5)
    ax.axis("off")
    items = [
        (0.15, 1.8, "Bits &\nLogic"),
        (2.1, 1.8, "FSM &\nPerformance"),
        (4.05, 1.8, "ISA &\nAssembly"),
        (6.0, 1.8, "CPU &\nPipeline"),
        (7.95, 1.8, "Memory &\nSystems"),
    ]
    for i, (x, y, t) in enumerate(items):
        box(ax, x, y, 1.7, 1.2, t, SHADE if i % 2 == 0 else SHADE2)
        if i < len(items) - 1:
            arrow(ax, x + 1.75, y + 0.6, items[i + 1][0] - 0.05, y + 0.6)
    ax.set_title("MIT 6.004 Computer Organization roadmap", fontsize=13)
    save(fig, "coa-moc-roadmap.svg")


def fig_bits_levels():
    fig, ax = plt.subplots(figsize=(5.2, 4.2))
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 6)
    ax.axis("off")
    levels = [
        (0.6, 4.8, "Application / OS"),
        (0.6, 3.7, "ISA / Assembly"),
        (0.6, 2.6, "Datapath / Control"),
        (0.6, 1.5, "Gates / Flip-flops"),
        (0.6, 0.4, "CMOS / Voltage levels"),
    ]
    for i, (x, y, t) in enumerate(levels):
        box(ax, x, y, 3.8, 0.85, t, SHADE if i % 2 == 0 else SHADE2)
        if i < len(levels) - 1:
            arrow(ax, 2.5, y, 2.5, levels[i + 1][1] + 0.85, GRAY, 1.1)
    ax.set_title("Abstraction layers", fontsize=12)
    save(fig, "coa-abstraction-layers.svg")


def fig_combinational():
    fig, ax = plt.subplots(figsize=(6.0, 3.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")
    box(ax, 0.4, 1.3, 1.6, 1.4, "A\nB", SHADE)
    # triangle-ish gate box
    box(ax, 3.5, 1.3, 2.2, 1.4, "Combinational\nLogic", SHADE2, TEAL)
    box(ax, 7.5, 1.3, 1.8, 1.4, "Y", SHADE, RED)
    arrow(ax, 2.1, 2.0, 3.4, 2.0)
    arrow(ax, 5.8, 2.0, 7.4, 2.0)
    ax.text(4.6, 3.2, r"$Y=f(A,B)$  (no internal state)", color=GRAY, ha="center", fontsize=10)
    ax.set_title("Combinational circuit", fontsize=12)
    save(fig, "coa-combinational.svg")


def fig_sequential_fsm():
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")
    box(ax, 3.2, 3.2, 3.4, 1.0, "Next-state / Output logic", SHADE2, TEAL)
    box(ax, 3.2, 0.8, 3.4, 1.2, "State register\n(flip-flops)", SHADE, BLUE)
    arrow(ax, 4.9, 3.2, 4.9, 2.1)
    arrow(ax, 5.5, 2.0, 5.5, 3.2, ORANGE)
    ax.text(5.7, 2.5, "clk", color=ORANGE, fontsize=9)
    arrow(ax, 1.2, 1.4, 3.1, 1.4, GRAY)
    ax.text(0.3, 1.3, "inputs", color=GRAY, fontsize=9)
    arrow(ax, 6.7, 3.7, 8.8, 3.7, GRAY)
    ax.text(8.9, 3.6, "outputs", color=GRAY, fontsize=9)
    ax.set_title("Sequential system / FSM skeleton", fontsize=12)
    save(fig, "coa-fsm.svg")


def fig_isa():
    fig, ax = plt.subplots(figsize=(6.8, 3.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")
    # instruction word fields
    fields = [(0.4, "opcode"), (2.4, "Ra"), (3.8, "Rb"), (5.2, "Rc"), (6.6, "literal")]
    widths = [1.8, 1.2, 1.2, 1.2, 2.6]
    x = 0.4
    for (w, (_, lab)) in zip(widths, fields):
        box(ax, x, 1.5, w, 1.2, lab, SHADE if int(x) % 2 == 0 else SHADE2)
        x += w + 0.05
    ax.text(5, 3.2, "Example RISC instruction encoding (Beta-style)", ha="center", color=GRAY, fontsize=10)
    ax.set_title("Instruction Set Architecture fields", fontsize=12)
    save(fig, "coa-isa-format.svg")


def fig_stack_frame():
    fig, ax = plt.subplots(figsize=(4.6, 4.8))
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 7)
    ax.axis("off")
    rows = [
        (5.5, "higher addresses"),
        (4.5, "caller frame"),
        (3.5, "saved FP / RA"),
        (2.5, "locals / spills"),
        (1.5, "outgoing args"),
        (0.5, "lower addresses\n(stack grows down)"),
    ]
    for i, (y, t) in enumerate(rows[1:-1], start=1):
        box(ax, 1.0, y, 3.0, 0.85, t, SHADE if i % 2 else SHADE2)
    ax.text(2.5, 5.7, rows[0][1], ha="center", color=GRAY, fontsize=9)
    ax.text(2.5, 0.55, rows[-1][1], ha="center", color=GRAY, fontsize=9)
    ax.annotate("", xy=(4.3, 1.4), xytext=(4.3, 4.3), arrowprops=dict(arrowstyle="<->", color=ORANGE, lw=1.4))
    ax.text(4.45, 2.8, "SP/FP", color=ORANGE, fontsize=9, rotation=90, va="center")
    ax.set_title("Procedure stack frame", fontsize=12)
    save(fig, "coa-stack-frame.svg")


def fig_single_cycle():
    fig, ax = plt.subplots(figsize=(7.2, 4.0))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis("off")
    box(ax, 0.3, 2.2, 1.8, 1.6, "PC", SHADE)
    box(ax, 2.6, 2.2, 2.0, 1.6, "I-Mem", SHADE2, TEAL)
    box(ax, 5.2, 2.2, 2.2, 1.6, "RegFile", SHADE)
    box(ax, 8.0, 2.2, 1.8, 1.6, "ALU", SHADE2, TEAL)
    box(ax, 10.2, 2.2, 1.5, 1.6, "D-Mem", SHADE, RED)
    for x0, x1 in [(2.2, 2.55), (4.7, 5.15), (7.5, 7.95), (9.9, 10.15)]:
        arrow(ax, x0, 3.0, x1, 3.0)
    box(ax, 4.5, 4.5, 3.0, 0.9, "Control", SHADE2, ORANGE)
    arrow(ax, 6.0, 4.5, 6.0, 3.9, ORANGE)
    ax.set_title("Single-cycle datapath (schematic)", fontsize=12)
    save(fig, "coa-single-cycle.svg")


def fig_pipeline():
    fig, ax = plt.subplots(figsize=(7.4, 3.2))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 3.5)
    ax.axis("off")
    stages = ["IF", "ID", "EX", "MEM", "WB"]
    for i, s in enumerate(stages):
        box(ax, 0.4 + i * 2.1, 1.1, 1.7, 1.3, s, SHADE if i % 2 == 0 else SHADE2)
        if i < 4:
            arrow(ax, 0.4 + i * 2.1 + 1.75, 1.75, 0.4 + (i + 1) * 2.1 - 0.05, 1.75)
    ax.text(5.5, 2.8, "5-stage pipeline", ha="center", color=GRAY, fontsize=10)
    ax.set_title("Pipelined processor stages", fontsize=12)
    save(fig, "coa-pipeline.svg")


def fig_pipeline_hazard():
    fig, ax = plt.subplots(figsize=(7.0, 3.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")
    box(ax, 0.5, 3.2, 4.0, 1.0, "add r1, r2, r3", SHADE)
    box(ax, 0.5, 1.6, 4.0, 1.0, "sub r4, r1, r5", SHADE2, TEAL)
    ax.text(5.2, 3.5, "produces r1 in WB", color=GRAY, fontsize=9)
    ax.text(5.2, 1.9, "needs r1 in EX", color=GRAY, fontsize=9)
    arrow(ax, 4.6, 3.5, 4.6, 2.7, RED)
    ax.text(4.8, 2.9, "RAW hazard", color=RED, fontsize=10)
    box(ax, 6.5, 2.2, 3.0, 1.2, "fix:\nstall / forward", SHADE2, ORANGE)
    ax.set_title("Data hazard example", fontsize=12)
    save(fig, "coa-hazard.svg")


def fig_cache():
    fig, ax = plt.subplots(figsize=(6.8, 3.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")
    box(ax, 0.4, 1.8, 2.0, 1.6, "CPU", SHADE)
    box(ax, 3.2, 1.8, 2.4, 1.6, "Cache", SHADE2, TEAL)
    box(ax, 6.6, 1.8, 2.8, 1.6, "Main Memory", SHADE, RED)
    arrow(ax, 2.5, 2.8, 3.1, 2.8)
    arrow(ax, 5.7, 2.8, 6.5, 2.8)
    ax.text(4.4, 3.7, "hit: fast", color=TEAL, ha="center", fontsize=9)
    ax.text(6.0, 1.2, "miss: fetch block", color=RED, ha="center", fontsize=9)
    ax.set_title("Memory hierarchy: cache", fontsize=12)
    save(fig, "coa-cache.svg")


def fig_virtual_memory():
    fig, ax = plt.subplots(figsize=(7.0, 3.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")
    box(ax, 0.4, 2.0, 2.4, 1.6, "Virtual\nAddress", SHADE)
    box(ax, 3.6, 2.0, 2.8, 1.6, "Page Table\n(+ TLB)", SHADE2, TEAL)
    box(ax, 7.2, 2.0, 2.4, 1.6, "Physical\nAddress", SHADE, RED)
    arrow(ax, 2.9, 2.8, 3.5, 2.8)
    arrow(ax, 6.5, 2.8, 7.1, 2.8)
    ax.text(5.0, 4.0, "VPN → PPN translation", ha="center", color=GRAY, fontsize=10)
    ax.set_title("Virtual memory translation", fontsize=12)
    save(fig, "coa-virtual-memory.svg")


def fig_interrupt():
    fig, ax = plt.subplots(figsize=(6.8, 3.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.5)
    ax.axis("off")
    box(ax, 0.5, 2.5, 2.2, 1.2, "User program", SHADE)
    box(ax, 3.8, 2.5, 2.4, 1.2, "Handler / ISR", SHADE2, TEAL)
    box(ax, 7.2, 2.5, 2.2, 1.2, "Device", SHADE, RED)
    arrow(ax, 2.8, 3.1, 3.7, 3.1, ORANGE)
    ax.text(3.1, 3.4, "interrupt", color=ORANGE, fontsize=9)
    arrow(ax, 6.3, 3.1, 7.1, 3.1, GRAY)
    arrow(ax, 5.0, 2.5, 5.0, 1.2, TEAL)
    ax.text(5.2, 1.5, "save/restore context", color=TEAL, fontsize=9)
    ax.set_title("Interrupt / exception path", fontsize=12)
    save(fig, "coa-interrupt.svg")


def fig_parallel():
    fig, ax = plt.subplots(figsize=(6.6, 3.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")
    box(ax, 0.5, 1.3, 2.0, 1.5, "Core 0", SHADE)
    box(ax, 2.8, 1.3, 2.0, 1.5, "Core 1", SHADE2, TEAL)
    box(ax, 5.1, 1.3, 2.0, 1.5, "Core 2", SHADE)
    box(ax, 7.8, 1.3, 1.8, 1.5, "Shared\nMemory", SHADE2, RED)
    for x in [2.5, 4.8, 7.1]:
        arrow(ax, x, 2.0, x + 0.25 if x < 7 else 7.7, 2.0, GRAY)
    ax.set_title("Multicore shared-memory sketch", fontsize=12)
    save(fig, "coa-parallel.svg")


def fig_performance():
    fig, ax = plt.subplots(figsize=(5.6, 3.4))
    labels = ["CPI", "Cycle\ntime", "Inst\ncount"]
    vals = [1.2, 0.8, 1.0]
    colors = [BLUE, TEAL, ORANGE]
    ax.bar(labels, vals, color=colors, width=0.55)
    ax.set_ylabel("relative factor")
    ax.set_title(r"CPU time $\propto$ IC $\times$ CPI $\times$ $T_{clk}$", fontsize=12)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    save(fig, "coa-performance.svg")


def main():
    setup()
    fig_moc()
    fig_bits_levels()
    fig_combinational()
    fig_sequential_fsm()
    fig_isa()
    fig_stack_frame()
    fig_single_cycle()
    fig_pipeline()
    fig_pipeline_hazard()
    fig_cache()
    fig_virtual_memory()
    fig_interrupt()
    fig_parallel()
    fig_performance()
    print("done")


if __name__ == "__main__":
    main()
