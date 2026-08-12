---
title: "Feedback Example - The Inverted Pendulum"
aliases:
  - "倒立摆"
  - "反馈镇定"
  - "Inverted Pendulum"
  - "PD 控制"
tags: [signals_and_systems, ee, feedback, control]
up: "[[Signals and Systems MOC]]"
related:
  - "[[Feedback]]"
  - "[[The Laplace Transform]]"
  - "[[Continuous-Time Second-Order Systems]]"
---
# Feedback Example - The Inverted Pendulum

> [!summary] 核心结论
> 倒立摆的开环传递函数有一个**右半平面极点** $s=+\sqrt{g/L}$ —— 本质不稳定，放手就倒。
> 纯比例反馈只能把极点推到虚轴上（等幅摆动，仍不能用）；必须再引入**角速度**反馈（微分项）才能提供阻尼，把极点拉进左半平面。
> 这是全课的收尾例子，也是反馈最有说服力的一处：**反馈能让一个本来不稳定的对象变稳定。** 反过来同样成立 —— 同一个分母 $1+GH$ 两面都管。

依据：奥本海姆 MIT OCW RES.6-007 [Lecture 26](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-26-feedback-example-the-inverted-pendulum/)；教材 §11.3。

前置：[[Feedback]]、[[The Laplace Transform]]。

---

## 1. 对象：一个天生不稳定的系统

![[ss-feedback-example-the-inverted-pendulum-01.svg]]

长为 $L$ 的杆铰接在可移动小车上，倒立。小角度线性化后：

$$
\ddot\theta-\frac{g}{L}\theta=-\frac{1}{L}\ddot{s}
$$

其中 $\theta$ 是与竖直方向的夹角，$s$ 是小车位置。取变换（初始松弛）：

$$
H(s)=\frac{\Theta(s)}{F(s)}=\frac{-1/L}{s^2-g/L}
$$

极点：

$$
s=\pm\sqrt{\frac{g}{L}}
$$

> [!warning] 注意那个正号
> 是 $s^2-g/L$ 而不是 $s^2+g/L$。**极点在右半平面**，对应时域里的 $e^{+\sqrt{g/L}\,t}$ —— 任何微小偏离都指数发散。
> 这和普通单摆（$\ddot\theta+\frac{g}{L}\theta=0$，极点在虚轴上、等幅摆动）只差一个符号，但行为天差地别。

$L=1\,\mathrm{m}$ 时 $\sqrt{g/L}\approx3.13\,\mathrm{s^{-1}}$，时间常数约 $0.32\,\mathrm{s}$ —— 偏离每 $0.22\,\mathrm{s}$ 翻一倍。人用手指顶扫帚能做到，是因为人眼-手回路的延迟刚好够快。

---

## 2. 纯比例反馈：不够

用力正比于角度：$f=-K\theta$。闭环特征方程：

$$
1+\frac{K/L}{s^2-g/L}=0
\quad\Longrightarrow\quad
s^2+\frac{K-g}{L}=0
$$

- $K<g$：$s^2=$ 正数 $\Rightarrow$ 仍有右半平面极点，还是倒。
- $K>g$：$s^2=$ 负数 $\Rightarrow$ 极点变成**纯虚数** $\pm j\sqrt{(K-g)/L}$。

$K>g$ 时极点确实从实轴移到了虚轴 —— 不再发散了，但也**不收敛**：摆会等幅振荡下去，永远停不下来。

这在 [[Continuous-Time Second-Order Systems]] 的语言里就是 $\zeta=0$：无阻尼。系统临界稳定，BIBO 意义下仍然不稳定。

> [!note] 为什么比例项做不到
> 比例反馈只提供**恢复力**（像弹簧），不提供**耗散**。能量没有出口，只在动能和势能之间来回倒。
> 要让它停下来，反馈必须包含一个与**速度**反向的分量。

---

## 3. 加微分项：PD 控制

$$
f=-K_p\theta-K_d\dot\theta
$$

闭环特征方程变成

$$
s^2+\frac{K_d}{L}s+\frac{K_p-g}{L}=0
$$

对照 [[Continuous-Time Second-Order Systems|标准二阶形式]]：

$$
\omega_n=\sqrt{\frac{K_p-g}{L}},
\qquad
2\zeta\omega_n=\frac{K_d}{L}
$$

现在两个增益各管一件事：

| 增益 | 作用 |
| ---- | ---- |
| $K_p$ | 必须 $>g$ 才能把极点从实轴拉走；再决定 $\omega_n$（响应快慢） |
| $K_d$ | 提供**阻尼** $\zeta$，把极点从虚轴推进左半平面 |

只要 $K_p>g$ 且 $K_d>0$，两个闭环极点就都在左半平面 —— **系统稳定了**。

再按 $\zeta\approx0.7$ 选 $K_d$ 就能得到超调小、收敛快的响应。

---

## 4. 这个例子说明了什么

**(1) 反馈能改变系统的本质属性。**
开环不稳定 $\to$ 闭环稳定。这是开环控制绝对做不到的事 —— 无论怎么精心设计输入波形，一个发散的对象都会发散。

**(2) 反馈的信息必须够。**
只测角度不够，还得知道角速度。实际系统里要么加陀螺仪，要么对角度做（带滤波的）微分。「测什么」和「反馈什么」是控制设计的第一个决策。

**(3) 极点配置是设计语言。**
「选 $K_p, K_d$」等价于「把闭环极点放到 $s$ 平面的哪个位置」。这是现代控制理论的起点。

**(4) 同一个机制两面都管。**
$1+GH$ 能把右半平面极点拉进来，也能把左半平面极点推出去。[[Feedback|上一讲]] 讲的稳定裕度就是防后者。

---

## 5. 现实中被略过的东西

线性化模型很干净，真实系统还有：

- **大角度非线性**：$\sin\theta\approx\theta$ 只在小角度成立，倒得太多就救不回来了（吸引域有限）。
- **执行器饱和**：小车加速度有上限，$f$ 不能无限大。
- **传感器噪声**：微分放大高频噪声（见 [[Systems Represented by Differential and Difference Equations#3. 方框图实现|为什么用积分器不用微分器]]），实际用带限微分或状态观测器。
- **延迟**：计算和通信延迟带来额外相位滞后，直接吃掉相位裕度。
- **小车位置本身也要控**：上面只稳住了 $\theta$，小车可能一路跑掉。完整设计是双回路的。

---

## 6. 速查

| 项目 | 内容 |
| ---- | ---- |
| 线性化模型 | $\ddot\theta-\frac{g}{L}\theta=-\frac{1}{L}\ddot s$ |
| 开环 $H(s)$ | $\dfrac{-1/L}{s^2-g/L}$ |
| 开环极点 | $\pm\sqrt{g/L}$ —— **一个在右半平面** |
| 纯比例 $K_p>g$ | 极点到虚轴，等幅振荡（$\zeta=0$） |
| PD 控制 | $\omega_n=\sqrt{(K_p-g)/L}$，$2\zeta\omega_n=K_d/L$ |
| 稳定条件 | $K_p>g$ 且 $K_d>0$ |

---

## 参见

- [[Signals and Systems MOC]]
- [[Feedback]]（闭环公式与稳定裕度）
- [[The Laplace Transform]]（右半平面极点意味着什么）
- [[Continuous-Time Second-Order Systems]]（$\zeta$、$\omega_n$ 与极点位置）
- [OCW Lecture 26 notes (PDF)](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec26/)
