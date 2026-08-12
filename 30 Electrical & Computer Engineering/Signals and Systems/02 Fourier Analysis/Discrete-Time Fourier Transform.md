---
title: "Discrete-Time Fourier Transform"
aliases:
  - "离散时间傅里叶变换"
  - "DTFT"
  - "2π 周期性"
tags: [signals_and_systems, ee, fourier]
up: "[[Signals and Systems MOC]]"
related:
  - "[[Discrete-Time Fourier Series]]"
  - "[[Continuous-Time Fourier Transform]]"
  - "[[Filtering]]"
  - "[[The z-Transform]]"
---
# Discrete-Time Fourier Transform

> [!summary] 核心结论
> $$X(e^{j\Omega})=\sum_{n=-\infty}^{\infty}x[n]e^{-j\Omega n},\qquad x[n]=\frac{1}{2\pi}\int_{2\pi}X(e^{j\Omega})e^{j\Omega n}d\Omega$$
> 与 CTFT 的**决定性差别**：$X(e^{j\Omega})$ 对 $\Omega$ 恒为 $2\pi$ 周期。因为 $e^{j(\Omega+2\pi)n}=e^{j\Omega n}$ —— 离散时间里根本不存在高于 $\pi$ 的频率。
> $\Omega=0$ 是直流，$\Omega=\pi$ 是**最高频率**（相邻样点正负交替），$\Omega=2\pi$ 又回到直流。

依据：奥本海姆 MIT OCW RES.6-007 [Lecture 11](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-11-discrete-time-fourier-transform/)；教材 §5.1–5.2。

前置：[[Discrete-Time Fourier Series]]、[[Continuous-Time Fourier Transform]]。

---

## 1. 从 DTFS 取极限

与 CTFS $\to$ CTFT 的路线完全平行：把有限长序列以周期 $N$ 延拓，求 DTFS 系数，再令 $N\to\infty$。

谐波间距 $\Omega_0=2\pi/N\to0$，离散的 $\{Na_k\}$ 铺满成连续函数 $X(e^{j\Omega})$，求和过渡为积分。

**唯一的差别**：CT 里 $T_0\to\infty$ 让频率轴变成整条实轴；DT 里 $N\to\infty$ 只让频率轴在**长度 $2\pi$ 的一个区间内**变稠密 —— 区间本身不会变长。这正是周期性的来源。

---

## 2. 分析式与综合式

$$
\boxed{\;X(e^{j\Omega})=\sum_{n=-\infty}^{\infty}x[n]\,e^{-j\Omega n}\;}
$$

$$
\boxed{\;x[n]=\frac{1}{2\pi}\int_{2\pi}X(e^{j\Omega})\,e^{j\Omega n}\,d\Omega\;}
$$

注意积分只在**任意一个长度 $2\pi$ 的区间**上做（通常取 $-\pi$ 到 $\pi$），不是整条实轴。

记号 $X(e^{j\Omega})$ 而非 $X(\Omega)$ 是刻意的：它提醒你自变量实际是单位圆上的点 $e^{j\Omega}$，这直接接到 [[The z-Transform|z 变换]]（$z=e^{j\Omega}$ 就是单位圆）。

---

## 3. $2\pi$ 周期性

![[ss-discrete-time-fourier-transform-01.svg]]

$$
X(e^{j(\Omega+2\pi)})=X(e^{j\Omega})
$$

> [!important] 「高频」在离散时间里是什么意思
> 连续时间：$\omega$ 越大振荡越快，没有上限。
> 离散时间：$\Omega$ 从 0 增大到 $\pi$ 时振荡越来越快；**过了 $\pi$ 反而变慢**，到 $2\pi$ 又回到直流。
>
> $\Omega=\pi$ 时 $e^{j\pi n}=(-1)^n$ —— 相邻样点正负交替，这是采样序列能表现的最快变化。想更快？做不到，样点之间没有东西。
>
> 这条直接解释了采样定理里的 $\pi$（或 $\omega_s/2$）为什么是那个魔法边界。

实用后果：所有 DT 频率响应图只需画 $0$ 到 $\pi$（实信号再加上对称性）。

