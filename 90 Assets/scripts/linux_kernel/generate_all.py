#!/usr/bin/env python3
"""Generate SVGs for Linux Kernel (Bootlin) notes."""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle, Rectangle, FancyArrowPatch

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "90 Assets" / "diagrams" / "linux-kernel"
BLUE, TEAL, RED, ORANGE, GRAY = "#2f5f8f", "#2a7a6b", "#a33b3b", "#c47a2c", "#666666"
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
    ax.add_patch(
        FancyBboxPatch(
            (x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
            facecolor=fc, edgecolor=ec, lw=1.3,
        )
    )
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=ec)


def arrow(ax, x0, y0, x1, y1, c=ORANGE, lw=1.4):
    ax.annotate(
        "",
        xy=(x1, y1),
        xytext=(x0, y0),
        arrowprops=dict(arrowstyle="-|>", color=c, lw=lw, mutation_scale=11),
    )


def fig_moc():
    fig, ax = plt.subplots(figsize=(9.6, 3.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 3.5)
    ax.axis("off")
    items = [
        (0.15, 1.8, "Sources &\nBuild"),
        (2.1, 1.8, "Modules &\nDT/Model"),
        (4.05, 1.8, "Char &\nMM/DMA"),
        (6.0, 1.8, "Process &\nIRQ/Locks"),
        (7.95, 1.8, "Sleep &\nDebug"),
    ]
    for i, (x, y, t) in enumerate(items):
        box(ax, x, y, 1.7, 1.2, t, SHADE if i % 2 == 0 else SHADE2)
        if i < len(items) - 1:
            arrow(ax, x + 1.75, y + 0.6, items[i + 1][0] - 0.05, y + 0.6)
    ax.set_title("Bootlin Linux Kernel roadmap", fontsize=13)
    save(fig, "lk-moc-roadmap.svg")


def fig_kernel_layers():
    fig, ax = plt.subplots(figsize=(5.4, 4.4))
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 6)
    ax.axis("off")
    levels = [
        (0.5, 4.8, "User space (apps, libc)", SHADE2, TEAL),
        (0.5, 3.6, "System call interface", SHADE, BLUE),
        (0.5, 2.4, "Kernel subsystems\n(fs, mm, net, drivers…)", SHADE2, TEAL),
        (0.5, 1.2, "Arch + drivers", SHADE, BLUE),
        (0.5, 0.2, "Hardware", SHADE2, RED),
    ]
    for x, y, t, fc, ec in levels:
        box(ax, x, y, 4.0, 0.95, t, fc, ec, 10)
    ax.set_title("Linux in the system", fontsize=12)
    save(fig, "lk-kernel-layers.svg")


def fig_source_tree():
    fig, ax = plt.subplots(figsize=(6.2, 4.2))
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 6)
    ax.axis("off")
    box(ax, 2.5, 5.0, 3.0, 0.7, "linux/", SHADE, BLUE, 11)
    rows = [
        (0.3, 3.6, "arch/", "CPU arch"),
        (2.1, 3.6, "kernel/", "core"),
        (3.9, 3.6, "mm/", "memory"),
        (5.7, 3.6, "fs/", "VFS"),
        (0.3, 2.2, "drivers/", "devices"),
        (2.1, 2.2, "net/", "network"),
        (3.9, 2.2, "include/", "headers"),
        (5.7, 2.2, "init/", "boot"),
    ]
    for x, y, a, b in rows:
        box(ax, x, y, 1.6, 1.0, f"{a}\n{b}", SHADE2 if "driver" in a or "mm" in a else SHADE, TEAL if "driver" in a else BLUE, 9)
    ax.set_title("Kernel source tree (selected)", fontsize=12)
    save(fig, "lk-source-tree.svg")


def fig_module_lifecycle():
    fig, ax = plt.subplots(figsize=(7.0, 2.8))
    ax.set_xlim(0, 11)
    ax.set_ylim(0, 3)
    ax.axis("off")
    steps = [(0.3, "compile\n.ko"), (2.5, "insmod/\nmodprobe"), (4.7, "init"), (6.5, "running"), (8.5, "exit/\nrmmod")]
    for i, (x, t) in enumerate(steps):
        box(ax, x, 0.9, 1.8, 1.2, t, SHADE if i % 2 == 0 else SHADE2)
        if i < len(steps) - 1:
            arrow(ax, x + 1.85, 1.5, steps[i + 1][0] - 0.05, 1.5)
    ax.set_title("Loadable module lifecycle", fontsize=12)
    save(fig, "lk-module-lifecycle.svg")


