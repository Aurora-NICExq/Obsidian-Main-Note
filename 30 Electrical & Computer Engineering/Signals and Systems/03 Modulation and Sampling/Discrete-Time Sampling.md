---
title: "Discrete-Time Sampling"
aliases:
  - "离散时间采样"
  - "抽取"
  - "decimation"
  - "多速率"
  - "采样率转换"
tags: [signals_and_systems, ee, sampling, dsp]
up: "[[Signals and Systems MOC]]"
related:
  - "[[Sampling]]"
  - "[[Interpolation]]"
  - "[[Discrete-Time Fourier Transform]]"
  - "[[Discrete-Time Modulation]]"
---
# Discrete-Time Sampling

> [!summary] 核心结论
> 离散域里的抽取（$\downarrow M$，每 $M$ 个样点留一个）与连续域的采样是同一件事：**降采样率 $\Rightarrow$ 频谱副本靠拢 $\Rightarrow$ 不够带限就混叠**。
> 频域上抽取把频率轴**展宽 $M$ 倍**、幅度除以 $M$；无混叠条件 $M\Omega_M<\pi$。
> 所以抽取器前面**必须**先接一个截止在 $\pi/M$ 的抗混叠低通。反向的内插（$\uparrow L$ 后低通）把频率轴**压窄 $L$ 倍**。两者级联即得有理倍率 $L/M$ 的采样率转换。

依据：奥本海姆 MIT OCW RES.6-007 [Lecture 19](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-19-discrete-time-sampling/)；教材 §7.5。

前置：[[Sampling]]、[[Discrete-Time Fourier Transform]]。

---

## 1. 抽取（decimation）

$$
x_d[n]=x[nM]
$$

只保留下标是 $M$ 倍数的样点。频域上：

$$
X_d(e^{j\Omega})=\frac{1}{M}\sum_{k=0}^{M-1}X\big(e^{j(\Omega-2\pi k)/M}\big)
$$

![[ss-discrete-time-sampling-01.svg]]

拆开看是两步：

1. **展宽**：$\Omega\to\Omega/M$，即频率轴被拉伸 $M$ 倍。原来在 $\Omega_M$ 的边缘跑到了 $M\Omega_M$。
2. **叠加 $M$ 份副本**（$k=0,\dots,M-1$）并除以 $M$。

无混叠条件：

$$
\boxed{\;M\,\Omega_M<\pi\;}
$$

即原序列必须带限于 $\pi/M$。

> [!important] 与连续时间采样是同一条定理
> 连续：$\omega_s>2\omega_M$。离散：$\Omega_M<\pi/M$。
> 两者说的都是「采样率至少要是信号带宽的两倍」，只是一个用绝对频率、一个用归一化频率表述。

---

## 2. 抽取前必须低通

同一张图的下半部分。标准抽取器是两级：

$$
x[n]\;\longrightarrow\;\boxed{\text{低通 }\Omega_{co}=\pi/M}\;\longrightarrow\;\boxed{\downarrow M}\;\longrightarrow\;x_d[n]
$$

低通把带宽先压到 $\pi/M$ 以内，抽取时展宽 $M$ 倍后正好占满 $\pi$，不重叠。

**顺序不能颠倒** —— 与连续时间「抗混叠滤波必须在 ADC 之前」是同一个道理。

代价：真实带宽超过 $\pi/M$ 的成分被主动丢掉了。这是降采样率的必然代价，不是缺陷。

---

## 3. 内插（$\uparrow L$）

反方向的操作，两步：

1. **零值填充**：每两个样点之间插 $L-1$ 个零。
   $$x_e[n]=\begin{cases}x[n/L],&n\ \text{是}\ L\ \text{的倍数}\\0,&\text{否则}\end{cases}$$
   频域上 $X_e(e^{j\Omega})=X(e^{j\Omega L})$ —— 频率轴**压窄 $L$ 倍**，于是一个 $2\pi$ 周期内出现了 $L$ 份镜像。
2. **低通**：截止 $\pi/L$、增益 $L$，滤掉多余的 $L-1$ 份镜像，只留基带那份。

低通之后那些零被「填」成了插值出来的样点 —— 这就是数字内插器。

> [!note] 为什么插零而不是重复
> 插零使频域只是压缩（不引入额外失真），镜像是干净可分的，一个理想低通就能处理。
> 直接重复样点等价于「插零 + ZOH 滤波」，通带会下垂 —— 与 [[Interpolation#3. 零阶保持|ZOH]] 是同一个毛病。

---

## 4. 有理倍率转换

要把采样率变成 $L/M$ 倍，把两者级联：

$$
x[n]\;\to\;\boxed{\uparrow L}\;\to\;\boxed{\text{低通 }\Omega_{co}=\min(\pi/L,\ \pi/M)}\;\to\;\boxed{\downarrow M}\;\to\;y[n]
$$

**先内插后抽取**，顺序不能反（先抽取会先丢掉信息）。中间两个低通可以合并成一个，截止取两者中较小的那个。

例：$44.1\,\mathrm{kHz}$（CD）转 $48\,\mathrm{kHz}$（专业音频）需要 $L/M=160/147$。级数很大，实际用多级分解或多相（polyphase）结构实现。

---

## 5. 多相实现：省掉白算的部分

朴素实现里有大量浪费：

- 抽取：低通算出 $M$ 个样点，只用 1 个 —— **$(M-1)/M$ 的运算被扔掉**。
- 内插：滤波器的输入有 $(L-1)/L$ 是零 —— **乘零白算**。

**多相分解**把滤波器系数按相位拆成 $M$（或 $L$）组，只算真正用得上的那些，运算量直接降到 $1/M$（或 $1/L$）。这是多速率信号处理里最重要的工程技巧。

---

## 6. 用途

| 场景 | 做法 |
| ---- | ---- |
| $\Sigma\Delta$ ADC | 极高速率 1-bit 采样 $\to$ 数字低通 $\to$ 大比例抽取 |
| 软件无线电 | 复调制搬到基带 + 低通 + 抽取（数字下变频 DDC） |
| 音频重采样 | $L/M$ 有理倍率转换 |
| 过采样 DAC | $\uparrow L$ 把镜像推远，模拟重建滤波器可以做得很缓 |

---

## 7. 速查

| 操作 | 时域 | 频域 |
| ---- | ---- | ---- |
| 抽取 $\downarrow M$ | $x[nM]$ | 展宽 $M$ 倍，幅度 $/M$，叠加 $M$ 份 |
| 无混叠条件 | — | $M\Omega_M<\pi$ |
| 零值填充 $\uparrow L$ | 插 $L-1$ 个零 | 压窄 $L$ 倍，出现 $L$ 份镜像 |
| 内插低通 | — | 截止 $\pi/L$，增益 $L$ |
| $L/M$ 转换 | 先 $\uparrow L$ 后 $\downarrow M$ | 中间一个低通，截止取 $\min(\pi/L,\pi/M)$ |

---

## 参见

- [[Signals and Systems MOC]]
- [[Sampling]]（连续时间的同一条定理）
- [[Interpolation]]（重建与内插核）
- [[Discrete-Time Fourier Transform]]（频率轴的 $2\pi$ 周期性）
- [[Discrete-Time Modulation]]（平移，与这里的伸缩配对）
- [OCW Lecture 19 notes (PDF)](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec19/)
