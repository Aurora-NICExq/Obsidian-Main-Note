#!/usr/bin/env python3
"""SVGs for MIT 18.642 Mathematics with Applications in Finance."""
from __future__ import annotations
from pathlib import Path
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "90 Assets" / "diagrams" / "math-finance"
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
    items = [(0.15, "Markets\n& linear"), (2.2, "Stochastic\n& regression"), (4.25, "Rates &\nportfolio"),
             (6.3, "Vol &\nBS"), (8.2, "SDE &\nML")]
    for i, (x, t) in enumerate(items):
        box(ax, x, 1.0, 1.85, 1.3, t, SHADE if i % 2 == 0 else SHADE2)
        if i < len(items) - 1:
            arrow(ax, x + 1.9, 1.65, items[i + 1][0] - 0.05, 1.65)
    ax.set_title("MIT 18.642 roadmap", fontsize=13)
    save(fig, "mf-moc-roadmap.svg")


def fig_one_period():
    fig, ax = plt.subplots(figsize=(6.2, 3.0))
    ax.set_xlim(0, 8); ax.set_ylim(0, 3.4); ax.axis("off")
    box(ax, 0.4, 1.3, 2.2, 1.2, "t=0\nprices p", SHADE)
    box(ax, 3.2, 1.3, 2.4, 1.2, "portfolio θ", SHADE2, TEAL)
    box(ax, 6.2, 1.3, 1.5, 1.2, "payoff", SHADE, ORANGE)
    arrow(ax, 2.7, 1.9, 3.1, 1.9); arrow(ax, 5.7, 1.9, 6.1, 1.9)
    ax.set_title("One-period market model", fontsize=12)
    save(fig, "mf-one-period.svg")


def fig_portfolio():
    fig, ax = plt.subplots(figsize=(5.8, 3.6))
    # efficient frontier sketch
    s = np.linspace(0.05, 0.4, 200)
    mu = 0.02 + 0.8 * (s - 0.05) ** 0.7
    ax.plot(s, mu, color=BLUE, lw=2)
    ax.scatter([0.12], [0.08], color=TEAL, s=40, zorder=3)
    ax.scatter([0.22], [0.12], color=ORANGE, s=40, zorder=3)
    ax.set_xlabel("σ"); ax.set_ylabel("E[r]")
    ax.set_title("Mean–variance frontier sketch", fontsize=12)
    save(fig, "mf-portfolio.svg")


def fig_bs():
    fig, ax = plt.subplots(figsize=(6.4, 3.2))
    ax.set_xlim(0, 10); ax.set_ylim(0, 3.6); ax.axis("off")
    box(ax, 0.3, 1.3, 2.6, 1.2, "dS = μS dt\n+ σS dW", SHADE2, TEAL)
    box(ax, 3.5, 1.3, 3.0, 1.2, "risk-neutral\nμ→r", SHADE, BLUE)
    box(ax, 7.2, 1.3, 2.4, 1.2, "BS call\nC(S,t)", SHADE2, ORANGE)
    arrow(ax, 3.0, 1.9, 3.4, 1.9); arrow(ax, 6.6, 1.9, 7.1, 1.9)
    ax.set_title("Black–Scholes path", fontsize=12)
    save(fig, "mf-black-scholes.svg")


def fig_vol():
    fig, ax = plt.subplots(figsize=(5.8, 3.2))
    t = np.arange(80)
    rng = np.random.default_rng(0)
    e = rng.normal(0, 1, size=80)
    r = np.zeros(80); h = np.zeros(80); h[0] = 0.02
    for i in range(1, 80):
        h[i] = 0.0001 + 0.1 * e[i - 1] ** 2 * h[i - 1] + 0.85 * h[i - 1]
        r[i] = np.sqrt(h[i]) * e[i]
    ax.plot(t, r, color=BLUE, lw=1.0)
    ax.set_title("Returns with clustered volatility", fontsize=12)
    ax.set_xlabel("t"); ax.set_ylabel("r_t")
    save(fig, "mf-volatility.svg")


def fig_ts():
    fig, ax = plt.subplots(figsize=(5.8, 3.0))
    t = np.arange(100)
    rng = np.random.default_rng(1)
    x = np.cumsum(rng.normal(0, 1, 100)) * 0.3
    ax.plot(t, x, color=TEAL, lw=1.2)
    ax.set_title("Financial time series sketch", fontsize=12)
    save(fig, "mf-timeseries.svg")


def fig_sde():
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    ax.set_xlim(0, 10); ax.set_ylim(0, 3.4); ax.axis("off")
    box(ax, 1.5, 1.2, 7.0, 1.4, "dX = a(X,t) dt + b(X,t) dW\nItô calculus", SHADE, BLUE, 11)
    ax.set_title("SDE intuition", fontsize=12)
    save(fig, "mf-sde.svg")


def main():
    setup()
    fig_moc(); fig_one_period(); fig_portfolio(); fig_bs()
    fig_vol(); fig_ts(); fig_sde()
    print("done mf")


if __name__ == "__main__":
    main()
