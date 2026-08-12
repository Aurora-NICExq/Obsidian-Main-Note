---
title: "正弦信号和指数信号"
aliases: ["Sinusoidal and Exponential Signals", "正弦与指数信号"]
tags: [signals_and_systems, ee]
up: "[[Signals and Systems MOC]]"
related: ["[[Ideal and Lossy LC Tanks]]", "[[Source-Free and Driven RC Response]]", "[[Differential Equations and the Number e]]", "[[Continuous-Time Fourier Series]]"]
---
# 正弦信号和指数信号

> [!summary] 核心结论
> 连续时间正弦信号中，时移与相移始终等价；离散时间正弦信号则不然——相移不一定对应整数采样点的时移，且周期性还额外要求数字角频率满足有理条件。实指数信号按指数律增长或衰减，是后续复指数与 LTI 分析的基础。

---
## 1. 连续时间正弦信号

### 1.1 定义与参数

$$
x(t)=A\cos(\omega_0 t+\phi)
$$

其中：

- $A$：振幅
- $\omega_0$：角频率（$\mathrm{rad/s}$），$f_0=\dfrac{|\omega_0|}{2\pi}$
- $\phi$：初相位（$\mathrm{rad}$）
- 基波周期：$T_0=\dfrac{2\pi}{|\omega_0|}$（$\omega_0\neq 0$）

也可用正弦形式写出，二者只差一个固定相位：
$$
A\sin(\omega_0 t)=A\cos\!\left(\omega_0 t-\frac{\pi}{2}\right)
$$

![[ss-cosine-ct.svg]]

### 1.2 时移与相移等价

把相位写成时延：
$$
A\cos(\omega_0 t+\phi)=A\cos\!\big(\omega_0(t-t_0)\big),\qquad t_0=-\frac{\phi}{\omega_0}
$$

连续时间下，$t_0$ 可以是任意实数，因此时移与相移始终一一对应。

> [!example] $\phi=-\pi/2$ 的三种等价写法
> $$
> \phi=-\frac{\pi}{2},\qquad
> x(t)=\begin{cases}
> A\cos\!\left(\omega_0 t-\dfrac{\pi}{2}\right)\\[6pt]
> A\sin\omega_0 t\\[6pt]
> A\cos\!\left[\omega_0\!\left(t-\dfrac{T_0}{4}\right)\right]
> \end{cases}
> $$
> 第三式成立是因为 $T_0=\dfrac{2\pi}{\omega_0}$，故
> $\omega_0\cdot\dfrac{T_0}{4}=\dfrac{\pi}{2}$。

### 1.3 奇偶性

对实信号：

- 偶信号：$x(-t)=x(t)$
- 奇信号：$x(-t)=-x(t)$

常见结论：

- $\cos(\omega_0 t)$ 是偶信号
- $\sin(\omega_0 t)$ 是奇信号
- 一般相位的 $A\cos(\omega_0 t+\phi)$ 既非奇也非偶（除非 $\phi$ 取特殊值，如 $0,\pm\pi/2,\pi$）

任意实信号都可唯一分解为偶部与奇部：
$$
x_e(t)=\frac{x(t)+x(-t)}{2},\qquad
x_o(t)=\frac{x(t)-x(-t)}{2}
$$

---
## 2. 离散时间正弦信号

### 2.1 定义

$$
x[n]=A\cos(\Omega_0 n+\phi)
$$

其中 $\Omega_0$ 是数字角频率（$\mathrm{rad/sample}$）。$n$ 只能取整数。

![[ss-cosine-dt.svg]]

### 2.2 时移与相移：不再总等价

形式上仍可写：
$$
A\cos(\Omega_0 n+\phi)=A\cos\!\big(\Omega_0(n-n_0)\big),\qquad n_0=-\frac{\phi}{\Omega_0}
$$

但序列的时移 $x[n-n_0]$ 要求 $n_0$ 为整数。因此：

- 连续时间：任意相移都对应某个实数时移
- 离散时间：只有当 $-\phi/\Omega_0$ 为整数时，相移才等于序列的整数时移；否则只能看作“相位变化”，不能简单解释成把样点整体左右搬移

### 2.3 周期性条件

$x[n]=A\cos(\Omega_0 n+\phi)$ 以正整数 $N$ 为周期，当且仅当存在整数 $m$，使
$$
\Omega_0 N=2\pi m
\quad\Leftrightarrow\quad
\frac{\Omega_0}{2\pi}=\frac{m}{N}\in\mathbb{Q}
$$

即 $\Omega_0/(2\pi)$ 必须是有理数。此时最小正周期是使上式成立的最小正整数 $N$。

> [!attention] 与连续时间的对比
> 连续时间正弦只要 $\omega_0\neq 0$ 就一定周期；离散时间正弦即使 $\Omega_0\neq 0$，若 $\Omega_0/(2\pi)$ 无理，则不是周期序列。

---
## 3. 实指数信号

### 3.1 连续时间

$$
x(t)=Ce^{at}
$$

- $a>0$：指数增长
- $a<0$：指数衰减（常称负指数）
- $a=0$：常数信号 $x(t)=C$

![[ss-real-exponential.svg]]

### 3.2 离散时间

$$
x[n]=Ca^{n}
$$

- $|a|>1$：幅度增长
- $|a|<1$：幅度衰减
- $a<0$：符号逐点交替，并叠加增长或衰减

> [!note] 与电路、ODE 的联系
> 一阶 RC/RL 的自然响应 $e^{-t/\tau}$、欠阻尼 RLC 的包络 $e^{-\alpha t}$，都是实指数衰减；正弦振荡则可看作虚指数（欧拉公式）的实部。参见 [[Ideal and Lossy LC Tanks]]、[[Source-Free and Driven RC Response]]。

---
## 4. 对照小结

| 项目 | 连续时间 | 离散时间 |
| --- | --- | --- |
| 正弦形式 | $A\cos(\omega_0 t+\phi)$ | $A\cos(\Omega_0 n+\phi)$ |
| 时移 $\Leftrightarrow$ 相移 | 始终成立 | 仅当时移量为整数时成立 |
| 周期性 | $\omega_0\neq 0$ 即周期 | 需 $\Omega_0/(2\pi)$ 为有理数 |
| 实指数 | $Ce^{at}$ | $Ca^{n}$ |

---
## 参见
- [[Signals and Systems MOC]]
- [[Ideal and Lossy LC Tanks]]（衰减正弦与指数包络）
- [[Source-Free and Driven RC Response]]（$e^{-t/\tau}$ 自然响应）
- [[Differential Equations and the Number e]]（实指数与虚指数的统一视角）
