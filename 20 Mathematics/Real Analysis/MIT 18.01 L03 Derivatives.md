---
aliases: [MIT18.1-Lec03-导数（Derivatives）, 导数, Derivatives]
tags: [math, single-variable-calculus]
up: "[[Single-Variable Calculus (MIT 18.01) MOC]]"
related: "[[MIT 18.01 L02 Limits]], [[MIT 18.01 L04 Chain Rule]], [[Differentiation|求导]], [[Derivative and Integral Formula Tables|导数和积分公式]]"
down: "[[MIT 18.01 L04 Chain Rule]]"
---
# Derivatives

> [!summary] 核心结论
> 导数 (derivative) 同时表示**切线斜率、瞬时速度与局部线性近似**。它由差商取极限定义，并满足幂、乘积、商三大求导法则。可导 (differentiable) 必连续 (continuous)。

> 关键词：导数定义、三角导数、乘积/商法则、切线方程、可导与连续。

---

## 1. 定义与意义 (Definition)

$$f'(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}.$$

几何上是切线斜率，物理上是瞬时变化率。更系统的多角度讨论见 [[Differentiation|求导]]。

> [!note] 定理：可导 ⟹ 连续
> 若 $f$ 在 $x$ 可导，则 $\lim_{h\to0}\big(f(x+h)-f(x)\big)=\lim_{h\to0}\dfrac{f(x+h)-f(x)}{h}\cdot h=f'(x)\cdot0=0$，故 $f$ 连续。反之不真（如 $|x|$ 在 $0$）。$\blacksquare$

## 2. 基本求导法则 (Rules)

- 幂法则 (power rule)：$\dfrac{d}{dx}x^n=nx^{n-1}$；
- 乘积法则 (product rule)：$(fg)'=f'g+fg'$；
- 商法则 (quotient rule)：$\left(\dfrac{f}{g}\right)'=\dfrac{f'g-fg'}{g^2}$。

## 3. 三角函数导数（弧度制, Trig Derivatives）

$(\sin x)'=\cos x$，$(\cos x)'=-\sin x$，由此 $(\tan x)'=\sec^2 x$。其根基是关键极限 $\lim_{h\to0}\tfrac{\sin h}{h}=1$（见 [[MIT 18.01 L02 Limits]]）。

> [!note] 推导 $(\sin x)'=\cos x$
> 由和角公式，$\dfrac{\sin(x+h)-\sin x}{h}=\sin x\cdot\dfrac{\cos h-1}{h}+\cos x\cdot\dfrac{\sin h}{h}$。当 $h\to0$，$\tfrac{\sin h}{h}\to1$、$\tfrac{\cos h-1}{h}\to0$，故极限为 $\cos x$。$\blacksquare$

## 4. 切线方程与线性近似 (Tangent Line)

在 $x=a$ 处：$y=f(a)+f'(a)(x-a)$，这也是局部线性近似的来源（见 [[MIT 18.01 L09 Linear and Quadratic Approximations]]）。

## 5. 典型例题 (Examples)

- 乘积 + 三角：$f(x)=x^2\sin x\Rightarrow f'=2x\sin x+x^2\cos x$；
- 商法则：$f(x)=\dfrac{x}{\sin x}\Rightarrow f'=\dfrac{\sin x-x\cos x}{\sin^2 x}$。

## 6. 易错点 (Pitfalls)

- 商法则分子顺序写反；三角导数忘记弧度制；只套公式不做"结构拆解"导致漏项。

---

> [!important] 一句话总结
> 导数是差商的极限，统一了切线、速度与线性近似三种意义。
