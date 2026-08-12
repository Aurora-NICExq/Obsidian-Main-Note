---
title: "单位阶跃和单位脉冲信号"
aliases: ["Unit Step and Unit Impulse", "阶跃与冲激", "单位样值"]
tags: [signals_and_systems, ee]
up: "[[Signals and Systems MOC]]"
related: ["[[Sinusoidal and Exponential Signals]]", "[[System Interconnection and Basic Properties]]", "[[Source-Free and Driven RC Response]]", "[[Convolution]]"]
---
# 单位阶跃和单位脉冲信号

> [!summary] 核心结论
> 单位阶跃描述“某时刻起接通”；单位脉冲（连续冲激 / 离散样值）描述“在单点集中单位面积（或单位幅度）的冲击”。二者互为积分–微分（连续）或累加–一阶差分（离散）关系，是表示任意信号、定义冲激响应的基础。

---
## 1. 连续时间：单位阶跃 $u(t)$

$$
u(t)=\begin{cases}
0,& t<0\\
1,& t>0
\end{cases}
$$

$t=0$ 处单点取值常取 $1$ 或 $1/2$，或干脆不定义；单点不影响积分与绝大多数系统分析。

![[ss-unit-step-ct.svg]]

用途：把“从 $t=0$ 开始作用”的信号写成乘积，例如受迫 RC 响应中的 $u(t)$ 因子，见 [[Source-Free and Driven RC Response]]。

---
## 2. 连续时间：单位冲激 $\delta(t)$

### 2.1 作为阶跃的广义导数

阶跃在 $t=0$ 不连续，其导数在普通函数意义下不存在，但在广义函数（分布）意义下：
$$
\delta(t)=\frac{du(t)}{dt}
$$

反过来，冲激的积累给出阶跃：
$$
u(t)=\int_{-\infty}^{t}\delta(\tau)\,d\tau
$$

### 2.2 用有限脉宽近似

先定义上升宽度为 $\Delta$ 的斜坡阶跃 $u_\Delta(t)$，再取导数得到高度为 $1/\Delta$、宽度为 $\Delta$ 的矩形脉冲：
$$
\delta_\Delta(t)=\frac{du_\Delta(t)}{dt}
$$

令 $\Delta\to 0$，$\delta_\Delta$ 趋近单位冲激：面积始终为 $1$，宽度趋于 $0$，峰值趋于无穷。

![[ss-impulse-approx.svg]]

### 2.3 基本性质

- 抽样（筛选）性质：若 $x(t)$ 在 $t_0$ 连续，则
$$
\int_{-\infty}^{\infty}x(t)\,\delta(t-t_0)\,dt=x(t_0)
$$
- 面积为 $1$：$\displaystyle\int_{-\infty}^{\infty}\delta(t)\,dt=1$
- 时移：$\delta(t-t_0)$ 表示集中在 $t=t_0$ 的单位冲激

图示上常用带箭头的竖线表示 $\delta(t)$，箭头旁标注强度（面积）。

![[ss-unit-impulse-ct.svg]]

---
## 3. 离散时间：单位阶跃与单位样值

### 3.1 定义

单位样值（单位脉冲序列）：
$$
\delta[n]=\begin{cases}
1,& n=0\\
0,& n\neq 0
\end{cases}
$$

单位阶跃序列：
$$
u[n]=\begin{cases}
1,& n\geq 0\\
0,& n<0
\end{cases}
$$

![[ss-impulse-step-dt.svg]]

### 3.2 一阶差分与累加

单位脉冲是单位阶跃的一阶差分：
$$
\delta[n]=u[n]-u[n-1]
$$

单位阶跃是单位脉冲的累加（奔跑和）：
$$
u[n]=\sum_{k=-\infty}^{n}\delta[k]
$$

> [!attention] 连续 vs 离散
> 连续时间用微分 / 积分联系 $\delta(t)$ 与 $u(t)$；离散时间用一阶差分 / 累加联系 $\delta[n]$ 与 $u[n]$。离散样值 $\delta[n]$ 是普通序列（取值就是 $0$ 或 $1$），不是广义函数。

---
## 4. 对照小结

| 项目            | 连续时间                                         | 离散时间                                 |
| ------------- | -------------------------------------------- | ------------------------------------ |
| 阶跃            | $u(t)$                                       | $u[n]$                               |
| 脉冲            | $\delta(t)$（冲激）                              | $\delta[n]$（样值）                      |
| 脉冲 ← 阶跃       | $\delta(t)=du/dt$                            | $\delta[n]=u[n]-u[n-1]$              |
| 阶跃 ← 脉冲       | $u(t)=\int_{-\infty}^{t}\delta(\tau)\,d\tau$ | $u[n]=\sum_{k=-\infty}^{n}\delta[k]$ |
| $t=0$ / $n=0$ | 阶跃单点可不定；冲激为广义函数                              | 二者取值均明确定义                            |

---
## 参见
- [[Signals and Systems MOC]]
- [[Sinusoidal and Exponential Signals]]
- [[System Interconnection and Basic Properties]]（原稿中系统部分已拆至此）
- [[Source-Free and Driven RC Response]]
