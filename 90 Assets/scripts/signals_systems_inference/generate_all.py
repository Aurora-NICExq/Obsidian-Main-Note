#!/usr/bin/env python3
"""SVGs for Signals, Systems and Inference (MIT 6.011)."""
from __future__ import annotations
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "90 Assets" / "diagrams" / "signals-systems-inference"
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
    items = [(0.2, "State-space\n& control"), (2.3, "LMMSE\nestimation"), (4.4, "WSS &\nPSD"),
             (6.5, "Wiener\nfilter"), (8.3, "Detect &\nmatched")]
    for i, (x, t) in enumerate(items):
        box(ax, x, 1.0, 1.8, 1.3, t, SHADE if i % 2 == 0 else SHADE2)
        if i < len(items) - 1:
            arrow(ax, x + 1.85, 1.65, items[i + 1][0] - 0.05, 1.65)
    ax.set_title("MIT 6.011 roadmap", fontsize=13)
    save(fig, "ssi-moc-roadmap.svg")


def fig_state_space():
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    ax.set_xlim(0, 10); ax.set_ylim(0, 3.5); ax.axis("off")
    box(ax, 0.3, 1.2, 1.8, 1.2, "u", SHADE2, TEAL)
    box(ax, 3.0, 1.2, 4.0, 1.2, "ẋ = Ax + Bu\ny = Cx + Du", SHADE, BLUE)
    box(ax, 7.8, 1.2, 1.8, 1.2, "y", SHADE2, RED)
    arrow(ax, 2.2, 1.8, 2.9, 1.8); arrow(ax, 7.1, 1.8, 7.7, 1.8)
    ax.set_title("State-space LTI model", fontsize=12)
    save(fig, "ssi-state-space.svg")


def fig_observer():
    fig, ax = plt.subplots(figsize=(6.8, 3.4))
    ax.set_xlim(0, 10); ax.set_ylim(0, 4); ax.axis("off")
    box(ax, 0.4, 2.2, 2.4, 1.2, "Plant\nx, y", SHADE)
    box(ax, 4.0, 2.2, 2.8, 1.2, "Observer\nẋ̂ = … + L(y−ŷ)", SHADE2, TEAL)
    box(ax, 7.6, 2.2, 2.0, 1.2, "x̂", SHADE, ORANGE)
    arrow(ax, 2.9, 2.8, 3.9, 2.8); arrow(ax, 6.9, 2.8, 7.5, 2.8)
    ax.text(5.0, 1.0, "error e = x − x̂ → (A−LC) dynamics", ha="center", color=GRAY, fontsize=10)
    ax.set_title("Luemberger observer sketch", fontsize=12)
    save(fig, "ssi-observer.svg")


def fig_lmmse():
    fig, ax = plt.subplots(figsize=(6.2, 3.2))
    ax.set_xlim(0, 8); ax.set_ylim(0, 4); ax.axis("off")
    box(ax, 0.5, 1.5, 2.2, 1.3, "observation\nY", SHADE2, TEAL)
    box(ax, 3.5, 1.5, 2.5, 1.3, "LMMSE\nX̂ = AY+b", SHADE, BLUE)
    box(ax, 6.5, 1.5, 1.3, 1.3, "X̂", SHADE2, RED)
    arrow(ax, 2.8, 2.15, 3.4, 2.15); arrow(ax, 6.1, 2.15, 6.4, 2.15)
    ax.text(4.0, 3.3, "(X−X̂) ⊥ linear fns of Y", ha="center", color=GRAY, fontsize=10)
    ax.set_title("LMMSE geometry", fontsize=12)
    save(fig, "ssi-lmmse.svg")


