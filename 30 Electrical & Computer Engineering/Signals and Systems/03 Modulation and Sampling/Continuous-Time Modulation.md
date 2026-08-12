---
title: "Continuous-Time Modulation"
aliases:
  - "连续时间调制"
  - "幅度调制"
  - "AM"
  - "同步解调"
  - "频分复用"
tags: [signals_and_systems, ee, modulation]
up: "[[Signals and Systems MOC]]"
related:
  - "[[Fourier Transform Properties]]"
  - "[[Discrete-Time Modulation]]"
  - "[[Sampling]]"
  - "[[Filtering]]"
---
# Continuous-Time Modulation

> [!summary] 核心结论
> 调制就是 [[Fourier Transform Properties#6. 调制（相乘）性质|相乘性质]] 的兑现：时域乘载波 $\Leftrightarrow$ 频域把基带谱**搬移**到 $\pm\omega_c$。
> 用途有二：把信号搬到适合传播 / 天线尺寸的频段，以及**频分复用**（把多路信号搬到互不重叠的频段共用一条信道）。
> 同步解调需要**同频同相**的本地载波 —— 相差 $\theta$ 时输出乘 $\cos\theta$，$\theta=\pi/2$ 完全收不到。这就是载波恢复（锁相环）存在的理由。

依据：奥本海姆 MIT OCW RES.6-007 [Lecture 13](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-13-continuous-time-modulation/)、[Lecture 14](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-14-demonstration-of-amplitude-modulation/)；教材 §8.1–8.4。

前置：[[Fourier Transform Properties]]、[[Filtering]]。

---

## 1. 为什么要调制

三个都很实在的理由：

1. **天线尺寸**。有效辐射要求天线尺度可比波长。语音信号 $3\,\mathrm{kHz}$ 对应波长 $100\,\mathrm{km}$ —— 搬到 $1\,\mathrm{MHz}$ 后波长 $300\,\mathrm{m}$，才有可能造出来。
2. **频分复用**。一条信道上同时传多路信号，各自搬到不同频段互不干扰。
3. **信道特性**。某些频段传播损耗低、噪声小，把信号搬过去更划算。

---

## 2. 正弦幅度调制

![[ss-continuous-time-modulation-01.svg]]

$$
y(t)=x(t)\cos(\omega_ct)
$$

载波的频谱是两根冲激：

$$
\cos\omega_ct\;\longleftrightarrow\;\pi\big[\delta(\omega-\omega_c)+\delta(\omega+\omega_c)\big]
$$

由相乘性质，

$$
Y(j\omega)=\frac{1}{2}X\big(j(\omega-\omega_c)\big)+\frac{1}{2}X\big(j(\omega+\omega_c)\big)
$$

**频谱被完整搬到 $\pm\omega_c$，幅度减半。** 要求两份副本不重叠：

$$
\omega_c>\omega_M
$$

调制后的带宽是基带的两倍（上下边带各占 $\omega_M$）—— 这是**双边带抑制载波（DSB-SC）**。单边带（SSB）用滤波器砍掉一个边带，带宽减半，代价是解调更麻烦。

---

## 3. 同步解调

同一张图的下半部分。再乘一次同样的载波：

$$
w(t)=y(t)\cos\omega_ct=x(t)\cos^2\omega_ct=\frac{1}{2}x(t)+\frac{1}{2}x(t)\cos(2\omega_ct)
$$

频域上：一份回到基带，两份搬到 $\pm2\omega_c$。低通滤掉后者即得 $\frac12x(t)$。

低通截止频率的取值范围：

$$
\omega_M<\omega_{co}<2\omega_c-\omega_M
$$

> [!warning] 相位失配是致命的
> 若本地载波是 $\cos(\omega_ct+\theta)$：
> $$y(t)\cos(\omega_ct+\theta)=\frac{1}{2}x(t)\cos\theta+\text{（$2\omega_c$ 处的项）}$$
> 输出被 $\cos\theta$ 缩放。$\theta=\pi/2$ 时**完全没有输出**。
>
> 频率失配 $\Delta\omega$ 更糟：输出乘上 $\cos(\Delta\omega\,t)$，信号周期性地淡入淡出（beating）。
>
> 所以 DSB-SC 接收机必须做载波恢复 —— 锁相环、Costas 环都是为这件事发明的。

---

## 4. 带载波的 AM：用包络检波换掉同步

在基带上加一个直流偏置再调制：

$$
y(t)=\big[A+x(t)\big]\cos\omega_ct
$$

若 $A>\max|x(t)|$，则 $[A+x(t)]$ 恒为正，**信号的包络就是 $A+x(t)$** —— 用一个二极管加 RC 就能检出来，不需要任何载波恢复。

这就是广播 AM 用了一百年的方案：**用发射功率换接收机成本**。代价是那根载波分量本身不携带信息却占了大部分功率（调制度 100% 时也只有 1/3 的功率在边带里）。

调制度 $m=\max|x|/A$。$m>1$ 时包络出现过零，检波失真（过调制）。

---

## 5. 频分复用

各路信号搬到不同的 $\omega_{c1},\omega_{c2},\dots$，只要间隔大于各自带宽就互不重叠：

$$
y(t)=\sum_i x_i(t)\cos(\omega_{ci}t)
$$

接收端用带通选出想要的那一路，再同步解调。广播电台、有线电视、早期电话干线全靠这个。

（对偶的方案是**时分复用** TDM —— 各路信号轮流占用整个频段。两者是采样定理和调制定理的一对镜像。）

---

## 6. 其他调制方式

| 方式 | 载波的什么被调制 | 特点 |
| ---- | ---- | ---- |
| AM / DSB-SC | 幅度 | 线性，分析简单，抗噪差 |
| SSB | 幅度（单边带） | 带宽减半，滤波器难做 |
| FM | 频率 | **非线性**，抗噪好，带宽大（卡森公式） |
| PM | 相位 | 与 FM 密切相关 |
| 脉冲幅度调制 PAM | 脉冲串的幅度 | 直通 [[Sampling]] |

本课只严格处理线性（幅度类）调制 —— FM 是非线性的，傅里叶方法不能直接套用。

---

## 7. 速查

| 项目 | 内容 |
| ---- | ---- |
| 调制 | $y=x\cos\omega_ct$ $\Rightarrow$ 谱搬到 $\pm\omega_c$，幅度减半 |
| 无重叠条件 | $\omega_c>\omega_M$ |
| 传输带宽 | DSB $2\omega_M$；SSB $\omega_M$ |
| 同步解调 | 再乘载波 + 低通（$\omega_M<\omega_{co}<2\omega_c-\omega_M$） |
| 相位误差 $\theta$ | 输出乘 $\cos\theta$；$\theta=\pi/2$ 为零 |
| 带载波 AM | $A>\max\lvert x\rvert$ $\Rightarrow$ 可包络检波 |

---

## 参见

- [[Signals and Systems MOC]]
- [[Fourier Transform Properties]]（相乘性质）
- [[Discrete-Time Modulation]]（离散时间的同一件事）
- [[Sampling]]（用冲激串做「载波」的调制）
- [[Filtering]]（解调端的低通）
- [OCW Lecture 13 notes (PDF)](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec13/)
