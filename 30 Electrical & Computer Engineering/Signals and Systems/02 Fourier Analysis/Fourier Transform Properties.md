---
title: "Fourier Transform Properties"
aliases:
  - "傅里叶变换性质"
  - "卷积性质"
  - "调制性质"
  - "帕塞瓦尔定理"
  - "对偶性"
tags: [signals_and_systems, ee, fourier]
up: "[[Signals and Systems MOC]]"
related:
  - "[[Continuous-Time Fourier Transform]]"
  - "[[Convolution]]"
  - "[[Filtering]]"
  - "[[Continuous-Time Modulation]]"
---
# Fourier Transform Properties

> [!summary] 核心结论
> 性质表不是用来背的，而是用来**避免做积分**的。三条最有分量：
> **卷积性质** $y=x*h\Leftrightarrow Y=XH$（滤波的全部理论基础）、**调制性质** $x(t)c(t)\Leftrightarrow\frac{1}{2\pi}X*C$（通信的全部理论基础）、**帕塞瓦尔** $\int|x|^2dt=\frac{1}{2\pi}\int|X|^2d\omega$（能量在两域相等）。
> 还有一条统摄性的：时域与频域**互为倒数** —— 一边窄另一边必宽。

依据：奥本海姆 MIT OCW RES.6-007 [Lecture 9](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-9-fourier-transform-properties/)；教材 §4.3–4.7。

前置：[[Continuous-Time Fourier Transform]]。

---

## 1. 线性与对称性

**线性**：$ax_1+bx_2\;\longleftrightarrow\;aX_1+bX_2$。

**实信号的共轭对称**：$x(t)$ 实 $\Rightarrow$ $X(-j\omega)=X^*(j\omega)$。展开来：

| $x(t)$ | $X(j\omega)$ |
| ---- | ---- |
| 实 | 幅度偶、相位奇 |
| 实且偶 | 实且偶 |
| 实且奇 | 纯虚且奇 |

实用后果：实信号的频谱只需画 $\omega\ge0$ 那一半，另一半由对称性给出。这就是为什么所有频谱图都是左右对称的。

---

## 2. 时移与频移

![[ss-fourier-transform-properties-01.svg]]

$$
x(t-t_0)\;\longleftrightarrow\;e^{-j\omega t_0}X(j\omega)
$$

$$
e^{j\omega_0t}x(t)\;\longleftrightarrow\;X(j(\omega-\omega_0))
$$

时移**只改变相位，幅度谱纹丝不动**，且加上去的相位是 $\omega$ 的线性函数，斜率 $=-t_0$。

> [!important] 线性相位 = 无失真延迟
> 若 $H(j\omega)=e^{-j\omega t_0}$（幅度恒为 1、相位线性），则 $y(t)=x(t-t_0)$ —— 波形完全不变，只是晚到了。
> 反过来，相位**非**线性意味着不同频率分量的延迟不同，波形会散开。这就是滤波器设计里为什么有人宁可牺牲幅度陡峭度去换线性相位（FIR 对称滤波器）。

频移就是**调制**：乘一个复指数把频谱整体搬走。详见 [[Continuous-Time Modulation]]。

---

## 3. 尺度变换：时宽与带宽的倒数关系

$$
x(at)\;\longleftrightarrow\;\frac{1}{|a|}X\!\left(\frac{j\omega}{a}\right)
$$

同一张图的上半部分。**时域压缩 $\Rightarrow$ 频域展宽**，反之亦然。

这不是巧合，而是一条不可逾越的约束。定义有效时宽 $\Delta t$ 与有效带宽 $\Delta\omega$（用二阶矩），可以证明

$$
\Delta t\cdot\Delta\omega\ \ge\ \frac{1}{2}
$$

等号在高斯脉冲处取到 —— 高斯是唯一的「自傅里叶」形状。

工程含义：想要短脉冲就必须占宽频带（雷达、UWB）；想要窄带就必须容忍长持续时间（窄带滤波器建立慢）。量子力学里同一条不等式叫不确定性原理。

---

## 4. 微分与积分

$$
\frac{dx}{dt}\;\longleftrightarrow\;j\omega X(j\omega),
\qquad
\int_{-\infty}^{t}x(\tau)d\tau\;\longleftrightarrow\;\frac{X(j\omega)}{j\omega}+\pi X(0)\delta(\omega)
$$

微分在频域是乘 $j\omega$ —— 高频被放大（噪声放大器）；积分是除以 $j\omega$ —— 高频被压制（天然低通）。积分那一项额外的冲激来自直流分量。

