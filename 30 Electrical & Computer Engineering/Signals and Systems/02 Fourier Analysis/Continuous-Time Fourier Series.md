---
title: "Continuous-Time Fourier Series"
aliases: ["连续时间傅立叶级数", "连续时间傅里叶级数", "CTFS", "Fourier Series"]
tags: [signals_and_systems, ee, fourier]
up: "[[Signals and Systems MOC]]"
related: ["[[Sinusoidal and Exponential Signals]]", "[[Convolution]]", "[[System Interconnection and Basic Properties]]", "[[Analog and Digital Signal Processing]]", "[[Continuous-Time Fourier Transform]]"]
---
# Continuous-Time Fourier Series

> [!summary] 核心结论
> 周期信号可写成**谐波相关复指数**的线性组合：$x(t)=\sum_k a_k e^{jk\omega_0 t}$。系数 $a_k$ 由一个周期上的积分求出。复指数是 LTI 的**本征函数**，故每个谐波只被频率响应 $H(j k\omega_0)$ 缩放。截断级数用低频项刻画慢变化；在跳变处出现**吉布斯涟波**。平方可积时误差能量随 $N\to\infty$ 趋于 0；点态收敛另需狄利克雷条件。

前置：[[Sinusoidal and Exponential Signals|复指数与正弦]]、[[Convolution|卷积]]（LTI 对指数输入的响应）。

---

## 1. 为什么看复指数：本征函数

连续 / 离散 LTI 的“好输入”分别是：

$$
\phi_k(t)=e^{s_k t}\quad(s_k\in\mathbb{C}),
\qquad
\phi_k[n]=z_k^n\quad(z_k\in\mathbb{C})
$$

对连续时间，取纯虚轴 $s=j\omega_k$，输入 $e^{j\omega_k t}$ 经冲激响应 $h$ 后：

$$
e^{j\omega_k t}\;\longrightarrow\;
e^{j\omega_k t}\underbrace{\int_{-\infty}^{\infty}h(\tau)e^{-j\omega_k\tau}\,d\tau}_{H(j\omega_k)}
$$

输出 = 输入 × 常数 $H(j\omega_k)$。因此把周期信号拆成谐波 $e^{jk\omega_0 t}$ 后，LTI 的稳态输出只要对每个系数乘上 $H(jk\omega_0)$。

> [!tip] 傅里叶级数 vs 傅里叶变换
> **级数（CTFS）**：针对**周期**信号，频谱是离散的 $\{a_k\}$。  
> **变换（CTFT）**：针对一般（常非周期）信号，频谱连续——见 [[Continuous-Time Fourier Transform]]（包络采样：$T_0 a_k=X(jk\omega_0)$，$T_0\to\infty$ 得变换）。

---

## 2. 谐波相关复指数

设基波角频率 $\omega_0$，基波周期

$$
T_0=\frac{2\pi}{\omega_0}
$$

第 $k$ 次谐波 $e^{jk\omega_0 t}$ 的周期为

$$
\frac{T_0}{|k|}=\frac{2\pi}{|k|\omega_0}\quad(k\neq 0)
$$

它们与基波**谐波相关**：每个都是基波频率的整数倍，合在一起仍以 $T_0$ 为周期。

任意（足够“好”的）周期信号可写成：

$$
x(t)=\sum_{k=-\infty}^{\infty} a_k\,e^{jk\omega_0 t}
$$

这是**综合（synthesis）公式**；复指数形式是最常用、也最便于接 LTI / 变换的写法。

![[ss-ctfs-spectrum.svg]]

---

## 3. 如何求系数 $a_k$（分析公式）

利用 $\{e^{jk\omega_0 t}\}$ 在一个周期上的正交性：

$$
\frac{1}{T_0}\int_{T_0}e^{jk\omega_0 t}e^{-jm\omega_0 t}\,dt
=\begin{cases}
1,& k=m\\
0,& k\neq m
\end{cases}
$$

两边乘 $e^{-jm\omega_0 t}$ 再在任一周期上积分，得

$$
a_k=\frac{1}{T_0}\int_{T_0}x(t)\,e^{-jk\omega_0 t}\,dt
$$

（积分限任意长度为 $T_0$ 的区间即可。）

$a_0=\dfrac{1}{T_0}\int_{T_0}x(t)\,dt$ 是直流（平均值）。

---

## 4. 三角函数形式（实信号）

$x(t)$ 为实信号时，$a_{-k}=a_k^*$，级数可改写成正弦 / 余弦：

$$
x(t)=a_0+\sum_{k=1}^{\infty}\Big(b_k\cos(k\omega_0 t)+c_k\sin(k\omega_0 t)\Big)
$$

或合成振幅–相位形式：

