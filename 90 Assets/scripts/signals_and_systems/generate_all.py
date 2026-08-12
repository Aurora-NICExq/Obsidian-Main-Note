#!/usr/bin/env python3
"""Generate SVGs for Signals and Systems notes.

Usage (from vault root or this directory):
  .venv/bin/python generate_all.py

Outputs to: 90 Assets/diagrams/signals-and-systems/
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle

ROOT = Path(__file__).resolve().parents[3]  # vault root (…/90 Assets/scripts/signals_and_systems -> up 3)
OUT = ROOT / "90 Assets" / "diagrams" / "signals-and-systems"

# Style
BLUE = "#2f5f8f"
TEAL = "#2a7a6b"
RED = "#a33b3b"
GRAY = "#666666"
LIGHT = "#aaaaaa"


def setup():
    plt.rcParams.update(
        {
            "font.size": 11,
            "axes.linewidth": 1.1,
            "mathtext.fontset": "dejavusans",
            "svg.fonttype": "none",  # editable text in SVG
        }
    )
    OUT.mkdir(parents=True, exist_ok=True)


def save(fig, name: str):
    path = OUT / name
    fig.savefig(path, format="svg", bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    print("wrote", path.relative_to(ROOT))


def axis_xy(ax, xmin, xmax, ymin, ymax, xlabel="", ylabel=""):
    ax.set_xlim(xmin, xmax)
    ax.set_ylim(ymin, ymax)
    ax.set_aspect("auto")
    ax.axhline(0, color=GRAY, lw=1)
    ax.axvline(0, color=GRAY, lw=1)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_position("zero")
    ax.spines["bottom"].set_position("zero")
    ax.spines["left"].set_color(GRAY)
    ax.spines["bottom"].set_color(GRAY)
    ax.tick_params(colors=GRAY)
    if xlabel:
        ax.set_xlabel(xlabel, loc="right")
    if ylabel:
        ax.set_ylabel(ylabel, loc="top", rotation=0)


def stem(ax, xs, ys, color=BLUE, label=None):
    markerline, stemlines, baseline = ax.stem(xs, ys, linefmt="-", markerfmt="o", basefmt=" ")
    plt.setp(stemlines, color=color, linewidth=1.8)
    plt.setp(markerline, color=color, markersize=5)
    if label:
        markerline.set_label(label)


# ---------- Unit Step / Impulse ----------


def fig_ct_step():
    fig, ax = plt.subplots(figsize=(5.2, 2.6))
    t = np.linspace(-2.2, 3.2, 400)
    y = np.where(t >= 0, 1.0, 0.0)
    ax.plot(t[t < 0], y[t < 0], color=BLUE, lw=2.2)
    ax.plot(t[t >= 0], y[t >= 0], color=BLUE, lw=2.2)
    ax.plot([0, 0], [0, 1], color=BLUE, lw=2.2, ls="--")
    ax.plot(0, 1, "o", color=BLUE, ms=6)
    axis_xy(ax, -2.2, 3.2, -0.2, 1.6)
    ax.set_yticks([1])
    ax.set_xticks([0])
    ax.text(0.15, 1.05, r"$1$", color=BLUE)
    ax.set_title(r"$u(t)$")
    ax.set_xlabel(r"$t$")
    save(fig, "ss-unit-step-ct.svg")


def fig_pulse_approx():
    fig, axes = plt.subplots(1, 2, figsize=(8.5, 2.8))
    ax = axes[0]
    ax.plot([-1, 0, 0.9, 2.5], [0, 0, 1.0, 1.0], color=TEAL, lw=2.2)
    axis_xy(ax, -1.2, 2.6, -0.15, 1.35)
    ax.annotate("", xy=(0.9, -0.08), xytext=(0, -0.08), arrowprops=dict(arrowstyle="<->", color=GRAY))
    ax.text(0.35, -0.22, r"$\Delta$", color=GRAY)
    ax.set_title(r"$u_\Delta(t)$")
    ax.set_xlabel(r"$t$")

    ax = axes[1]
    ax.plot([-1, 0, 0, 0.9, 0.9, 2.5], [0, 0, 1.2, 1.2, 0, 0], color=RED, lw=2.2)
    axis_xy(ax, -1.2, 2.6, -0.15, 1.5)
    ax.text(-0.05, 1.25, r"$1/\Delta$", ha="right", color=RED)
    ax.annotate("", xy=(0.9, -0.08), xytext=(0, -0.08), arrowprops=dict(arrowstyle="<->", color=GRAY))
    ax.text(0.35, -0.22, r"$\Delta$", color=GRAY)
    ax.set_title(r"$\delta_\Delta(t)$")
    ax.set_xlabel(r"$t$")
    fig.tight_layout()
    save(fig, "ss-impulse-approx.svg")


def fig_ct_impulse():
    fig, ax = plt.subplots(figsize=(5.0, 2.6))
    axis_xy(ax, -2.0, 3.0, -0.2, 1.6)
    ax.annotate("", xy=(0, 1.35), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=BLUE, lw=2.2))
    ax.text(0.12, 1.25, r"$1$", color=BLUE)
    ax.set_title(r"$\delta(t)$")
    ax.set_xlabel(r"$t$")
    ax.set_xticks([0])
    save(fig, "ss-unit-impulse-ct.svg")


def fig_dt_impulse_step():
    fig, axes = plt.subplots(1, 2, figsize=(9.0, 2.8))
    ax = axes[0]
    ns = np.arange(-3, 6)
    ys = (ns == 0).astype(float)
    stem(ax, ns, ys, BLUE)
    axis_xy(ax, -3.5, 5.5, -0.2, 1.5)
    ax.set_title(r"$\delta[n]$")
    ax.set_xlabel(r"$n$")
    ax.text(0.2, 1.05, r"$1$", color=BLUE)

    ax = axes[1]
    ys = (ns >= 0).astype(float)
    stem(ax, ns, ys, TEAL)
    axis_xy(ax, -3.5, 5.5, -0.2, 1.5)
    ax.set_title(r"$u[n]$")
    ax.set_xlabel(r"$n$")
    ax.text(-0.35, 1.05, r"$1$", color=TEAL, ha="right")
    fig.tight_layout()
    save(fig, "ss-impulse-step-dt.svg")


# ---------- Sinusoidal / Exponential ----------


def fig_ct_cosine():
    fig, ax = plt.subplots(figsize=(6.5, 3.0))
    t = np.linspace(0, 6.2, 500)
    w0 = 1.05
    y = 1.4 * np.cos(w0 * t)
    ax.plot(t, y, color=BLUE, lw=2.2)
    ax.axhline(1.4, color=LIGHT, ls="--", lw=1)
    ax.axhline(-1.4, color=LIGHT, ls="--", lw=1)
    axis_xy(ax, -0.2, 6.5, -1.9, 1.9)
    ax.text(-0.15, 1.4, r"$A$", ha="right", va="center")
    ax.text(-0.15, -1.4, r"$-A$", ha="right", va="center")
    T0 = 2 * np.pi / w0
    ax.annotate("", xy=(T0, -1.65), xytext=(0, -1.65), arrowprops=dict(arrowstyle="<->", color=GRAY))
    ax.text(T0 / 2, -1.82, r"$T_0$", ha="center", color=GRAY)
    ax.text(4.2, 1.5, r"$A\cos(\omega_0 t)$", color=BLUE)
    ax.set_xlabel(r"$t$")
    ax.set_ylabel(r"$x(t)$", rotation=0, labelpad=15)
    save(fig, "ss-cosine-ct.svg")


def fig_dt_cosine():
    fig, ax = plt.subplots(figsize=(6.5, 2.8))
    n = np.arange(0, 13)
    y = 1.35 * np.cos(np.deg2rad(30) * n)
    stem(ax, n, y, BLUE)
    axis_xy(ax, -0.5, 12.5, -1.7, 1.8)
    ax.text(8.5, 1.4, r"$A\cos(\Omega_0 n)$", color=BLUE)
    ax.set_xlabel(r"$n$")
    ax.set_ylabel(r"$x[n]$", rotation=0, labelpad=15)
    save(fig, "ss-cosine-dt.svg")


def fig_real_exp():
    fig, axes = plt.subplots(1, 2, figsize=(8.5, 2.8))
    t = np.linspace(0, 3.2, 200)
    axes[0].plot(t, 0.35 * np.exp(0.55 * t), color=RED, lw=2.2)
    axis_xy(axes[0], -0.15, 3.4, -0.1, 2.5)
    axes[0].text(1.5, 2.1, r"$a>0$", color=RED)
    axes[0].set_title(r"$e^{at}$ growth")
    axes[0].set_xlabel(r"$t$")

    axes[1].plot(t, 2.2 * np.exp(-0.7 * t), color=TEAL, lw=2.2)
    axis_xy(axes[1], -0.15, 3.4, -0.1, 2.5)
    axes[1].text(1.5, 1.3, r"$a<0$", color=TEAL)
    axes[1].set_title(r"$e^{at}$ decay")
    axes[1].set_xlabel(r"$t$")
    fig.tight_layout()
    save(fig, "ss-real-exponential.svg")


# ---------- System blocks ----------


def fig_system_box():
    fig, ax = plt.subplots(figsize=(5.5, 1.8))
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 2)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.annotate("", xy=(1.3, 1), xytext=(0.2, 1), arrowprops=dict(arrowstyle="->", color="k", lw=1.6))
    ax.text(0.7, 1.25, r"$x$", ha="center")
    ax.add_patch(FancyBboxPatch((1.4, 0.55), 2.2, 0.9, boxstyle="round,pad=0.02", fill=False, lw=1.6))
    ax.text(2.5, 1.0, "System", ha="center", va="center")
    ax.annotate("", xy=(4.9, 1), xytext=(3.7, 1), arrowprops=dict(arrowstyle="->", color="k", lw=1.6))
    ax.text(4.3, 1.25, r"$y$", ha="center")
    save(fig, "ss-system-box.svg")


def fig_parallel():
    fig, ax = plt.subplots(figsize=(7.2, 3.2))
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 4)
    ax.set_aspect("equal")
    ax.axis("off")
    # split
    ax.annotate("", xy=(1.2, 2), xytext=(0.2, 2), arrowprops=dict(arrowstyle="->", color="k", lw=1.5))
    ax.text(0.6, 2.25, r"$x$", ha="center")
    ax.plot([1.2, 1.2], [1.0, 3.0], "k-", lw=1.3)
    ax.plot(1.2, 2, "ko", ms=4)
    ax.annotate("", xy=(2.2, 3.0), xytext=(1.2, 3.0), arrowprops=dict(arrowstyle="->", color="k", lw=1.5))
    ax.annotate("", xy=(2.2, 1.0), xytext=(1.2, 1.0), arrowprops=dict(arrowstyle="->", color="k", lw=1.5))
    ax.text(1.7, 3.2, r"$x_1$", ha="center", fontsize=10)
    ax.text(1.7, 0.7, r"$x_2$", ha="center", fontsize=10)
    ax.add_patch(Rectangle((2.3, 2.55), 2.0, 0.9, fill=False, lw=1.5))
    ax.add_patch(Rectangle((2.3, 0.55), 2.0, 0.9, fill=False, lw=1.5))
    ax.text(3.3, 3.0, "System 1", ha="center", va="center", fontsize=10)
    ax.text(3.3, 1.0, "System 2", ha="center", va="center", fontsize=10)
    ax.annotate("", xy=(5.2, 3.0), xytext=(4.4, 3.0), arrowprops=dict(arrowstyle="->", color="k", lw=1.5))
    ax.annotate("", xy=(5.2, 1.0), xytext=(4.4, 1.0), arrowprops=dict(arrowstyle="->", color="k", lw=1.5))
    ax.text(4.8, 3.25, r"$y_1$", fontsize=10)
    ax.text(4.8, 0.7, r"$y_2$", fontsize=10)
    ax.plot([5.2, 5.7], [3.0, 3.0], "k-", lw=1.3)
    ax.plot([5.2, 5.7], [1.0, 1.0], "k-", lw=1.3)
    ax.plot([5.7, 5.7], [1.0, 3.0], "k-", lw=1.3)
    ax.add_patch(Circle((6.15, 2.0), 0.28, fill=False, lw=1.5))
    ax.text(6.15, 2.0, "+", ha="center", va="center")
    ax.annotate("", xy=(7.4, 2.0), xytext=(6.45, 2.0), arrowprops=dict(arrowstyle="->", color="k", lw=1.5))
    ax.text(6.9, 2.25, r"$y$", ha="center")
    save(fig, "ss-system-parallel.svg")


# ---------- Analog / Digital h ----------


def fig_memoryless_h():
    fig, axes = plt.subplots(1, 2, figsize=(8.5, 2.6))
    ax = axes[0]
    axis_xy(ax, -1.5, 2.5, -0.2, 1.7)
    ax.annotate("", xy=(0, 1.4), xytext=(0, 0), arrowprops=dict(arrowstyle="->", color=BLUE, lw=2))
    ax.text(0.15, 1.3, r"$k$", color=BLUE)
    ax.set_title(r"C-T: $h(t)=k\delta(t)$")
    ax.set_xlabel(r"$t$")

    ax = axes[1]
    ns = np.arange(-2, 3)
    ys = (ns == 0).astype(float) * 1.0
    # scale visual height
    stem(ax, ns, ys * 1.35, TEAL)
    axis_xy(ax, -2.5, 2.5, -0.2, 1.7)
    ax.text(0.2, 1.35, r"$k$", color=TEAL)
    ax.set_title(r"D-T: $h[n]=k\delta[n]$")
    ax.set_xlabel(r"$n$")
    fig.tight_layout()
    save(fig, "ss-memoryless-h.svg")


# ---------- Convolution ----------


def fig_pulse_decomp():
    fig, axes = plt.subplots(2, 1, figsize=(5.5, 4.2), sharex=True)
    ax = axes[0]
    ns = np.arange(-2, 4)
    ys = (ns == 0).astype(float)
    stem(ax, ns, ys * 1.4, BLUE)
    axis_xy(ax, -2.5, 3.5, -0.2, 1.8)
    ax.text(0.15, 1.5, r"$x[0]$", color=BLUE)
    ax.text(1.2, 1.1, r"$x[0]\delta[n]$", color=BLUE)
    ax.set_ylabel(r"$n$", rotation=0)

    ax = axes[1]
    ys = (ns == 1).astype(float)
    stem(ax, ns, ys * 1.4, TEAL)
    axis_xy(ax, -2.5, 3.5, -0.2, 1.8)
    ax.text(1.15, 1.5, r"$x[1]$", color=TEAL)
    ax.text(1.9, 1.1, r"$x[1]\delta[n-1]$", color=TEAL)
    ax.set_xlabel(r"$n$")
    fig.tight_layout()
    save(fig, "ss-pulse-decomposition.svg")


def fig_conv_flip_slide():
    fig, axes = plt.subplots(3, 1, figsize=(6.2, 5.5), sharex=True)
    k = np.arange(-3, 8)

    # x[k] step
    ax = axes[0]
    yx = (k >= 0).astype(float)
    stem(ax, k, yx * 1.1, BLUE)
    axis_xy(ax, -3.5, 7.5, -0.2, 1.5)
    ax.set_ylabel(r"$x[k]$", rotation=0, labelpad=20)

    # h[n-k] flipped exp-like
    ax = axes[1]
    vals = { -1: 0.25, 0: 0.4, 1: 0.6, 2: 0.85, 3: 1.15 }
    yh = np.array([vals.get(int(i), 0.0) for i in k])
    stem(ax, k, yh, TEAL)
    axis_xy(ax, -3.5, 7.5, -0.2, 1.5)
    ax.axvline(3, color=LIGHT, ls="--", lw=1)
    ax.text(3.1, -0.15, r"$n$", color=GRAY)
    ax.set_ylabel(r"$h[n-k]$", rotation=0, labelpad=28)

    # y[n]
    ax = axes[2]
    yn_map = {0: 0.35, 1: 0.6, 2: 0.85, 3: 1.05, 4: 1.2, 5: 1.28, 6: 1.32, 7: 1.35}
    yy = np.array([yn_map.get(int(i), 0.0) for i in k])
    stem(ax, k, yy, RED)
    axis_xy(ax, -3.5, 7.5, -0.2, 1.6)
    ax.set_ylabel(r"$y[n]$", rotation=0, labelpad=20)
    ax.set_xlabel(r"$k$ / $n$")
    fig.tight_layout()
    save(fig, "ss-convolution-flip-slide.svg")


def fig_step_response_geom():
    fig, ax = plt.subplots(figsize=(5.8, 2.8))
    n = np.arange(0, 9)
    a = 0.4
    y = (1 - a ** (n + 1)) / (1 - a)
    asympt = 1 / (1 - a)
    stem(ax, n, y, RED)
    ax.axhline(asympt, color=LIGHT, ls="--", lw=1.2)
    ax.text(8.2, asympt, r"$1/(1-\alpha)$", color=GRAY, va="center")
    axis_xy(ax, -0.8, 9.0, -0.15, asympt + 0.35)
    ax.set_xlabel(r"$n$")
    ax.set_ylabel(r"$y[n]$", rotation=0, labelpad=18)
    ax.set_title(r"Step response $y[n]=(1-\alpha^{n+1})/(1-\alpha)$")
    save(fig, "ss-step-response-geometric.svg")


# ---------- CTFS ----------


def fig_ctfs_spectrum():
    fig, ax = plt.subplots(figsize=(5.8, 2.8))
    ks = np.array([-5, -3, -1, 1, 3, 5])
    hs = np.array([0.35, 0.55, 1.5, 1.5, 0.55, 0.35])
    stem(ax, ks, hs, BLUE)
    zeros = np.array([-4, -2, 0, 2, 4])
    ax.plot(zeros, np.zeros_like(zeros), "o", color=LIGHT, ms=4)
    axis_xy(ax, -6, 6, -0.2, 2.0)
    ax.set_xlabel(r"$k$")
    ax.set_ylabel(r"$|a_k|$", rotation=0, labelpad=18)
    ax.set_title("CTFS magnitude (sketch)")
    save(fig, "ss-ctfs-spectrum.svg")


def fig_ctfs_odd_square():
    fig, ax = plt.subplots(figsize=(5.8, 3.0))
    pos = [(1, 1.8, "2"), (3, 0.6, r"$2/3$"), (5, 0.36, r"$2/5$")]
    neg = [(-1, -1.8), (-3, -0.6), (-5, -0.36)]
    for k, h, lab in pos:
        ax.plot([k, k], [0, h], color=TEAL, lw=2)
        ax.plot(k, h, "o", color=TEAL, ms=5)
        ax.text(k, h + 0.12, lab, ha="center", color=TEAL, fontsize=9)
    for k, h in neg:
        ax.plot([k, k], [0, h], color=TEAL, lw=2)
        ax.plot(k, h, "o", color=TEAL, ms=5)
    for k in [-4, -2, 0, 2, 4]:
        ax.plot(k, 0, "o", color=LIGHT, ms=4)
    axis_xy(ax, -6, 6, -2.2, 2.4)
    ax.set_xlabel(r"$k$")
    ax.set_ylabel(r"$j\pi a_k$", rotation=0, labelpad=22)
    ax.set_title("Odd-harmonic square wave (nonzero at odd $k$)")
    save(fig, "ss-ctfs-odd-square.svg")


def fig_gibbs():
    fig, axes = plt.subplots(2, 1, figsize=(6.2, 4.2), sharex=True)
    ax = axes[0]
    ax.plot([0.3, 0.3, 1.8, 1.8, 3.3, 3.3, 4.8], [-1, 1, 1, -1, -1, 1, 1], color=BLUE, lw=2.2)
    axis_xy(ax, 0, 5.2, -1.4, 1.5)
    ax.set_title("Ideal square wave")
    ax.set_ylabel(r"$x(t)$", rotation=0, labelpad=15)

    ax = axes[1]
    t = np.linspace(0.3, 4.8, 800)
    # truncated odd-harmonic square-ish
    u = t - 0.3
    y = (
        1.05 * np.sin(2.2 * u)
        + 0.35 * np.sin(6.6 * u)
        + 0.22 * np.sin(11 * u)
        + 0.15 * np.sin(15.4 * u)
    )
    ax.plot(t, y, color=TEAL, lw=2.0)
    axis_xy(ax, 0, 5.2, -1.5, 1.6)
    ax.set_title("Partial-sum approx. (Gibbs ripples)")
    ax.set_xlabel(r"$t$")
    fig.tight_layout()
    save(fig, "ss-gibbs-phenomenon.svg")


# ---------- CTFT ----------


def fig_period_extension():
    fig, axes = plt.subplots(2, 1, figsize=(6.5, 4.0))
    ax = axes[0]
    ax.plot([-0.7, -0.7, 0.7, 0.7], [0, 1.2, 1.2, 0], color=BLUE, lw=2.2)
    axis_xy(ax, -2.5, 2.5, -0.2, 1.6)
    ax.text(-0.7, -0.18, r"$-T_1$", ha="center", fontsize=9)
    ax.text(0.7, -0.18, r"$T_1$", ha="center", fontsize=9)
    ax.set_title(r"$x(t)$ (one pulse)")
    ax.set_xlabel(r"$t$")

    ax = axes[1]
    for c in [-3.0, 0.0, 3.0]:
        ax.plot([c - 0.6, c - 0.6, c + 0.6, c + 0.6], [0, 1.1, 1.1, 0], color=BLUE, lw=2.0)
    axis_xy(ax, -4.5, 4.5, -0.25, 1.5)
    ax.annotate("", xy=(2.4, -0.15), xytext=(-0.6, -0.15), arrowprops=dict(arrowstyle="<->", color=GRAY))
    ax.text(0.9, -0.32, r"$T_0$", ha="center", color=GRAY)
    ax.set_title(r"Periodic extension $\tilde{x}(t)$")
    ax.set_xlabel(r"$t$")
    fig.tight_layout()
    save(fig, "ss-ctft-period-extension.svg")


def _sinc_env(w):
    # |sinc|-like positive envelope sketch
    return np.abs(np.sinc(w / np.pi)) * 2.2 + 0.05


def fig_envelope_sparse():
    fig, ax = plt.subplots(figsize=(6.8, 3.0))
    w = np.linspace(-5.2, 5.2, 600)
    env = _sinc_env(w)
    ax.plot(w, env, color=LIGHT, lw=1.6)
    ks = np.array([-4, -2, 0, 2, 4], dtype=float)
    stem(ax, ks, _sinc_env(ks), BLUE)
    axis_xy(ax, -5.5, 5.5, -0.15, 2.6)
    ax.annotate("", xy=(2, -0.08), xytext=(0, -0.08), arrowprops=dict(arrowstyle="<->", color=GRAY))
    ax.text(1.0, -0.28, r"$\omega_0$", ha="center", color=GRAY)
    ax.set_title(r"Sparse samples (larger $\omega_0$)")
    ax.set_xlabel(r"$\omega$")
    ax.set_ylabel(r"$|X|$", rotation=0, labelpad=15)
    save(fig, "ss-ctft-envelope-sparse.svg")


def fig_envelope_dense():
    fig, ax = plt.subplots(figsize=(6.8, 3.0))
    w = np.linspace(-5.2, 5.2, 600)
    ax.plot(w, _sinc_env(w), color=LIGHT, lw=1.6)
    ks = np.arange(-4.5, 5.0, 0.5)
    stem(ax, ks, _sinc_env(ks), TEAL)
    axis_xy(ax, -5.5, 5.5, -0.15, 2.6)
    ax.annotate("", xy=(0.5, -0.08), xytext=(0, -0.08), arrowprops=dict(arrowstyle="<->", color=GRAY))
    ax.text(0.25, -0.28, r"$\omega_0$", ha="center", color=GRAY)
    ax.set_title(r"Dense samples (smaller $\omega_0$)")
    ax.set_xlabel(r"$\omega$")
    ax.set_ylabel(r"$|X|$", rotation=0, labelpad=15)
    save(fig, "ss-ctft-envelope-dense.svg")


def fig_bode():
    fig, ax = plt.subplots(figsize=(6.2, 3.0))
    # sketch: flat then -20 dB/dec on log-x
    ax.plot([0.1, 1.0, 100], [0, 0, -40], color=BLUE, lw=2.2)
    ax.set_xscale("log")
    ax.set_xlim(0.08, 120)
    ax.set_ylim(-45, 8)
    ax.axvline(1.0, color=LIGHT, ls="--", lw=1)
    ax.text(1.2, -42, r"$\omega\sim a$", color=GRAY)
    ax.text(20, -18, r"$-20$ dB/dec", color=BLUE)
    ax.set_xlabel(r"$\omega$ (log scale)")
    ax.set_ylabel("dB")
    ax.set_title(r"Bode magnitude sketch: $20\log_{10}|1/(a+j\omega)|$")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.grid(True, which="both", ls=":", alpha=0.4)
    save(fig, "ss-ctft-bode.svg")


def main():
    setup()
    fig_ct_step()
    fig_pulse_approx()
    fig_ct_impulse()
    fig_dt_impulse_step()
    fig_ct_cosine()
    fig_dt_cosine()
    fig_real_exp()
    fig_system_box()
    fig_parallel()
    fig_memoryless_h()
    fig_pulse_decomp()
    fig_conv_flip_slide()
    fig_step_response_geom()
    fig_ctfs_spectrum()
    fig_ctfs_odd_square()
    fig_gibbs()
    fig_period_extension()
    fig_envelope_sparse()
    fig_envelope_dense()
    fig_bode()
    print(f"done -> {OUT}")


if __name__ == "__main__":
    main()
