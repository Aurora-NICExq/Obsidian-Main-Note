---
title: "Systems Represented by Differential and Difference Equations"
aliases:
  - "微分方程与差分方程"
  - "LCCDE"
  - "递归实现"
  - "积分器与延迟器"
tags: [signals_and_systems, ee, lti]
up: "[[Signals and Systems MOC]]"
related:
  - "[[Convolution]]"
  - "[[System Interconnection and Basic Properties]]"
  - "[[The Laplace Transform]]"
  - "[[The z-Transform]]"
---
# Systems Represented by Differential and Difference Equations

> [!summary] 核心结论
> 常系数线性微分 / 差分方程（LCCDE）是描述 LTI 系统最常用的形式，但**方程本身不足以确定系统** —— 还必须附加辅助条件。取「初始松弛」（initial rest）时，得到的才是唯一的线性、时不变、因果系统。
> 实现上一律用**积分器**（连续）或**延迟器**（离散），不用微分器：微分器放大高频噪声，且理想微分器不可实现。

依据：奥本海姆 MIT OCW RES.6-007 [Lecture 6](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-6-systems-represented-by-differential-and-difference-equations/)；教材 §2.4。

前置：[[System Interconnection and Basic Properties|LTI 性质]]、[[Convolution|卷积]]。

---

## 1. 两类方程

**连续时间**（$N$ 阶常系数线性微分方程）：

$$
\sum_{k=0}^{N}a_k\frac{d^ky(t)}{dt^k}=\sum_{k=0}^{M}b_k\frac{d^kx(t)}{dt^k}
$$

**离散时间**（$N$ 阶常系数线性差分方程）：

$$
\sum_{k=0}^{N}a_k\,y[n-k]=\sum_{k=0}^{M}b_k\,x[n-k]
$$

两者结构完全平行。离散情形还有一个连续情形没有的好处：可以直接解出递归式

$$
y[n]=\frac{1}{a_0}\left(\sum_{k=0}^{M}b_kx[n-k]-\sum_{k=1}^{N}a_ky[n-k]\right)
$$

**给定初值就能一步步算下去** —— 这正是数字滤波器的实现方式。

---

## 2. 方程不等于系统

这一讲最重要的一点。考虑

$$
\frac{dy}{dt}+ay(t)=bx(t)
$$

它的通解是

$$
y(t)=\underbrace{y_p(t)}_{\text{特解}}+\underbrace{Ce^{-at}}_{\text{齐次解}}
$$

$C$ 是任意常数。**同一个方程对应无穷多个系统**，取决于怎么定 $C$。

要挑出「那个」LTI 因果系统，需要附加条件：

> [!important] 初始松弛（initial rest）
> 若 $x(t)=0$ 对所有 $t<t_0$，则 $y(t)=0$ 对所有 $t<t_0$。
>
> 离散情形同理：$x[n]=0$ 对 $n<n_0$ $\Rightarrow$ $y[n]=0$ 对 $n<n_0$。

加上这条之后：

| 附加条件 | 得到的系统 |
| ---- | ---- |
| 初始松弛 | **线性、时不变、因果**（唯一） |
| 固定非零初值 | 非线性（不满足零输入零输出）、时变 |
| 「终值松弛」 | 线性时不变但**反因果** |

注意「初始松弛」不是「初值为零」这么简单 —— 它是一族随输入起点滑动的条件，正是这个滑动性保证了时不变。

---

## 3. 方框图实现

![[ss-systems-represented-by-differential-and-difference-equations-01.svg]]

一阶情形的直接型实现：

- **连续**：一个积分器 + 一个反馈增益 $-a$ + 一个前馈增益 $b$。
- **离散**：一个延迟单元 $z^{-1}$ + 同样的两个增益。

> [!note] 为什么用积分器而不是微分器
> 三条理由，都很实在：
> 1. 微分器的频率响应 $H(j\omega)=j\omega$ 随频率无限增长 —— 高频噪声被放大到淹没信号。
> 2. 理想微分器不是 BIBO 稳定的。
> 3. 用运放搭积分器（RC 反馈）比搭微分器稳定得多。
>
> 离散情形对应的是「用延迟而不是差分」。

$N$ 阶系统就用 $N$ 个积分器 / 延迟器。所需的存储单元数就是**系统的阶数**，也就是状态变量的个数。

---

## 4. 冲激响应

一阶离散例子 $y[n]+ay[n-1]=bx[n]$，初始松弛，令 $x[n]=\delta[n]$：

$$
h[0]=b,\quad h[1]=-ab,\quad h[2]=a^2b,\ \dots
$$

$$
h[n]=b(-a)^n u[n]
$$

**有限个系数产生了无限长的冲激响应** —— 这就是 IIR（infinite impulse response）滤波器名字的来历。反馈路径（$a\neq0$）是无限长的根源；若 $N=0$（没有 $y$ 的历史项），$h$ 就是有限长的 FIR。

一阶连续例子 $\dot y+ay=bx$：

$$
h(t)=b\,e^{-at}u(t)
$$

BIBO 稳定要求 $a>0$（离散情形要求 $|a|<1$）。这个条件在 [[The Laplace Transform|拉普拉斯变换]] 和 [[The z-Transform|z 变换]] 里会变成「极点位置」的说法。

---

## 5. 与变换域的衔接

对方程两边做变换（假定初始松弛），微分 / 延迟都变成代数运算：

$$
\frac{d}{dt}\;\longrightarrow\;s,
\qquad
y[n-k]\;\longrightarrow\;z^{-k}Y(z)
$$

于是

$$
H(s)=\frac{\sum_k b_ks^k}{\sum_k a_ks^k},
\qquad
H(z)=\frac{\sum_k b_kz^{-k}}{\sum_k a_kz^{-k}}
$$

**系统函数是两个多项式的比** —— 分子的根是零点，分母的根是极点。整个后半门课（稳定性、频率响应、滤波器设计）都建立在这个有理形式上。

---

## 6. 速查

| 项目 | 连续 | 离散 |
| ---- | ---- | ---- |
| 方程 | $\sum a_k y^{(k)}=\sum b_k x^{(k)}$ | $\sum a_k y[n-k]=\sum b_k x[n-k]$ |
| 基本单元 | 积分器 | 延迟器 $z^{-1}$ |
| 唯一化条件 | 初始松弛 | 初始松弛 |
| 一阶冲激响应 | $be^{-at}u(t)$ | $b(-a)^nu[n]$ |
| 稳定条件 | $a>0$（极点在左半平面） | $\lvert a\rvert<1$（极点在单位圆内） |
| 系统函数 | $H(s)$ 有理式 | $H(z)$ 有理式 |

---

## 参见

- [[Signals and Systems MOC]]
- [[Convolution]]（由 $h$ 得到输出的另一条路）
- [[The Laplace Transform]]、[[The z-Transform]]（把方程变成代数）
- [[Continuous-Time Second-Order Systems]]（二阶 LCCDE 的完整讨论）
- [OCW Lecture 6 notes (PDF)](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec06/)