$$
x(t)=a_0+\sum_{k=1}^{\infty}A_k\cos(k\omega_0 t+\phi_k)
$$

与复指数系数的关系（记忆用）：

$$
b_k=a_k+a_{-k},\quad
c_k=j(a_k-a_{-k})
$$
（具体差一个约定因子时以所用教材为准；核心是**同一信息、两套坐标**。）

复指数形式便于分析 LTI；三角形式更直观地看见“第 $k$ 次谐波是多大的正弦”。

---

## 5. 例：奇对称方波与奇谐波

对称周期方波（奇函数、半周期对称）的典型结论：

- **偶次谐波为零**：只当 $k$ 为奇数时 $a_k\neq 0$
- 系数幅度常按 $1/|k|$ 衰减（跳变不连续信号的特征）

一种标准归一化下（幅度 $\pm 1$ 的奇方波）：

$$
j\pi\,a_k=
\begin{cases}
\dfrac{2}{k},& k\text{ 为奇数}\\[6pt]
0,& k\text{ 为偶数}
\end{cases}
\quad\Rightarrow\quad
a_k=-\,j\,\frac{2}{\pi k}\quad(k\text{ 奇})
$$

![[ss-ctfs-odd-square.svg]]

用有限个奇次谐波去逼近方波：先只有基波（像正弦），再加上 $3,5,7,\ldots$ 次，波形越来越“方”，平台上出现涟波——见下一节。

---

## 6. 部分和、误差与吉布斯现象

取前 $2N+1$ 项（$k=-N,\ldots,N$）得到部分和：

$$
x_N(t)\;\triangleq\;\sum_{k=-N}^{N}a_k\,e^{jk\omega_0 t}
$$

截断误差：

$$
e_N(t)\;\triangleq\;x(t)-x_N(t)
$$

直觉：

- **低频项**（小的 $|k|$）决定长时间尺度上的慢变化、总体轮廓  
- **高频项**刻画尖锐边沿、细节  

在**跳变不连续**处，部分和会出现过冲与振荡；增大 $N$ 时振荡变密、向跳变点挤，但过冲百分比并不趋于 0——这就是**吉布斯（Gibbs）现象**。涟波是截断的固有表现，不是“算错了”。

![[ss-gibbs-phenomenon.svg]]

---

## 7. 收敛：能表示哪些信号？

### 7.1 能量意义（平方可积）

若 $x$ 在一个周期内**平方可积**：

$$
\int_{T_0}\lvert x(t)\rvert^2\,dt<\infty
$$

则误差能量随项数增加趋于 0：

$$
\lim_{N\to\infty}\int_{T_0}\lvert e_N(t)\rvert^2\,dt=0
$$

即在 **$L^2$（均方）** 意义下收敛到 $x$。这回答草稿里的问题：一个周期内能量有限 $\Rightarrow$ $N\to\infty$ 时差异中的能量趋于 0。

### 7.2 点态收敛：狄利克雷（Dirichlet）条件

若还关心“每个 $t$ 上是否等于 $x(t)$”，常用充分条件（狄利克雷条件，表述因教材略异，核心是）：

1. 一个周期内绝对可积：$\int_{T_0}\lvert x(t)\rvert\,dt<\infty$  
2. 一个周期内极大 / 极小值个数有限（有界变差的一种常用说法）  
3. 不连续点个数有限  

则在连续点 $x_N(t)\to x(t)$；在跳变点收敛到左右极限的平均。吉布斯涟波与“能量收敛但仍有局部过冲”并不矛盾。

---

## 8. 速查

| 项目 | 公式 / 结论 |
| ---- | ----------- |
| 综合 | $\displaystyle x(t)=\sum_{k=-\infty}^{\infty}a_k e^{jk\omega_0 t}$ |
| 分析 | $\displaystyle a_k=\frac{1}{T_0}\int_{T_0}x(t)e^{-jk\omega_0 t}\,dt$ |
| 基波 | $T_0=2\pi/\omega_0$，$k$ 次谐波周期 $T_0/\|k\|$ |
| LTI | $e^{jk\omega_0 t}\mapsto H(jk\omega_0)\,e^{jk\omega_0 t}$ |
| 部分和 | $x_N=\sum_{k=-N}^{N}a_k e^{jk\omega_0 t}$，$e_N=x-x_N$ |
| 奇方波 | 常仅奇次谐波；$|a_k|\sim 1/\|k\|$；截断 → 吉布斯 |

---

## 参见

- [[Signals and Systems MOC]]
- [[Sinusoidal and Exponential Signals]]
- [[Convolution]]
- [[Analog and Digital Signal Processing]]
- [[Continuous-Time Fourier Transform]]
- [[Markov Matrices and Fourier Series]]（线性代数视角：正交基上的投影）
