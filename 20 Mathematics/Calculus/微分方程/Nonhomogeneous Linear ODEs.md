---
aliases: [非齐次微分方程, Nonhomogeneous Linear ODEs, Method of Undetermined Coefficients]
tags: [math, calculus]
up: "[[Integral Calculus and Differential Equations MOC]]"
related: "[[Ordinary Differential Equations (Foundations and Methods)|一阶微分方程]], [[Particular-Solution Forms Table|非齐次特解微分方程特解表格]], [[Differential Equations and the Number e|微分方程与自然常数]], [[Differential Equations through Linear Algebra|微分方程与线性代数]]"
down: "[[Particular-Solution Forms Table|非齐次特解微分方程特解表格]]"
---
# Nonhomogeneous Linear ODEs

> [!summary] 核心结论
> 非齐次线性方程的通解 $=$ **齐次通解 $y_h$** $+$ **一个特解 $y_p$**。求 $y_p$ 常用**待定系数法 (method of undetermined coefficients)**：按非齐次项 $f(x)$ 的形态假设 $y_p$ 的形式。若假设的 $y_p$ 与齐次解线性相关，需乘上 $x^k$ 加以修正。

前置知识：[[Ordinary Differential Equations (Foundations and Methods)|一阶微分方程]]（特征方程与齐次解）。

---

## 1. 特解与待定系数法 (Particular Solution)

对 $f(x)$ 的各种常见形态，$y_p$ 的假设形式见专表：[[Particular-Solution Forms Table|非齐次特解微分方程特解表格]]。基本思路是"以同类函数试探"——多项式配多项式、指数配指数、正余弦配正余弦。

---

## 2. 修正规则：乘以 $x^k$ (The $x^k$ Correction)

> [!important] 何时需要修正
> 当假设的 $y_p$ 与齐次解 $y_h$ **线性相关**（即试探函数本身已是齐次解）时，代入后左边恒为 $0$，无法匹配右边，必须把 $y_p$ 乘以 $x^k$。

### $k$ 的取值规则

设非齐次项为 $e^{\lambda x}P_m(x)$ 型，则 $k$ 等于 $\lambda$ 作为特征根的**重数 (multiplicity)**：

- $k=0$：$\lambda$ 不是特征根（无需乘）；
- $k=1$：$\lambda$ 是单根（乘 $x$）；
- $k=2$：$\lambda$ 是二重根（乘 $x^2$）；以此类推。

**本质原因**：若 $\lambda$ 是二重根，则 $e^{\lambda x}$ 与 $xe^{\lambda x}$ 都是齐次解。此时即便取 $y_p=Axe^{\lambda x}$ 仍是齐次解，代入得 $0$；必须乘 $x^2$ 取 $y_p=Ax^2e^{\lambda x}$，才能跳出齐次解空间。

---

## 3. 示例 (Worked Example)

$$y''-y'=e^x.$$

**第一步：齐次解。** 特征方程 $r^2-r=0\Rightarrow r(r-1)=0$，根 $r_1=0,\ r_2=1$，故

$$y_h=C_1+C_2e^x.$$

**第二步：试探（不乘 $x$）。** 右端是 $e^x$，$\lambda=1$ 恰为特征单根。若硬设 $y_p=Ae^x$，则 $y_p'=y_p''=Ae^x$，代入得 $Ae^x-Ae^x=0\neq e^x$，**无解**。

**第三步：修正后求解。** 因 $\lambda=1$ 是单根（$k=1$），改设 $y_p=Axe^x$。则

$$y_p'=A(x+1)e^x,\qquad y_p''=A(x+2)e^x,$$

$$y_p''-y_p'=A(x+2)e^x-A(x+1)e^x=Ae^x\overset{!}{=}e^x\ \Rightarrow\ A=1.$$

故特解 $y_p=xe^x$，通解为

$$y=C_1+C_2e^x+xe^x.$$
