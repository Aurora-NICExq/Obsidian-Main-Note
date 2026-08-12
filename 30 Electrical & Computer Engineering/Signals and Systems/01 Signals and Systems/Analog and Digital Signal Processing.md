---
title: "Analog and Digital Signal Processing"
aliases: ["模拟与数字信号处理", "冲激响应与系统属性", "LTI 因果稳定无记忆"]
tags: [signals_and_systems, ee, lti]
up: "[[Signals and Systems MOC]]"
related: ["[[Convolution]]", "[[System Interconnection and Basic Properties]]", "[[Unit Step and Unit Impulse Signals]]"]
---
# Analog and Digital Signal Processing

> [!summary] 核心结论
> 对 **LTI** 系统，许多属性都可以直接翻译成对冲激响应 $h$ 的条件：无记忆 $\Leftrightarrow$ $h$ 是冲激的倍数；因果 $\Leftrightarrow$ $h$ 在负时间全为零；BIBO 稳定 $\Leftrightarrow$ $h$ 绝对可积 / 绝对可和。连续（模拟）与离散（数字）结论平行，只是积分换成求和、$\delta(t)$ 换成 $\delta[n]$。

前置：[[System Interconnection and Basic Properties|系统属性]]、[[Convolution|卷积与冲激响应]]、[[Unit Step and Unit Impulse Signals|阶跃与冲激]]。

---

## 1. 冲激响应是什么

LTI 系统对单位冲激（连续 $\delta(t)$ / 离散 $\delta[n]$）的输出，记为冲激响应（脉冲响应）$h(t)$ 或 $h[n]$。

一旦有了 $h$，任意输入的**零状态响应**就是卷积：

$$
y(t)=x(t)*h(t),\qquad
y[n]=x[n]*h[n]
$$

> [!note] 零输入响应
> 线性系统总响应常写成：**零输入响应**（仅由初始条件 / 储能引起）+ **零状态响应**（初始松弛时由输入经卷积产生）。本笔记里用 $h$ 刻画的，默认是松弛 LTI 的零状态部分。

---

## 2. 无记忆 $\Leftrightarrow$ $h$ 是冲激的倍数

无记忆：时刻 $t$（或 $n$）的输出只依赖**同一时刻**的输入。

卷积里 $y(t)=\int x(\tau)h(t-\tau)\,d\tau$。若输出不能“看见” $\tau\neq t$ 的输入，就要求

$$
h(t-\tau)\ \text{仅在}\ \tau=t\ \text{处非零}
$$

即 $h$ 本身集中在原点：

| | 连续（C-T / 模拟） | 离散（D-T / 数字） |
| --- | --- | --- |
| 无记忆 LTI | $h(t)=k\,\delta(t)$ | $h[n]=k\,\delta[n]$ |
| 含义 | 瞬时增益 $k$（如电阻 $v=Ri$） | 同一拍的数乘 |

![[ss-memoryless-h.svg]]

若 $h$ 在原点以外还有值（或有宽度），系统就有记忆。

---

## 3. 因果性 $\Leftrightarrow$ $h$ 的支撑在“现在及以后”

因果：输出不依赖**未来**输入。

对 LTI，这等价于冲激响应在负时间全为零：

$$
h(t)=0\ (t<0),\qquad
h[n]=0\ (n<0)
$$

直观：$\delta$ 在 $0$ 时刻才“敲一下”，因果系统在敲之前不能先有输出。

> [!tip]
> 因果与无记忆是两件事：电阻因果且无记忆；$h[n]=u[n]$（累加器）因果但有记忆；用到 $x[n+1]$ 的平滑器有记忆且非因果。

---

## 4. BIBO 稳定性 $\Leftrightarrow$ $h$ 绝对可积 / 可和

BIBO：凡有界输入都产生有界输出。

对 LTI，充要条件是冲激响应**绝对可积（连续）或绝对可和（离散）**：

