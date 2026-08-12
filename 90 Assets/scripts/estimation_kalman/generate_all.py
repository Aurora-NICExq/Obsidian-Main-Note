#!/usr/bin/env python3
"""SVGs for Estimation and Kalman Filtering (NPTEL)."""
from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import FancyBboxPatch, Circle, Ellipse

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "90 Assets" / "diagrams" / "estimation-kalman"
BLUE, TEAL, RED, ORANGE, GRAY = "#2f5f8f", "#2a7a6b", "#a33b3b", "#c47a2c", "#666666"
SHADE, SHADE2 = "#d6e4f0", "#f0e6d6"


def setup():
    plt.rcParams.update({"font.size": 11, "axes.unicode_minus": False, "svg.fonttype": "none"})
    OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name):
    fig.savefig(OUT / name, format="svg", bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    print("wrote", name)


def box(ax, x, y, w, h, text, fc=SHADE, ec=BLUE, fs=10):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.02,rounding_size=0.08",
                                facecolor=fc, edgecolor=ec, lw=1.3))
    ax.text(x + w / 2, y + h / 2, text, ha="center", va="center", fontsize=fs, color=ec)


def arrow(ax, x0, y0, x1, y1, c=ORANGE):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle="-|>", color=c, lw=1.4, mutation_scale=11))


def fig_moc():
    fig, ax = plt.subplots(figsize=(9.8, 3.2))
    ax.set_xlim(0, 10); ax.set_ylim(0, 3.2); ax.axis("off")
    items = [(0.15, "Random\nprocess"), (2.2, "LMMSE &\ninnovations"), (4.25, "Kalman\nfilter"),
             (6.3, "Adaptive\n/ RLS"), (8.2, "Identifi-\ncation")]
    for i, (x, t) in enumerate(items):
        box(ax, x, 1.0, 1.85, 1.3, t, SHADE if i % 2 == 0 else SHADE2)
        if i < len(items) - 1:
            arrow(ax, x + 1.9, 1.65, items[i + 1][0] - 0.05, 1.65)
    ax.set_title("Estimation & Kalman roadmap", fontsize=13)
    save(fig, "ekf-moc-roadmap.svg")


def fig_kf_cycle():
    fig, ax = plt.subplots(figsize=(6.8, 3.6))
    ax.set_xlim(0, 10); ax.set_ylim(0, 4.2); ax.axis("off")
    box(ax, 0.4, 2.4, 2.8, 1.2, "Predict\nx̂⁻, P⁻", SHADE, BLUE)
    box(ax, 3.6, 2.4, 2.8, 1.2, "Update\nK, x̂, P", SHADE2, TEAL)
    box(ax, 6.8, 2.4, 2.8, 1.2, "Next time", SHADE, ORANGE)
    arrow(ax, 3.3, 3.0, 3.5, 3.0); arrow(ax, 6.5, 3.0, 6.7, 3.0)
    ax.text(5.0, 1.2, "x̂⁻ = F x̂,  P⁻ = FPFᵀ + Q\nK = P⁻Hᵀ(HP⁻Hᵀ+R)⁻¹", ha="center", fontsize=9, color=GRAY)
    ax.set_title("Kalman predict / update cycle", fontsize=12)
    save(fig, "ekf-kf-cycle.svg")


def fig_innovation():
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    ax.set_xlim(0, 10); ax.set_ylim(0, 3.4); ax.axis("off")
    box(ax, 0.4, 1.2, 2.4, 1.2, "y_k", SHADE)
    box(ax, 3.5, 1.2, 3.0, 1.2, "innovation\nν = y − H x̂⁻", SHADE2, TEAL)
    box(ax, 7.2, 1.2, 2.4, 1.2, "update x̂", SHADE, BLUE)
    arrow(ax, 2.9, 1.8, 3.4, 1.8); arrow(ax, 6.6, 1.8, 7.1, 1.8)
    ax.set_title("Innovation", fontsize=12)
    save(fig, "ekf-innovation.svg")


def fig_adaptive():
    fig, ax = plt.subplots(figsize=(6.6, 3.2))
    ax.set_xlim(0, 10); ax.set_ylim(0, 3.6); ax.axis("off")
    box(ax, 0.4, 1.3, 2.2, 1.2, "u[n]", SHADE2)
    box(ax, 3.2, 1.3, 3.4, 1.2, "adaptive w[n]\nLMS / RLS", SHADE, BLUE)
    box(ax, 7.3, 1.3, 2.3, 1.2, "e[n]", SHADE2, RED)
    arrow(ax, 2.7, 1.9, 3.1, 1.9); arrow(ax, 6.7, 1.9, 7.2, 1.9)
    ax.set_title("Adaptive filtering sketch", fontsize=12)
    save(fig, "ekf-adaptive.svg")


def fig_gauss():
    fig, ax = plt.subplots(figsize=(5.6, 3.4))
    x = np.linspace(-4, 4, 400)
    ax.plot(x, np.exp(-0.5 * x**2) / np.sqrt(2 * np.pi), color=BLUE, lw=2, label="prior")
    ax.plot(x, np.exp(-0.5 * (x - 1.2)**2 / 0.5) / np.sqrt(2 * np.pi * 0.5), color=TEAL, lw=2, label="likelihood-ish")
    ax.plot(x, np.exp(-0.5 * (x - 0.7)**2 / 0.35) / np.sqrt(2 * np.pi * 0.35), color=ORANGE, lw=2, label="posterior sketch")
    ax.legend(fontsize=9); ax.set_title("Gaussian update intuition", fontsize=12)
    ax.set_xlabel("x"); ax.set_yticks([])
    save(fig, "ekf-gaussian-update.svg")


def fig_ident():
    fig, ax = plt.subplots(figsize=(6.6, 3.2))
    ax.set_xlim(0, 10); ax.set_ylim(0, 3.6); ax.axis("off")
    box(ax, 0.4, 1.3, 2.4, 1.2, "u, y\ndata", SHADE)
    box(ax, 3.5, 1.3, 3.0, 1.2, "LS / RLS\nθ̂", SHADE2, TEAL)
    box(ax, 7.2, 1.3, 2.4, 1.2, "model\nvalidate", SHADE, ORANGE)
    arrow(ax, 2.9, 1.9, 3.4, 1.9); arrow(ax, 6.6, 1.9, 7.1, 1.9)
    ax.set_title("System identification flow", fontsize=12)
    save(fig, "ekf-identification.svg")


def fig_ekf():
    fig, ax = plt.subplots(figsize=(6.6, 3.2))
    ax.set_xlim(0, 10); ax.set_ylim(0, 3.6); ax.axis("off")
    box(ax, 0.4, 1.3, 2.8, 1.2, "nonlinear\nf, h", SHADE2, RED)
    box(ax, 3.8, 1.3, 2.8, 1.2, "linearize\nF, H @ x̂", SHADE, BLUE)
    box(ax, 7.2, 1.3, 2.4, 1.2, "KF step", SHADE2, TEAL)
    arrow(ax, 3.3, 1.9, 3.7, 1.9); arrow(ax, 6.7, 1.9, 7.1, 1.9)
    ax.set_title("EKF idea", fontsize=12)
    save(fig, "ekf-nonlinear.svg")


def main():
    setup()
    fig_moc(); fig_kf_cycle(); fig_innovation(); fig_adaptive()
    fig_gauss(); fig_ident(); fig_ekf()
    print("done ekf")


if __name__ == "__main__":
    main()
