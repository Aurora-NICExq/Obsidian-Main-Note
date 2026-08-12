#!/usr/bin/env python3
"""SVGs for MIT 15.450 Analytics of Finance."""
from __future__ import annotations
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "90 Assets" / "diagrams" / "analytics-finance"
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
    items = [(0.15, "RN &\nItô/BS"), (2.2, "Rates &\nDP"), (4.25, "Monte\nCarlo"),
             (6.3, "Econometrics\nGMM"), (8.2, "GARCH\n& pred.")]
    for i, (x, t) in enumerate(items):
        box(ax, x, 1.0, 1.85, 1.3, t, SHADE if i % 2 == 0 else SHADE2)
        if i < len(items) - 1:
            arrow(ax, x + 1.9, 1.65, items[i + 1][0] - 0.05, 1.65)
    ax.set_title("MIT 15.450 roadmap", fontsize=13)
    save(fig, "af-moc-roadmap.svg")


def fig_rn():
    fig, ax = plt.subplots(figsize=(6.6, 3.2))
    ax.set_xlim(0, 10); ax.set_ylim(0, 3.6); ax.axis("off")
    box(ax, 0.3, 1.3, 2.8, 1.2, "no arbitrage", SHADE2, TEAL)
    box(ax, 3.6, 1.3, 3.0, 1.2, "∃ Q ~ P\nrisk-neutral", SHADE, BLUE)
    box(ax, 7.2, 1.3, 2.4, 1.2, "price =\nE^Q[payoff]", SHADE2, ORANGE)
    arrow(ax, 3.2, 1.9, 3.5, 1.9); arrow(ax, 6.7, 1.9, 7.1, 1.9)
    ax.set_title("FTAP sketch", fontsize=12)
    save(fig, "af-risk-neutral.svg")


def fig_mc():
    fig, ax = plt.subplots(figsize=(5.8, 3.4))
    rng = np.random.default_rng(2)
    t = np.linspace(0, 1, 50)
    for _ in range(12):
        w = np.cumsum(rng.normal(0, np.sqrt(1 / 49), 50))
        s = 100 * np.exp((0.05 - 0.5 * 0.2**2) * t + 0.2 * w)
        ax.plot(t, s, color=BLUE, alpha=0.35, lw=1)
    ax.set_title("GBM Monte Carlo paths", fontsize=12)
    ax.set_xlabel("t"); ax.set_ylabel("S")
    save(fig, "af-monte-carlo.svg")


def fig_dp():
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    ax.set_xlim(0, 10); ax.set_ylim(0, 3.4); ax.axis("off")
    box(ax, 0.4, 1.2, 2.6, 1.2, "wealth W_t", SHADE)
    box(ax, 3.6, 1.2, 3.0, 1.2, "π_t allocation\nBellman", SHADE2, TEAL)
    box(ax, 7.2, 1.2, 2.4, 1.2, "max E[U]", SHADE, ORANGE)
    arrow(ax, 3.1, 1.8, 3.5, 1.8); arrow(ax, 6.7, 1.8, 7.1, 1.8)
    ax.set_title("Dynamic portfolio choice", fontsize=12)
    save(fig, "af-dynamic-opt.svg")


def fig_gmm():
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    ax.set_xlim(0, 10); ax.set_ylim(0, 3.4); ax.axis("off")
    box(ax, 0.5, 1.2, 2.8, 1.2, "moments\nE[g(θ)]=0", SHADE)
    box(ax, 4.0, 1.2, 2.6, 1.2, "GMM / OLS", SHADE2, TEAL)
    box(ax, 7.3, 1.2, 2.2, 1.2, "θ̂, SE", SHADE, BLUE)
    arrow(ax, 3.4, 1.8, 3.9, 1.8); arrow(ax, 6.7, 1.8, 7.2, 1.8)
    ax.set_title("GMM estimation sketch", fontsize=12)
    save(fig, "af-gmm.svg")


def fig_garch():
    fig, ax = plt.subplots(figsize=(5.8, 3.2))
    t = np.arange(100)
    rng = np.random.default_rng(3)
    e = rng.normal(size=100)
    h = np.zeros(100); r = np.zeros(100); h[0] = 0.01
    for i in range(1, 100):
        h[i] = 1e-4 + 0.08 * r[i - 1] ** 2 + 0.9 * h[i - 1]
        r[i] = np.sqrt(h[i]) * e[i]
    ax.plot(t, np.sqrt(h), color=RED, lw=1.2)
    ax.set_title("GARCH conditional σ_t", fontsize=12)
    ax.set_xlabel("t"); ax.set_ylabel("σ_t")
    save(fig, "af-garch.svg")


def main():
    setup()
    fig_moc(); fig_rn(); fig_mc(); fig_dp(); fig_gmm(); fig_garch()
    print("done af")


if __name__ == "__main__":
    main()