$$
\int_{-\infty}^{\infty}\lvert h(\tau)\rvert\,d\tau<\infty,
\qquad
\sum_{k=-\infty}^{\infty}\lvert h[k]\rvert<\infty
$$

记忆口诀：**脉冲可（绝对）求和 / 可积 $\Rightarrow$ 稳定**。

| 系统 | $h$ | 稳定？ |
| ---- | --- | ------ |
| 恒等 | $\delta(t)$ / $\delta[n]$ | 是（积分为 1） |
| 理想延时 | $\delta(t-t_0)$ / $\delta[n-n_0]$ | 是 |
| 积分器 / 累加器 | $u(t)$ / $u[n]$ | **否**（不可积 / 不可和） |
| 指数衰减 $a^{n}u[n]$（$\lvert a\rvert<1$） | — | 是 |

---

## 5. 累加器：递归实现与逆系统

离散累加器

$$
y[n]=\sum_{k=-\infty}^{n}x[k]
$$

可写成递归（一阶差分方程）：

$$
y[n]=\sum_{k=-\infty}^{n-1}x[k]+x[n]=y[n-1]+x[n]
$$

只要记住上一步输出，不必每次从 $-\infty$ 重加——这是 IIR / 递归实现的典型想法。

冲激响应：$x=\delta$ 时 $h[n]=u[n]$，故**不稳定**（见上节）。

但其**逆系统**是一阶差分：

$$
x[n]=y[n]-y[n-1]
$$

冲激响应 $h_{\mathrm{inv}}[n]=\delta[n]-\delta[n-1]$，绝对可和，**稳定**。

> [!important]
> 不稳定系统的逆仍可能稳定（累加器 ↔ 差分器）。稳定与可逆是不同属性。

连续对偶：积分器 $h(t)=u(t)$ 不稳定；微分器是其逆，在分布意义下 $h(t)=\delta'(t)$。

---

## 6. 积分器、微分器与冲激的“操作性”看法

### 6.1 单位积分器

$$
y(t)=\int_{-\infty}^{t}x(\tau)\,d\tau
\quad\Rightarrow\quad
h(t)=u(t)
$$

（因为对 $\delta$ 从 $-\infty$ 积到 $t$ 得到阶跃。）

两个积分器串联 $\Rightarrow$ 冲激响应是阶跃再积分：

$$
h(t)=\int_{-\infty}^{t}u(\tau)\,d\tau=t\,u(t)
$$
（单位斜坡；仍不稳定。）

### 6.2 微分器

$$
y(t)=\frac{dx(t)}{dt}
\quad\Rightarrow\quad
h(t)=\delta'(t)
$$
（广义函数意义下的冲激导数。）

### 6.3 脉冲的操作性定义

工程上常不纠缠 $\delta$ 的点值，而用它“做什么”来定义，例如抽样性质：

$$
\int_{-\infty}^{\infty}x(t)\,\delta(t-t_0)\,dt=x(t_0)
$$

或把 $\delta$ 看成宽度→0、面积=1 的脉冲极限。离散 $\delta[n]$ 则只是普通序列：在 $0$ 为 $1$、别处为 $0$。

---

## 7. 连续 vs 离散对照（本笔记速查）

| 属性 | 连续 LTI | 离散 LTI |
| ---- | -------- | -------- |
| 无记忆 | $h(t)=k\delta(t)$ | $h[n]=k\delta[n]$ |
| 因果 | $h(t)=0,\ t<0$ | $h[n]=0,\ n<0$ |
| BIBO 稳定 | $\int\lvert h\rvert<\infty$ | $\sum\lvert h\rvert<\infty$ |
| 积分器 / 累加器 | $h=u(t)$，不稳定 | $h=u[n]$，不稳定；递归 $y[n]=y[n-1]+x[n]$ |
| 其逆 | 微分器 | 一阶差分，稳定 |

---

## 参见

- [[Signals and Systems MOC]]
- [[Convolution]]
- [[System Interconnection and Basic Properties]]
- [[Unit Step and Unit Impulse Signals]]