**这条性质是把微分方程变成代数方程的关键**，也是 [[The Laplace Transform|拉普拉斯变换]] 的直接前身。

---

## 5. 卷积性质

$$
\boxed{\;y(t)=x(t)*h(t)\;\longleftrightarrow\;Y(j\omega)=X(j\omega)H(j\omega)\;}
$$

时域里麻烦的翻转-平移-积分，在频域退化成一次**逐点乘法**。

这条性质的分量再怎么强调都不过分：

- 它是「频率响应」这个概念存在的理由。
- 它把「设计系统」变成「设计一条曲线 $H(j\omega)$」，即滤波器设计（见 [[Filtering]]）。
- 级联系统的总响应是各级 $H$ 相乘，一眼可见。

其根源在 [[Sinusoidal and Exponential Signals|复指数是 LTI 系统的特征函数]]：$e^{j\omega t}$ 进去，出来还是 $H(j\omega)e^{j\omega t}$，只是被缩放了。

---

## 6. 调制（相乘）性质

$$
x(t)\,c(t)\;\longleftrightarrow\;\frac{1}{2\pi}\,X(j\omega)*C(j\omega)
$$

与卷积性质**对偶**：时域相乘 $\leftrightarrow$ 频域卷积。

当 $c(t)=\cos\omega_ct$（频谱是 $\pm\omega_c$ 处的两根冲激）时，卷积就是把 $X$ 复制搬移到 $\pm\omega_c$ —— 这就是幅度调制。整个 [[Continuous-Time Modulation]] 和 [[Sampling]] 都是这条性质的应用。

---

## 7. 对偶性

CTFT 的分析式与综合式除了一个 $2\pi$ 和符号外形式相同，于是

$$
x(t)\longleftrightarrow X(j\omega)
\quad\Longrightarrow\quad
X(t)\longleftrightarrow 2\pi\,x(-\omega)
$$

一对变换对能白送另一对。例如：

| 已知 | 对偶给出 |
| ---- | ---- |
| 矩形脉冲 $\leftrightarrow$ sinc | sinc $\leftrightarrow$ 矩形（理想低通） |
| $\delta(t)\leftrightarrow 1$ | $1\leftrightarrow 2\pi\delta(\omega)$ |
| 时域卷积 $\leftrightarrow$ 频域相乘 | 时域相乘 $\leftrightarrow$ 频域卷积 |

对偶性也解释了为什么性质表总是成对出现。

---

## 8. 帕塞瓦尔定理

$$
\int_{-\infty}^{\infty}|x(t)|^2dt=\frac{1}{2\pi}\int_{-\infty}^{\infty}|X(j\omega)|^2d\omega
$$

**能量在两域相等**，傅里叶变换是（差一个 $2\pi$ 的）保范映射。$|X(j\omega)|^2$ 称为能量谱密度，描述能量在频率上怎么分布。

用途：算能量时可以挑好算的那一域；也是信噪比、滤波器噪声带宽等概念的基础。

---

## 9. 速查表

| 性质 | 时域 | 频域 |
| ---- | ---- | ---- |
| 线性 | $ax_1+bx_2$ | $aX_1+bX_2$ |
| 时移 | $x(t-t_0)$ | $e^{-j\omega t_0}X$ |
| 频移 | $e^{j\omega_0t}x(t)$ | $X(j(\omega-\omega_0))$ |
| 尺度 | $x(at)$ | $\frac{1}{\lvert a\rvert}X(j\omega/a)$ |
| 共轭 | $x^*(t)$ | $X^*(-j\omega)$ |
| 微分 | $dx/dt$ | $j\omega X$ |
| 积分 | $\int_{-\infty}^t x$ | $X/(j\omega)+\pi X(0)\delta(\omega)$ |
| **卷积** | $x*h$ | $XH$ |
| **相乘** | $xc$ | $\frac{1}{2\pi}X*C$ |
| 对偶 | $X(t)$ | $2\pi x(-\omega)$ |
| 帕塞瓦尔 | $\int\lvert x\rvert^2dt$ | $\frac{1}{2\pi}\int\lvert X\rvert^2d\omega$ |

---

## 参见

- [[Signals and Systems MOC]]
- [[Continuous-Time Fourier Transform]]
- [[Convolution]]（卷积性质的时域一侧）
- [[Filtering]]（卷积性质的直接应用）
- [[Continuous-Time Modulation]]、[[Sampling]]（相乘性质的直接应用）
- [OCW Lecture 9 notes (PDF)](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec09/)
