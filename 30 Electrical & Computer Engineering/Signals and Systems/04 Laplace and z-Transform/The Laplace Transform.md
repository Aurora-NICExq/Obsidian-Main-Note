---
title: "The Laplace Transform"
aliases:
  - "拉普拉斯变换"
  - "ROC"
  - "收敛域"
  - "极点零点"
  - "s 平面"
tags: [signals_and_systems, ee, laplace]
up: "[[Signals and Systems MOC]]"
related:
  - "[[Continuous-Time Fourier Transform]]"
  - "[[Systems Represented by Differential and Difference Equations]]"
  - "[[The z-Transform]]"
  - "[[Continuous-Time Second-Order Systems]]"
---
# The Laplace Transform

> [!summary] 核心结论
> $$X(s)=\int_{-\infty}^{\infty}x(t)e^{-st}\,dt,\qquad s=\sigma+j\omega$$
> 把 CTFT 的 $j\omega$ 推广成整个复平面。多出来的 $e^{-\sigma t}$ 因子让**原本发散的信号也能变换**（比如 $e^{2t}u(t)$）。
> 代价是必须同时给出**收敛域 ROC** —— 同一个代数式配不同 ROC 对应完全不同的时域信号，只写 $X(s)$ 是不完整的。
> 两条判据：**ROC 含 $j\omega$ 轴 $\Leftrightarrow$ BIBO 稳定**；**ROC 是最右极点右侧的半平面 $\Leftrightarrow$ 因果**。两者同时成立 $\Leftrightarrow$ 全部极点在左半平面。

依据：奥本海姆 MIT OCW RES.6-007 [Lecture 20](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-20-the-laplace-transform/)；教材 §9。

前置：[[Continuous-Time Fourier Transform]]、[[Systems Represented by Differential and Difference Equations]]。

---

## 1. 为什么要推广 CTFT

CTFT 要求 $x$ 绝对可积。很多常见信号不满足：$u(t)$、$e^{2t}u(t)$、$t\,u(t)$ 都没有（常规意义的）傅里叶变换。

思路：先乘一个衰减因子 $e^{-\sigma t}$ 把它压下去，再做傅里叶变换：

$$
\mathcal{F}\{x(t)e^{-\sigma t}\}=\int x(t)e^{-\sigma t}e^{-j\omega t}dt=\int x(t)e^{-(\sigma+j\omega)t}dt
$$

令 $s=\sigma+j\omega$ 就是拉普拉斯变换。**CTFT 是拉普拉斯变换在 $\sigma=0$（虚轴）上的取值**：

$$
X(j\omega)=X(s)\big|_{s=j\omega}\quad(\text{当 } j\omega \text{ 轴在 ROC 内时})
$$

---

## 2. 收敛域（ROC）

$\int x(t)e^{-\sigma t}dt$ 是否收敛只取决于 $\sigma=\mathrm{Re}\{s\}$，所以 ROC 总是**平行于虚轴的带状 / 半平面区域**。

![[ss-the-laplace-transform-01.svg]]

| 信号类型 | ROC |
| ---- | ---- |
| 右边信号（$t<T_1$ 时为 0） | 最右极点**右侧**的半平面 |
| 左边信号（$t>T_2$ 时为 0） | 最左极点**左侧**的半平面 |
| 双边信号 | 两极点之间的**带状**区域 |
| 有限持续时间 | **整个 $s$ 平面**（可能除 0 或 $\infty$） |

ROC 内**不含任何极点**（极点处积分发散）。

> [!important] 为什么 ROC 不能省
> $$X(s)=\frac{1}{s+a}$$
> - ROC 为 $\mathrm{Re}\{s\}>-a$ $\Rightarrow$ $x(t)=e^{-at}u(t)$（右边）
> - ROC 为 $\mathrm{Re}\{s\}<-a$ $\Rightarrow$ $x(t)=-e^{-at}u(-t)$（左边）
>
> **同一个代数式，两个完全不同的信号。** 所以「$X(s)=1/(s+a)$」这句话本身没有意义，必须带上 ROC。
> 这也是拉普拉斯变换比傅里叶变换「麻烦」的唯一来源。

---

## 3. 有理系统函数

对 LCCDE 系统（见 [[Systems Represented by Differential and Difference Equations]]），两边取变换后得

$$
H(s)=\frac{\sum_kb_ks^k}{\sum_ka_ks^k}=\frac{N(s)}{D(s)}
$$

- $N(s)=0$ 的根：**零点**
- $D(s)=0$ 的根：**极点**

极点零点图（加上 ROC 和一个增益常数）**完整刻画了系统**。这是本课后半段的核心表示法。

---

## 4. 稳定性与因果性

两条判据，各自独立：

$$
\boxed{\;\text{BIBO 稳定}\iff \text{ROC 包含 } j\omega \text{ 轴}\;}
$$

