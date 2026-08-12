---
aliases: [MIT18.1-Lec05-隐函数求导（Implicit Differentiation）, 隐函数求导, Implicit Differentiation]
tags: [math, single-variable-calculus]
up: "[[Single-Variable Calculus (MIT 18.01) MOC]]"
related: "[[MIT 18.01 L04 Chain Rule]], [[MIT 18.01 L06 Exponentials and Logarithms]]"
down: "[[MIT 18.01 L06 Exponentials and Logarithms]]"
---
# Implicit Differentiation

> [!summary] 核心结论
> 隐函数求导 (implicit differentiation) 把 $y$ 视为 $x$ 的函数，对方程**两边同时求导**（含 $y$ 的项用链式法则），再解出 $y'$。无需先解出 $y=f(x)$。

> 关键词：$F(x,y)=0$、$y=y(x)$、收集 $y'$、水平/竖直切线。

---

## 1. 为什么要隐式求导 (Motivation)

曲线常由方程 $F(x,y)=0$ 定义，未必能（或不想）解出 $y=f(x)$。目标通常是求 $dy/dx$、切线方程，或水平/竖直切线点。

## 2. 标准流程 (Procedure)

1. 视 $y$ 为 $y(x)$；
2. 两边对 $x$ 求导（对含 $y$ 的项用 [[MIT 18.01 L04 Chain Rule|链式法则]]，如 $(y^2)'=2yy'$）；
3. 收集 $y'$ 并解出。

## 3. 快速公式 (Quick Formula)

若 $F(x,y)=0$ 且 $F_y\neq0$，则

$$\frac{dy}{dx}=-\frac{F_x}{F_y}.$$

> [!note] 公式来历
> 对 $F(x,y(x))=0$ 两边用多元链式法则求导得 $F_x+F_y\,y'=0$，解出 $y'=-F_x/F_y$。这正是机械流程的"一步到位"版本（多元视角见 [[Total Differential and the Chain Rule|微分、链式法则]]）。

## 4. 切线类型判别 (Tangent Types)

- 水平切线 (horizontal)：$y'=0$ 且点在曲线上；
- 竖直切线 (vertical)：$y'$ 不存在（常见为分母为 $0$ 而分子非 $0$）。

## 5. 例题 (Examples)

- 圆 $x^2+y^2=1$：$2x+2yy'=0\Rightarrow y'=-x/y$；
- 水平切线：$y'=0\Rightarrow x=0$，点 $(0,\pm1)$；
- 竖直切线：要求 $y=0$，点 $(\pm1,0)$。

## 6. 易错点 (Pitfalls)

- 漏写 $(y^2)'=2yy'$；把分母为 $0$ 的点直接"约掉"而丢失竖直切线信息。

---

> [!important] 一句话总结
> 隐函数求导 = 两边求导 + 收集 $y'$，把链式法则用到方程定义的曲线上。
