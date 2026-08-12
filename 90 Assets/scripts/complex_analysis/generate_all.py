#!/usr/bin/env python3
"""Generate SVGs for Complex Analysis (MIT 18.04) notes.

Usage:
  .venv/bin/python generate_all.py

Outputs to: 90 Assets/diagrams/complex-analysis/
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Arc, Circle, FancyArrowPatch, FancyBboxPatch, Rectangle, Wedge
from matplotlib.patches import FancyArrowPatch as Arrow

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "90 Assets" / "diagrams" / "complex-analysis"

BLUE = "#2f5f8f"
TEAL = "#2a7a6b"
RED = "#a33b3b"
ORANGE = "#c47a2c"
GRAY = "#666666"
LIGHT = "#aaaaaa"
SHADE = "#d6e4f0"
SHADE2 = "#f0e6d6"


def setup():
    plt.rcParams.update(
        {
            "font.size": 11,
            "font.sans-serif": ["PingFang SC", "Heiti SC", "Arial Unicode MS", "DejaVu Sans"],
            "axes.unicode_minus": False,
            "axes.linewidth": 1.1,
            "mathtext.fontset": "dejavusans",
            "svg.fonttype": "none",
        }
    )
    OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name: str):
    path = OUT / name
    fig.savefig(path, format="svg", bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    print("wrote", path.relative_to(ROOT))


def complex_axes(ax, lim=2.6, xlabel=r"$\mathrm{Re}$", ylabel=r"$\mathrm{Im}$"):
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_aspect("equal")
    ax.axhline(0, color=GRAY, lw=1)
    ax.axvline(0, color=GRAY, lw=1)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.text(lim * 0.92, -0.22, xlabel, color=GRAY, ha="right", va="top")
    ax.text(0.08, lim * 0.92, ylabel, color=GRAY, ha="left", va="top")


def axes_c(ax, lim=2.6):
    """Alias used by topic 3–13 figures."""
    complex_axes(ax, lim=lim)


def arrow(ax, x0, y0, x1, y1, color=BLUE, lw=1.8, ms=12):
    ax.annotate(
        "",
        xy=(x1, y1),
        xytext=(x0, y0),
        arrowprops=dict(arrowstyle="-|>", color=color, lw=lw, mutation_scale=ms),
    )


# ---------- Topic 1 ----------


def fig_complex_plane():
    fig, ax = plt.subplots(figsize=(4.6, 4.6))
    complex_axes(ax, lim=2.8)
    x, y = 1.8, 1.3
    arrow(ax, 0, 0, x, y, BLUE)
    ax.plot([x], [y], "o", color=BLUE, ms=6)
    ax.plot([x], [-y], "o", color=TEAL, ms=6)
    arrow(ax, 0, 0, x, -y, TEAL)
    ax.plot([x, x], [0, y], "--", color=LIGHT, lw=1)
    ax.plot([0, x], [y, y], "--", color=LIGHT, lw=1)
    ax.text(x + 0.12, y + 0.08, r"$z=x+iy$", color=BLUE)
    ax.text(x + 0.12, -y - 0.22, r"$\bar z=x-iy$", color=TEAL)
    ax.text(x / 2 - 0.15, -0.28, r"$x$", color=GRAY)
    ax.text(-0.28, y / 2, r"$y$", color=GRAY)
    ax.set_title(r"Complex plane: $z$ and $\bar z$", fontsize=12, pad=8)
    save(fig, "ca-complex-plane.svg")


def fig_triangle_inequality():
    fig, ax = plt.subplots(figsize=(4.8, 4.2))
    complex_axes(ax, lim=3.0)
    z1 = np.array([1.6, 0.4])
    z2 = np.array([0.5, 1.5])
    s = z1 + z2
    arrow(ax, 0, 0, z1[0], z1[1], BLUE)
    arrow(ax, z1[0], z1[1], s[0], s[1], TEAL)
    arrow(ax, 0, 0, s[0], s[1], RED)
    ax.plot([0], [0], "o", color=GRAY, ms=4)
    ax.text(z1[0] * 0.55, z1[1] * 0.55 - 0.28, r"$z_1$", color=BLUE)
    ax.text(z1[0] + z2[0] * 0.45 + 0.1, z1[1] + z2[1] * 0.45, r"$z_2$", color=TEAL)
    ax.text(s[0] * 0.55 - 0.35, s[1] * 0.55 + 0.1, r"$z_1+z_2$", color=RED)
    ax.set_title(r"$|z_1|+|z_2|\geq|z_1+z_2|$", fontsize=12, pad=8)
    save(fig, "ca-triangle-inequality.svg")


def fig_polar_form():
    fig, ax = plt.subplots(figsize=(4.6, 4.6))
    complex_axes(ax, lim=2.6)
    circ = Circle((0, 0), 1.0, fill=False, color=LIGHT, lw=1.2, ls="--")
    ax.add_patch(circ)
    th = np.pi / 3
    r = 1.85
    x, y = r * np.cos(th), r * np.sin(th)
    arrow(ax, 0, 0, x, y, BLUE)
    ax.plot([x], [y], "o", color=BLUE, ms=6)
    arc = Arc((0, 0), 1.1, 1.1, angle=0, theta1=0, theta2=np.degrees(th), color=ORANGE, lw=1.6)
    ax.add_patch(arc)
    ax.plot([1, 0], [0, 0], color=TEAL, lw=1.5)  # unit tip marker area
    ax.plot([np.cos(th)], [np.sin(th)], "o", color=TEAL, ms=5)
    ax.text(0.55, 0.22, r"$\theta=\arg(z)$", color=ORANGE)
    ax.text(x * 0.55 - 0.35, y * 0.55 + 0.15, r"$r=|z|$", color=BLUE)
    ax.text(x + 0.1, y + 0.05, r"$z=re^{i\theta}$", color=BLUE)
    ax.text(1.05, -0.28, r"$e^{i\theta}$", color=TEAL, fontsize=10)
    ax.set_title("Polar / exponential form", fontsize=12, pad=8)
    save(fig, "ca-polar-form.svg")


def fig_multiply_by_2i():
    fig, axes = plt.subplots(1, 2, figsize=(8.2, 3.8))
    for ax in axes:
        complex_axes(ax, lim=3.0)

    z = np.array([1.4, 0.7])
    w = np.array([-1.4, 2.8])  # 2i * z = 2i(x+iy)=2(-y+ix)

    arrow(axes[0], 0, 0, z[0], z[1], BLUE)
    axes[0].plot([z[0]], [z[1]], "o", color=BLUE, ms=6)
    axes[0].text(z[0] + 0.1, z[1] - 0.35, r"$z$", color=BLUE)
    arc = Arc((0, 0), 1.2, 1.2, angle=0, theta1=0, theta2=np.degrees(np.arctan2(z[1], z[0])), color=ORANGE, lw=1.4)
    axes[0].add_patch(arc)
    axes[0].set_title(r"Original $z$", fontsize=11)

    arrow(axes[1], 0, 0, z[0], z[1], LIGHT, lw=1.2)
    arrow(axes[1], 0, 0, w[0], w[1], RED)
    axes[1].plot([w[0]], [w[1]], "o", color=RED, ms=6)
    axes[1].text(w[0] - 0.1, w[1] + 0.15, r"$2iz$", color=RED, ha="right")
    axes[1].text(0.2, 1.1, r"$\times 2i$", color=ORANGE)
    # rotation hint
    arc2 = Arc((0, 0), 2.0, 2.0, angle=0, theta1=np.degrees(np.arctan2(z[1], z[0])), theta2=np.degrees(np.arctan2(w[1], w[0])), color=ORANGE, lw=1.4)
    axes[1].add_patch(arc2)
    axes[1].set_title(r"$\times 2i$: scale by 2, rotate $90^\circ$", fontsize=11)

    fig.suptitle(r"$2i=2e^{i\pi/2}$", fontsize=12, y=1.02)
    save(fig, "ca-multiply-by-2i.svg")


def fig_nth_roots():
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 4.0))
    for ax in axes:
        complex_axes(ax, lim=1.8)

    # cube roots of -1
    r = 1.0
    angles = [np.pi / 3, np.pi, 5 * np.pi / 3]
    labels = [r"$e^{i\pi/3}$", r"$-1$", r"$e^{i5\pi/3}$"]
    circ = Circle((0, 0), r, fill=False, color=LIGHT, lw=1.2)
    axes[0].add_patch(circ)
    for th, lab in zip(angles, labels):
        x, y = r * np.cos(th), r * np.sin(th)
        axes[0].plot([x], [y], "o", color=BLUE, ms=7)
        axes[0].plot([0, x], [0, y], color=BLUE, lw=1.2, alpha=0.5)
        off = 0.18
        axes[0].text(x * (1 + off / r) - 0.05, y * (1 + off / r), lab, color=BLUE, fontsize=10, ha="center")
    axes[0].set_title(r"Cube roots of $-1$", fontsize=11)

    # fifth roots of 1+i
    rho = 2 ** 0.1
    circ2 = Circle((0, 0), rho, fill=False, color=LIGHT, lw=1.2)
    axes[1].add_patch(circ2)
    base = np.pi / 20
    for k in range(5):
        th = base + 2 * np.pi * k / 5
        x, y = rho * np.cos(th), rho * np.sin(th)
        axes[1].plot([x], [y], "o", color=TEAL, ms=7)
        axes[1].plot([0, x], [0, y], color=TEAL, lw=1.0, alpha=0.45)
    axes[1].plot([1], [1], "x", color=RED, ms=8, mew=1.5)
    axes[1].text(1.05, 1.05, r"$1+i$", color=RED, fontsize=10)
    axes[1].set_title(r"Fifth roots of $1+i$", fontsize=11)

    fig.suptitle(r"$n$th roots lie equally spaced on a circle", fontsize=12, y=1.02)
    save(fig, "ca-nth-roots.svg")


def fig_exp_unit_circle():
    fig, ax = plt.subplots(figsize=(4.8, 4.8))
    complex_axes(ax, lim=1.7)
    circ = Circle((0, 0), 1.0, fill=False, color=BLUE, lw=1.6)
    ax.add_patch(circ)
    ts = [0, np.pi / 4, np.pi / 2, np.pi, 3 * np.pi / 2]
    labels = [r"$1$", r"$e^{i\pi/4}$", r"$i$", r"$-1$", r"$-i$"]
    for t, lab in zip(ts, labels):
        x, y = np.cos(t), np.sin(t)
        ax.plot([x], [y], "o", color=TEAL, ms=6)
        ax.text(1.22 * x, 1.22 * y, lab, color=TEAL, ha="center", va="center", fontsize=10)
    # arrow showing direction of increasing t
    th = np.linspace(0.15, 1.0, 40)
    ax.plot(np.cos(th), np.sin(th), color=ORANGE, lw=2.0)
    ax.annotate(
        "",
        xy=(np.cos(1.05), np.sin(1.05)),
        xytext=(np.cos(0.95), np.sin(0.95)),
        arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.5, mutation_scale=12),
    )
    ax.text(0.55, 0.85, r"$t\uparrow$", color=ORANGE)
    ax.set_title(r"$t\mapsto e^{it}$ wraps the unit circle", fontsize=12, pad=8)
    save(fig, "ca-exp-unit-circle.svg")


def fig_map_z_squared():
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 4.0))
    complex_axes(axes[0], lim=2.4)
    complex_axes(axes[1], lim=3.2)

    # left: rays in first two quadrants
    colors = [BLUE, TEAL, ORANGE, RED]
    thetas = [np.pi / 8, np.pi / 4, 3 * np.pi / 8, np.pi / 2]
    for th, c in zip(thetas, colors):
        rs = np.linspace(0, 2.2, 50)
        axes[0].plot(rs * np.cos(th), rs * np.sin(th), color=c, lw=1.8)
        axes[0].plot(rs * np.cos(th + np.pi), rs * np.sin(th + np.pi), color=c, lw=1.2, ls="--", alpha=0.6)
    axes[0].add_patch(Wedge((0, 0), 2.2, 0, 180, facecolor=SHADE, alpha=0.35, edgecolor="none"))
    axes[0].set_title(r"$z$-plane rays", fontsize=11)

    # right: doubled angles
    for th, c in zip(thetas, colors):
        rs = np.linspace(0, 2.8, 50)
        axes[1].plot(rs * np.cos(2 * th), rs * np.sin(2 * th), color=c, lw=1.8)
    axes[1].set_title(r"$w=z^2$ doubles angles", fontsize=11)
    fig.suptitle(r"Mapping $z\mapsto z^2$", fontsize=12, y=1.02)
    save(fig, "ca-map-z-squared.svg")


def fig_map_exp():
    fig, axes = plt.subplots(1, 2, figsize=(8.8, 4.0))
    # left: horizontal strip
    ax = axes[0]
    complex_axes(ax, lim=3.2)
    ax.set_xlim(-2.2, 2.5)
    ax.set_ylim(-1.2, 7.2)
    ax.set_aspect("auto")
    rect = Rectangle((-2.0, 0), 4.2, 2 * np.pi, facecolor=SHADE, edgecolor=BLUE, lw=1.4, alpha=0.5)
    ax.add_patch(rect)
    for y in [0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi]:
        ax.plot([-2.0, 2.2], [y, y], color=TEAL, lw=1.2)
        ax.text(2.25, y, rf"${y/np.pi:.2g}\pi$" if y else r"$0$", color=TEAL, va="center", fontsize=9)
    for x in [-1, 0, 1, 2]:
        ax.plot([x, x], [0, 2 * np.pi], color=ORANGE, lw=1.2, ls="--")
    ax.text(-1.8, 3.4, r"$0\leq y<2\pi$", color=BLUE)
    ax.set_title(r"$z$-plane horizontal strip", fontsize=11)

    # right: punctured plane
    ax = axes[1]
    complex_axes(ax, lim=3.0)
    # circles from vertical lines
    for r, c in zip([np.exp(-1), 1, np.exp(1), np.exp(2)], [ORANGE, ORANGE, ORANGE, ORANGE]):
        circ = Circle((0, 0), r, fill=False, color=c, lw=1.2, ls="--")
        ax.add_patch(circ)
    # rays from horizontal lines
    for th in [0, np.pi / 2, np.pi, 3 * np.pi / 2]:
        ax.plot([0, 2.8 * np.cos(th)], [0, 2.8 * np.sin(th)], color=TEAL, lw=1.4)
    ax.plot([0], [0], "o", color=RED, ms=5)
    ax.text(0.15, -0.35, r"punctured at $0$", color=RED, fontsize=9)
    ax.set_title(r"$w=e^z$ → punctured plane", fontsize=11)
    fig.suptitle(r"Mapping $z\mapsto e^z$", fontsize=12, y=1.02)
    save(fig, "ca-map-exp.svg")


def fig_arg_branches():
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 4.0))

    # principal branch
    ax = axes[0]
    complex_axes(ax, lim=2.2)
    # branch cut negative real axis
    ax.plot([-2.1, 0], [0, 0], color=ORANGE, lw=4, solid_capstyle="butt", alpha=0.85)
    ax.plot([0], [0], "o", color=ORANGE, ms=6)
    pts = {
        r"$1$": (1.3, 0),
        r"$i$": (0, 1.3),
        r"$-1$": (-1.3, 0.08),
        r"$-i$": (0, -1.3),
    }
    args = {r"$1$": r"$0$", r"$i$": r"$\pi/2$", r"$-1$": r"$\pi$", r"$-i$": r"$-\pi/2$"}
    for lab, (x, y) in pts.items():
        ax.plot([x], [y], "o", color=BLUE, ms=6)
        ax.text(x + 0.12, y + 0.12, f"{lab}: {args[lab]}", color=BLUE, fontsize=9)
    ax.set_title(r"Principal: $-\pi<\mathrm{Arg}\,z\leq\pi$", fontsize=11)

    # branch 0 to 2pi
    ax = axes[1]
    complex_axes(ax, lim=2.2)
    ax.plot([0, 2.1], [0, 0], color=ORANGE, lw=4, solid_capstyle="butt", alpha=0.85)
    ax.plot([0], [0], "o", color=ORANGE, ms=6)
    args2 = {r"$1$": r"$0$", r"$i$": r"$\pi/2$", r"$-1$": r"$\pi$", r"$-i$": r"$3\pi/2$"}
    for lab, (x, y) in pts.items():
        yy = 0.08 if lab == r"$-1$" else y
        xx = x
        ax.plot([xx], [yy if lab != r"$1$" else 0.08], "o", color=TEAL, ms=6)
        ax.text(xx + 0.12, (yy if lab != r"$1$" else 0.08) + 0.12, f"{lab}: {args2[lab]}", color=TEAL, fontsize=9)
    ax.set_title(r"Branch: $0\leq\arg z<2\pi$", fontsize=11)

    fig.suptitle(r"Branches of $\arg z$ (thick = branch cut)", fontsize=12, y=1.02)
    save(fig, "ca-arg-branches.svg")


def fig_log_principal():
    fig, axes = plt.subplots(1, 2, figsize=(8.8, 4.0))
    ax = axes[0]
    complex_axes(ax, lim=3.0)
    ax.plot([-2.8, 0], [0, 0], color=ORANGE, lw=4, alpha=0.85)
    for r in [1, 2]:
        circ = Circle((0, 0), r, fill=False, color=BLUE, lw=1.3)
        ax.add_patch(circ)
    for th in [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi, -np.pi / 2, -np.pi / 4]:
        ax.plot([0, 2.7 * np.cos(th)], [0, 2.7 * np.sin(th)], color=TEAL, lw=1.1)
    ax.plot([1], [0], "o", color=RED, ms=6)
    ax.plot([0], [1], "o", color=RED, ms=6)
    ax.text(1.1, 0.15, r"$1$", color=RED)
    ax.text(0.15, 1.1, r"$i$", color=RED)
    ax.set_title(r"$z$-plane (cut removed)", fontsize=11)

    ax = axes[1]
    ax.set_xlim(-1.5, 2.2)
    ax.set_ylim(-4.0, 4.0)
    ax.set_aspect("auto")
    ax.axhline(0, color=GRAY, lw=1)
    ax.axvline(0, color=GRAY, lw=1)
    for spine in ax.spines.values():
        spine.set_visible(False)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.text(2.0, -0.35, r"$\mathrm{Re}$", color=GRAY)
    ax.text(0.08, 3.6, r"$\mathrm{Im}$", color=GRAY)
    rect = Rectangle((-1.2, -np.pi), 3.2, 2 * np.pi, facecolor=SHADE, edgecolor=BLUE, lw=1.3, alpha=0.45)
    ax.add_patch(rect)
    # images of circles -> vertical lines
    for x in [0, np.log(2)]:
        ax.plot([x, x], [-np.pi, np.pi], color=BLUE, lw=1.5)
    # images of rays -> horizontal lines
    for y in [0, np.pi / 2, -np.pi / 2, np.pi, -np.pi]:
        ax.plot([-0.8, 1.8], [y, y], color=TEAL, lw=1.1)
    ax.plot([0], [0], "o", color=RED, ms=6)
    ax.plot([0], [np.pi / 2], "o", color=RED, ms=6)
    ax.text(0.1, 0.15, r"$\mathrm{Log}\,1=0$", color=RED, fontsize=9)
    ax.text(0.1, np.pi / 2 + 0.15, r"$\mathrm{Log}\,i=i\pi/2$", color=RED, fontsize=9)
    ax.text(-1.05, 2.5, r"$-\pi<\mathrm{Im}\leq\pi$", color=BLUE, fontsize=10)
    ax.set_title(r"$w=\mathrm{Log}\,z$ principal strip", fontsize=11)
    fig.suptitle(r"Principal $\mathrm{Log}\,z=\ln|z|+i\,\mathrm{Arg}\,z$", fontsize=12, y=1.02)
    save(fig, "ca-log-principal.svg")


def fig_moc_roadmap():
    fig, ax = plt.subplots(figsize=(9.2, 3.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")
    boxes = [
        (0.3, 2.2, "Complex\nplane"),
        (2.3, 2.2, "Analytic\nfunctions"),
        (4.3, 2.2, "Contour\nintegrals"),
        (6.3, 2.2, "Taylor /\nLaurent"),
        (8.3, 2.2, "Residues &\nreal integrals"),
    ]
    for i, (x, y, t) in enumerate(boxes):
        ax.add_patch(
            FancyBboxPatch(
                (x, y),
                1.5,
                1.2,
                boxstyle="round,pad=0.05,rounding_size=0.15",
                facecolor=SHADE if i % 2 == 0 else SHADE2,
                edgecolor=BLUE,
                lw=1.3,
            )
        )
        ax.text(x + 0.75, y + 0.6, t, ha="center", va="center", fontsize=10, color=BLUE)
        if i < len(boxes) - 1:
            ax.annotate(
                "",
                xy=(boxes[i + 1][0] - 0.05, y + 0.6),
                xytext=(x + 1.55, y + 0.6),
                arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.5),
            )
    apps = [(2.3, 0.4, "Harmonic /\n2D flow"), (4.3, 0.4, "Conformal\nmaps"), (6.3, 0.4, "Laplace /\narg principle")]
    for x, y, t in apps:
        ax.add_patch(
            FancyBboxPatch(
                (x, y),
                1.5,
                0.9,
                boxstyle="round,pad=0.05,rounding_size=0.12",
                facecolor="#f7f7f7",
                edgecolor=TEAL,
                lw=1.1,
            )
        )
        ax.text(x + 0.75, y + 0.45, t, ha="center", va="center", fontsize=9, color=TEAL)
        ax.plot([x + 0.75, x + 0.75], [1.3, 2.2], color=LIGHT, lw=1.0, ls=":")
    ax.set_title("MIT 18.04 Complex Variables roadmap", fontsize=13, pad=6)
    save(fig, "ca-moc-roadmap.svg")


# ---------- Topic 2 ----------


def fig_open_disk():
    fig, axes = plt.subplots(1, 2, figsize=(8.2, 3.8))
    for ax in axes:
        complex_axes(ax, lim=2.4)

    circ = Circle((0.2, 0.3), 1.2, fill=True, facecolor=SHADE, edgecolor=BLUE, lw=1.5, ls="--")
    axes[0].add_patch(circ)
    axes[0].plot([0.2], [0.3], "o", color=RED, ms=6)
    axes[0].plot([0.2, 0.2 + 1.2], [0.3, 0.3], color=ORANGE, lw=1.4)
    axes[0].text(0.7, 0.45, r"$r$", color=ORANGE)
    axes[0].text(0.35, 0.45, r"$z_0$", color=RED)
    axes[0].set_title(r"Open disk $|z-z_0|<r$", fontsize=11)

    circ2 = Circle((0.2, 0.3), 1.2, fill=True, facecolor=SHADE, edgecolor=BLUE, lw=1.5, ls="--")
    axes[1].add_patch(circ2)
    axes[1].plot([0.2], [0.3], "o", color="white", ms=10, markeredgecolor=RED, markeredgewidth=2)
    axes[1].text(0.35, 0.45, r"$z_0$ removed", color=RED, fontsize=9)
    axes[1].set_title(r"Deleted disk $0<|z-z_0|<r$", fontsize=11)
    fig.suptitle("Open / punctured disks", fontsize=12, y=1.02)
    save(fig, "ca-open-disk.svg")


def fig_limit_paths():
    fig, ax = plt.subplots(figsize=(4.8, 4.6))
    complex_axes(ax, lim=2.2)
    ax.plot([0], [0], "o", color=RED, ms=7)
    ax.text(0.12, -0.35, r"$0$", color=RED)
    # several paths approaching 0
    t = np.linspace(1.8, 0.15, 40)
    ax.plot(t, np.zeros_like(t), color=BLUE, lw=1.8)
    ax.plot(np.zeros_like(t), t, color=TEAL, lw=1.8)
    ax.plot(t / np.sqrt(2), t / np.sqrt(2), color=ORANGE, lw=1.8)
    ax.plot(t * np.cos(np.pi / 5), -t * np.sin(np.pi / 5), color=GRAY, lw=1.6)
    ax.annotate("", xy=(0.2, 0), xytext=(0.45, 0), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.2))
    ax.annotate("", xy=(0, 0.2), xytext=(0, 0.45), arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=1.2))
    ax.text(1.2, 0.15, r"real axis", color=BLUE, fontsize=9)
    ax.text(0.15, 1.5, r"imag axis", color=TEAL, fontsize=9)
    ax.set_title(r"Limit must agree along every path", fontsize=12, pad=8)
    save(fig, "ca-limit-paths.svg")


def fig_cr_directions():
    fig, ax = plt.subplots(figsize=(4.8, 4.6))
    complex_axes(ax, lim=2.4)
    z0x, z0y = 0.6, 0.5
    ax.plot([z0x], [z0y], "o", color=RED, ms=7)
    ax.text(z0x + 0.12, z0y + 0.12, r"$z_0$", color=RED)
    # horizontal approach
    arrow(ax, z0x - 1.2, z0y, z0x - 0.15, z0y, BLUE)
    arrow(ax, z0x + 0.15, z0y, z0x + 1.2, z0y, BLUE)
    # vertical approach
    arrow(ax, z0x, z0y - 1.2, z0x, z0y - 0.15, TEAL)
    arrow(ax, z0x, z0y + 0.15, z0x, z0y + 1.2, TEAL)
    ax.text(1.5, z0y + 0.15, r"$\Delta y=0$", color=BLUE, fontsize=10)
    ax.text(z0x + 0.15, 1.7, r"$\Delta x=0$", color=TEAL, fontsize=10)
    ax.text(-2.1, -2.1, r"$f'=u_x+iv_x=-\,i(u_y+iv_y)$", color=GRAY, fontsize=10)
    ax.set_title("Cauchy–Riemann: two approach directions", fontsize=12, pad=8)
    save(fig, "ca-cr-directions.svg")


def fig_not_diff_conj():
    fig, ax = plt.subplots(figsize=(4.8, 4.6))
    complex_axes(ax, lim=2.2)
    # show conjugate as reflection
    x, y = 1.4, 1.0
    arrow(ax, 0, 0, x, y, BLUE)
    arrow(ax, 0, 0, x, -y, TEAL)
    ax.plot([x], [y], "o", color=BLUE, ms=6)
    ax.plot([x], [-y], "o", color=TEAL, ms=6)
    ax.plot([-2, 2], [0, 0], color=ORANGE, lw=2, alpha=0.5)
    ax.text(x + 0.1, y + 0.1, r"$z$", color=BLUE)
    ax.text(x + 0.1, -y - 0.25, r"$\bar z$", color=TEAL)
    ax.text(-2.0, 1.8, r"$f(z)=\bar z$ fails CR", color=RED, fontsize=11)
    ax.set_title(r"$f(z)=\bar z$ is nowhere analytic", fontsize=12, pad=8)
    save(fig, "ca-conj-not-analytic.svg")


def fig_sqrt_branch_composition():
    fig, axes = plt.subplots(1, 2, figsize=(8.6, 3.8))
    for ax in axes:
        complex_axes(ax, lim=2.6)

    # left: sqrt principal cut
    axes[0].plot([-2.4, 0], [0, 0], color=ORANGE, lw=4, alpha=0.85)
    axes[0].plot([0], [0], "o", color=ORANGE, ms=6)
    axes[0].add_patch(Circle((0, 0), 2.3, facecolor=SHADE, edgecolor="none", alpha=0.35))
    axes[0].set_title(r"$\sqrt{w}$ cut: $w\leq 0$", fontsize=11)

    # right: 1-z on negative real => z>=1
    axes[1].plot([1, 2.4], [0, 0], color=ORANGE, lw=4, alpha=0.85)
    axes[1].plot([1], [0], "o", color=ORANGE, ms=6)
    axes[1].text(1.1, 0.2, r"$1$", color=ORANGE)
    axes[1].set_title(r"$\sqrt{1-z}$ cut: $z\geq 1$ (real)", fontsize=11)
    fig.suptitle(r"Composition moves the branch cut", fontsize=12, y=1.02)
    save(fig, "ca-sqrt-branch-composition.svg")

# ---------- Topics 3–13 ----------

def fig_contour_cauchy():
    fig, axes = plt.subplots(1,2, figsize=(8.6,3.9))
    for ax in axes: axes_c(ax, 2.8)
    # left: simply connected
    t=np.linspace(0,2*np.pi,200)
    axes[0].plot(1.6*np.cos(t)+0.1*np.cos(2*t), 1.2*np.sin(t), color=BLUE, lw=2)
    axes[0].annotate("", xy=(1.7,0.15), xytext=(1.65,-0.05), arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.4))
    axes[0].add_patch(Circle((0.2,0.1), 0.35, facecolor=SHADE, edgecolor=TEAL, lw=1))
    axes[0].text(-2.5,2.3, r"$\int_C f=0$ (analytic, simply connected)", color=BLUE, fontsize=9)
    axes[0].set_title("Cauchy theorem", fontsize=11)
    # right: annulus deformation
    axes[1].plot(2.2*np.cos(t), 2.2*np.sin(t), color=BLUE, lw=2)
    axes[1].plot(0.7*np.cos(t), 0.7*np.sin(t), color=TEAL, lw=2)
    axes[1].plot([0],[0], "o", color=RED, ms=6)
    axes[1].text(0.1,0.15, r"$0$", color=RED)
    axes[1].annotate("", xy=(2.2,0.2), xytext=(2.15,-0.05), arrowprops=dict(arrowstyle="-|>", color=ORANGE))
    axes[1].annotate("", xy=(0.7,-0.15), xytext=(0.72,0.05), arrowprops=dict(arrowstyle="-|>", color=ORANGE))
    axes[1].set_title(r"$\int_{C_1}=\int_{C_2}$ (same holes)", fontsize=11)
    fig.suptitle("Contour integrals / deformation", y=1.02)
    save(fig, "ca-contour-cauchy.svg")

def fig_cif():
    fig, ax = plt.subplots(figsize=(4.8,4.6))
    axes_c(ax, 2.5)
    t=np.linspace(0,2*np.pi,200)
    ax.plot(1.8*np.cos(t), 1.5*np.sin(t)+0.1*np.cos(2*t), color=BLUE, lw=2)
    ax.plot([0.4],[0.3], "o", color=RED, ms=7)
    ax.text(0.55,0.4, r"$z_0$", color=RED)
    ax.add_patch(Circle((0.4,0.3), 0.35, fill=False, ls="--", color=TEAL, lw=1.3))
    ax.annotate("", xy=(1.75,0.2), xytext=(1.7,-0.05), arrowprops=dict(arrowstyle="-|>", color=ORANGE))
    ax.text(-2.3,2.1, r"$f(z_0)=\frac{1}{2\pi i}\oint\frac{f}{z-z_0}dz$", fontsize=10, color=BLUE)
    ax.set_title("Cauchy integral formula", fontsize=12)
    save(fig, "ca-cif.svg")

def fig_harmonic_grid():
    fig, ax = plt.subplots(figsize=(5.0,4.6))
    axes_c(ax, 2.4)
    # u=x^2-y^2 level curves (hyperbolas) and v=2xy
    xs=np.linspace(-2.2,2.2,400)
    for c in [-2,-1,-0.5,0.5,1,2]:
        # x^2-y^2=c => y=±sqrt(x^2-c) when x^2>c
        for s in [1,-1]:
            mask=xs**2>c if c>0 else xs**2>=0
            yy=s*np.sqrt(np.clip(xs**2-c,0,None))
            ax.plot(xs[np.isfinite(yy)], yy[np.isfinite(yy)], color=BLUE, lw=1.1, alpha=0.85)
    for c in [-2,-1,-0.5,0.5,1,2]:
        # 2xy=c => y=c/(2x)
        xx=np.concatenate([np.linspace(-2.2,-0.15,100), np.linspace(0.15,2.2,100)])
        ax.plot(xx, c/(2*xx), color=TEAL, lw=1.1, alpha=0.85)
    ax.plot([0],[0], "o", color=RED, ms=5)
    ax.text(-2.2,2.05, r"$u=x^2-y^2$ (blue), $v=2xy$ (teal)", fontsize=9, color=GRAY)
    ax.set_title(r"Orthogonal level curves of $z^2$", fontsize=12)
    save(fig, "ca-harmonic-orthogonal.svg")

def fig_flow_gallery():
    fig, axes = plt.subplots(1,3, figsize=(10.2,3.4))
    titles=[r"Uniform $\Phi=z$", r"Source $\Phi=\log z$", r"Vortex $\Phi=-i\log z$"]
    for ax,title in zip(axes,titles):
        axes_c(ax, 2.2); ax.set_title(title, fontsize=10)
    # uniform
    for y in np.linspace(-1.8,1.8,7):
        axes[0].annotate("", xy=(1.8,y), xytext=(-1.8,y), arrowprops=dict(arrowstyle="-|>", color=BLUE, lw=1.2))
    # source
    for th in np.linspace(0,2*np.pi,12, endpoint=False):
        axes[1].annotate("", xy=(1.7*np.cos(th),1.7*np.sin(th)), xytext=(0.25*np.cos(th),0.25*np.sin(th)), arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=1.1))
    axes[1].plot([0],[0],"o",color=RED,ms=5)
    # vortex
    for r in [0.6,1.1,1.6]:
        t=np.linspace(0,2*np.pi,100)
        axes[2].plot(r*np.cos(t), r*np.sin(t), color=ORANGE, lw=1.3)
        axes[2].annotate("", xy=(0,r), xytext=(0.2,r), arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.1))
    axes[2].plot([0],[0],"o",color=RED,ms=5)
    fig.suptitle("2D complex potentials", y=1.05)
    save(fig, "ca-flow-gallery.svg")

def fig_laurent_annulus():
    fig, ax = plt.subplots(figsize=(4.8,4.6))
    axes_c(ax, 2.6)
    ax.add_patch(Wedge((0,0), 2.2, 0, 360, width=1.4, facecolor=SHADE, edgecolor=BLUE, lw=1.5))
    ax.plot([0],[0],"o", color=RED, ms=6)
    ax.text(0.1,0.15,r"$z_0$", color=RED)
    ax.text(1.5,0.2,r"$r_1<|z-z_0|<r_2$", color=BLUE, fontsize=10)
    ax.set_title("Laurent annulus of convergence", fontsize=12)
    save(fig, "ca-laurent-annulus.svg")

def fig_residue_theorem():
    fig, ax = plt.subplots(figsize=(5.0,4.6))
    axes_c(ax, 2.7)
    t=np.linspace(0,2*np.pi,200)
    ax.plot(2.3*np.cos(t), 1.9*np.sin(t), color=BLUE, lw=2)
    for p,lab in [((-0.7,0.5),r"$z_1$"), ((0.9,-0.4),r"$z_2$"), ((0.2,1.0),r"$z_3$")]:
        ax.plot([p[0]],[p[1]], "o", color=RED, ms=6)
        ax.add_patch(Circle(p, 0.28, fill=False, ls="--", color=TEAL, lw=1.1))
        ax.text(p[0]+0.15,p[1]+0.15, lab, color=RED)
    ax.annotate("", xy=(2.25,0.2), xytext=(2.2,-0.05), arrowprops=dict(arrowstyle="-|>", color=ORANGE))
    ax.text(-2.5,2.35, r"$\oint f=2\pi i\sum \mathrm{Res}$", color=BLUE, fontsize=11)
    ax.set_title("Residue theorem", fontsize=12)
    save(fig, "ca-residue-theorem.svg")

def fig_semicircle():
    fig, ax = plt.subplots(figsize=(5.2,3.2))
    ax.set_xlim(-3.2,3.2); ax.set_ylim(-0.4,3.0); ax.set_aspect("equal"); ax.axis("off")
    ax.axhline(0, color=GRAY, lw=1)
    ax.plot([-3,3],[0,0], color=BLUE, lw=2)
    t=np.linspace(0,np.pi,100)
    ax.plot(2.6*np.cos(t), 2.6*np.sin(t), color=TEAL, lw=2)
    ax.annotate("", xy=(1.2,0), xytext=(0.8,0), arrowprops=dict(arrowstyle="-|>", color=BLUE))
    ax.annotate("", xy=(-0.2,2.58), xytext=(0.2,2.58), arrowprops=dict(arrowstyle="-|>", color=TEAL))
    ax.plot([0.7],[0.9],"o", color=RED, ms=6); ax.text(0.85,1.0,r"poles", color=RED)
    ax.plot([-0.8],[1.2],"o", color=RED, ms=6)
    ax.text(-3,2.6, r"$C_R$", color=TEAL); ax.text(2.2,-0.3, r"$[-R,R]$", color=BLUE)
    ax.set_title(r"Standard upper semicircle for $\int_{-\infty}^{\infty}$", fontsize=12)
    save(fig, "ca-semicircle-contour.svg")

def fig_keyhole():
    fig, ax = plt.subplots(figsize=(5.0,4.6))
    axes_c(ax, 2.6)
    # keyhole: outer arc, inner arc, two rays
    t=np.linspace(0.08, 2*np.pi-0.08, 150)
    ax.plot(2.2*np.cos(t), 2.2*np.sin(t), color=BLUE, lw=2)
    ax.plot(0.35*np.cos(t), 0.35*np.sin(t), color=TEAL, lw=2)
    ax.plot([0.35,2.2],[0.04,0.08], color=ORANGE, lw=1.6)
    ax.plot([0.35,2.2],[-0.04,-0.08], color=ORANGE, lw=1.6)
    ax.plot([0],[0],"o", color=RED, ms=5)
    ax.text(-2.4,2.2, "keyhole / branch cut contour", color=GRAY, fontsize=10)
    ax.set_title(r"Contour for $x^{\alpha}$ integrals", fontsize=12)
    save(fig, "ca-keyhole.svg")

def fig_mobius():
    fig, axes = plt.subplots(1,2, figsize=(8.6,3.9))
    for ax in axes: axes_c(ax, 2.4)
    # left: upper half plane
    axes[0].add_patch(Rectangle((-2.3,0), 4.6, 2.2, facecolor=SHADE, edgecolor=BLUE, lw=1.3, alpha=0.6))
    axes[0].plot([-2.3,2.3],[0,0], color=ORANGE, lw=3)
    axes[0].plot([0],[1],"o", color=RED, ms=6); axes[0].text(0.1,1.15,r"$i$", color=RED)
    axes[0].set_title("Upper half-plane", fontsize=11)
    # right: unit disk
    axes[1].add_patch(Circle((0,0), 1.4, facecolor=SHADE, edgecolor=BLUE, lw=1.5, alpha=0.6))
    t=np.linspace(0,2*np.pi,100)
    axes[1].plot(1.4*np.cos(t), 1.4*np.sin(t), color=ORANGE, lw=2)
    axes[1].plot([0],[0],"o", color=RED, ms=6); axes[1].text(0.1,0.15,r"$0$", color=RED)
    axes[1].set_title(r"$w=(z-i)/(z+i)$", fontsize=11)
    fig.suptitle("Mobius: UHP <-> unit disk", y=1.02)
    save(fig, "ca-mobius-uhp-disk.svg")

def fig_conformal_local():
    fig, axes = plt.subplots(1,2, figsize=(8.4,3.8))
    for ax in axes: axes_c(ax, 2.2)
    # two curves crossing
    x=np.linspace(-1.5,1.5,50)
    axes[0].plot(x, 0.4*x, color=BLUE, lw=2)
    axes[0].plot(x, -0.8*x, color=TEAL, lw=2)
    axes[0].plot([0],[0],"o", color=RED, ms=6)
    axes[0].set_title(r"$z$-plane curves at $z_0$", fontsize=11)
    # image rotated/scaled
    axes[1].plot(x, 0.9*x+0.2*x**2*0, color=BLUE, lw=2)
    axes[1].plot(x, -0.3*x, color=TEAL, lw=2)
    axes[1].plot([0],[0],"o", color=RED, ms=6)
    axes[1].text(-2,1.8, r"multiply tangents by $f'(z_0)$", color=GRAY, fontsize=9)
    axes[1].set_title(r"$w=f(z)$ local similarity", fontsize=11)
    fig.suptitle("Conformal map preserves oriented angles", y=1.02)
    save(fig, "ca-conformal-local.svg")

def fig_argument_principle():
    fig, axes = plt.subplots(1,2, figsize=(8.6,3.9))
    for ax in axes: axes_c(ax, 2.4)
    t=np.linspace(0,2*np.pi,200)
    axes[0].plot(1.7*np.cos(t), 1.4*np.sin(t), color=BLUE, lw=2)
    axes[0].plot([-0.5],[0.4],"o", color=TEAL, ms=8); axes[0].text(-0.35,0.55,r"zero", color=TEAL)
    axes[0].plot([0.7],[-0.3],"x", color=RED, ms=10, mew=2); axes[0].text(0.85,-0.2,r"pole", color=RED)
    axes[0].set_title(r"$\gamma$ in $z$-plane", fontsize=11)
    # image winding
    axes[1].plot(1.2*np.cos(2*t)*np.cos(t), 1.2*np.cos(2*t)*np.sin(t), color=ORANGE, lw=2)  # approx limaçon-ish
    # better: circle around 0 twice-ish
    axes[1].plot(1.3*np.cos(t)+0.3*np.cos(2*t), 1.3*np.sin(t)+0.3*np.sin(2*t), color=ORANGE, lw=2)
    axes[1].plot([0],[0],"o", color=RED, ms=6)
    axes[1].text(-2.2,2.0, r"$\mathrm{Ind}(f\circ\gamma,0)=N-P$", color=BLUE, fontsize=10)
    axes[1].set_title(r"$f\circ\gamma$ winds about 0", fontsize=11)
    fig.suptitle("Argument principle", y=1.02)
    save(fig, "ca-argument-principle.svg")

def fig_nyquist():
    fig, axes = plt.subplots(1,2, figsize=(8.6,3.9))
    for ax in axes:
        ax.axhline(0,color=GRAY,lw=1); ax.axvline(0,color=GRAY,lw=1)
        for s in ax.spines.values(): s.set_visible(False)
        ax.set_xticks([]); ax.set_yticks([]); ax.set_aspect("equal")
    # right half-plane contour
    axes[0].set_xlim(-1,3); axes[0].set_ylim(-2.5,2.5)
    axes[0].plot([0,0],[-2.2,2.2], color=BLUE, lw=2)
    t=np.linspace(-np.pi/2,np.pi/2,80)
    axes[0].plot(2.2*np.cos(t), 2.2*np.sin(t), color=TEAL, lw=2)
    axes[0].text(0.1,2.0,r"$i\omega$", color=BLUE)
    axes[0].set_title("RHP Nyquist contour", fontsize=11)
    # Nyquist plot
    axes[1].set_xlim(-2.5,2.5); axes[1].set_ylim(-2.0,2.0)
    th=np.linspace(0.15, np.pi-0.15, 100)
    # typical D-contour image: loop left of -1
    x=-1.2+0.9*np.cos(th); y=1.1*np.sin(th)
    axes[1].plot(np.concatenate([x,x[::-1]]), np.concatenate([y,-y[::-1]]), color=ORANGE, lw=2)
    axes[1].plot([-1],[0], "x", color=RED, ms=10, mew=2)
    axes[1].text(-0.9,0.2,r"$-1$", color=RED)
    axes[1].set_title(r"Nyquist plot of $KG(i\omega)$", fontsize=11)
    fig.suptitle("Nyquist stability criterion", y=1.02)
    save(fig, "ca-nyquist.svg")

def fig_bromwich():
    fig, ax = plt.subplots(figsize=(5.0,4.6))
    ax.set_xlim(-3,2.5); ax.set_ylim(-3,3); ax.set_aspect("equal"); ax.axis("off")
    ax.axhline(0,color=GRAY,lw=1); ax.axvline(0,color=GRAY,lw=1)
    # Bromwich line
    ax.plot([0.8,0.8],[-2.6,2.6], color=BLUE, lw=2.2)
    ax.annotate("", xy=(0.8,1.5), xytext=(0.8,1.1), arrowprops=dict(arrowstyle="-|>", color=BLUE))
    # left arc
    t=np.linspace(np.pi/2, 3*np.pi/2, 100)
    ax.plot(0.8+2.4*np.cos(t), 2.4*np.sin(t), color=TEAL, lw=1.8)
    for p in [(-0.6,0.8),(-1.2,-0.5),(-0.3,-1.2)]:
        ax.plot([p[0]],[p[1]], "o", color=RED, ms=6)
    ax.text(0.95,2.3, r"$c+i\infty$", color=BLUE)
    ax.text(-2.8,2.4, r"$t>0$: close left", color=GRAY, fontsize=10)
    ax.text(0.9,-0.3, r"$\mathrm{Re}\,s=c$", color=BLUE, fontsize=10)
    ax.set_title("Bromwich inversion contour", fontsize=12)
    ax.text(-2.5,-2.7, r"$f(t)=\sum \mathrm{Res}(F(s)e^{st})$", color=BLUE, fontsize=10)
    save(fig, "ca-bromwich.svg")

def fig_gamma_poles():
    fig, ax = plt.subplots(figsize=(5.4,3.2))
    ax.set_xlim(-6.5,4); ax.set_ylim(-1.5,1.5); ax.set_aspect("equal"); ax.axis("off")
    ax.axhline(0,color=GRAY,lw=1); ax.axvline(0,color=GRAY,lw=1)
    ax.add_patch(Rectangle((0,-1.3), 3.8, 2.6, facecolor=SHADE, edgecolor=BLUE, lw=1.2, alpha=0.5))
    ax.text(1.2,1.0, r"$\mathrm{Re}\,z>0$", color=BLUE)
    for n in range(0,6):
        ax.plot([-n],[0], "x", color=RED, ms=9, mew=2)
    ax.text(-5.8,0.9, r"poles at $0,-1,-2,\ldots$", color=RED, fontsize=10)
    ax.annotate("", xy=(-2.5,0.3), xytext=(1.5,0.3), arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.5))
    ax.text(-1.2,0.45, r"$\Gamma(z)=\Gamma(z+1)/z$", color=ORANGE, fontsize=10)
    ax.set_title(r"Analytic continuation of $\Gamma(z)$", fontsize=12)
    save(fig, "ca-gamma-poles.svg")


def main():
    setup()
    fig_complex_plane()
    fig_triangle_inequality()
    fig_polar_form()
    fig_multiply_by_2i()
    fig_nth_roots()
    fig_exp_unit_circle()
    fig_map_z_squared()
    fig_map_exp()
    fig_arg_branches()
    fig_log_principal()
    fig_moc_roadmap()
    fig_open_disk()
    fig_limit_paths()
    fig_cr_directions()
    fig_not_diff_conj()
    fig_sqrt_branch_composition()
    fig_contour_cauchy()
    fig_cif()
    fig_harmonic_grid()
    fig_flow_gallery()
    fig_laurent_annulus()
    fig_residue_theorem()
    fig_semicircle()
    fig_keyhole()
    fig_mobius()
    fig_conformal_local()
    fig_argument_principle()
    fig_nyquist()
    fig_bromwich()
    fig_gamma_poles()
    print("done")


if __name__ == "__main__":
    main()
