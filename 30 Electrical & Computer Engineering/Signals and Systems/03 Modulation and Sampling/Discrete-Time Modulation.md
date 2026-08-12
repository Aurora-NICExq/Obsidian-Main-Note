---
title: "Discrete-Time Modulation"
aliases:
  - "离散时间调制"
  - "DT 调制"
  - "复调制"
tags: [signals_and_systems, ee, modulation]
up: "[[Signals and Systems MOC]]"
related:
  - "[[Continuous-Time Modulation]]"
  - "[[Discrete-Time Fourier Transform]]"
  - "[[Discrete-Time Sampling]]"
---
# Discrete-Time Modulation

> [!summary] 核心结论
> 形式与连续时间调制**完全相同**：乘 $\cos(\Omega_cn)$ 把谱搬到 $\pm\Omega_c$。
> 但多了一条硬约束：所有频率都住在长度 $2\pi$ 的区间里。搬得太远，副本会从 $\pi$ 那一头**绕回来撞上自己** —— 无混叠条件是 $\Omega_c+\Omega_M<\pi$。
> 复调制 $e^{j\Omega_cn}$ 只搬一份（不产生镜像），因此在数字通信里比实余弦更常用。

依据：奥本海姆 MIT OCW RES.6-007 [Lecture 15](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-15-discrete-time-modulation/)；教材 §8.7。

前置：[[Continuous-Time Modulation]]、[[Discrete-Time Fourier Transform]]。

---

## 1. 相乘性质（离散版）

$$
x[n]\,c[n]\;\longleftrightarrow\;\frac{1}{2\pi}X(e^{j\Omega})\circledast C(e^{j\Omega})
$$

注意是**周期卷积** $\circledast$（在长度 $2\pi$ 的区间上做），因为两个频谱本身都是 $2\pi$ 周期的。

载波 $\cos(\Omega_cn)$ 的 DTFT 是 $\pm\Omega_c$ 处的冲激串（每 $2\pi$ 重复）：

$$
\cos(\Omega_cn)\;\longleftrightarrow\;\pi\sum_{k}\big[\delta(\Omega-\Omega_c-2\pi k)+\delta(\Omega+\Omega_c-2\pi k)\big]
$$

---

## 2. 搬移与绕回

![[ss-discrete-time-modulation-01.svg]]

$$
Y(e^{j\Omega})=\frac{1}{2}X\big(e^{j(\Omega-\Omega_c)}\big)+\frac{1}{2}X\big(e^{j(\Omega+\Omega_c)}\big)
$$

搬移、减半，与连续时间一模一样。差别只在边界：

> [!important] 频率轴是有限的
> 连续时间里 $\omega_c$ 想调多大调多大；离散时间里频率轴总长只有 $2\pi$。
> 把基带搬到 $\Omega_c$ 时，$+\Omega_c$ 那份的右边缘到了 $\Omega_c+\Omega_M$。如果它超过 $\pi$，就会与从 $2\pi$ 那边周期延拓过来的 $-\Omega_c$ 副本相撞。
>
> 无混叠条件：
> $$\Omega_c+\Omega_M<\pi$$
>
> 这与 [[Sampling|采样定理]] 是同一件事的两种说法 —— 都是「频谱副本别撞上」。

---

## 3. 解调

同样是再乘一次载波然后低通：

$$
w[n]=y[n]\cos(\Omega_cn)=\frac{1}{2}x[n]+\frac{1}{2}x[n]\cos(2\Omega_cn)
$$

低通截止取在 $\Omega_M$ 与 $2\Omega_c-\Omega_M$ 之间。相位失配的后果与连续时间完全相同（输出乘 $\cos\theta$）。

---

## 4. 复调制：更常用的做法

用复指数而不是实余弦：

$$
y[n]=x[n]\,e^{j\Omega_cn}
\qquad\Longleftrightarrow\qquad
Y(e^{j\Omega})=X\big(e^{j(\Omega-\Omega_c)}\big)
$$

**只搬一份，不产生 $-\Omega_c$ 处的镜像，幅度也不减半。**

好处：

- 频谱利用率翻倍（不浪费一个边带）。
- 不需要担心两份副本互撞，条件放宽成 $\Omega_c+\Omega_M<2\pi$ 之类。
- 数字系统里复数运算本来就是家常便饭（I/Q 两路实信号）。

代价：$y[n]$ 是复序列，需要两路实通道传输。这正是现代数字通信里 **I/Q 调制**的由来 —— 实部走 I 路、虚部走 Q 路。

解调只需乘 $e^{-j\Omega_cn}$，一步搬回来，连低通都省了（如果没有别的信号占用）。

---

## 5. 与抽取 / 内插的关系

调制把频谱**平移**，抽取和内插把频谱**伸缩**。两类操作合起来构成了多速率信号处理的全部基本工具：

| 操作 | 频域效果 |
| ---- | ---- |
| 乘 $e^{j\Omega_cn}$ | 平移 $\Omega_c$ |
| 抽取 $\downarrow M$ | 展宽 $M$ 倍（副本靠拢） |
| 内插 $\uparrow L$ | 压窄 $L$ 倍（产生镜像） |

数字下变频（DDC）就是「复调制搬到基带 + 低通 + 抽取」的标准组合。详见 [[Discrete-Time Sampling]]。

---

## 6. 速查

| 项目 | 连续时间 | 离散时间 |
| ---- | ---- | ---- |
| 实调制 | $x\cos\omega_ct$ | $x[n]\cos\Omega_cn$ |
| 频域 | 搬到 $\pm\omega_c$，减半 | 搬到 $\pm\Omega_c$，减半 |
| 无混叠条件 | $\omega_c>\omega_M$ | $\Omega_c+\Omega_M<\pi$ |
| 频率轴 | 整条实轴 | 长度 $2\pi$（周期） |
| 复调制 | $xe^{j\omega_ct}$ | $x[n]e^{j\Omega_cn}$，只搬一份 |

---

## 参见

- [[Signals and Systems MOC]]
- [[Continuous-Time Modulation]]（对照的连续版本）
- [[Discrete-Time Fourier Transform]]（$2\pi$ 周期性的来源）
- [[Discrete-Time Sampling]]（抽取与内插）
- [OCW Lecture 15 notes (PDF)](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec15/)
