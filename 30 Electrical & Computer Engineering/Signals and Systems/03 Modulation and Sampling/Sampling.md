---
title: "Sampling"
aliases:
  - "采样"
  - "采样定理"
  - "奈奎斯特"
  - "混叠"
  - "Nyquist"
tags: [signals_and_systems, ee, sampling]
up: "[[Signals and Systems MOC]]"
related:
  - "[[Continuous-Time Modulation]]"
  - "[[Interpolation]]"
  - "[[Discrete-Time Processing of Continuous-Time Signals]]"
  - "[[Fourier Transform Properties]]"
---
# Sampling

> [!summary] 核心结论
> 用冲激串采样 = 用冲激串做「载波」的调制，所以频域上得到**原频谱的周期复制**，间隔 $\omega_s=2\pi/T$。
> **采样定理**：若 $x(t)$ 带限于 $\omega_M$ 且 $\omega_s>2\omega_M$，则副本不重叠，用理想低通可以**完整恢复**原信号 —— 离散的样点里没有丢失任何信息。
> 若 $\omega_s<2\omega_M$，副本重叠即**混叠**，高频被折叠成低频，此后任何处理都救不回来。防混叠只能在**采样之前**用模拟低通做。

依据：奥本海姆 MIT OCW RES.6-007 [Lecture 16](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-16-sampling/)；教材 §7.1。

前置：[[Continuous-Time Modulation]]、[[Fourier Transform Properties]]。

---

## 1. 冲激串采样

采样可以建模成乘一个冲激串：

$$
p(t)=\sum_{n=-\infty}^{\infty}\delta(t-nT),
\qquad
x_p(t)=x(t)p(t)=\sum_n x(nT)\,\delta(t-nT)
$$

冲激串的 CTFT 还是冲激串（这是它最漂亮的性质）：

$$
P(j\omega)=\frac{2\pi}{T}\sum_{k}\delta(\omega-k\omega_s),
\qquad \omega_s=\frac{2\pi}{T}
$$

由 [[Fourier Transform Properties#6. 调制（相乘）性质|相乘性质]]，

$$
\boxed{\;X_p(j\omega)=\frac{1}{T}\sum_{k=-\infty}^{\infty}X\big(j(\omega-k\omega_s)\big)\;}
$$

**采样在频域造成周期复制。** 这是本讲唯一需要记的式子，其余全是它的推论。

> [!note] 又一次是「一域离散 ⇒ 另一域周期」
> 时域采样（变离散）$\Rightarrow$ 频域周期。这与 [[Discrete-Time Fourier Transform#7. 四种傅里叶表示的全景|四种傅里叶表示]] 里的对偶律是同一条规律。

---

## 2. 采样定理

![[ss-sampling-01.svg]]

副本中心相距 $\omega_s$，每份宽 $2\omega_M$。不重叠的条件：

$$
\boxed{\;\omega_s>2\omega_M\;}
$$

$2\omega_M$ 称为**奈奎斯特率**（Nyquist rate），$\omega_s/2$ 称为**奈奎斯特频率**（折叠频率）。

满足条件时，用截止在 $\omega_M$ 与 $\omega_s-\omega_M$ 之间的理想低通（增益 $T$）就能取出中央那一份，完整恢复 $x(t)$。

> [!important] 这个结论有多强
> 一个连续信号有不可数无穷多个值，采样后只剩可数无穷多个数 —— 竟然没有信息损失。
> 前提是「带限」这个极强的假设：它让信号的自由度实际上是可数的。
> 严格说带限信号必然是时间无限长的（时限与带限不能兼得），所以现实中永远是近似。工程做法：用足够高的采样率 + 采样前的抗混叠滤波，把误差压到可接受。

---

## 3. 混叠

$\omega_s<2\omega_M$ 时副本重叠。重叠区域的频谱是几份的**和**，无法分离。后果：

- 高于 $\omega_s/2$ 的成分被「折叠」到 $\omega_s-\omega$ 处，冒充低频。
- 这是**不可逆**的信息破坏。事后再滤波、再插值，都恢复不了。

经典可视例子：车轮在电影里倒转（帧率 24 Hz 对轮辐旋转频率欠采样）；条纹衬衫在视频里出现彩色摩尔纹。

> [!warning] 抗混叠滤波必须在采样之前
> 这是初学者最容易搞错的一点。ADC 之后再怎么数字滤波都没用 —— 混叠发生在采样那一刻，之后低频里已经掺进了原本的高频，两者不可分。
> 所以每个正经的 ADC 前面都有一级模拟低通（anti-aliasing filter）。

**过采样**（$\omega_s\gg2\omega_M$）的好处正在于此：采样率越高，抗混叠滤波器的过渡带可以越宽，模拟滤波器就越容易做。这是 $\Sigma\Delta$ ADC 的核心思路之一。

---

## 4. 零阶保持采样

实际的采样保持电路不是理想冲激串，而是**保持**一段时间：

$$
x_0(t)=x(nT),\quad nT\le t<(n+1)T
$$

等价于「冲激串采样 + 与宽度 $T$ 的矩形卷积」，于是

$$
X_0(j\omega)=X_p(j\omega)\cdot H_0(j\omega),
\qquad
H_0(j\omega)=T\,e^{-j\omega T/2}\frac{\sin(\omega T/2)}{\omega T/2}
$$

多出来一个 sinc 包络：通带内**下垂**（$\omega_s/2$ 处约 $-3.9\,\mathrm{dB}$），带外副本没被完全压掉。补偿方法见 [[Interpolation]]。

---

## 5. 欠采样也可以是有意的

带通信号（能量集中在 $\omega_1<|\omega|<\omega_2$）不必按最高频率采样。只要副本落在空隙里不相撞，采样率可以低到接近 $2(\omega_2-\omega_1)$，即两倍**带宽**而非两倍最高频率。

这叫**带通采样 / 欠采样**（bandpass sampling），软件无线电里靠它直接用 ADC 完成下变频。代价是对采样时钟抖动和模拟前端带宽的要求高得多。

---

## 6. 速查

| 项目 | 内容 |
| ---- | ---- |
| 采样模型 | $x_p=x\cdot\sum\delta(t-nT)$ |
| 频域 | $X_p(j\omega)=\frac{1}{T}\sum_kX(j(\omega-k\omega_s))$ |
| $\omega_s$ | $2\pi/T$ |
| 采样定理 | $\omega_s>2\omega_M$ |
| 奈奎斯特率 | $2\omega_M$ |
| 恢复 | 理想低通，增益 $T$，截止在 $(\omega_M,\ \omega_s-\omega_M)$ |
| 混叠 | $\omega_s<2\omega_M$，不可逆 |
| 防混叠 | **采样前**的模拟低通 |
| ZOH | 多一个 sinc 包络，通带下垂 |

---

## 参见

- [[Signals and Systems MOC]]
- [[Continuous-Time Modulation]]（采样就是用冲激串做载波）
- [[Interpolation]]（怎么从样点重建）
- [[Discrete-Time Processing of Continuous-Time Signals]]（采样定理的工程兑现）
- [[Discrete-Time Sampling]]（离散域里的同一件事）
- [OCW Lecture 16 notes (PDF)](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec16/)
