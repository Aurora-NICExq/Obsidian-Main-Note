---
aliases: [MIT18.1-Lec22-体积（Volumes）, 体积, Volumes]
tags: [math, single-variable-calculus]
up: "[[Single-Variable Calculus (MIT 18.01) MOC]]"
related: "[[MIT 18.01 L21 Applications of the Integral to Logarithms]], [[MIT 18.01 L23 Work, Average Value, and Probability]]"
down: "[[MIT 18.01 L23 Work, Average Value, and Probability]]"
---
# Volumes

> [!summary] 核心结论
> 求体积 (volume) 的核心是选取**切片面积 $A(x)$**，再把切片沿轴累加成积分 $V=\int A(x)\,dx$。旋转体用圆盘/垫片法 (disk/washer) 或壳层法 (shell)。

> 关键词：切片法、旋转体、圆盘/垫片、壳层法。

---

## 1. 通用切片法 (Slicing)

若垂直某轴的截面积为 $A(x)$，则

$$V=\int_a^b A(x)\,dx.$$

## 2. 圆盘 / 垫片（绕 $x$ 轴, Disk/Washer）

- 圆盘 (disk)：$V=\pi\displaystyle\int_a^b R(x)^2\,dx$；
- 垫片 (washer)：$V=\pi\displaystyle\int_a^b\big(R(x)^2-r(x)^2\big)\,dx$（中空时减去内半径）。

## 3. 壳层法（绕 $y$ 轴, Shell）

$$V=2\pi\int_a^b x\,h(x)\,dx.$$

每个薄壳是周长 $2\pi x$ × 高 $h(x)$ × 厚 $dx$。

## 4. 例题 (Examples)

- $y=\sqrt x$ 绕 $x$ 轴（$0\le x\le1$）：$V=\pi\int_0^1 x\,dx=\dfrac\pi2$；
- $0\le y\le x\le1$ 绕 $y$ 轴（壳层）：$V=2\pi\int_0^1 x\cdot x\,dx=\dfrac{2\pi}{3}$。

## 5. 易错点 (Pitfalls)

- 半径/高度读错；忘记平方（圆盘）或忘记 $2\pi$（壳层）；绕轴选错导致方法用反。

---

> [!important] 一句话总结
> 体积 = 选切片面积 $A(x)$ 再积分；旋转体在圆盘/垫片与壳层之间按绕轴选择。
