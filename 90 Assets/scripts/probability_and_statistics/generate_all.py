#!/usr/bin/env python3
"""Generate SVGs for Probability and Statistics (MIT 18.05) notes.

Usage:
  .venv/bin/python generate_all.py
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle, FancyBboxPatch, Rectangle
from math import comb

ROOT = Path(__file__).resolve().parents[3]
OUT = ROOT / "90 Assets" / "diagrams" / "probability-and-statistics"

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
    path = OUT / name
    fig.savefig(path, format="svg", bbox_inches="tight", pad_inches=0.15)
    plt.close(fig)
    print("wrote", path.relative_to(ROOT))


def axis_plain(ax, xlabel="", ylabel=""):
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.spines["left"].set_color(GRAY)
    ax.spines["bottom"].set_color(GRAY)
    ax.tick_params(colors=GRAY)
    if xlabel:
        ax.set_xlabel(xlabel)
    if ylabel:
        ax.set_ylabel(ylabel)


def fig_moc_roadmap():
    fig, ax = plt.subplots(figsize=(9.4, 3.6))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 4)
    ax.axis("off")
    boxes = [
        (0.2, 2.2, "Counting &\nProbability"),
        (2.2, 2.2, "Random\nVariables"),
        (4.2, 2.2, "LLN /\nCLT"),
        (6.2, 2.2, "Estimation &\nBayes / NHST"),
        (8.2, 2.2, "CI &\nRegression"),
    ]
    for i, (x, y, t) in enumerate(boxes):
        ax.add_patch(
            FancyBboxPatch(
                (x, y), 1.6, 1.2, boxstyle="round,pad=0.05,rounding_size=0.15",
                facecolor=SHADE if i % 2 == 0 else SHADE2, edgecolor=BLUE, lw=1.3,
            )
        )
        ax.text(x + 0.8, y + 0.6, t, ha="center", va="center", fontsize=10, color=BLUE)
        if i < len(boxes) - 1:
            ax.annotate("", xy=(boxes[i + 1][0] - 0.05, y + 0.6), xytext=(x + 1.65, y + 0.6),
                        arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.5))
    ax.set_title("MIT 18.05 Probability and Statistics roadmap", fontsize=13, pad=6)
    save(fig, "ps-moc-roadmap.svg")


def fig_venn_events():
    fig, ax = plt.subplots(figsize=(5.0, 4.2))
    ax.set_xlim(-2.2, 2.2)
    ax.set_ylim(-2.0, 2.2)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.add_patch(Rectangle((-2.0, -1.8), 4.0, 3.8, fill=False, edgecolor=GRAY, lw=1.5))
    ax.text(-1.85, 1.75, r"$\Omega$", color=GRAY, fontsize=12)
    ax.add_patch(Circle((-0.45, 0.1), 1.05, facecolor=SHADE, edgecolor=BLUE, lw=1.6, alpha=0.7))
    ax.add_patch(Circle((0.55, 0.1), 1.05, facecolor=SHADE2, edgecolor=TEAL, lw=1.6, alpha=0.55))
    ax.text(-1.0, 0.2, r"$A$", color=BLUE, fontsize=13)
    ax.text(0.95, 0.2, r"$B$", color=TEAL, fontsize=13)
    ax.text(-0.05, 0.05, r"$A\cap B$", color=RED, fontsize=9, ha="center")
    ax.set_title("Sample space and events", fontsize=12)
    save(fig, "ps-venn-events.svg")


def fig_bayes_tree():
    fig, ax = plt.subplots(figsize=(6.2, 4.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    # nodes
    nodes = {
        "O": (1.2, 3.0),
        "D": (4.0, 4.5),
        "H": (4.0, 1.5),
        "Dp": (7.2, 5.2),
        "Dn": (7.2, 3.8),
        "Hp": (7.2, 2.2),
        "Hn": (7.2, 0.8),
    }
    labels = {
        "O": "start",
        "D": r"$D$",
        "H": r"$D^c$",
        "Dp": r"$+$",
        "Dn": r"$-$",
        "Hp": r"$+$",
        "Hn": r"$-$",
    }
    edges = [
        ("O", "D", r"$P(D)$"),
        ("O", "H", r"$P(D^c)$"),
        ("D", "Dp", r"$P(+|D)$"),
        ("D", "Dn", r"$P(-|D)$"),
        ("H", "Hp", r"$P(+|D^c)$"),
        ("H", "Hn", r"$P(-|D^c)$"),
    ]
    for a, b, lab in edges:
        x0, y0 = nodes[a]
        x1, y1 = nodes[b]
        ax.annotate("", xy=(x1 - 0.35, y1), xytext=(x0 + 0.35, y0),
                    arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.3))
        ax.text((x0 + x1) / 2, (y0 + y1) / 2 + 0.25, lab, fontsize=9, color=ORANGE, ha="center")
    for k, (x, y) in nodes.items():
        ax.add_patch(Circle((x, y), 0.38, facecolor=SHADE, edgecolor=BLUE, lw=1.3))
        ax.text(x, y, labels[k], ha="center", va="center", fontsize=11, color=BLUE)
    ax.set_title("Bayes: disease test tree", fontsize=12)
    save(fig, "ps-bayes-tree.svg")


def fig_binomial_pmf():
    fig, ax = plt.subplots(figsize=(5.4, 3.4))
    n, p = 10, 0.4
    ks = np.arange(0, n + 1)
    pmf = np.array([comb(n, int(k)) * p**k * (1 - p) ** (n - k) for k in ks])
    ax.vlines(ks, 0, pmf, colors=BLUE, lw=2)
    ax.plot(ks, pmf, "o", color=BLUE, ms=6)
    axis_plain(ax, r"$k$", r"$P(X=k)$")
    ax.set_title(r"Binomial$(n=10,p=0.4)$", fontsize=12)
    save(fig, "ps-binomial-pmf.svg")


def fig_normal_pdf():
    fig, ax = plt.subplots(figsize=(5.6, 3.4))
    x = np.linspace(-4, 4, 400)
    pdf = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)
    ax.plot(x, pdf, color=BLUE, lw=2)
    ax.fill_between(x, pdf, where=(x >= -1) & (x <= 1), color=SHADE, alpha=0.8)
    ax.axvline(0, color=GRAY, lw=1, ls="--")
    axis_plain(ax, r"$x$", r"$f(x)$")
    ax.text(0.2, 0.28, r"$\approx 68\%$", color=TEAL, fontsize=10)
    ax.set_title(r"Standard normal $N(0,1)$", fontsize=12)
    save(fig, "ps-normal-pdf.svg")


def fig_joint_scatter():
    rng = np.random.default_rng(0)
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.6))
    # uncorrelated
    x = rng.normal(0, 1, 200)
    y = rng.normal(0, 1, 200)
    axes[0].scatter(x, y, s=12, color=BLUE, alpha=0.7)
    axes[0].set_title(r"Uncorrelated / independent-ish", fontsize=11)
    axis_plain(axes[0], r"$X$", r"$Y$")
    # correlated
    x2 = rng.normal(0, 1, 200)
    y2 = 0.85 * x2 + 0.5 * rng.normal(0, 1, 200)
    axes[1].scatter(x2, y2, s=12, color=TEAL, alpha=0.7)
    axes[1].set_title(r"Positive correlation", fontsize=11)
    axis_plain(axes[1], r"$X$", r"$Y$")
    fig.suptitle("Joint samples and correlation", y=1.02)
    save(fig, "ps-joint-correlation.svg")


def fig_clt():
    rng = np.random.default_rng(1)
    fig, axes = plt.subplots(1, 3, figsize=(9.2, 3.0))
    # exponential parent
    parent = rng.exponential(1.0, 5000)
    axes[0].hist(parent, bins=40, density=True, color=SHADE, edgecolor=BLUE)
    axes[0].set_title("Exp(1) parent", fontsize=10)
    axis_plain(axes[0])
    for ax, n, title in zip(axes[1:], [5, 30], [r"$\bar X_{5}$", r"$\bar X_{30}$"]):
        means = rng.exponential(1.0, (4000, n)).mean(axis=1)
        ax.hist(means, bins=40, density=True, color=SHADE2, edgecolor=TEAL)
        xs = np.linspace(means.min(), means.max(), 200)
        mu, sig = 1.0, 1.0 / np.sqrt(n)
        ax.plot(xs, (1 / (sig * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((xs - mu) / sig) ** 2), color=RED, lw=1.8)
        ax.set_title(title + " vs normal", fontsize=10)
        axis_plain(ax)
    fig.suptitle("Central Limit Theorem", y=1.05)
    save(fig, "ps-clt.svg")


def fig_mle_likelihood():
    fig, ax = plt.subplots(figsize=(5.4, 3.4))
    # Bernoulli MLE: L(p)=p^k (1-p)^{n-k}
    n, k = 20, 12
    p = np.linspace(0.01, 0.99, 300)
    L = p**k * (1 - p) ** (n - k)
    ax.plot(p, L / L.max(), color=BLUE, lw=2)
    ax.axvline(k / n, color=RED, ls="--", lw=1.5)
    ax.text(k / n + 0.02, 0.9, r"$\hat p_{\mathrm{MLE}}=k/n$", color=RED, fontsize=10)
    axis_plain(ax, r"$p$", r"normalized $L(p)$")
    ax.set_title(r"Bernoulli likelihood (n=20, k=12)", fontsize=12)
    save(fig, "ps-mle-likelihood.svg")


def fig_bayes_update():
    fig, ax = plt.subplots(figsize=(5.6, 3.6))
    # Beta prior/posterior illustration
    theta = np.linspace(0, 1, 400)
    # Beta(2,2) prior, after 7 successes 3 failures -> Beta(9,5)
    def beta_pdf(a, b, x):
        # unnormalized then normalize numerically
        y = x ** (a - 1) * (1 - x) ** (b - 1)
        return y / np.trapezoid(y, x)

    prior = beta_pdf(2, 2, theta)
    post = beta_pdf(9, 5, theta)
    ax.plot(theta, prior, color=GRAY, lw=1.8, label=r"prior Beta(2,2)")
    ax.plot(theta, post, color=BLUE, lw=2.2, label=r"posterior Beta(9,5)")
    ax.fill_between(theta, post, color=SHADE, alpha=0.5)
    axis_plain(ax, r"$\theta$", "density")
    ax.legend(frameon=False, fontsize=9)
    ax.set_title("Bayesian updating (Beta–Binomial)", fontsize=12)
    save(fig, "ps-bayes-update.svg")


def fig_nhst_rejection():
    fig, ax = plt.subplots(figsize=(5.8, 3.4))
    x = np.linspace(-4, 4, 400)
    pdf = (1 / np.sqrt(2 * np.pi)) * np.exp(-0.5 * x**2)
    ax.plot(x, pdf, color=BLUE, lw=2)
    zcrit = 1.96
    ax.fill_between(x, pdf, where=(x <= -zcrit), color=RED, alpha=0.45)
    ax.fill_between(x, pdf, where=(x >= zcrit), color=RED, alpha=0.45)
    ax.axvline(-zcrit, color=ORANGE, ls="--", lw=1.2)
    ax.axvline(zcrit, color=ORANGE, ls="--", lw=1.2)
    ax.text(2.3, 0.15, r"reject $H_0$", color=RED, fontsize=10)
    ax.text(-3.8, 0.15, r"reject $H_0$", color=RED, fontsize=10)
    ax.text(-0.6, 0.35, r"retain $H_0$", color=TEAL, fontsize=10)
    axis_plain(ax, r"$z$", "density under $H_0$")
    ax.set_title(r"Two-sided $z$-test, $\alpha=0.05$", fontsize=12)
    save(fig, "ps-nhst-rejection.svg")


def fig_confidence_interval():
    rng = np.random.default_rng(2)
    fig, ax = plt.subplots(figsize=(5.6, 4.2))
    mu = 0
    ax.axvline(mu, color=RED, lw=1.5, label=r"true $\mu$")
    for i in range(25):
        sample = rng.normal(mu, 1, 30)
        m = sample.mean()
        se = 1 / np.sqrt(30)
        lo, hi = m - 1.96 * se, m + 1.96 * se
        color = TEAL if lo <= mu <= hi else ORANGE
        ax.plot([lo, hi], [i, i], color=color, lw=1.6)
        ax.plot(m, i, "o", color=color, ms=4)
    ax.set_yticks([])
    axis_plain(ax, "parameter axis", "repeated samples")
    ax.set_title(r"95% CI coverage across replications", fontsize=12)
    save(fig, "ps-confidence-interval.svg")


def fig_bootstrap():
    rng = np.random.default_rng(3)
    fig, axes = plt.subplots(1, 2, figsize=(8.4, 3.4))
    data = rng.exponential(2.0, 40)
    axes[0].hist(data, bins=12, color=SHADE, edgecolor=BLUE)
    axes[0].axvline(np.mean(data), color=RED, lw=1.5)
    axes[0].set_title("Original sample", fontsize=11)
    axis_plain(axes[0], r"$x$", "count")
    boots = np.array([rng.choice(data, size=len(data), replace=True).mean() for _ in range(2000)])
    axes[1].hist(boots, bins=30, color=SHADE2, edgecolor=TEAL, density=True)
    lo, hi = np.quantile(boots, [0.025, 0.975])
    axes[1].axvline(lo, color=ORANGE, ls="--")
    axes[1].axvline(hi, color=ORANGE, ls="--")
    axes[1].set_title(r"Bootstrap means + 95% CI", fontsize=11)
    axis_plain(axes[1], r"$\bar x^*$", "density")
    fig.suptitle("Bootstrap confidence interval", y=1.02)
    save(fig, "ps-bootstrap.svg")


def fig_regression():
    rng = np.random.default_rng(4)
    fig, ax = plt.subplots(figsize=(5.4, 3.8))
    x = np.linspace(0, 10, 40)
    y = 1.5 + 0.8 * x + rng.normal(0, 1.2, size=x.size)
    ax.scatter(x, y, color=BLUE, s=28, alpha=0.8)
    # least squares
    A = np.vstack([np.ones_like(x), x]).T
    beta, slope = np.linalg.lstsq(A, y, rcond=None)[0]
    xs = np.linspace(0, 10, 100)
    ax.plot(xs, beta + slope * xs, color=RED, lw=2, label=r"$\hat y=\hat\beta_0+\hat\beta_1 x$")
    # residual lines for a few points
    for i in [5, 15, 25, 35]:
        yi = beta + slope * x[i]
        ax.plot([x[i], x[i]], [y[i], yi], color=ORANGE, lw=1.0, alpha=0.8)
    axis_plain(ax, r"$x$", r"$y$")
    ax.legend(frameon=False, fontsize=9)
    ax.set_title("Simple linear regression residuals", fontsize=12)
    save(fig, "ps-regression.svg")


def fig_lln():
    rng = np.random.default_rng(5)
    fig, ax = plt.subplots(figsize=(5.6, 3.4))
    n = np.arange(1, 1001)
    for c in [BLUE, TEAL, ORANGE]:
        s = np.cumsum(rng.binomial(1, 0.5, 1000)) / n
        ax.plot(n, s, color=c, lw=1.2, alpha=0.85)
    ax.axhline(0.5, color=RED, ls="--", lw=1.5)
    axis_plain(ax, r"$n$", r"$\bar X_n$")
    ax.set_title(r"LLN: sample mean $\to p=1/2$", fontsize=12)
    save(fig, "ps-lln.svg")


def main():
    setup()
    fig_moc_roadmap()
    fig_venn_events()
    fig_bayes_tree()
    fig_binomial_pmf()
    fig_normal_pdf()
    fig_joint_scatter()
    fig_clt()
    fig_lln()
    fig_mle_likelihood()
    fig_bayes_update()
    fig_nhst_rejection()
    fig_confidence_interval()
    fig_bootstrap()
    fig_regression()
    print("done")


if __name__ == "__main__":
    main()
