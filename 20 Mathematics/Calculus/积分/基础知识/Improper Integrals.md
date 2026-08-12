---
aliases: [反常积分, Improper Integrals, 瑕积分]
tags: [math, calculus]
up: "[[Integral Calculus and Differential Equations MOC]]"
related: "[[Definite Integrals and the Fundamental Theorem of Calculus|定积分]], [[Integration by Parts|分部积分]], [[Variable-Limit Integrals and the Leibniz Rule|变限积分]]"
down: ""
---
# Improper Integrals

> [!summary] 核心结论
> 反常积分 (improper integral) 是普通定积分的极限推广，出现在两种情形：积分**区间无穷**，或被积函数在区间内**无界（瑕点）**。其值由极限定义，极限存在则**收敛 (converges)**，否则**发散 (diverges)**。判敛的核心工具是 $p$-积分基准 + 比较判别法。

前置知识：[[Definite Integrals and the Fundamental Theorem of Calculus|定积分]]。

---

## 1. 两类反常积分 (Two Types)

### 1.1 无穷区间 (Infinite Interval)

$$\int_a^{+\infty} f(x)\,dx=\lim_{t\to+\infty}\int_a^{t} f(x)\,dx=\lim_{t\to+\infty}\big[F(t)-F(a)\big].$$

极限存在则收敛。双侧无穷需**拆分**且**两段都收敛**才收敛：

$$\int_{-\infty}^{+\infty} f=\int_{-\infty}^{a} f+\int_{a}^{+\infty} f.$$

> [!warning] 对称性陷阱
> $(-\infty,+\infty)$ 不是有限对称区间，$\int_{-\infty}^{+\infty}f$ **不能**直接套用"偶倍奇零"。必须先确认两段各自收敛——否则会把发散积分误判为 $0$。

### 1.2 无界函数 / 瑕积分 (Unbounded Integrand)

设 $a$ 为**瑕点 (singularity)**（$f$ 在 $a$ 邻域无界），则

$$\int_a^{b} f(x)\,dx=\lim_{t\to a^+}\int_t^{b} f(x)\,dx=F(b)-F(a^+),$$

极限存在则收敛。

---

## 2. 基准结论：$p$-积分 (The $p$-Integrals)

这些是判敛的"标尺"，务必记牢两端的分界线 $p=1$：

$$\int_a^{+\infty}\frac{dx}{x^{p}}\ (a>0):\quad\begin{cases}p>1,&\text{收敛}\\ p\le 1,&\text{发散}\end{cases}$$

$$\int_a^{b}\frac{dx}{(x-a)^{q}},\ \int_a^{b}\frac{dx}{(b-x)^{q}}:\quad\begin{cases}q<1,&\text{收敛}\\ q\ge 1,&\text{发散}\end{cases}$$

含对数的精细情形（$a>1$）：

$$\int_a^{+\infty}\frac{dx}{x^{\alpha}\ln^{\beta}x}:\quad\begin{cases}\alpha>1,&\text{收敛}\\ \alpha<1,&\text{发散}\\ \alpha=1,&\begin{cases}\beta>1,&\text{收敛}\\ \beta\le 1,&\text{发散}\end{cases}\end{cases}$$

> [!note] 关键直觉：$f(x)=1/x$ 始终发散
> - 无穷区间 $[1,+\infty)$：$\int_1^{+\infty}\frac1x\,dx=\lim_{t\to\infty}\ln t=+\infty$，**发散**（虽然 $1/x\to0$，但衰减太慢）。
> - 瑕点附近 $(0,1]$：$\int_0^1\frac1x\,dx=\lim_{t\to0^+}(-\ln t)=+\infty$，**发散**。
>
> 故对 $1/x^p$，$p=1$ 是分界：无穷区间要 $p>1$ 收敛，瑕点附近要 $p<1$ 收敛，而 $p=1$ 两头都发散。

---

## 3. 判别法 (Convergence Tests)

### 3.1 比较判别法 (Comparison Test)

对 $\int_a^{+\infty} f$，若恒有 $0\le f(x)\le g(x)$，则

$$\int_a^{+\infty} g\ \text{收敛}\implies \int_a^{+\infty} f\ \text{收敛};\qquad \int_a^{+\infty} f\ \text{发散}\implies \int_a^{+\infty} g\ \text{发散}.$$

直觉：被更小的收敛积分压住者必收敛；比更大的发散积分还大者必发散。

### 3.2 极限形式判别法 (Limit Comparison Test)

若

$$\lim_{x\to+\infty\ (\text{或瑕点})}\frac{f(x)}{g(x)}=\ell\neq 0\ (\text{有限}),$$

则 $f$ 与 $g$ 的反常积分**同敛散**。实用做法是把 $f$ 与一个 $p$-积分比较，由 $\ell$ 有限非零读出敛散性。

---

## 4. 综合练习 (Worked Example)

> 判断 $\displaystyle\int_0^{+\infty}\frac{\sqrt{x}}{\arctan x+x^2}\,dx$ 的敛散性。

**拆分区间**分别讨论：
- 在 $0$ 附近，$\arctan x\sim x$，故被积函数 $\sim \dfrac{\sqrt x}{x}=x^{-1/2}$，对应瑕积分 $q=\tfrac12<1$，**收敛**；
- 在 $+\infty$，分母 $\sim x^2$，被积函数 $\sim \dfrac{\sqrt x}{x^2}=x^{-3/2}$，对应 $p=\tfrac32>1$，**收敛**。

两段皆收敛，故原积分**收敛**。计算技巧上常配合 [[Integration by Parts|分部积分]] 与 [[Variable-Limit Integrals and the Leibniz Rule|变限积分]] 的极限处理。
