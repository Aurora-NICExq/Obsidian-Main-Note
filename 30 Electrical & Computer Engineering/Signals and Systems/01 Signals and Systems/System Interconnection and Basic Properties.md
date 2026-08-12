---
title: "系统互联与基本属性"
aliases: ["System Interconnections and Properties", "系统属性"]
tags: [signals_and_systems, ee]
up: "[[Signals and Systems MOC]]"
related: ["[[Unit Step and Unit Impulse Signals]]", "[[Sinusoidal and Exponential Signals]]", "[[Convolution]]", "[[Analog and Digital Signal Processing]]"]
---
# 系统互联与基本属性

> [!summary] 核心结论
> 系统是把输入信号映射为输出信号的变换。串联、并联是基本互联方式。无记忆、稳定性、时不变、线性等属性各自独立，需分别检验；后两者合称 LTI，是卷积表示的前提。

---
## 1. 一般系统

系统：从输入信号到输出信号的一种转换。常用方框表示：

![[ss-system-box.svg]]

连续时间与离散时间写法相同，只是信号记为 $x(t),y(t)$ 或 $x[n],y[n]$。

---
## 2. 系统互联

### 2.1 串联（级联）

输出依次经过多个系统：$x\to\mathrm{Sys}_1\to\mathrm{Sys}_2\to y$。
一般不可交换顺序；若两者都是 LTI，则卷积核满足 $h=h_1*h_2=h_2*h_1$，级联可交换。

### 2.2 并联

同一输入送入两个系统，输出相加：

![[ss-system-parallel.svg]]

其中 $x_1=x_2=x$，$y=y_1+y_2$。对 LTI，总冲激响应 $h=h_1+h_2$。

---
## 3. 若干基本属性

### 3.1 无记忆

任意时刻的输出只依赖该时刻的输入，不依赖过去或未来。

例：电阻 $y(t)=Rx(t)$ 无记忆；含电容/电感的电路有记忆。

### 3.2 恒等系统

输出等于输入：$y(t)=x(t)$（或 $y[n]=x[n]$）。它是无记忆、稳定、线性、时不变的。

### 3.3 积分器

$$
y(t)=\int_{-\infty}^{t}x(\tau)\,d\tau
$$

有记忆；是线性、时不变的。

> [!attention] 积分器与 BIBO 稳定性
> 有界输入–有界输出（BIBO）稳定性要求：凡有界输入都产生有界输出。
> 对积分器，取 $x(t)=u(t)$（有界），则 $y(t)=t\,u(t)$ 随 $t\to\infty$ 无界，故积分器不是 BIBO 稳定的。

### 3.4 离散时间累加器（对偶）

$$
y[n]=\sum_{k=-\infty}^{n}x[k]
$$

与连续积分器类似：线性、时不变、有记忆，但不是 BIBO 稳定。

---
## 4. 示例

### 4.1 滑动平均（离散）

例如三点滑动平均：
$$
y[n]=\frac{1}{3}\big(x[n-1]+x[n]+x[n+1]\big)
$$

- 有记忆（用到邻点）
- 线性、时不变
- BIBO 稳定（输出幅度不超过输入幅度上界）

（若窗口只含当前与过去样点，则还是因果的；上式用了 $x[n+1]$，非因果。）

### 4.2 时变乘法器

$$
y(t)=(\sin t)\,x(t)
$$

检验时不变性：输入 $x(t)$ 得 $y(t)=(\sin t)x(t)$；输入 $x(t-t_0)$ 得
$$
(\sin t)\,x(t-t_0)
$$
而 $y(t-t_0)=(\sin(t-t_0))x(t-t_0)$。二者一般不等，故系统时变。

它仍是线性的（对 $x$ 齐次且可加），因此是线性时变系统。

### 4.3 属性对照（速查）

| 系统 | 无记忆 | 线性 | 时不变 | BIBO 稳定 |
| --- | --- | --- | --- | --- |
| 恒等 $y=x$ | 是 | 是 | 是 | 是 |
| 积分器 | 否 | 是 | 是 | 否 |
| 滑动平均 | 否 | 是 | 是 | 是 |
| $y=(\sin t)x$ | 是 | 是 | 否 | 是 |

---
## 参见
- [[Signals and Systems MOC]]
- [[Unit Step and Unit Impulse Signals]]
- [[Sinusoidal and Exponential Signals]]
- [[Convolution]]
- [[Analog and Digital Signal Processing]]
