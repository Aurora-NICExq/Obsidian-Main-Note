---
aliases: [非齐次特解微分方程特解表格, Particular-Solution Forms Table]
tags: [math, calculus]
up: "[[Nonhomogeneous Linear ODEs|非齐次微分方程]]"
related: "[[Nonhomogeneous Linear ODEs|非齐次微分方程]], [[Ordinary Differential Equations (Foundations and Methods)|一阶微分方程]], [[Differential Equations and the Number e|微分方程与自然常数]], [[Differential Equations through Linear Algebra|微分方程与线性代数]]"
down: ""
---
# Particular-Solution Forms Table

> [!summary] 核心结论
> 用**待定系数法 (undetermined coefficients)** 解非齐次线性方程时，按非齐次项 $f(x)$ 的形态"同类试探"假设特解 $y_p$ 的形式。本表给出常见 $f(x)$ 对应的 $y_p$ 模板；详见 [[Nonhomogeneous Linear ODEs|非齐次微分方程]]。

前置知识：[[Nonhomogeneous Linear ODEs|非齐次微分方程]]。

---

## 特解形式对照表 (Trial-Form Table)

| 若 $f(x)$ 是 | 则设 $y_p$ 为 |
| :-- | :-- |
| **次数为 $n$ 的多项式** | **次数为 $n$ 的一般多项式** |
| 例：$f(x)=7$ | $y_p=a$ |
| $f(x)=3x-2$ | $y_p=ax+b$ |
| $f(x)=10x^2$ | $y_p=ax^2+bx+c$ |
| $f(x)=-x^3-x^2+x+22$ | $y_p=ax^3+bx^2+cx+d$ |
| **指数 $e^{kx}$ 的倍数** | **$y_p=Ce^{kx}$** |
| 例：$f(x)=10e^{-4x}$ | $y_p=Ce^{-4x}$ |
| $f(x)=e^{x}$ | $y_p=Ce^{x}$ |
| **$\cos(kx)$、$\sin(kx)$ 的倍数** | **$y_p=C\cos(kx)+D\sin(kx)$** |
| 例：$f(x)=2\sin(3x)-5\cos(3x)$ | $y_p=C\cos(3x)+D\sin(3x)$ |
| $f(x)=\cos(x)$ | $y_p=C\cos(x)+D\sin(x)$ |
| $f(x)=2\sin(11x)$ | $y_p=C\cos(11x)+D\sin(11x)$ |
| **以上各型的和或积** | **相应的和或积（若为积，删去一个冗余常数）** |
| 例：$f(x)=2x^2+e^{-6x}$ | $y_p=ax^2+bx+c+Ce^{-6x}$ |
| $f(x)=2x^2e^{-6x}$ | $y_p=(ax^2+bx+c)e^{-6x}$ |
| $f(x)=7e^{2x}\sin(3x)$ | $y_p=(C\cos(3x)+D\sin(3x))e^{2x}$ |
| $f(x)=\cos(2x)+6\sin(x)$ | $y_p=C\cos(2x)+D\sin(2x)+E\cos(x)+F\sin(x)$ |
| $f(x)=4x\cos(3x)$ | $y_p=(ax+b)(C\cos(3x)+D\sin(3x))$ |

> [!warning] 修正规则 (Resonance Correction)
> 若试探的 $y_p$ 与齐次通解 $y_h$ 中的项**线性相关（共振）**，需将 $y_p$ 整体乘以 $x$（或 $x^2$，按重根次数）。原理见 [[Nonhomogeneous Linear ODEs|非齐次微分方程]] 的 $x^k$ 规则。
