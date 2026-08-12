---
aliases: [MIT18.1-Lec23-功、平均值与概率（Work & Probability）, 功、平均值与概率, Work Average Value and Probability]
tags: [math, single-variable-calculus]
up: "[[Single-Variable Calculus (MIT 18.01) MOC]]"
related: "[[MIT 18.01 L22 Volumes]], [[Double Integrals in Polar Coordinates and Applications|极坐标的二重积分应用]]"
down: ""
---
# Work, Average Value, and Probability

> [!summary] 核心结论
> 平均值 (average value)、功 (work) 与概率 (probability) 都是"在某种权重下的积分累积"。理解关键在于**先明确权重 ($dx$、弧长 $ds$、密度 $p$)**，再做积分。

> 关键词：平均值（不同权重）、功、概率密度、极坐标、$\int e^{-x^2}$。

---

## 1. 平均值 (Average Value)

- 按 $dx$ 加权：$\dfrac{1}{b-a}\displaystyle\int_a^b f(x)\,dx$；
- 按弧长 $ds$ 加权：$\dfrac1L\displaystyle\int_C f\,ds$。

同一函数在不同权重下的平均值**可能不同**。

> [!example] 半圆弧平均高度
> $y=\sqrt{1-x^2}$ 在 $[-1,1]$：按 $dx$ 平均为 $\dfrac\pi4$；按弧长平均为 $\dfrac2\pi$——权重不同，结果不同。

## 2. 功 (Work)

$W=\displaystyle\int_a^b F(x)\,dx$。弹簧 $F=kx$ 时 $W=\displaystyle\int_0^a kx\,dx=\tfrac12 ka^2$。

## 3. 概率密度 (Probability Density)

密度 $p\ge0$ 且**归一化** $\int p=1$；则 $P(a\le X\le b)=\displaystyle\int_a^b p(x)\,dx$。

## 4. 高斯积分 (Gaussian Integral)

设 $Q=\displaystyle\int_{-\infty}^{\infty}e^{-x^2}\,dx$。考虑 $Q^2=\displaystyle\iint e^{-(x^2+y^2)}\,dx\,dy$，转极坐标得 $Q^2=\pi$，故 $Q=\sqrt\pi$（极坐标二重积分技巧见 [[Double Integrals in Polar Coordinates and Applications|极坐标的二重积分应用]]）。

## 5. 易错点 (Pitfalls)

- 平均值先明确权重；概率先归一化再积分。

---

> [!important] 一句话总结
> 功、平均值、概率本质相同——都是"权重 × 量"沿区间的积分累积，关键先认清权重。
