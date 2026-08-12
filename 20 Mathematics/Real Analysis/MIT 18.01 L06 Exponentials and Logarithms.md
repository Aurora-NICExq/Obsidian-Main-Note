---
aliases: [MIT18.1-Lec06-指数与对数（Exponentials and Logs）, 指数与对数, Exponentials and Logarithms]
tags: [math, single-variable-calculus]
up: "[[Single-Variable Calculus (MIT 18.01) MOC]]"
related: "[[MIT 18.01 L05 Implicit Differentiation]], [[MIT 18.01 L16 Separable Differential Equations]], [[Differential Equations and the Number e|微分方程与自然常数]]"
down: "[[MIT 18.01 L07 Exam 1 Review]]"
---
# Exponentials and Logarithms

> [!summary] 核心结论
> 指数函数 (exponential) 描述"按当前量成比例变化"，对数 (logarithm) 把乘法结构转成加法结构。$e^x$ 的导数等于自身，这是它成为增长/衰减模型核心的原因。

> 关键词：$e^x$、$\ln x$、对数求导、指数增长/衰减。

---

## 1. 基本关系 (Basics)

- $\ln x$ 是 $e^x$ 的反函数（$x>0$）；
- 对数恒等式：$\ln(ab)=\ln a+\ln b$，$\ln(a^k)=k\ln a$——把乘除幂化为加减乘。

## 2. 导数公式 (Derivatives)

$(e^x)'=e^x$，$(a^x)'=a^x\ln a$，$(\ln x)'=\dfrac1x\ (x>0)$，更通用 $(\ln|x|)'=\dfrac1x\ (x\neq0)$。

> [!note] 用隐函数法推 $(\ln x)'$
> 设 $y=\ln x$，即 $e^y=x$。两边对 $x$ 求导（[[MIT 18.01 L05 Implicit Differentiation|隐函数求导]]）：$e^y\,y'=1$，故 $y'=\dfrac{1}{e^y}=\dfrac1x$。$\blacksquare$

## 3. 对数求导 (Logarithmic Differentiation)

当幂、指数都含变量时，先取对数再求导。例：$f(x)=x^x$，$\ln f=x\ln x$，求导 $\dfrac{f'}{f}=\ln x+1$，故 $f'=x^x(\ln x+1)$。

## 4. 指数模型 (Exponential Models)

$y'=ky$ 的解为 $y=Ce^{kx}$，初值 $y(x_0)=y_0$ 定出 $C$。这是后续 [[MIT 18.01 L16 Separable Differential Equations|可分离方程]] 与 [[Differential Equations and the Number e|微分方程中的 e]] 的直接来源。

## 5. 易错点 (Pitfalls)

- 忽略 $\ln$ 的定义域；混淆 $a^x$ 与 $x^a$ 的导数。

---

> [!important] 一句话总结
> $e^x$ 导数等于自身，对数化乘为加——二者是指数增长模型与对数求导的两根支柱。
