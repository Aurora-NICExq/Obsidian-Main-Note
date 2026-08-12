---
title: "Butterworth Filters"
aliases:
  - "巴特沃斯滤波器"
  - "最大平坦"
  - "Butterworth"
  - "极点半圆分布"
tags: [signals_and_systems, ee, filter]
up: "[[Signals and Systems MOC]]"
related:
  - "[[Filtering]]"
  - "[[Continuous-Time Second-Order Systems]]"
  - "[[The Laplace Transform]]"
  - "[[Mapping Continuous-Time Filters to Discrete-Time Filters]]"
---
# Butterworth Filters

> [!summary] 核心结论
> $$|H(j\omega)|^2=\frac{1}{1+(\omega/\omega_c)^{2N}}$$
> **最大平坦**：前 $2N-1$ 阶导数在 $\omega=0$ 处全为零，通带内没有任何纹波。
> 极点是 $2N$ 个**等角均布**在半径 $\omega_c$ 的圆上的点；取左半平面那 $N$ 个即得因果稳定的 $H(s)$。
> 代价：过渡带在所有经典家族里**最宽**。想要更陡就得换切比雪夫（容忍纹波）或椭圆（两边都容忍纹波）。

依据：奥本海姆 MIT OCW RES.6-007 [Lecture 24](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-24-butterworth-filters/)；教材 §6.5、§9.7。

前置：[[Filtering]]、[[The Laplace Transform]]。

---

## 1. 定义与「最大平坦」

$$
|H(j\omega)|^2=\frac{1}{1+\left(\dfrac{\omega}{\omega_c}\right)^{2N}}
$$

![[ss-butterworth-filters-01.svg]]

三条恒成立的性质：

- $|H(0)|=1$（直流增益归一）
- $|H(j\omega_c)|=1/\sqrt2$ —— **$\omega_c$ 永远是 $-3\,\mathrm{dB}$ 点，与阶数无关**
- $\omega\gg\omega_c$ 时 $|H|\approx(\omega_c/\omega)^N$，即 $-20N\,\mathrm{dB/dec}$

「最大平坦」的确切含义：在 $\omega=0$ 处，$|H|^2$ 的前 $2N-1$ 阶导数全为零。这是在「通带内单调无纹波」这个约束下能做到的最平坦。

> [!note] 平坦是有代价的
> 把全部「设计自由度」都花在 $\omega=0$ 附近，过渡带自然就没什么资源了。
> 切比雪夫的思路正好相反：允许通带里有等纹波，把自由度均摊到整个通带，换来更陡的过渡带。同阶数下切比雪夫的过渡带明显更窄。

---

## 2. 极点在半圆上

从 $|H|^2=H(s)H(-s)|_{s=j\omega}$ 出发，令 $\omega^2=-s^2$：

$$
H(s)H(-s)=\frac{1}{1+\left(\dfrac{s}{j\omega_c}\right)^{2N}}
$$

分母为零得 $2N$ 个根：

$$
s_k=\omega_c\,e^{j\pi\left(\frac{2k+N+1}{2N}\right)},\qquad k=0,1,\dots,2N-1
$$

它们**等角均布**（间隔 $\pi/N$）在半径 $\omega_c$ 的圆上，且从不落在虚轴上。

**取左半平面那 $N$ 个**给 $H(s)$（右半平面的镜像归 $H(-s)$）—— 这样得到的系统因果且稳定。

$$
H(s)=\frac{\omega_c^N}{\prod_{k=1}^{N}(s-s_k)}
$$

### 低阶实例

| $N$ | 归一化 $H(s)$（$\omega_c=1$） |
| ---- | ---- |
| 1 | $\dfrac{1}{s+1}$ |
| 2 | $\dfrac{1}{s^2+\sqrt2\,s+1}$ |
| 3 | $\dfrac{1}{(s+1)(s^2+s+1)}$ |
| 4 | $\dfrac{1}{(s^2+0.765s+1)(s^2+1.848s+1)}$ |

二阶节 $s^2+\sqrt2s+1$ 对照 [[Continuous-Time Second-Order Systems|标准二阶形式]]：$2\zeta\omega_n=\sqrt2$、$\omega_n=1$，即

