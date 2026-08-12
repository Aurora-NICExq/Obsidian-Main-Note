---
aliases: [MIT18.1-Lec02-极限（Limits）, 极限, Limits]
tags: [math, single-variable-calculus]
up: "[[Single-Variable Calculus (MIT 18.01) MOC]]"
related: "[[MIT 18.01 L01 Rate of Change]], [[MIT 18.01 L03 Derivatives]]"
down: "[[MIT 18.01 L03 Derivatives]]"
---
# Limits

> [!summary] 核心结论
> 极限 (limit) 关注函数值在靠近某点或趋于无穷时的**稳定趋势**，是导数与积分的共同基础。其严格语言是 $\varepsilon$-$\delta$ 定义。

> 关键词：左右极限、ε-δ、极限运算、夹逼、无穷与渐近线。

---

## 1. 定义与基本概念 (Definition)

- **$\varepsilon$-$\delta$ 定义**：

$$\lim_{x\to a}f(x)=L\iff(\forall\varepsilon>0)(\exists\delta>0):0<|x-a|<\delta\Rightarrow|f(x)-L|<\varepsilon.$$

- **左右极限 (one-sided limits)**：$\lim_{x\to a^-}f,\ \lim_{x\to a^+}f$；双侧极限存在 $\iff$ 左右极限都存在且相等。
- 极限与函数值无关：$f(a)$ 可不存在，而 $\lim_{x\to a}f$ 仍可能存在。

## 2. 极限运算法则 (Limit Laws)

- 线性：$\lim(af+bg)=a\lim f+b\lim g$；
- 乘积：$\lim(fg)=(\lim f)(\lim g)$；
- 商：$\lim(f/g)=(\lim f)/(\lim g)$，要求 $\lim g\neq 0$；
- 复合：若 $g(x)\to b$ 且 $f$ 在 $b$ 连续，则 $f(g(x))\to f(b)$。

## 3. 计算技巧 (Techniques)

- **因式分解/约分**：解决 $0/0$ 的可去型；
- **有理化 (rationalization)**：处理根式差；
- **关键极限**：$\displaystyle\lim_{x\to 0}\frac{\sin x}{x}=1$；
- **夹逼定理 (Squeeze Theorem)**：用上下界确定极限。

> [!note] 关键极限的几何证明 $\lim_{x\to0}\frac{\sin x}{x}=1$
> 在单位圆中，对 $0<x<\tfrac\pi2$ 比较面积：三角形 $<$ 扇形 $<$ 大三角形，得 $\tfrac12\sin x<\tfrac12 x<\tfrac12\tan x$。除以 $\tfrac12\sin x$ 得 $1<\dfrac{x}{\sin x}<\dfrac{1}{\cos x}$，取倒数 $\cos x<\dfrac{\sin x}{x}<1$。$x\to0$ 时 $\cos x\to1$，由夹逼得极限为 $1$。$\blacksquare$

## 4. 无穷远与渐近线 (Infinity & Asymptotes)

- $\lim_{x\to\infty}f(x)=L$ 对应水平渐近线 $y=L$；
- 有理函数：同次看最高次系数比，异次看增长阶。

## 5. 典型例题 (Examples)

$$\lim_{x\to1}\frac{x^2-1}{x-1}=2,\quad \lim_{x\to0}\frac{\sqrt{1+x}-1}{x}=\frac12,\quad \lim_{x\to\infty}\frac{3x^2-1}{x^2+2}=3.$$

## 6. 易错点 (Pitfalls)

- 忘记检查分母极限是否为 $0$；只算单侧就断言双侧极限存在；把"极限存在"误当"连续"。

---

> [!important] 一句话总结
> 极限刻画函数的稳定趋势——它把"无限逼近"严格化，为 [[MIT 18.01 L03 Derivatives|导数]] 与积分奠基。
