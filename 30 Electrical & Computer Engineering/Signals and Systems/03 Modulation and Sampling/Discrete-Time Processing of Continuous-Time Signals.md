---
title: "Discrete-Time Processing of Continuous-Time Signals"
aliases:
  - "用离散系统处理连续信号"
  - "C/D 与 D/C"
  - "数字信号处理链路"
  - "等效连续系统"
tags: [signals_and_systems, ee, sampling, dsp]
up: "[[Signals and Systems MOC]]"
related:
  - "[[Sampling]]"
  - "[[Interpolation]]"
  - "[[Discrete-Time Fourier Transform]]"
  - "[[Filtering]]"
---
# Discrete-Time Processing of Continuous-Time Signals

> [!summary] 核心结论
> 「C/D $\to$ 离散系统 $H(e^{j\Omega})$ $\to$ D/C」这条链路，在输入带限且无混叠的前提下，**整体等效于一个连续时间 LTI 系统**：
> $$H_c(j\omega)=\begin{cases}H(e^{j\omega T}),&|\omega|<\pi/T\\0,&\text{否则}\end{cases}$$
> 数字频率 $\Omega=\omega T$ 是**归一化**的 —— 同一套滤波器系数换个采样率就换了截止频率。这既是 DSP 可复用的根源，也是「数字滤波器的截止频率总用 $\pi$ 的分数表示」的原因。

依据：奥本海姆 MIT OCW RES.6-007 [Lecture 18](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-18-discrete-time-processing-of-continuous-time-signals/)；教材 §7.4。

前置：[[Sampling]]、[[Interpolation]]、[[Discrete-Time Fourier Transform]]。

---

## 1. 链路

![[ss-discrete-time-processing-of-continuous-time-signals-01.svg]]

三个环节：

1. **C/D（连续转离散）**：$x[n]=x_c(nT)$。频域上 $X(e^{j\Omega})=\frac{1}{T}\sum_kX_c\big(j(\tfrac{\Omega-2\pi k}{T})\big)$ —— 把 $\omega$ 轴按 $\Omega=\omega T$ 归一化，再周期化。
2. **离散 LTI 系统**：$Y(e^{j\Omega})=H(e^{j\Omega})X(e^{j\Omega})$。
3. **D/C（离散转连续）**：理想带限内插，截止 $\pi/T$。

---

## 2. 等效连续系统

若 $x_c$ 带限于 $\pi/T$（即满足采样定理，无混叠），三步串起来的净效果是：

$$
\boxed{\;H_c(j\omega)=\begin{cases}H(e^{j\omega T}),&|\omega|<\pi/T\\[2pt]0,&\text{否则}\end{cases}\;}
$$

**整条链路对外表现为一个普通的连续时间 LTI 系统。** 这条结论是全部数字信号处理的许可证 —— 它保证了「用软件做滤波器」和「用电阻电容做滤波器」在数学上是等价的。

> [!warning] 「无混叠」这个前提不能省
> 一旦 C/D 处发生混叠，整条链路就**不再是 LTI 的**（甚至不是时不变的）。上面的等效关系直接失效。
> 这就是为什么每个 ADC 前面都必须有抗混叠滤波器 —— 它不只是为了保真度，更是为了让后面的全部理论成立。

---

## 3. 频率归一化

$$
\Omega=\omega T=\frac{2\pi\omega}{\omega_s}
$$

对应关系：

| 连续频率 $\omega$ | 数字频率 $\Omega$ |
| ---- | ---- |
| $0$ | $0$ |
| $\omega_s/4$ | $\pi/2$ |
| $\omega_s/2$（奈奎斯特） | $\pi$ |
| $\omega_s$ | $2\pi$ |

$\Omega$ 无量纲（弧度/样本）。一个设计好的数字低通「截止在 $0.2\pi$」，在 $f_s=48\,\mathrm{kHz}$ 时是 $4.8\,\mathrm{kHz}$，在 $f_s=8\,\mathrm{kHz}$ 时就变成 $800\,\mathrm{Hz}$ —— **同一套系数，换采样率就换了实际频率**。

这正是数字滤波器可以做成标准库的原因，也是设计时必须始终清楚「当前采样率是多少」的原因。

---

## 4. 一个完整例子：数字微分器

想要连续时间微分器 $H_c(j\omega)=j\omega$（在 $|\omega|<\pi/T$ 内）。代入等效关系：

$$
H(e^{j\Omega})=j\frac{\Omega}{T},\qquad |\Omega|<\pi
$$

对应的冲激响应（做逆 DTFT）：

$$
h[n]=\frac{\cos(\pi n)}{nT}-\frac{\sin(\pi n)}{\pi n^2T}
=\frac{(-1)^n}{nT}\ (n\neq0),\qquad h[0]=0
$$

双边无限长、非因果 —— 与理想低通同样的毛病，实用时要截断加窗并接受一个群延迟。

反过来，最简单的实用近似是一阶差分 $y[n]=(x[n]-x[n-1])/T$，其 $H(e^{j\Omega})=(1-e^{-j\Omega})/T$，在低频处 $\approx j\Omega/T$ —— 只在 $\Omega\ll\pi$ 时才像微分器。

---

## 5. 为什么要绕这一圈

明明可以直接用模拟电路，为什么要 ADC $\to$ 算 $\to$ DAC？

| 优势 | 说明 |
| ---- | ---- |
| **精度可控** | 位宽决定精度，不受元件容差、温漂、老化影响 |
| **可编程** | 换系数就换特性，不用改硬件 |
| **可做模拟做不到的事** | 严格线性相位、自适应滤波、极窄带 |
| **可存储、可重复** | 同样输入永远同样输出 |

代价：延迟（抗混叠 + 重建滤波器 + 算法本身）、功耗、以及必须处理量化噪声。

---

## 6. 速查

| 项目 | 内容 |
| ---- | ---- |
| C/D | $x[n]=x_c(nT)$ |
| 归一化 | $\Omega=\omega T$ |
| 等效系统 | $H_c(j\omega)=H(e^{j\omega T})$ 对 $\lvert\omega\rvert<\pi/T$，否则 0 |
| 成立前提 | $x_c$ 带限于 $\pi/T$（无混叠） |
| 奈奎斯特 | $\omega=\omega_s/2\ \leftrightarrow\ \Omega=\pi$ |
| 混叠的后果 | 整条链路不再是 LTI |

---

## 参见

- [[Signals and Systems MOC]]
- [[Sampling]]（C/D 的理论）
- [[Interpolation]]（D/C 的理论）
- [[Discrete-Time Fourier Transform]]（$\Omega$ 的 $2\pi$ 周期性）
- [[Mapping Continuous-Time Filters to Discrete-Time Filters]]（怎么设计那个 $H(e^{j\Omega})$）
- [OCW Lecture 18 notes (PDF)](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec18/)