def fig_wss():
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    ax.set_xlim(0, 10); ax.set_ylim(0, 3.5); ax.axis("off")
    box(ax, 0.4, 1.2, 2.2, 1.3, "WSS\nx[n]", SHADE)
    box(ax, 3.5, 1.2, 3.0, 1.3, "LTI h\nS_y = |H|² S_x", SHADE2, TEAL)
    box(ax, 7.4, 1.2, 2.2, 1.3, "y[n]", SHADE, ORANGE)
    arrow(ax, 2.7, 1.85, 3.4, 1.85); arrow(ax, 6.6, 1.85, 7.3, 1.85)
    ax.set_title("WSS through LTI", fontsize=12)
    save(fig, "ssi-wss-lti.svg")


def fig_wiener():
    fig, ax = plt.subplots(figsize=(6.6, 3.2))
    ax.set_xlim(0, 10); ax.set_ylim(0, 3.8); ax.axis("off")
    box(ax, 0.3, 1.4, 2.0, 1.2, "s + w", SHADE2)
    box(ax, 3.0, 1.4, 3.5, 1.2, "Wiener H_opt\nmin E|s−ŝ|²", SHADE, BLUE)
    box(ax, 7.3, 1.4, 2.2, 1.2, "ŝ", SHADE2, TEAL)
    arrow(ax, 2.4, 2.0, 2.9, 2.0); arrow(ax, 6.6, 2.0, 7.2, 2.0)
    ax.set_title("Wiener filtering", fontsize=12)
    save(fig, "ssi-wiener.svg")


def fig_detection():
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    ax.set_xlim(0, 8); ax.set_ylim(0, 4); ax.axis("off")
    box(ax, 0.5, 2.4, 3.0, 1.1, "H0: noise only", SHADE)
    box(ax, 4.5, 2.4, 3.0, 1.1, "H1: signal + noise", SHADE2, TEAL)
    box(ax, 2.0, 0.6, 4.0, 1.1, "LRT / NP threshold", SHADE, ORANGE)
    arrow(ax, 2.0, 2.4, 3.5, 1.8, GRAY); arrow(ax, 6.0, 2.4, 4.5, 1.8, GRAY)
    ax.set_title("Binary hypothesis testing", fontsize=12)
    save(fig, "ssi-detection.svg")


def fig_matched():
    fig, ax = plt.subplots(figsize=(6.4, 3.0))
    ax.set_xlim(0, 10); ax.set_ylim(0, 3.4); ax.axis("off")
    box(ax, 0.4, 1.2, 2.4, 1.2, "known s(t)\n+ white noise", SHADE)
    box(ax, 3.5, 1.2, 3.0, 1.2, "h(t) ∝ s(T−t)\nmatched", SHADE2, TEAL)
    box(ax, 7.2, 1.2, 2.4, 1.2, "max SNR\nat T", SHADE, RED)
    arrow(ax, 2.9, 1.8, 3.4, 1.8); arrow(ax, 6.6, 1.8, 7.1, 1.8)
    ax.set_title("Matched filter", fontsize=12)
    save(fig, "ssi-matched.svg")


def fig_feedback():
    fig, ax = plt.subplots(figsize=(6.6, 3.2))
    ax.set_xlim(0, 10); ax.set_ylim(0, 3.6); ax.axis("off")
    box(ax, 0.3, 1.3, 2.0, 1.2, "r", SHADE2)
    box(ax, 3.0, 1.3, 2.4, 1.2, "K / L\nfeedback", SHADE, BLUE)
    box(ax, 6.2, 1.3, 3.2, 1.2, "closed-loop\nA−BK / A−LC", SHADE2, TEAL)
    arrow(ax, 2.4, 1.9, 2.9, 1.9); arrow(ax, 5.5, 1.9, 6.1, 1.9)
    ax.set_title("State feedback / observer poles", fontsize=12)
    save(fig, "ssi-feedback.svg")


def main():
    setup()
    fig_moc(); fig_state_space(); fig_observer(); fig_lmmse()
    fig_wss(); fig_wiener(); fig_detection(); fig_matched(); fig_feedback()
    print("done ssi")


if __name__ == "__main__":
    main()
