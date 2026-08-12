---
aliases: [分部积分, Integration by Parts]
tags: [math, calculus]
up: "[[Integral Calculus and Differential Equations MOC]]"
related: "[[Partial Fraction Decomposition|部分分式]], [[Derivative and Integral Formula Tables|导数和积分公式]], [[Definite Integrals and the Fundamental Theorem of Calculus|定积分]]"
down: ""
---
# Integration by Parts

> [!summary] 核心结论
> 分部积分 (integration by parts) 是乘积求导法则的逆运算：$\int u\,dv=uv-\int v\,du$。它把一个难积的积分**交换**成一个更易积的积分。选 $u$ 用 **LIATE** 优先级（反对幂指三），目标是让 $\int v\,du$ 比原积分简单。

前置知识：[[Definite Integrals and the Fundamental Theorem of Calculus|定积分]]、求导乘法法则。

---

## 1. 原理 (The Formula)

公式直接来自乘积的微分法则 $d(uv)=u\,dv+v\,du$。两边积分并移项：

$$\int u\,dv=uv-\int v\,du.$$

含义：把被积式拆成 $u$ 与 $dv$ 两部分，用"已积出的 $uv$"换取"一个新积分 $\int v\,du$"——只要新积分更简单，交换就划算。

---

## 2. 如何选 $u$：LIATE 原则

按下列优先级**自上而下**选 $u$（剩下的归入 $dv$）：

1. **L**ogarithmic 对数函数（$\ln x$）
2. **I**nverse trig 反三角函数（$\arctan x,\arcsin x$）
3. **A**lgebraic 代数/幂函数（$x^n$）
4. **T**rigonometric 三角函数（$\sin x,\cos x$）
5. **E**xponential 指数函数（$e^x$）

中文口诀即"**反对幂指三**"。

> [!note] 为什么这样选
> 优先级高者（如 $\ln x$）求导后会**变简单**，适合当 $u$；优先级低者（如 $e^x,\cos x$）容易积分，适合当 $dv$。反过来选会让 $\int v\,du$ 越来越复杂。

---

## 3. 基本示例 (Basic Example)

$$\int x\cos x\,dx.$$

按 LIATE，代数项 $x$ 当 $u$，$dv=\cos x\,dx$；则 $du=dx$，$v=\sin x$：

$$\int x\cos x\,dx=x\sin x-\int\sin x\,dx=x\sin x+\cos x+C.$$

---

## 4. 进阶技巧 (Advanced Patterns)

### 4.1 循环积分 (Cyclic Integration)

$$I=\int e^x\sin x\,dx.$$

两次分部积分后**原积分重新出现**，解方程即可。取 $u=\sin x,\ dv=e^x dx$：

$$I=e^x\sin x-\int e^x\cos x\,dx.$$

对右端再分部（$u=\cos x,\ dv=e^x dx$）：

$$\int e^x\cos x\,dx=e^x\cos x+\int e^x\sin x\,dx=e^x\cos x+I.$$

代回：$I=e^x\sin x-\big(e^x\cos x+I\big)$，即 $2I=e^x(\sin x-\cos x)$，故

$$\int e^x\sin x\,dx=\frac{e^x(\sin x-\cos x)}{2}+C.$$

### 4.2 表格法 (Tabular Method)

当形如 $\int P(x)\,e^{ax}\,dx$（$P$ 为多项式）需多次分部时，用表格更快：左列对 $P$ **反复求导直到 $0$**，右列对 $e^{ax}$ **反复积分**，再按 $+,-,+,\dots$ 交错相乘相加。

$$\int x^3 e^x\,dx.$$

| 符号 | 求导列 $D$ | 积分列 $I$ |
| :--: | :-- | :-- |
| $+$ | $x^3$ | $e^x$ |
| $-$ | $3x^2$ | $e^x$ |
| $+$ | $6x$ | $e^x$ |
| $-$ | $6$ | $e^x$ |
| $+$ | $0$ | $e^x$ |

沿对角线相乘并按符号求和：

$$\int x^3 e^x\,dx=e^x\big(x^3-3x^2+6x-6\big)+C.$$

> [!tip] 衔接
> 若被积式是有理函数而非乘积，应改用 [[Partial Fraction Decomposition|部分分式]]；常用基本积分见 [[Derivative and Integral Formula Tables|导数和积分公式]]。
