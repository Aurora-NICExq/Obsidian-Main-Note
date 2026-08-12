---
title: "Continuous-Time Second-Order Systems"
aliases:
  - "二阶系统"
  - "阻尼比"
  - "自然频率"
  - "欠阻尼"
  - "品质因数 Q"
tags: [signals_and_systems, ee, laplace]
up: "[[Signals and Systems MOC]]"
related:
  - "[[The Laplace Transform]]"
  - "[[Systems Represented by Differential and Difference Equations]]"
  - "[[Butterworth Filters]]"
  - "[[Feedback]]"
---
# Continuous-Time Second-Order Systems

> [!summary] 核心结论
> $$H(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_ns+\omega_n^2},\qquad s=-\zeta\omega_n\pm j\omega_n\sqrt{1-\zeta^2}$$
> 两个参数说完一切：$\omega_n$ 定**快慢**，$\zeta$ 定**振荡与否**。欠阻尼极点恒落在半径 $\omega_n$ 的圆上，与负实轴的夹角满足 $\cos\theta=\zeta$。
> 一句话的几何直觉：**离虚轴越远衰减越快，离实轴越远振荡越快**。设计二阶系统就是在这两件事之间挑一个 $\theta$。

依据：奥本海姆 MIT OCW RES.6-007 [Lecture 21](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-21-continuous-time-second-order-systems/)；教材 §6.5。

前置：[[The Laplace Transform]]、[[Systems Represented by Differential and Difference Equations]]。

---

## 1. 标准形式

二阶 LCCDE

$$
\frac{d^2y}{dt^2}+2\zeta\omega_n\frac{dy}{dt}+\omega_n^2y=\omega_n^2x
$$

对应

$$
H(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_ns+\omega_n^2}
$$

两个参数：

- $\omega_n$ —— **自然频率**（undamped natural frequency），设定整个时间尺度。
- $\zeta$ —— **阻尼比**（damping ratio），无量纲，决定响应形态。

极点：

$$
s_{1,2}=-\zeta\omega_n\pm\omega_n\sqrt{\zeta^2-1}
$$

二阶系统之所以值得单独一讲，是因为**任何高阶系统都可以分解成一阶和二阶节的级联** —— 二阶是复极点对的最小载体。

---

## 2. 三种阻尼

![[ss-continuous-time-second-order-systems-01.svg]]

| $\zeta$ | 极点 | 阶跃响应 |
| ---- | ---- | ---- |
| $\zeta>1$ | 两个**实**极点 | 过阻尼：无超调，慢（被靠近虚轴的那个慢极点主导） |
| $\zeta=1$ | **重**实极点 $-\omega_n$ | 临界阻尼：**最快的无超调响应** |
| $0<\zeta<1$ | 一对**复共轭** | 欠阻尼：振荡衰减，有超调 |
| $\zeta=0$ | 纯虚 $\pm j\omega_n$ | 无阻尼：等幅振荡（临界稳定） |
| $\zeta<0$ | 在右半平面 | 发散 |

欠阻尼情形的阶跃响应：

$$
s(t)=1-\frac{e^{-\zeta\omega_nt}}{\sqrt{1-\zeta^2}}\sin\big(\omega_d t+\theta\big)u(t),
\qquad \omega_d=\omega_n\sqrt{1-\zeta^2}
$$

$\omega_d$ 是**阻尼振荡频率**，总是小于 $\omega_n$。

---

## 3. 极点位置的几何读法

这是本讲最有价值的部分。欠阻尼极点写成极坐标：

$$
s=-\zeta\omega_n\pm j\omega_d = \omega_n e^{\pm j(\pi-\theta)},\qquad \cos\theta=\zeta
$$

于是：

| 几何量 | 对应的时域含义 |
| ---- | ---- |
| 到原点的距离 $=\omega_n$ | 整体速度尺度 |
| **实部** $-\zeta\omega_n$ | 包络衰减率（时间常数 $1/\zeta\omega_n$） |
| **虚部** $\omega_d$ | 振荡频率 |
| 与负实轴夹角 $\theta$ | $\cos\theta=\zeta$，决定超调量 |

**沿着圆弧移动**（$\omega_n$ 不变、$\zeta$ 变）：改变振荡与阻尼的配比。
**沿着射线移动**（$\zeta$ 不变、$\omega_n$ 变）：波形形状不变，只是时间轴缩放。

