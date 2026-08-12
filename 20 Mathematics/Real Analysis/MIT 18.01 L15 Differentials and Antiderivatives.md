---
aliases: [MIT18.1-Lec15-微分与原函数（Differentials and Antiderivatives）, 微分与原函数, Differentials and Antiderivatives]
tags: [math, single-variable-calculus]
up: "[[Single-Variable Calculus (MIT 18.01) MOC]]"
related: "[[MIT 18.01 L09 Linear and Quadratic Approximations]], [[MIT 18.01 L16 Separable Differential Equations]], [[Derivative and Integral Formula Tables|导数和积分公式]]"
down: "[[MIT 18.01 L16 Separable Differential Equations]]"
---
# Differentials and Antiderivatives

> [!summary] 核心结论
> 微分 (differential) $dy=f'(x)\,dx$ 用于线性近似与**误差传播 (error propagation)**；原函数 (antiderivative) 是求导的逆运算，其全体记作不定积分 $\int f\,dx=F+C$。

> 关键词：微分、误差传播、原函数、不定积分、积分常数。

---

## 1. 微分与近似 (Differentials)

$f(x+dx)\approx f(x)+f'(x)\,dx$，记 $dy=f'(x)\,dx$，并以 $\Delta y\approx dy$ 估算（见 [[MIT 18.01 L09 Linear and Quadratic Approximations]]）。

## 2. 误差传播例子 (Error Propagation)

- $A=\pi r^2\Rightarrow dA=2\pi r\,dr$；
- $V=\tfrac43\pi r^3\Rightarrow dV=4\pi r^2\,dr$。

即半径的小误差 $dr$ 如何放大为面积/体积误差。

## 3. 原函数与不定积分 (Antiderivative)

若 $F'(x)=f(x)$，则 $F$ 是 $f$ 的原函数，$\displaystyle\int f(x)\,dx=F(x)+C$。常数 $C$ 不可省（同一导数对应一族相差常数的原函数）。

## 4. 常用积分（反求导, Basic Table）

$\int x^n dx=\dfrac{x^{n+1}}{n+1}+C\ (n\neq-1)$，$\int\tfrac1x dx=\ln|x|+C$，$\int\sin x\,dx=-\cos x+C$，$\int\cos x\,dx=\sin x+C$。完整表见 [[Derivative and Integral Formula Tables|导数和积分公式]]。

## 5. 易错点 (Pitfalls)

- 漏写 $+C$；$\ln$ 忘记绝对值。

---

> [!important] 一句话总结
> 微分把导数变成可加的"误差砖块"，原函数把求导反过来——为定积分与微分方程铺路。
