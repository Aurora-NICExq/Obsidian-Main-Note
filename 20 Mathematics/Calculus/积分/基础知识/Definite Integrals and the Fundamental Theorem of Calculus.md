---
aliases: [定积分, Definite Integral, Fundamental Theorem of Calculus, FTC]
tags: [math, calculus]
up: "[[Integral Calculus and Differential Equations MOC]]"
related: "[[Variable-Limit Integrals and the Leibniz Rule|变限积分]], [[Improper Integrals|反常积分]], [[Integration by Parts|分部积分]], [[Partial Fraction Decomposition|部分分式]], [[Derivative and Integral Formula Tables|导数和积分公式]]"
down: "[[Variable-Limit Integrals and the Leibniz Rule|变限积分]], [[Improper Integrals|反常积分]]"
---
# Definite Integrals and the Fundamental Theorem of Calculus

> [!summary] 核心结论
> 微积分基本定理 (Fundamental Theorem of Calculus, FTC) 把"求积分"与"求导数"互为逆运算地联系起来：第一部分说**变上限积分的导数等于被积函数**；第二部分（牛顿–莱布尼茨公式）说**定积分等于原函数的增量**，从而把面积计算化为求原函数。

前置知识：[[Differentiation|求导]]。

---

## 1. 第一基本定理 (FTC, Part I)

若 $f$ 在 $[a,b]$ 上连续，定义变上限积分

$$F(x)=\int_a^x f(t)\,dt\quad (x\in[a,b]),$$

则 $F$ 在 $(a,b)$ 上可导，且

$$F'(x)=f(x),\qquad\text{即}\qquad \frac{\mathrm d}{\mathrm dx}\int_a^x f(t)\,\mathrm dt=f(x).$$

它说明：**积分的累积速度，恰好就是被积函数当前的高度**。

### 证明（导数定义 + 连续性夹逼）

对任意 $x\in(a,b)$，取充分小的 $h$（使 $x+h\in(a,b)$），由积分的区间可加性，

$$\frac{F(x+h)-F(x)}{h}=\frac{1}{h}\left(\int_a^{x+h}f(t)\,dt-\int_a^{x}f(t)\,dt\right)=\frac{1}{h}\int_x^{x+h}f(t)\,dt.$$

因为 $f$ 在 $x$ 处连续：对任意 $\varepsilon>0$，存在 $\delta>0$，使 $|t-x|<\delta$ 时 $f(x)-\varepsilon<f(t)<f(x)+\varepsilon$。当 $|h|<\delta$ 时，积分区间内的 $t$ 均满足此式，对其在长度 $h$ 上取平均得

$$f(x)-\varepsilon<\frac{1}{h}\int_x^{x+h}f(t)\,dt<f(x)+\varepsilon$$

（$h<0$ 时上下限与不等号同时翻转，结论一致）。这说明差商被夹在 $f(x)\pm\varepsilon$ 之间，故 $\lim_{h\to0}\dfrac{F(x+h)-F(x)}{h}=f(x)$，即 $F'(x)=f(x)$。$\blacksquare$

---

## 2. 第二基本定理 (FTC, Part II / Newton–Leibniz)

若 $f$ 在 $[a,b]$ 上连续，$F$ 是 $f$ 的**任意一个**原函数（反导数，antiderivative），则

$$\int_a^b f(x)\,\mathrm dx=F(b)-F(a).$$

> [!note] 与第一部分的联系
> 由 Part I，$G(x)=\int_a^x f$ 是 $f$ 的一个原函数。任意原函数 $F$ 与 $G$ 仅相差常数，故 $F(b)-F(a)=G(b)-G(a)=\int_a^b f-0=\int_a^b f$。这正是 Part II。

---

## 3. 变上限积分的求导处理 (Differentiating Variable-Limit Integrals)

当积分限是 $x$ 的函数或被积函数含参数时，需结合链式法则等技巧，分情形处理：

- **变量在积分下限**：交换上下限并变号，化为上限情形；
- **积分上限是函数 $\beta(x)$**：套用链式法则，详见 [[Chain Rule for Variable-Limit Integrals (Worked Example)|不定积分链式求导法则示例]]；
- **上下限都是函数**：拆成两段或用一般的 Leibniz 公式，见 [[Variable-Limit Integrals and the Leibniz Rule|变限积分]]。

---

## 4. 不定积分 (Indefinite Integral)

> [!important] 定义
> 若 $\dfrac{\mathrm d}{\mathrm dx}F(x)=f(x)$，则 $\displaystyle\int f(x)\,\mathrm dx=F(x)+C$。

不定积分表示 $f$ 的**全体原函数**，故必须带任意常数 $C$。计算上以基本公式（见 [[Derivative and Integral Formula Tables|导数和积分公式]]）为基石，配合换元 (substitution)、[[Integration by Parts|分部积分]] (integration by parts)、[[Partial Fraction Decomposition|部分分式]] (partial fractions) 等方法逐步化简。