理由：稳定 $\Leftrightarrow$ $\int|h(t)|dt<\infty$ $\Leftrightarrow$ $H(j\omega)$ 存在 $\Leftrightarrow$ 虚轴在 ROC 内。

$$
\boxed{\;\text{因果}\iff \text{ROC 是最右极点右侧的半平面}\;}
$$

（对有理 $H(s)$；一般情形是「ROC 是某个右半平面」。）

两条合起来：

$$
\text{因果 + 稳定}\iff\text{全部极点在左半平面（}\mathrm{Re}<0\text{）}
$$

这是控制和电路里天天用的那条判据的严格来源。

> [!note] 虚轴上的极点
> 极点恰在虚轴上（如 $1/s$ 对应积分器、$\frac{\omega_0}{s^2+\omega_0^2}$ 对应正弦振荡）$\Rightarrow$ 临界稳定：不发散但也不衰减。
> BIBO 意义下**不稳定**（有界输入可产生无界输出，比如给积分器加直流）。

---

## 5. 常用变换对

| $x(t)$ | $X(s)$ | ROC |
| ---- | ---- | ---- |
| $\delta(t)$ | $1$ | 全平面 |
| $u(t)$ | $1/s$ | $\mathrm{Re}\{s\}>0$ |
| $e^{-at}u(t)$ | $1/(s+a)$ | $\mathrm{Re}\{s\}>-a$ |
| $-e^{-at}u(-t)$ | $1/(s+a)$ | $\mathrm{Re}\{s\}<-a$ |
| $t^{n-1}e^{-at}u(t)/(n-1)!$ | $1/(s+a)^n$ | $\mathrm{Re}\{s\}>-a$ |
| $\cos(\omega_0t)u(t)$ | $s/(s^2+\omega_0^2)$ | $\mathrm{Re}\{s\}>0$ |
| $\sin(\omega_0t)u(t)$ | $\omega_0/(s^2+\omega_0^2)$ | $\mathrm{Re}\{s\}>0$ |

---

## 6. 性质

| 性质 | 时域 | $s$ 域 | ROC |
| ---- | ---- | ---- | ---- |
| 线性 | $ax_1+bx_2$ | $aX_1+bX_2$ | 至少是交集 |
| 时移 | $x(t-t_0)$ | $e^{-st_0}X(s)$ | 不变 |
| $s$ 域平移 | $e^{s_0t}x(t)$ | $X(s-s_0)$ | 平移 $\mathrm{Re}\{s_0\}$ |
| 尺度 | $x(at)$ | $\frac{1}{\lvert a\rvert}X(s/a)$ | 相应缩放 |
| **卷积** | $x*h$ | $XH$ | 至少是交集 |
| 微分 | $dx/dt$ | $sX(s)$ | 至少不变 |
| 积分 | $\int_{-\infty}^tx$ | $X(s)/s$ | 至少交 $\mathrm{Re}\{s\}>0$ |
| 初值 | $x(0^+)$ | $\lim_{s\to\infty}sX(s)$ | — |
| 终值 | $\lim_{t\to\infty}x(t)$ | $\lim_{s\to0}sX(s)$ | 需极点在左半平面 |

微分变成乘 $s$ —— 这就是「微分方程 $\to$ 代数方程」的机制。

---

## 7. 单边拉普拉斯变换

工程上更常用的是

$$
X(s)=\int_{0^-}^{\infty}x(t)e^{-st}dt
$$

好处：微分性质里自动带上初始条件

$$
\mathcal{L}\{x'(t)\}=sX(s)-x(0^-)
$$

于是可以直接求解**非零初值**的微分方程 —— 电路暂态分析走的就是这条路。双边变换则更适合讨论系统性质（稳定性、因果性），因为它保留了完整的 ROC 信息。

---

## 8. 速查

| 项目 | 内容 |
| ---- | ---- |
| 定义 | $X(s)=\int x(t)e^{-st}dt$ |
| 与 CTFT | $X(j\omega)=X(s)\rvert_{s=j\omega}$（虚轴在 ROC 内时） |
| ROC 形状 | 平行虚轴的半平面或带状；不含极点 |
| 稳定 | ROC 含 $j\omega$ 轴 |
| 因果 | ROC 是最右极点右侧的半平面 |
| 因果+稳定 | **全部极点在左半平面** |
| 微分 | $\to sX(s)$ |
| 卷积 | $\to X(s)H(s)$ |

---

## 参见

- [[Signals and Systems MOC]]
- [[Continuous-Time Fourier Transform]]（$\sigma=0$ 的特例）
- [[Systems Represented by Differential and Difference Equations]]（有理 $H(s)$ 的来源）
- [[Continuous-Time Second-Order Systems]]（极点位置与时域响应）
- [[The z-Transform]]（离散时间的对应物）
- [OCW Lecture 20 notes (PDF)](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec20/)
