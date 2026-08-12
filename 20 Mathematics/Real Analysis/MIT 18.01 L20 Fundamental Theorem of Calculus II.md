---
aliases: [MIT18.1-Lec20-微积分基本定理II（FTC 2）, 微积分基本定理II, Fundamental Theorem of Calculus II, FTC 2]
tags: [math, single-variable-calculus]
up: "[[Single-Variable Calculus (MIT 18.01) MOC]]"
related: "[[MIT 18.01 L19 Fundamental Theorem of Calculus I]], [[MIT 18.01 L21 Applications of the Integral to Logarithms]], [[Definite Integrals and the Fundamental Theorem of Calculus|定积分]], [[Derivative and Integral Formula Tables|导数和积分公式]]"
down: "[[MIT 18.01 L21 Applications of the Integral to Logarithms]]"
---
# Fundamental Theorem of Calculus II

> [!summary] 核心结论
> 微积分基本定理第二部分 (FTC, Part II / Newton–Leibniz)：定积分等于**任意一个原函数的端点差** $\int_a^b f=F(b)-F(a)$。它把"求面积"变成"求原函数"，是定积分计算的主通道。

> 关键词：用原函数算定积分、净变化、计算主通道。

---

## 1. FTC II (Newton–Leibniz)

若 $F'(x)=f(x)$，则

$$\int_a^b f(x)\,dx=F(b)-F(a).$$

它与 [[MIT 18.01 L19 Fundamental Theorem of Calculus I|FTC I]] 互补：Part I 保证原函数存在（面积函数即是），Part II 用任意原函数算定积分。

## 2. 净变化定理 (Net Change Theorem)

若变化率为 $r(t)$，则累计变化

$$\int_{t_0}^{t_1}r(t)\,dt=\text{末值}-\text{初值}.$$

这是 FTC II 的"应用口径"：积累变化率即得净变化。

## 3. 典型计算 (Examples)

$$\int_1^e\frac1x\,dx=\ln e-\ln1=1,\qquad \int_0^{\pi}\sin x\,dx=\big[-\cos x\big]_0^{\pi}=2.$$

基本原函数见 [[Derivative and Integral Formula Tables|导数和积分公式]]。

## 4. 易错点 (Pitfalls)

- 代上下限括号/符号错误；原函数相差常数不影响定积分，但中间运算不要丢符号。

---

> [!important] 一句话总结
> FTC II：定积分 = 原函数端点差——把面积问题转化为反求导问题。