$$
\zeta=\frac{1}{\sqrt2}\approx0.707
$$

**这正是那个「最平坦、无谐振峰、超调 4.3%」的临界值** —— 巴特沃斯的最大平坦性和二阶系统的 $\zeta=0.707$ 是同一件事。

奇数阶总有一个实极点（$s=-\omega_c$），偶数阶全是复共轭对。

---

## 3. 定阶

给定阻带指标（$\omega\ge\omega_s$ 时衰减至少 $A_s$ dB）：

$$
N\ \ge\ \frac{\log_{10}\left(10^{A_s/10}-1\right)}{2\log_{10}(\omega_s/\omega_c)}
$$

> [!example] 数值感觉
> 要求 $\omega_s=2\omega_c$ 处衰减 $40\,\mathrm{dB}$：
> $$N\ge\frac{\log_{10}(10^4-1)}{2\log_{10}2}=\frac{4}{0.602}\approx 6.6\ \Rightarrow\ N=7$$
> 七阶！同样指标用椭圆滤波器只要三阶。这就是最大平坦的代价。

---

## 4. 实现

高阶不要用直接型 —— 系数量化误差会把极点推得乱七八糟。标准做法是**分解成二阶节（biquad）级联**：

$$
H(s)=\prod_{i}\frac{\omega_c^2}{s^2+2\zeta_i\omega_cs+\omega_c^2}
$$

各节的 $\zeta_i=\cos\theta_i$，$\theta_i$ 就是各极点与负实轴的夹角。

模拟实现常用 Sallen–Key 或多重反馈拓扑，一节一个运放。数字实现则先做双线性变换再级联 biquad，见 [[Mapping Continuous-Time Filters to Discrete-Time Filters]]。

---

## 5. 四大家族对照

| | 通带 | 阻带 | 同指标阶数 | 相位 |
| ---- | ---- | ---- | ---- | ---- |
| **巴特沃斯** | 最大平坦，**无纹波** | 单调 | 最高 | 最好 |
| 切比雪夫 I | **等纹波** | 单调 | 中 | 差 |
| 切比雪夫 II | 单调 | **等纹波** | 中 | 差 |
| 椭圆（Cauer） | 等纹波 | 等纹波 | **最低** | 最差 |

一条通用规律：**允许纹波的地方越多，同样指标需要的阶数越低，相位失真越大**。

选型经验：
- 要求波形保真（音频、示波器前端）$\to$ 巴特沃斯甚至贝塞尔（最大平坦**群延迟**）。
- 要求陡峭、只看幅度（抗混叠、信道选择）$\to$ 椭圆。
- 要求严格线性相位 $\to$ 放弃 IIR，改用 FIR。

---

## 6. 速查

| 项目 | 内容 |
| ---- | ---- |
| $\lvert H\rvert^2$ | $1/\big(1+(\omega/\omega_c)^{2N}\big)$ |
| $-3\,\mathrm{dB}$ 点 | 恒为 $\omega_c$（与 $N$ 无关） |
| 滚降 | $-20N\,\mathrm{dB/dec}$ |
| 极点 | $2N$ 个等角均布在半径 $\omega_c$ 的圆上，取左半平面 $N$ 个 |
| 二阶节 $\zeta$ | $\cos\theta_i$；$N=2$ 时 $\zeta=1/\sqrt2$ |
| 定阶 | $N\ge\dfrac{\log_{10}(10^{A_s/10}-1)}{2\log_{10}(\omega_s/\omega_c)}$ |
| 实现 | biquad 级联 |

---

## 参见

- [[Signals and Systems MOC]]
- [[Filtering]]（滤波器指标与理想滤波器的不可实现性）
- [[Continuous-Time Second-Order Systems]]（$\zeta=1/\sqrt2$ 的由来）
- [[The Laplace Transform]]（极点位置与稳定性）
- [[Mapping Continuous-Time Filters to Discrete-Time Filters]]（做成数字滤波器）
- [OCW Lecture 24 notes (PDF)](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec24/)
