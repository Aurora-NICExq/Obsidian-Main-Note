---
aliases: [MIT18.1-Lec14-平均值定理（Mean Value Theorem）, 平均值定理, Mean Value Theorem, MVT]
tags: [math, single-variable-calculus]
up: "[[Single-Variable Calculus (MIT 18.01) MOC]]"
related: "[[MIT 18.01 L13 Newton's Method]], [[MIT 18.01 L15 Differentials and Antiderivatives]]"
down: "[[MIT 18.01 L15 Differentials and Antiderivatives]]"
---
# Mean Value Theorem

> [!summary] 核心结论
> 平均值定理 (Mean Value Theorem, MVT) 把区间上的**平均变化率**与某内点的**瞬时变化率**联系起来：存在 $c$ 使 $f'(c)$ 等于割线斜率。它是"由导数信息反推函数性质"的桥梁。

> 关键词：Rolle、MVT、导数界、单调性、差值估计。

---

## 1. 罗尔定理 (Rolle's Theorem)

若 $f$ 在 $[a,b]$ 连续、在 $(a,b)$ 可导，且 $f(a)=f(b)$，则 $\exists c\in(a,b)$ 使 $f'(c)=0$。

## 2. 平均值定理 (MVT)

条件同上（去掉 $f(a)=f(b)$），则

$$\exists c\in(a,b):\quad f'(c)=\frac{f(b)-f(a)}{b-a}.$$

> [!note] 证明骨架（值得记住）
> 构造 $g(x)=f(x)-\ell(x)$，其中 $\ell$ 是连接 $(a,f(a))$、$(b,f(b))$ 的割线。则 $g(a)=g(b)$，对 $g$ 用罗尔定理得 $g'(c)=0$，即 $f'(c)=\ell'=\dfrac{f(b)-f(a)}{b-a}$。$\blacksquare$

## 3. 推论 (Corollaries)

- 区间内 $f'\equiv0\Rightarrow f$ 为常数；
- $f'>0\Rightarrow f$ 严格递增；
- $|f'|\le M\Rightarrow |f(b)-f(a)|\le M|b-a|$（导数界给出函数界，是误差估计的利器）。

## 4. 易错点 (Pitfalls)

- 忽略连续/可导条件；把"存在某点"误当"处处成立"。

---

> [!important] 一句话总结
> MVT：割线斜率必被某点的切线斜率命中——它让导数的局部信息约束函数的整体行为。
