---
aliases: [MIT18.1-Lec18-定积分（Definite Integrals）, 定积分（黎曼和）, Definite Integrals]
tags: [math, single-variable-calculus]
up: "[[Single-Variable Calculus (MIT 18.01) MOC]]"
related: "[[MIT 18.01 L19 Fundamental Theorem of Calculus I]], [[Definite Integrals and the Fundamental Theorem of Calculus|定积分]]"
down: "[[MIT 18.01 L19 Fundamental Theorem of Calculus I]]"
---
# Definite Integrals

> [!summary] 核心结论
> 定积分 (definite integral) 是**黎曼和 (Riemann sum) 的极限**，表示有向面积 (signed area) 与累积量。它满足线性、区间可加、比较等基本性质。

> 关键词：黎曼和、左/右/中点和、面积与累积、性质。

---

## 1. 黎曼和定义 (Riemann Sum)

$$\int_a^b f(x)\,dx=\lim_{\max\Delta x_i\to0}\sum_{i=1}^{n}f(x_i^*)\,\Delta x_i.$$

## 2. 等分区间的常用写法 (Equal Partition)

记 $\Delta x=\dfrac{b-a}{n}$：

- 左端点和：$\sum_{i=0}^{n-1}f(a+i\Delta x)\Delta x$；
- 右端点和：$\sum_{i=1}^{n}f(a+i\Delta x)\Delta x$；
- 中点和：$\sum_{i=0}^{n-1}f\big(a+(i+\tfrac12)\Delta x\big)\Delta x$。

## 3. 基本性质 (Properties)

线性 $\int(af+bg)=a\int f+b\int g$；区间可加 $\int_a^b=\int_a^c+\int_c^b$；反向变号 $\int_b^a f=-\int_a^b f$；比较 $f\le g\Rightarrow\int f\le\int g$。

## 4. 积分与面积 (Area)

$f\ge0$ 时积分为面积；允许负值时为"有向面积"。求**几何面积**时需对负区间取绝对值或分段。

## 5. 例题 (Example)

$$\int_0^1 x^2\,dx=\lim_{n\to\infty}\sum_{i=1}^n\Big(\tfrac in\Big)^2\tfrac1n=\lim_{n\to\infty}\frac{1}{n^3}\cdot\frac{n(n+1)(2n+1)}{6}=\frac13.$$

## 6. 易错点 (Pitfalls)

- 把积分值当几何面积（忽略符号）；上下限交换漏负号。

> [!tip] 衔接
> 用黎曼和直接算很繁琐；下一讲的 [[MIT 18.01 L19 Fundamental Theorem of Calculus I|FTC]] 把它化为求原函数，详见 [[Definite Integrals and the Fundamental Theorem of Calculus|定积分]]。

---

> [!important] 一句话总结
> 定积分是黎曼和的极限——有向面积与累积量的精确化身。
