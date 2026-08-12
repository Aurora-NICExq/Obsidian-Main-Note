---
title: "Filtering"
aliases:
  - "滤波"
  - "理想滤波器"
  - "频率响应"
  - "低通高通带通"
tags: [signals_and_systems, ee, filter]
up: "[[Signals and Systems MOC]]"
related:
  - "[[Fourier Transform Properties]]"
  - "[[Discrete-Time Fourier Transform]]"
  - "[[Butterworth Filters]]"
  - "[[Convolution]]"
---
# Filtering

> [!summary] 核心结论
> 滤波 = 用 $H(j\omega)$ 逐点乘输入频谱。这是 [[Fourier Transform Properties#5. 卷积性质|卷积性质]] 的直接兑现。
> **理想滤波器不可实现**：矩形频率响应对应 sinc 冲激响应，它非因果（$t<0$ 就有响应）且不绝对可积（不 BIBO 稳定）。
> 所以实际滤波器只能在**通带纹波 / 阻带衰减 / 过渡带宽度**三者之间折中 —— 巴特沃斯、切比雪夫、椭圆就是三种不同的折中点。

依据：奥本海姆 MIT OCW RES.6-007 [Lecture 12](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-12-filtering/)；教材 §3.9–3.11、§6.

前置：[[Fourier Transform Properties]]、[[Convolution]]。

---

## 1. 频率响应就是设计对象

对 LTI 系统，

$$
Y(j\omega)=H(j\omega)X(j\omega)
$$

于是「设计一个系统」就变成「画一条曲线 $H(j\omega)$」。这是傅里叶方法最大的实用价值。

$H(j\omega)$ 一般是复数，拆成两部分：

- $|H(j\omega)|$ —— **幅度响应**，决定各频率成分被放大还是压制。
- $\angle H(j\omega)$ —— **相位响应**，决定各频率成分的延迟。

> [!note] 两者都重要，但常被忽视的是相位
> 幅度对了、相位乱了，波形照样面目全非。$\angle H=-\omega t_0$（线性相位）才等价于「纯延迟、不失真」。
> 音频里人耳对相位不敏感，所以可以只管幅度；但在数据通信、图像、雷达里相位失真是致命的。

---

## 2. 四种理想滤波器

![[ss-filtering-01.svg]]

| 类型 | 通带 |
| ---- | ---- |
| 低通 LP | $\lvert\omega\rvert<\omega_c$ |
| 高通 HP | $\lvert\omega\rvert>\omega_c$ |
| 带通 BP | $\omega_1<\lvert\omega\rvert<\omega_2$ |
| 带阻 BS | 上面的补集 |

实值系统的 $H$ 满足共轭对称，所以通带总是关于 $\omega=0$ **成对**出现。画频谱时只需看右半边。

---

## 3. 为什么理想滤波器造不出来

理想低通 $H(j\omega)=1$（$|\omega|<\omega_c$）的冲激响应：

$$
h(t)=\frac{\sin(\omega_ct)}{\pi t}
$$

两条致命问题：

**(1) 非因果。** $h(t)$ 在 $t<0$ 处非零 —— 系统要在输入到达之前就开始响应。物理上不可能。

**(2) 不稳定。** $\int|h(t)|dt=\infty$（sinc 衰减只有 $1/t$），不满足 BIBO 条件。

离散情形一模一样：$h[n]=\sin(\Omega_cn)/(\pi n)$，双边无限长、不绝对可和。

> [!tip] 「近似因果」的实用出路
> 把 $h(t)$ 截断并右移一个足够大的 $t_0$，就得到一个因果、有限长的近似：$\hat h(t)=h(t-t_0)w(t)$。
> 代价是：截断在频域造成吉布斯型纹波（加窗可缓解），右移带来 $t_0$ 的延迟。
> 这就是 **FIR 滤波器窗函数设计法**的全部思路，也是为什么 FIR 滤波器天然有群延迟。

---

## 4. 实际滤波器的指标

既然做不到矩形，就得说清楚「差多少可以接受」。四个参数：

$$
1-\delta_p\le|H(j\omega)|\le1+\delta_p \quad(\text{通带 }|\omega|\le\omega_p)
$$
$$
|H(j\omega)|\le\delta_s \quad(\text{阻带 }|\omega|\ge\omega_s)
$$

- $\delta_p$：通带纹波
- $\delta_s$：阻带衰减
- $\omega_p\to\omega_s$：过渡带宽度
- 阶数 $N$：实现复杂度

**四者互相牵制**：指标定死三个，第四个就被决定了。滤波器设计的全部工作就是在这个约束下找一个可实现的 $H$。

| 家族 | 通带 | 阻带 | 过渡带 | 相位 |
| ---- | ---- | ---- | ---- | ---- |
| 巴特沃斯 | 最大平坦，无纹波 | 单调 | 最宽 | 较好 |
| 切比雪夫 I | 等纹波 | 单调 | 中 | 差 |
| 切比雪夫 II | 单调 | 等纹波 | 中 | 差 |
| 椭圆 | 等纹波 | 等纹波 | **最窄** | 最差 |
| FIR 线性相位 | 可等纹波 | 可等纹波 | 宽（阶数换） | **严格线性** |

前四种见 [[Butterworth Filters]] 及其后续。

---

## 5. 一阶 RC 电路：一个真实的低通

$$
H(j\omega)=\frac{1}{1+j\omega RC}
\qquad
|H|=\frac{1}{\sqrt{1+(\omega RC)^2}}
$$

- 截止频率（$-3\,\mathrm{dB}$ 点）：$\omega_c=1/RC$
- 高频滚降：$-20\,\mathrm{dB/dec}$
- 冲激响应：$h(t)=\frac{1}{RC}e^{-t/RC}u(t)$ —— **因果、绝对可积**，完全可实现

代价当然是：过渡带极宽，阻带衰减极慢。想陡就得提高阶数（级联更多极点），这就通往巴特沃斯。

时域看，$\tau=RC$ 既是上升时间的尺度又是带宽的倒数：

$$
t_r \cdot BW \approx \text{常数}
$$

又一次是 [[Fourier Transform Properties#3. 尺度变换：时宽与带宽的倒数关系|时宽-带宽]] 那条约束。

---

## 6. 离散时间滤波

结构完全平行，$H(e^{j\Omega})$ 以 $2\pi$ 为周期（见 [[Discrete-Time Fourier Transform]]）。两条实用差别：

- **「低通」指的是 $\Omega$ 靠近 0 或 $2\pi$ 的部分**，「高通」指靠近 $\pi$ 的部分。
- 一阶递归滤波器 $y[n]=ay[n-1]+(1-a)x[n]$ 是最常用的数字低通（指数平滑），$a$ 越接近 1 截止频率越低。

FIR 与 IIR 的分野：

| | FIR | IIR |
| ---- | ---- | ---- |
| $h[n]$ | 有限长 | 无限长 |
| 结构 | 只有前馈 | 有反馈 |
| 稳定性 | **恒稳定** | 需检查极点 |
| 线性相位 | 容易（对称即可） | 做不到 |
| 同样指标的阶数 | 高 | 低 |

---

## 7. 速查

| 项目 | 内容 |
| ---- | ---- |
| 滤波本质 | $Y=HX$（时域 $y=h*x$） |
| 理想 LP 的 $h$ | $\sin(\omega_ct)/(\pi t)$ —— 非因果、不稳定 |
| 不可实现的两个理由 | $h(t)\neq0$ 对 $t<0$；$\int\lvert h\rvert=\infty$ |
| 实际指标 | $\delta_p$、$\delta_s$、过渡带、阶数（四者互相牵制） |
| 线性相位 | $\angle H=-\omega t_0$ $\Leftrightarrow$ 纯延迟不失真 |
| 一阶 RC | $\omega_c=1/RC$，$-20\,\mathrm{dB/dec}$ |

---

## 参见

- [[Signals and Systems MOC]]
- [[Fourier Transform Properties]]（卷积性质是滤波的理论基础）
- [[Discrete-Time Fourier Transform]]（DT 滤波器的频率轴）
- [[Butterworth Filters]]（第一个具体的逼近方案）
- [[Mapping Continuous-Time Filters to Discrete-Time Filters]]（把模拟设计搬到数字）
- [OCW Lecture 12 notes (PDF)](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec12/)