---

## 4. 例：矩形序列

$x[n]=1$ 对 $|n|\le N_1$，其余为 0：

$$
X(e^{j\Omega})=\sum_{n=-N_1}^{N_1}e^{-j\Omega n}
=\frac{\sin\big(\Omega(N_1+\tfrac12)\big)}{\sin(\Omega/2)}
$$

这是 **Dirichlet 核**，也叫「周期 sinc」。注意分母是 $\sin(\Omega/2)$ 而不是 $\Omega/2$ —— 正是这个 $\sin$ 造成了 $2\pi$ 周期。当 $\Omega$ 很小时 $\sin(\Omega/2)\approx\Omega/2$，局部退化成普通 sinc。

对偶的例子：理想低通 $H(e^{j\Omega})=1$ 对 $|\Omega|<\Omega_c$（在一个周期内），其冲激响应

$$
h[n]=\frac{\sin(\Omega_cn)}{\pi n}
$$

同样非因果、同样不绝对可和 —— 见 [[Filtering]]。

---

## 5. 收敛性

分析式是无穷和，需要条件。两个充分条件：

- **绝对可和** $\sum|x[n]|<\infty$ $\Rightarrow$ 一致收敛。
- **平方可和** $\sum|x[n]|^2<\infty$ $\Rightarrow$ 均方收敛（此时有吉布斯现象）。

理想低通的 $h[n]=\sin(\Omega_cn)/(\pi n)$ 属于第二类：平方可和但不绝对可和，所以它的 DTFT 只在均方意义下等于矩形，在跳变处有过冲。

综合式那边则完全没有问题 —— 有限区间上的积分。

---

## 6. 性质

与 CTFT 基本一一对应，但每条都要加上「模 $2\pi$」的意识：

| 性质 | 时域 | 频域 |
| ---- | ---- | ---- |
| 线性 | $ax_1+bx_2$ | $aX_1+bX_2$ |
| 时移 | $x[n-n_0]$ | $e^{-j\Omega n_0}X$ |
| 频移 | $e^{j\Omega_0n}x[n]$ | $X(e^{j(\Omega-\Omega_0)})$ |
| **卷积** | $x*h$ | $XH$ |
| 相乘 | $x_1x_2$ | $\frac{1}{2\pi}X_1\circledast X_2$（**周期**卷积） |
| 差分 | $x[n]-x[n-1]$ | $(1-e^{-j\Omega})X$ |
| 累加 | $\sum_{m\le n}x[m]$ | $\frac{X}{1-e^{-j\Omega}}+\pi X(e^{j0})\sum_k\delta(\Omega-2\pi k)$ |
| 帕塞瓦尔 | $\sum\lvert x[n]\rvert^2$ | $\frac{1}{2\pi}\int_{2\pi}\lvert X\rvert^2d\Omega$ |

**没有尺度变换性质** —— 因为 $x[an]$ 对非整数 $a$ 无定义。相应的角色由抽取和内插承担，见 [[Discrete-Time Sampling]]。

---

## 7. 四种傅里叶表示的全景

到此四种都齐了，规律非常整齐：

| | 时域 | 频域 |
| ---- | ---- | ---- |
| CTFS | 连续、**周期** | **离散**、非周期 |
| CTFT | 连续、非周期 | 连续、非周期 |
| DTFS | **离散**、**周期** | **离散**、**周期** |
| DTFT | **离散**、非周期 | 连续、**周期** |

一句话记：**一个域离散 $\Leftrightarrow$ 另一个域周期。** 采样定理、频谱周期复制、循环卷积这些结论，全都是这条对偶律的不同侧面。

---

## 参见

- [[Signals and Systems MOC]]
- [[Discrete-Time Fourier Series]]（$N$ 有限的情形）
- [[Continuous-Time Fourier Transform]]（对照的连续版本）
- [[Filtering]]（DT 理想滤波器）
- [[Sampling]]（$2\pi$ 周期性与采样定理的联系）
- [[The z-Transform]]（把单位圆推广到整个 $z$ 平面）
- [OCW Lecture 11 notes (PDF)](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec11/)
