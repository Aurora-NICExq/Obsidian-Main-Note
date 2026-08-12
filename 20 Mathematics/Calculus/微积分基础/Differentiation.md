---
aliases: [求导, Differentiation, Derivative]
tags: [math, calculus]
up: "[[Integral Calculus and Differential Equations MOC]]"
related: "[[Derivative and Integral Formula Tables|导数和积分公式]], [[Variable-Limit Integrals and the Leibniz Rule|变限积分]]"
down: "[[Definite Integrals and the Fundamental Theorem of Calculus|定积分]]"
---
# Differentiation

> [!summary] 核心结论
> 导数 (derivative) 度量函数在某点的**瞬时变化率**，几何上等于曲线该点处**切线的斜率**。它由差商 (difference quotient) 取极限定义；可导 (differentiable) 必连续 (continuous)，反之不然。

---

## 1. 三种等价的理解 (Three Views)

### 1.1 几何意义：切线斜率 (Geometric — Slope of the Tangent)

函数 $f(x)$ 在点 $P(x_0,y_0)$ 的导数，就是曲线在 $P$ 处**切线 (tangent line)** 的斜率：

- **割线 (secant line)**：连接曲线上 $A$、$B$ 两点的直线，其斜率代表两点间的**平均变化率 (average rate of change)**；
- **切线 (tangent line)**：当 $B$ 沿曲线无限趋近 $A$ 时，割线的极限位置即为切线。

因此求导的几何本质是：**取平均变化率在区间缩成一点时的极限**。

### 1.2 极限定义 (Limit Definition)

设 $y=f(x)$ 在 $x_0$ 的某邻域内有定义。自变量取增量 $\Delta x$ 时函数增量为 $\Delta y=f(x_0+\Delta x)-f(x_0)$，则 $f$ 在 $x_0$ 处的导数定义为差商的极限：

$$f'(x_0)=\lim_{\Delta x\to 0}\frac{\Delta y}{\Delta x}=\lim_{\Delta x\to 0}\frac{f(x_0+\Delta x)-f(x_0)}{\Delta x}.$$

常用 $h$ 记增量，写作 $f'(x)=\lim\limits_{h\to 0}\dfrac{f(x+h)-f(x)}{h}$。

> [!note] 可导的判据
> 只有当上述极限**存在且有限**（左、右极限相等）时，才称 $f$ 在该点**可导**。尖点、竖直切线、跳跃间断都会破坏可导性。

### 1.3 物理意义：瞬时变化率 (Instantaneous Rate of Change)

导数刻画"变化的快慢"。最典型的是运动学：

- 位移 $s(t)$ 求导得**瞬时速度 (velocity)** $v(t)=s'(t)$；
- 速度 $v(t)$ 求导得**瞬时加速度 (acceleration)** $a(t)=v'(t)$。

---

## 2. 可导与连续 (Differentiability ⟹ Continuity)

> [!important] 定理
> 若 $f$ 在 $x_0$ 处可导，则 $f$ 在 $x_0$ 处连续；反之不成立。

**证明.** 由可导性，$\lim_{x\to x_0}\dfrac{f(x)-f(x_0)}{x-x_0}=f'(x_0)$ 存在。于是

$$\lim_{x\to x_0}\big(f(x)-f(x_0)\big)=\lim_{x\to x_0}\frac{f(x)-f(x_0)}{x-x_0}\cdot(x-x_0)=f'(x_0)\cdot 0=0,$$

即 $\lim_{x\to x_0}f(x)=f(x_0)$，故 $f$ 连续。$\blacksquare$

反例说明逆命题不真：$f(x)=|x|$ 在 $0$ 处连续，但左导数 $-1\neq$ 右导数 $+1$，故不可导。

---

## 3. 记号体系 (Notation)

| 记号 | 名称 | 适用场合 |
| :-- | :-- | :-- |
| $f'(x),\ y'$ | 拉格朗日记号 (Lagrange) | 最常用 |
| $\dfrac{dy}{dx},\ \dfrac{d}{dx}f(x)$ | 莱布尼茨记号 (Leibniz) | 强调增量比、便于换元/链式法则 |
| $\dot{x},\ \dot{y}$ | 牛顿记号 (Newton) | 物理中对时间求导 |

> [!tip] 衔接
> 各类函数的具体求导公式见 [[Derivative and Integral Formula Tables|导数和积分公式]]；导数取极限的逆运算（积分）见 [[Definite Integrals and the Fundamental Theorem of Calculus|定积分]]。
