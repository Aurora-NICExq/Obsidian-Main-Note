---
aliases: [一阶微分方程, Ordinary Differential Equations, First-Order Differential Equations]
tags: [math, calculus]
up: "[[Integral Calculus and Differential Equations MOC]]"
related: "[[Nonhomogeneous Linear ODEs|非齐次微分方程]], [[Differential Equations and the Number e|微分方程与自然常数]], [[Differential Equations through Linear Algebra|微分方程与线性代数]], [[Particular-Solution Forms Table|非齐次特解微分方程特解表格]]"
down: "[[Nonhomogeneous Linear ODEs|非齐次微分方程]]"
---
# Ordinary Differential Equations (Foundations and Methods)

> [!summary] 核心结论
> 微分方程 (differential equation) 描述未知函数与其导数之间的关系，刻画的是"如何变化"而非"是多少"。本笔记从定义与阶 (order) 出发，依次给出三类基本可解方程：**可分离变量 (separable)**、**一阶线性 (first-order linear, 积分因子法)**、**二阶常系数齐次 (constant-coefficient homogeneous, 特征方程法)**。

---

## 1. 定义与阶 (Definition & Order)

只要方程含未知函数 $y$ **及其导数** $\big(\tfrac{dy}{dx},y'',\dots\big)$，它就是微分方程。其**阶 (order)** 是出现的最高阶导数的阶。例如

$$x^2\frac{d^4y}{dx^4}+\sin(x)\frac{d^2y}{dx^2}\left(\frac{dy}{dx}\right)^7+e^x y=\tan x$$

是**四阶**方程（最高为四阶导数）。

> [!note] 核心视角
> 微分方程不是静态地描述"$y$ 等于多少"，而是动态地描述"$y$ 如何变化"。求解就是从这条变化规律反推出函数本身。

---

## 2. 可分离变量方程 (Separable Equations)

若能把所有含 $y$ 的部分（含 $dy$）移到一边、所有含 $x$ 的部分（含 $dx$）移到另一边，则方程**可分离变量**，两边分别积分即可。

最重要的范例是 $\dfrac{dy}{dx}=ky$：分离为 $\dfrac{1}{ky}\,dy=dx$，积分得 $y=Ce^{kx}$——这正是指数增长/衰减的来源（详见 [[Differential Equations and the Number e|微分方程与自然常数]]）。另一个三角范例：

$$\frac{dy}{dx}-\cos^2(y)\cos(x)=0\ \Longrightarrow\ \sec^2(y)\,dy=\cos(x)\,dx.$$

---

## 3. 一阶线性方程：积分因子法 (Integrating Factor)

**标准形式**（务必先令 $y'$ 系数为 $1$）：

$$\frac{dy}{dx}+P(x)\,y=Q(x).$$

引入**积分因子 (integrating factor)** $\mu(x)=e^{\int P(x)\,dx}$（此处积分不另加常数 $C$，取 $C=0$）。

> [!important] 为什么是 $e^{\int P\,dx}$
> 我们希望方程左边恰好是某个乘积的导数。两边乘 $\mu$ 后左边为 $\mu y'+\mu P y$；要它等于 $(\mu y)'=\mu y'+\mu' y$，只需 $\mu'=\mu P$，即 $\dfrac{\mu'}{\mu}=P$，积分得 $\ln\mu=\int P\,dx$，故 $\mu=e^{\int P\,dx}$。这就是积分因子的来历。

**求解步骤：**

1. **标准化**：化为 $y'+P(x)y=Q(x)$。
2. **求积分因子**：$\mu(x)=e^{\int P\,dx}$。
3. **两边乘 $\mu$**：左边凑成 $\dfrac{d}{dx}\big[\mu(x)\,y\big]=\mu(x)Q(x)$。
4. **两边积分**：$\mu(x)\,y=\displaystyle\int \mu(x)Q(x)\,dx+C$。
5. **解出 $y$**：

$$y=\frac{1}{\mu(x)}\left(\int \mu(x)Q(x)\,dx+C\right).$$

---

## 4. 常系数线性方程 (Constant-Coefficient Linear ODE)

一般形式为

$$a_n\frac{d^n y}{dx^n}+\cdots+a_1\frac{dy}{dx}+a_0 y=f(x).$$

当 $f(x)\equiv 0$ 时为**齐次 (homogeneous)**；否则为**非齐次 (nonhomogeneous)**，其通解 $=$ 齐次通解 $+$ 一个特解（见 [[Nonhomogeneous Linear ODEs|非齐次微分方程]] 与 [[Differential Equations through Linear Algebra|微分方程与线性代数]]）。

---

## 5. 二阶常系数齐次方程 (Second-Order Homogeneous)

对 $ay''+by'+cy=0$，设 $y=e^{tx}$ 代入得**特征方程 (characteristic equation)**：

$$at^2+bt+c=0.$$

按判别式分三种情形给出通解：

| 特征根情况 | 通解形式 |
| :-- | :-- |
| 两个相异实根 $\alpha\neq\beta$ | $y=A e^{\alpha x}+B e^{\beta x}$ |
| 一个重根 $\alpha$ | $y=A e^{\alpha x}+Bx\,e^{\alpha x}$ |
| 共轭复根 $\alpha\pm i\beta$ | $y=e^{\alpha x}\big(A\cos\beta x+B\sin\beta x\big)$ |

这三种情形恰好对应物理中的三类运动：[[Damped Oscillation|根对应阻尼振动的三种形态]]（过阻尼、临界阻尼、欠阻尼）。
