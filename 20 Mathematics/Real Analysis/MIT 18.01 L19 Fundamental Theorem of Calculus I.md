---
aliases: [MIT18.1-Lec19-微积分基本定理I（FTC 1）, 微积分基本定理I, Fundamental Theorem of Calculus I, FTC 1]
tags: [math, single-variable-calculus]
up: "[[Single-Variable Calculus (MIT 18.01) MOC]]"
related: "[[MIT 18.01 L18 Definite Integrals]], [[MIT 18.01 L20 Fundamental Theorem of Calculus II]], [[Definite Integrals and the Fundamental Theorem of Calculus|定积分]], [[Variable-Limit Integrals and the Leibniz Rule|变限积分]]"
down: "[[MIT 18.01 L20 Fundamental Theorem of Calculus II]]"
---
# Fundamental Theorem of Calculus I

> [!summary] 核心结论
> 微积分基本定理第一部分 (FTC, Part I)：**面积函数 (area function) 的导数等于被积函数**。即 $\dfrac{d}{dx}\int_a^x f(t)\,dt=f(x)$，从而积分与微分互逆。

> 关键词：面积函数、变上限积分求导、$F'(x)=f(x)$。

---

## 1. 面积函数 (Area Function)

$$F(x)=\int_a^x f(t)\,dt.$$

## 2. FTC I（核心结论）

若 $f$ 连续，则 $F$ 可导且 $F'(x)=f(x)$。

> [!note] 直觉证明（短区间近似）
> $F(x+h)-F(x)=\int_x^{x+h}f(t)\,dt$。当 $h$ 很小，$f(t)\approx f(x)$，故积分 $\approx f(x)h$，差商 $\dfrac{F(x+h)-F(x)}{h}\approx f(x)$，取极限即得。严格的连续性夹逼版本见 [[Definite Integrals and the Fundamental Theorem of Calculus|定积分]]。

## 3. 常用推广 (Generalizations)

结合链式法则（见 [[Variable-Limit Integrals and the Leibniz Rule|变限积分]]）：

$$\frac{d}{dx}\int_a^{g(x)}f(t)\,dt=f(g(x))\,g'(x),\qquad \frac{d}{dx}\int_{u(x)}^{v(x)}f=f(v)v'-f(u)u'.$$

## 4. 例题 (Example)

$$\frac{d}{dx}\int_0^{\sin x}\sqrt{1+t^2}\,dt=\sqrt{1+\sin^2 x}\cdot\cos x.$$

## 5. 易错点 (Pitfalls)

- 漏乘上限导数 $g'(x)$；把积分哑变量 $t$ 与外部变量 $x$ 混淆。

---

> [!important] 一句话总结
> FTC I：求面积的累积速度，就是被积函数本身——积分与微分由此互为逆运算。
