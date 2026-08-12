---
aliases: [MIT18.1-Lec16-微分方程与变量分离（Differential Equations）, 微分方程与变量分离, Separable Differential Equations]
tags: [math, single-variable-calculus]
up: "[[Single-Variable Calculus (MIT 18.01) MOC]]"
related: "[[MIT 18.01 L06 Exponentials and Logarithms]], [[Ordinary Differential Equations (Foundations and Methods)|一阶微分方程]], [[Differential Equations and the Number e|微分方程与自然常数]]"
down: "[[MIT 18.01 L17 Exam 2]]"
---
# Separable Differential Equations

> [!summary] 核心结论
> 可分离方程 (separable ODE)：把含 $y$ 的项（含 $dy$）与含 $x$ 的项（含 $dx$）分到两边，再各自积分得隐式解，最后用初值定常数。

> 关键词：可分离方程、两边积分、初值、指数模型。

---

## 1. 可分离变量 (Separation of Variables)

若 $y'=g(x)h(y)$，则分离为 $\dfrac{dy}{h(y)}=g(x)\,dx$，两边积分得隐式解 (implicit solution)，再代初值定常数。

## 2. 典型方程 (Typical Cases)

- $y'=ky\Rightarrow y=Ce^{kx}$（指数模型，见 [[MIT 18.01 L06 Exponentials and Logarithms]]）；
- $y'=xy\Rightarrow \ln|y|=\tfrac{x^2}{2}+C$。

## 3. 初值问题 (Initial Value Problem)

给定 $y(x_0)=y_0$，代入隐式解求出 $C$，得到唯一确定的解。

## 4. 易错点 (Pitfalls)

- $\int\tfrac1y\,dy=\ln|y|$ 的绝对值；只写解族不落到具体解。

> [!tip] 更广的方法
> 一阶线性方程的积分因子法、常系数高阶方程等系统方法见 [[Ordinary Differential Equations (Foundations and Methods)|一阶微分方程]]；$e$ 为何是微分方程"母语"见 [[Differential Equations and the Number e|微分方程与自然常数]]。

---

> [!important] 一句话总结
> 可分离方程 = 分离变量 + 两边积分 + 初值定常数，是最早能上手的一类 ODE。
