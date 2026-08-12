---
title: "Convolution"
aliases: ["卷积", "Convolution Sum", "Convolution Integral", "冲激响应与卷积"]
tags: [signals_and_systems, ee, convolution]
up: "[[Signals and Systems MOC]]"
related: ["[[Unit Step and Unit Impulse Signals]]", "[[System Interconnection and Basic Properties]]", "[[Sinusoidal and Exponential Signals]]", "[[Analog and Digital Signal Processing]]", "[[Continuous-Time Fourier Series]]"]
---
# Convolution

> [!summary] 核心结论
> 任意信号可写成**延迟脉冲的加权叠加**。对 **LTI** 系统，每个脉冲 $\delta[n-k]$（或 $\delta(t-\tau)$）只产生延迟了的冲激响应 $h[n-k]$（或 $h(t-\tau)$），再按线性叠加，输出就是输入与冲激响应的**卷积**。离散为求和 $y=x*h$，连续为积分；阶跃激励下常得到几何级数的闭式。

前置：[[Unit Step and Unit Impulse Signals|单位阶跃与单位脉冲]]、[[System Interconnection and Basic Properties|LTI 系统]]。

---

## 1. 两条分析主线

对线性时不变系统，常选“容易算”的基信号把输入拆开，再合成输出：

| 思路 | 把输入拆成 | 得到的表示 |
| ---- | ---------- | ---------- |
| **卷积** | 延迟脉冲的线性组合 | $y=x*h$（冲激响应） |
| **傅里叶分析** | 复指数的线性组合 | 频域乘积（见 [[Continuous-Time Fourier Series|连续时间傅里叶级数]]） |

本笔记只展开卷积这一条。

---

## 2. 离散时间：信号的脉冲分解

任意序列 $x[n]$ 可看成一系列**幅度为 $x[k]$、位于 $n=k$ 的样值**之和：

$$
x[n]=\sum_{k=-\infty}^{\infty} x[k]\,\delta[n-k]
$$

每一项 $x[k]\delta[n-k]$ 只在 $n=k$ 处非零，值为 $x[k]$。

![[ss-pulse-decomposition.svg]]

这正是离散单位样值的**筛选 / 重建**性质；连续时间对应
$$
x(t)=\int_{-\infty}^{\infty} x(\tau)\,\delta(t-\tau)\,d\tau
$$
见 [[Unit Step and Unit Impulse Signals#2.3 基本性质|冲激的抽样性质]]。

---

## 3. 离散卷积和（Convolution Sum）

设系统对 $\delta[n]$ 的响应为冲激响应 $h[n]$。若系统**线性且时不变**：

- 对 $\delta[n-k]$ 的响应是 $h[n-k]$
- 对 $x[k]\delta[n-k]$ 的响应是 $x[k]\,h[n-k]$
- 对整个 $x$ 的响应是各项叠加：

$$
y[n]=\sum_{k=-\infty}^{\infty} x[k]\,h[n-k]=x[n]*h[n]
$$

这就是**离散时间卷积和**。记号 $*$ 表示卷积，不是普通乘法。

> [!note] 计算图像（flip–slide–sum）
> 固定时刻 $n$ 时：把 $h[k]$ **翻转**为 $h[-k]$，再**平移**到 $h[n-k]$，与 $x[k]$ 逐点相乘后对 $k$ 求和，得到 $y[n]$。对每个 $n$ 重复一次。

![[ss-convolution-flip-slide.svg]]

上图示意：输入为阶跃型、$h$ 为因果指数型时，输出从 $0$ 逐渐爬升并趋于稳态（一阶系统的阶跃响应形态）。

---

## 4. 连续卷积积分（Convolution Integral）

连续时间完全平行：把 $x(t)$ 拆成冲激片，LTI 下叠加得

$$
y(t)=\int_{-\infty}^{\infty} x(\tau)\,h(t-\tau)\,d\tau=x(t)*h(t)
$$

计算时同样是对 $h(\tau)$ **翻转、平移**，再与 $x(\tau)$ 相乘并对重叠区间积分。

> [!tip] 与离散的对照
> | | 离散 | 连续 |
> | --- | --- | --- |
> | 基信号 | $\delta[n]$ | $\delta(t)$ |
> | 运算 | $\displaystyle\sum_k x[k]h[n-k]$ | $\displaystyle\int x(\tau)h(t-\tau)\,d\tau$ |
> | 前提 | LTI | LTI |

---

## 5. 例：阶跃输入与指数冲激响应

取离散因果指数冲激响应与单位阶跃输入（$|\alpha|<1$ 时系统 BIBO 稳定，公式对 $\alpha\neq 1$ 成立）：

$$
h[n]=\alpha^n u[n],\qquad x[n]=u[n]
$$

则对 $n\geq 0$，

$$
y[n]=\sum_{k=-\infty}^{\infty} x[k]h[n-k]=\sum_{k=0}^{n}\alpha^{n-k}
$$

令 $m=n-k$，得有限几何级数：

$$
y[n]=\sum_{m=0}^{n}\alpha^{m}=\frac{1-\alpha^{n+1}}{1-\alpha},\qquad n\geq 0
$$

（$n<0$ 时 $y[n]=0$。）这也是该 LTI 系统的**阶跃响应**。

![[ss-step-response-geometric.svg]]

连续时间对偶常见例子：$h(t)=e^{-at}u(t)$ 与 $x(t)=u(t)$，

$$
y(t)=\int_{0}^{t}e^{-a(t-\tau)}\,d\tau=\frac{1-e^{-at}}{a},\qquad t\geq 0
$$
（$a\neq 0$）。

---

## 6. 几条常用性质（速查）

对 LTI，卷积满足：

- **交换**：$x*h=h*x$
- **结合**：$(x*h_1)*h_2=x*(h_1*h_2)$（级联冲激响应相卷）
- **分配**：$x*(h_1+h_2)=x*h_1+x*h_2$（并联冲激响应相加）

这与 [[System Interconnection and Basic Properties#2. 系统互联|串联 / 并联]] 中 LTI 的结论一致。

---

## 参见

- [[Signals and Systems MOC]]
- [[Unit Step and Unit Impulse Signals]]
- [[System Interconnection and Basic Properties]]
- [[Analog and Digital Signal Processing]]（用 $h$ 判断无记忆 / 因果 / 稳定）
- [[Sinusoidal and Exponential Signals]]（傅里叶路线的基信号）