def fig_device_model():
    fig, ax = plt.subplots(figsize=(6.8, 3.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")
    box(ax, 3.5, 3.6, 3.0, 1.0, "Bus (platform/I2C/…)", SHADE2, ORANGE)
    box(ax, 0.8, 1.4, 3.0, 1.3, "Device\n(resources)", SHADE, BLUE)
    box(ax, 6.2, 1.4, 3.0, 1.3, "Driver\n(probe/remove)", SHADE2, TEAL)
    arrow(ax, 5.0, 3.6, 2.5, 2.8, GRAY)
    arrow(ax, 5.0, 3.6, 7.5, 2.8, GRAY)
    arrow(ax, 4.0, 2.0, 6.0, 2.0, RED)
    ax.text(5.0, 2.25, "match + probe", color=RED, ha="center", fontsize=9)
    ax.set_title("Linux device / driver model", fontsize=12)
    save(fig, "lk-device-model.svg")


def fig_char_fops():
    fig, ax = plt.subplots(figsize=(6.6, 3.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.5)
    ax.axis("off")
    box(ax, 0.4, 1.6, 2.4, 1.4, "User\nopen/read/…", SHADE2, TEAL)
    box(ax, 3.6, 1.6, 2.8, 1.4, "VFS\nfile_operations", SHADE, BLUE)
    box(ax, 7.2, 1.6, 2.4, 1.4, "Driver\n.cdev", SHADE2, RED)
    arrow(ax, 2.9, 2.3, 3.5, 2.3)
    arrow(ax, 6.5, 2.3, 7.1, 2.3)
    ax.text(5.0, 3.5, "char device path", ha="center", color=GRAY, fontsize=10)
    ax.set_title("Character driver call path", fontsize=12)
    save(fig, "lk-char-fops.svg")


def fig_mm():
    fig, ax = plt.subplots(figsize=(6.4, 3.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.5)
    ax.axis("off")
    box(ax, 0.4, 2.4, 2.8, 1.4, "page allocator\n(buddy)", SHADE, BLUE)
    box(ax, 3.6, 2.4, 2.8, 1.4, "slab/slub\nk*alloc", SHADE2, TEAL)
    box(ax, 6.8, 2.4, 2.8, 1.4, "vmalloc /\nioremap", SHADE, ORANGE)
    box(ax, 2.0, 0.5, 6.0, 1.1, "physical pages / zones", SHADE2, RED)
    arrow(ax, 1.8, 2.4, 3.5, 1.7, GRAY)
    arrow(ax, 5.0, 2.4, 5.0, 1.7, GRAY)
    arrow(ax, 8.2, 2.4, 6.5, 1.7, GRAY)
    ax.set_title("Kernel memory management map", fontsize=12)
    save(fig, "lk-mm.svg")


def fig_dma():
    fig, ax = plt.subplots(figsize=(6.8, 3.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")
    box(ax, 0.4, 1.4, 2.4, 1.4, "CPU", SHADE)
    box(ax, 3.5, 1.4, 3.0, 1.4, "DMA engine /\ncontroller", SHADE2, TEAL)
    box(ax, 7.2, 1.4, 2.4, 1.4, "Device", SHADE, RED)
    arrow(ax, 2.9, 2.3, 3.4, 2.3)
    arrow(ax, 6.6, 2.3, 7.1, 2.3)
    ax.text(5.0, 3.3, "coherent / streaming DMA API", ha="center", color=GRAY, fontsize=10)
    ax.set_title("DMA data path sketch", fontsize=12)
    save(fig, "lk-dma.svg")


def fig_process_states():
    fig, ax = plt.subplots(figsize=(6.6, 3.8))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")
    nodes = {
        "R": (2.0, 3.5, "TASK_RUNNING"),
        "I": (5.0, 3.5, "interruptible\nsleep"),
        "U": (8.0, 3.5, "uninterruptible"),
        "S": (5.0, 1.2, "stopped /\nzombie…"),
    }
    for k, (x, y, t) in nodes.items():
        box(ax, x - 1.1, y - 0.55, 2.2, 1.1, t, SHADE if k != "R" else SHADE2, BLUE if k == "R" else TEAL, 9)
    arrow(ax, 3.2, 3.5, 3.8, 3.5)
    arrow(ax, 6.2, 3.5, 6.8, 3.5)
    arrow(ax, 5.0, 2.9, 5.0, 2.4, ORANGE)
    ax.set_title("Process / task states (simplified)", fontsize=12)
    save(fig, "lk-process-states.svg")


def fig_waitqueue():
    fig, ax = plt.subplots(figsize=(6.4, 3.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")
    box(ax, 0.5, 1.4, 2.6, 1.4, "Task A\nwait_event", SHADE)
    box(ax, 3.7, 1.4, 2.6, 1.4, "wait_queue\nhead", SHADE2, TEAL)
    box(ax, 6.9, 1.4, 2.6, 1.4, "waker\nwake_up", SHADE, ORANGE)
    arrow(ax, 3.2, 2.1, 3.6, 2.1, GRAY)
    arrow(ax, 6.4, 2.1, 6.8, 2.1, RED)
    ax.set_title("Sleeping on a wait queue", fontsize=12)
    save(fig, "lk-waitqueue.svg")


def fig_irq():
    fig, ax = plt.subplots(figsize=(6.8, 3.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4.5)
    ax.axis("off")
    box(ax, 0.4, 2.6, 2.6, 1.2, "Hardware IRQ", SHADE, RED)
    box(ax, 3.6, 2.6, 2.8, 1.2, "Top half\nhandler", SHADE2, TEAL)
    box(ax, 7.0, 2.6, 2.6, 1.2, "Bottom half\n(tasklet/WQ)", SHADE, BLUE)
    arrow(ax, 3.1, 3.2, 3.5, 3.2)
    arrow(ax, 6.5, 3.2, 6.9, 3.2)
    ax.text(5.0, 1.5, "defer heavy work out of hardirq", ha="center", color=GRAY, fontsize=10)
    ax.set_title("Interrupt top / bottom half", fontsize=12)
    save(fig, "lk-irq.svg")


def fig_locking():
    fig, ax = plt.subplots(figsize=(6.6, 3.4))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")
    locks = [
        (0.3, "spinlock\n(atomic ctx)"),
        (2.7, "mutex\n(sleep OK)"),
        (5.1, "rwsem /\nRCU"),
        (7.5, "atomics /\nbarriers"),
    ]
    for i, (x, t) in enumerate(locks):
        box(ax, x, 1.2, 2.1, 1.5, t, SHADE if i % 2 == 0 else SHADE2, BLUE if i < 2 else TEAL, 9)
    ax.set_title("Common kernel locking primitives", fontsize=12)
    save(fig, "lk-locking.svg")


def fig_device_tree():
    fig, ax = plt.subplots(figsize=(5.6, 4.0))
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 5)
    ax.axis("off")
    box(ax, 1.8, 4.0, 2.4, 0.7, "/", SHADE, BLUE)
    box(ax, 0.4, 2.6, 2.2, 0.8, "soc", SHADE2, TEAL)
    box(ax, 3.4, 2.6, 2.2, 0.8, "memory", SHADE2, TEAL)
    box(ax, 0.4, 1.2, 2.2, 0.8, "uart0", SHADE, ORANGE)
    box(ax, 3.4, 1.2, 2.2, 0.8, "i2c1", SHADE, ORANGE)
    arrow(ax, 3.0, 4.0, 1.5, 3.5, GRAY, 1.1)
    arrow(ax, 3.0, 4.0, 4.5, 3.5, GRAY, 1.1)
    arrow(ax, 1.5, 2.6, 1.5, 2.1, GRAY, 1.1)
    arrow(ax, 4.5, 2.6, 4.5, 2.1, GRAY, 1.1)
    ax.set_title("Device Tree hierarchy sketch", fontsize=12)
    save(fig, "lk-device-tree.svg")


def main():
    setup()
    fig_moc()
    fig_kernel_layers()
    fig_source_tree()
    fig_module_lifecycle()
    fig_device_model()
    fig_char_fops()
    fig_mm()
    fig_dma()
    fig_process_states()
    fig_waitqueue()
    fig_irq()
    fig_locking()
    fig_device_tree()
    print("done")


if __name__ == "__main__":
    main()
