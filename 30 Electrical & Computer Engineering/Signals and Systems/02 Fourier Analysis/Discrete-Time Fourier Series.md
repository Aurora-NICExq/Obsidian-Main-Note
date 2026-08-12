---
title: "Discrete-Time Fourier Series"
aliases:
  - "离散时间傅里叶级数"
  - "DTFS"
  - "周期序列的谱"
tags: [signals_and_systems, ee, fourier]
up: "[[Signals and Systems MOC]]"
related:
  - "[[Continuous-Time Fourier Series]]"
  - "[[Discrete-Time Fourier Transform]]"
  - "[[Sinusoidal and Exponential Signals]]"
---
# Discrete-Time Fourier Series

> [!summary] 核心结论
> 周期为 $N$ 的序列只有 **$N$ 个不同的谐波**（因为 $e^{j(k+N)(2\pi/N)n}=e^{jk(2\pi/N)n}$），所以 DTFS 是一个**有限和**。
> 这一条带来了 CTFS 没有的好处：**没有收敛性问题，没有吉布斯现象**，级数严格等于原序列。DTFS 是四种傅里叶表示里唯一完全没有分析学麻烦的。
> 另一个后果：系数序列 $a_k$ 自己也是周期 $N$ 的。

依据：奥本海姆 MIT OCW RES.6-007 [Lecture 10](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-10-discrete-time-fourier-series/)；教材 §3.6–3.7。

前置：[[Continuous-Time Fourier Series]]、[[Sinusoidal and Exponential Signals]]。

---

## 1. 谐波只有 $N$ 个

离散复指数 $\phi_k[n]=e^{jk(2\pi/N)n}$ 有一条连续时间没有的性质：

$$
\phi_{k+N}[n]=e^{j(k+N)(2\pi/N)n}=e^{jk(2\pi/N)n}\cdot\underbrace{e^{j2\pi n}}_{=1}=\phi_k[n]
$$

**第 $k+N$ 次谐波与第 $k$ 次谐波是同一个序列。** 所以只有 $N$ 个线性无关的谐波，取 $k=0,1,\dots,N-1$（或任意 $N$ 个连续整数）即可。

这与连续时间形成鲜明对比：CT 里 $e^{jk\omega_0t}$ 对不同 $k$ 全都不同，谐波有无穷多个。

---

## 2. 分析式与综合式

**综合**（有限和！）：

$$
x[n]=\sum_{k=\langle N\rangle}a_k\,e^{jk(2\pi/N)n}
$$

**分析**：

$$
a_k=\frac{1}{N}\sum_{n=\langle N\rangle}x[n]\,e^{-jk(2\pi/N)n}
$$

$\langle N\rangle$ 表示任意 $N$ 个连续整数。两式高度对称 —— 只差一个共轭、一个 $1/N$。

![[ss-discrete-time-fourier-series-01.svg]]

由同样的理由，系数序列也是周期的：

$$
a_{k+N}=a_k
$$

所以 DTFS 是**周期序列 $\leftrightarrow$ 周期序列**的映射，两边都只有 $N$ 个自由度。信息量守恒，一目了然。

---

## 3. 没有收敛性问题

CTFS 需要讨论狄利克雷条件、均方收敛、吉布斯现象（见 [[Continuous-Time Fourier Series]]）；DTFS 完全不需要。

原因很简单：综合式是 $N$ 项的**有限**和，只要 $x[n]$ 有界，一切都是有限运算。不存在「部分和是否收敛到原函数」的问题 —— 取满 $N$ 项就**严格相等**。

> [!important] 为什么不会有吉布斯现象
> 吉布斯现象来自「用有限项逼近一个有跳变的函数」。DTFS 里根本没有「有限项逼近」这回事 —— $N$ 项就是全部。
> 离散序列也没有「跳变」的概念：相邻样点差多少都只是两个数，不构成不连续点。

---

## 4. 与 CTFS 的对照

| | CTFS | DTFS |
| ---- | ---- | ---- |
| 谐波个数 | 无穷 | **$N$ 个** |
| 综合式 | 无穷级数 | **有限和** |
| 系数 | $a_k$ 非周期 | $a_k$ **周期 $N$** |
| 收敛性 | 需狄利克雷条件 | 无条件成立 |
| 吉布斯现象 | 有 | **无** |
| 基频 | $\omega_0=2\pi/T_0$ | $\Omega_0=2\pi/N$ |

---

## 5. 例：离散周期方波

设周期 $N$，一个周期内 $|n|\le N_1$ 时 $x[n]=1$，其余为 0。

$$
a_k=\frac{1}{N}\sum_{n=-N_1}^{N_1}e^{-jk(2\pi/N)n}
=\frac{1}{N}\cdot\frac{\sin\big(k(2\pi/N)(N_1+\tfrac12)\big)}{\sin\big(k\pi/N\big)}
$$

这是**离散形式的 sinc**（Dirichlet 核）。$k=0$ 时取极限得 $a_0=(2N_1+1)/N$，即占空比。

注意它与 [[Discrete-Time Fourier Transform|DTFT]] 里同一个矩形序列的变换长得一模一样 —— 后者正是前者在 $N\to\infty$ 时的包络，这与 CTFS $\to$ CTFT 的关系完全平行。

---

## 6. 性质

与 CTFS 基本一一对应，但所有「移位」都是**循环**的（因为一切都以 $N$ 为周期）：

| 性质 | 时域 | 频域 |
| ---- | ---- | ---- |
| 线性 | $ax_1+bx_2$ | $aa_k+bb_k$ |
| 时移 | $x[n-n_0]$ | $a_ke^{-jk(2\pi/N)n_0}$ |
| 频移 | $e^{jM(2\pi/N)n}x[n]$ | $a_{k-M}$ |
| **周期卷积** | $\sum_{r=\langle N\rangle}x_1[r]x_2[n-r]$ | $N\,a_kb_k$ |
| 相乘 | $x_1[n]x_2[n]$ | $\sum_{l=\langle N\rangle}a_lb_{k-l}$ |
| 帕塞瓦尔 | $\frac{1}{N}\sum_{n=\langle N\rangle}\lvert x\rvert^2$ | $\sum_{k=\langle N\rangle}\lvert a_k\rvert^2$ |

「周期卷积」而非普通卷积这一点很关键 —— 它是后来 DFT / FFT 里「循环卷积」陷阱的根源。

---

## 7. 与 DFT 的关系

DTFS 系数（乘个 $N$）就是**离散傅里叶变换（DFT）**：

$$
X[k]=N\,a_k=\sum_{n=0}^{N-1}x[n]e^{-j2\pi kn/N}
$$

FFT 算的就是这个。所以 DTFS 不只是理论上的对称品，它是**唯一一种计算机能直接算的傅里叶表示** —— 两边都是有限个数。

---

## 参见

- [[Signals and Systems MOC]]
- [[Continuous-Time Fourier Series]]（对照的连续版本）
- [[Discrete-Time Fourier Transform]]（$N\to\infty$ 的极限）
- [[Sinusoidal and Exponential Signals]]（离散复指数的周期性）
- [OCW Lecture 10 notes (PDF)](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec10/)