---

## 4. 时域指标

工程上常用的四个（欠阻尼）：

$$
\text{超调量 } M_p=e^{-\pi\zeta/\sqrt{1-\zeta^2}}
$$

$$
\text{峰值时间 } t_p=\frac{\pi}{\omega_d},\qquad
\text{上升时间 } t_r\approx\frac{1.8}{\omega_n},\qquad
\text{调节时间 } t_s\approx\frac{4}{\zeta\omega_n}\ (\pm2\%)
$$

常用数值：

| $\zeta$ | 超调 $M_p$ |
| ---- | ---- |
| $0.3$ | $37\%$ |
| $0.5$ | $16\%$ |
| $0.707$ | $4.3\%$ |
| $0.8$ | $1.5\%$ |
| $1.0$ | $0$ |

$\zeta=0.707$（即 $\theta=45°$）是最常用的折中点：超调小、调节快、频响也最平坦 —— 这正是巴特沃斯二阶节的取值（见 [[Butterworth Filters]]）。

---

## 5. 频率响应与 Q

$$
|H(j\omega)|=\frac{\omega_n^2}{\sqrt{(\omega_n^2-\omega^2)^2+(2\zeta\omega_n\omega)^2}}
$$

$\zeta<1/\sqrt2$ 时出现**谐振峰**：

$$
\omega_r=\omega_n\sqrt{1-2\zeta^2},
\qquad
|H|_{\max}=\frac{1}{2\zeta\sqrt{1-\zeta^2}}
$$

$\zeta\ge1/\sqrt2$ 时频响单调下降，无峰。

定义**品质因数**

$$
Q=\frac{1}{2\zeta}
$$

$Q$ 大 $\Leftrightarrow$ 阻尼小 $\Leftrightarrow$ 峰尖、带宽窄、振荡持久。RLC 电路里 $Q=\frac{1}{R}\sqrt{L/C}$，同一个量的电路版本。

> [!note] 时域与频域的同一件事
> 时域超调大 $\leftrightarrow$ 频域有谐振峰 $\leftrightarrow$ 极点靠近虚轴 $\leftrightarrow$ $Q$ 大 $\leftrightarrow$ $\zeta$ 小。
> 这五种说法描述的是同一个物理状态，只是看的角度不同。能在它们之间自由切换，就算是掌握了二阶系统。

---

## 6. 例：RLC 串联

$$
H(s)=\frac{V_C}{V_{in}}=\frac{1/LC}{s^2+\frac{R}{L}s+\frac{1}{LC}}
$$

对照标准形式：

$$
\omega_n=\frac{1}{\sqrt{LC}},\qquad
2\zeta\omega_n=\frac{R}{L}\ \Rightarrow\ \zeta=\frac{R}{2}\sqrt{\frac{C}{L}}
$$

$R$ 就是阻尼的来源（耗散元件）。$R\to0$ 时 $\zeta\to0$，极点跑到虚轴上 —— LC 谐振回路等幅振荡。

---

## 7. 速查

| 项目 | 内容 |
| ---- | ---- |
| $H(s)$ | $\dfrac{\omega_n^2}{s^2+2\zeta\omega_ns+\omega_n^2}$ |
| 极点 | $-\zeta\omega_n\pm j\omega_n\sqrt{1-\zeta^2}$ |
| $\cos\theta$ | $=\zeta$ |
| $\omega_d$ | $\omega_n\sqrt{1-\zeta^2}$ |
| 超调 | $e^{-\pi\zeta/\sqrt{1-\zeta^2}}$ |
| 调节时间 | $\approx4/(\zeta\omega_n)$ |
| 谐振条件 | $\zeta<1/\sqrt2$ |
| $Q$ | $1/(2\zeta)$ |

---

## 参见

- [[Signals and Systems MOC]]
- [[The Laplace Transform]]（极点零点的框架）
- [[Systems Represented by Differential and Difference Equations]]（二阶 LCCDE）
- [[Butterworth Filters]]（$\zeta=1/\sqrt2$ 的二阶节）
- [[Feedback]]（反馈怎么移动极点）
- [OCW Lecture 21 notes (PDF)](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec21/)
