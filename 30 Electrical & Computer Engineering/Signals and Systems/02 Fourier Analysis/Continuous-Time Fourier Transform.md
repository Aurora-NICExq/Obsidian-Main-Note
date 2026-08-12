---
title: "Continuous-Time Fourier Transform"
aliases:
  - "连续时间傅里叶采样"
  - "连续时间傅里叶变换"
  - "CTFT"
  - "Fourier Transform"
  - "包络采样"
tags: [signals_and_systems, ee, fourier]
up: "[[Signals and Systems MOC]]"
related:
  - "[[Continuous-Time Fourier Series]]"
  - "[[Sinusoidal and Exponential Signals]]"
  - "[[Convolution]]"
  - "[[Analog and Digital Signal Processing]]"
---
# Continuous-Time Fourier Transform

> [!summary] 核心结论
> 非周期信号的 CTFT 由 CTFS 极限得到：先把有限片段周期延拓，再令 $T_0\to\infty$。一个周期对应的 $X(j\omega)$ 是**包络**；级数系数是包络上间距 $\omega_0=2\pi/T_0$ 的样本：$T_0 a_k=X(jk\omega_0)$。$T_0$ 越大采样越密，极限下包络即连续频谱。

依据：奥本海姆 MIT OCW RES.6-007 [Lecture 8](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-8-continuous-time-fourier-transform/)；教材 §4.4–4.5。

前置：[[Continuous-Time Fourier Series]]。

---

## 1. 从 CTFS 到 CTFT

思路（OCW Lecture 8）：

1. 非周期 $x(t)$（有限支撑片段）→ 以周期 $T_0$ **周期延拓**得 $\tilde{x}(t)$
2. $\tilde{x}$ 有 CTFS $\{a_k\}$
3. $T_0\to\infty$ 时副本拉远，$\tilde{x}\to x$，离散谐波和 → 连续频率积分（CTFT）

![[ss-ctft-period-extension.svg]]

- $T_0$ 有限：用 [[Continuous-Time Fourier Series|CTFS]]
- $T_0\to\infty$：用 CTFT

---

## 2. 包络与采样关系

周期信号分析式：

$$
a_k=\frac{1}{T_0}\int_{T_0}\tilde{x}(t)\,e^{-jk\omega_0 t}\,dt,
\qquad
\omega_0=\frac{2\pi}{T_0}
$$

一个周期内 $\tilde{x}$ 与 $x$ 相同，且周期外 $x=0$ 时，定义包络

$$
X(j\omega)=\int_{-\infty}^{\infty}x(t)\,e^{-j\omega t}\,dt
$$

则

$$
T_0 a_k = X(jk\omega_0)
\qquad\text{i.e.}\qquad
a_k=\frac{1}{T_0}X(jk\omega_0)
$$

要点：

| 事实 | 含义 |
| ---- | ---- |
| 包络形状 | 只由**一个周期内的波形**决定，与 $T_0$ 无关 |
| $\{a_k\}$ | 包络在 $\omega=k\omega_0$ 上的样本（常看 $T_0 a_k$） |
| $T_0$ 增大 | $\omega_0$ 变小，样本变密 |

> [!tip] 不是时域采样定理
> 这里是对频域包络 $X(j\omega)$ 按 $\omega_0$ 取样。时域冲激串采样 → 频谱周期复制，属另一专题。

---

## 3. $T_0$ 增大：样本变密

同一包络，不同 $\omega_0$（示意图；折线近似 $\lvert\operatorname{sinc}\rvert$ 型包络）。

**较小 $T_0$（较大 $\omega_0$）——样本疏：**

![[ss-ctft-envelope-sparse.svg]]

**较大 $T_0$（较小 $\omega_0$）——样本密：**

![[ss-ctft-envelope-dense.svg]]

$T_0\to\infty$ 时 $\omega_0\to 0$，样本铺满包络 → 连续 $X(j\omega)$。

---

## 4. CTFT 分析式与综合式

**分析（Fourier transform）**

$$
X(j\omega)=\int_{-\infty}^{\infty}x(t)\,e^{-j\omega t}\,dt
$$

**综合（inverse Fourier transform）**

$$
x(t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}X(j\omega)\,e^{j\omega t}\,d\omega
$$

$\sum_k a_k e^{jk\omega_0 t}$ 在 $\omega_0\to 0$ 时过渡为上面积分。记 $X(j\omega)$ 便于与 $H(j\omega)$、$s=j\omega$ 对齐。

---

## 5. 周期信号与同一框架

| 情形 | 关系 |
| ---- | ---- |
| 非周期 $x$ 的周期延拓 $\tilde{x}$ | $T_0 a_k=X(jk\omega_0)$（包络采样） |
| $T_0\to\infty$ | CTFS → CTFT |
| 周期信号本身的 CTFT | 冲激串，面积常取 $2\pi a_k$，位于 $k\omega_0$ |

本笔记重点是第 2–3 行的桥；冲激串表示可另开专题。

---

## 6. 例：$e^{-at}u(t)$ 与波特图

$a>0$：

$$
x(t)=e^{-at}u(t)
\qquad\longleftrightarrow\qquad
X(j\omega)=\frac{1}{a+j\omega}
$$

$$
\bigl|X(j\omega)\bigr|=\frac{1}{\sqrt{a^2+\omega^2}}
$$

波特图：横轴 $\log\omega$，纵轴

$$
20\log_{10}\bigl|X(j\omega)\bigr|\quad(\mathrm{dB})
$$

一阶情形：低频近似水平；过 $\omega\sim a$ 后约 $-20\,\mathrm{dB}/\mathrm{dec}$。

![[ss-ctft-bode.svg]]

该 $X(j\omega)$ 本身就是连续包络；若周期延拓，则 $a_k$ 仍是其上离散样本。

---

## 7. 速查

| 项目 | 内容 |
| ---- | ---- |
| 包络 | $X(j\omega)=\int x(t)e^{-j\omega t}\,dt$ |
| 采样 | $T_0 a_k=X(jk\omega_0)$，$\omega_0=2\pi/T_0$ |
| $T_0\uparrow$ | 包络不变，谐波点变密 |
| 极限 | CTFT 分析 / 综合对 |
| Bode | $20\log_{10}\|X\|$ vs $\log\omega$ |

---

## 参见

- [[Signals and Systems MOC]]
- [[Continuous-Time Fourier Series]]
- [[Sinusoidal and Exponential Signals]]
- [[Convolution]]
- [OCW Lecture 8 notes (PDF)](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec08/)
