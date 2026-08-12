---
title: "Interpolation"
aliases:
  - "内插"
  - "重建"
  - "零阶保持"
  - "sinc 内插"
  - "ZOH"
tags: [signals_and_systems, ee, sampling]
up: "[[Signals and Systems MOC]]"
related:
  - "[[Sampling]]"
  - "[[Filtering]]"
  - "[[Discrete-Time Processing of Continuous-Time Signals]]"
---
# Interpolation

> [!summary] 核心结论
> 从样点重建连续信号 = 用某个 $h(t)$ 对冲激串做卷积。**内插核就是重建滤波器的冲激响应**。
> 理想内插核是 $\mathrm{sinc}$：它在本采样点处为 1、在其余所有采样点处为 0，因此重建曲线**精确穿过每个样本**。但它无限长、非因果。
> 实用的零阶保持（ZOH）代价是通带下垂 + 副本泄漏，标准补救是「ZOH + 模拟低通 + 数字端预加重」。

依据：奥本海姆 MIT OCW RES.6-007 [Lecture 17](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-17-interpolation/)；教材 §7.2。

前置：[[Sampling]]。

---

## 1. 内插 = 卷积

从 [[Sampling]] 得到的 $x_p(t)=\sum_nx(nT)\delta(t-nT)$ 送进一个 LTI 系统 $h(t)$：

$$
x_r(t)=x_p(t)*h(t)=\sum_{n}x(nT)\,h(t-nT)
$$

**每个样点放一个 $h$ 的副本，加起来就是重建结果。** 所以「选内插方式」就是「选 $h$」。

---

## 2. 理想带限内插

![[ss-interpolation-01.svg]]

理想低通（截止 $\omega_c=\omega_s/2$，增益 $T$）的冲激响应：

$$
h(t)=\frac{\sin(\pi t/T)}{\pi t/T}=\mathrm{sinc}(t/T)
$$

关键性质：

$$
h(0)=1,\qquad h(nT)=0\ (n\neq0)
$$

于是在每个采样时刻 $t=mT$，求和里只有 $n=m$ 那一项存活：

$$
x_r(mT)=x(mT)
$$

**重建曲线精确穿过每一个样本**，且在样本之间也严格等于原信号（前提是满足采样定理）。这就是采样定理的构造性证明：

$$
x(t)=\sum_{n=-\infty}^{\infty}x(nT)\,\frac{\sin\big(\pi(t-nT)/T\big)}{\pi(t-nT)/T}
$$

代价与 [[Filtering#3. 为什么理想滤波器造不出来|理想滤波器]] 完全一样：$h$ 双边无限长、非因果、衰减只有 $1/t$。

---

## 3. 零阶保持

最简单也最常用：

$$
h_0(t)=\begin{cases}1,&0\le t<T\\0,&\text{否则}\end{cases}
$$

输出是阶梯波形。频率响应：

$$
H_0(j\omega)=T\,e^{-j\omega T/2}\,\frac{\sin(\omega T/2)}{\omega T/2}
$$

两个问题：

1. **通带下垂**：$|H_0|$ 是 sinc 包络，在 $\omega_s/2$ 处衰减到 $2/\pi\approx0.64$（约 $-3.9\,\mathrm{dB}$）。高频被系统性地削弱。
2. **副本泄漏**：sinc 的旁瓣没有把 $\pm\omega_s$ 处的副本压干净，输出里残留镜像。

好处是极其便宜 —— 一个 DAC 的输出天然就是 ZOH。

### 标准补救

工程上三件事一起用：

- ZOH 之后接一级模拟低通（**重建滤波器 / 平滑滤波器**）压掉残留副本；
- 数字端做 $1/\mathrm{sinc}$ **预加重**，把通带下垂补回来；
- **过采样**：先数字内插把采样率抬高 $L$ 倍，副本被推得很远，模拟滤波器就可以做得很缓（CD 播放机的「$8\times$ 过采样」就是这个）。

---

## 4. 一阶保持（线性内插）

$$
h_1(t)=\begin{cases}1-|t|/T,&|t|<T\\0,&\text{否则}\end{cases}
$$

三角形核 = 两个矩形卷积，所以频响是 $\mathrm{sinc}^2$ —— 旁瓣衰减更快，副本压得更干净；代价是通带下垂更严重，且需要「知道下一个样点」（非因果，实现时延迟一拍）。

| 内插核 | $h(t)$ | $H(j\omega)$ | 旁瓣 | 因果 |
| ---- | ---- | ---- | ---- | ---- |
| 理想 | sinc | 矩形 | 无 | 否 |
| ZOH | 矩形 | sinc | $-13\,\mathrm{dB}$ | 是 |
| 一阶保持 | 三角 | $\mathrm{sinc}^2$ | $-26\,\mathrm{dB}$ | 否（延迟一拍即可） |

一般规律：**时域越平滑 $\Rightarrow$ 频域旁瓣越低 $\Rightarrow$ 副本压得越好**，但通带失真也越大。

---

## 5. 与数字内插（$\uparrow L$）的关系

上面讲的是「离散 $\to$ 连续」的重建。纯数字域里的内插（提高采样率）是同一件事的离散版本：

1. **零值填充** $\uparrow L$：每两个样点之间插 $L-1$ 个零。频域上把频率轴**压窄 $L$ 倍**，于是一个周期内出现 $L$ 份镜像。
2. **低通** 截止 $\pi/L$、增益 $L$：滤掉多余镜像，只留一份。

这个「$\uparrow L$ + 低通」就是数字内插器，与「$\downarrow M$」配对使用即得有理数倍采样率转换。详见 [[Discrete-Time Sampling]]。

---

## 6. 速查

| 项目 | 内容 |
| ---- | ---- |
| 内插 | $x_r(t)=\sum_nx(nT)h(t-nT)$ |
| 理想核 | $\mathrm{sinc}(t/T)$，$h(nT)=\delta[n]$ |
| 采样定理构造式 | $x(t)=\sum_nx(nT)\mathrm{sinc}\big((t-nT)/T\big)$ |
| ZOH | 矩形核；$H_0$ 为 sinc；$\omega_s/2$ 处 $-3.9\,\mathrm{dB}$ |
| ZOH 补救 | 模拟低通 + $1/\mathrm{sinc}$ 预加重 + 过采样 |
| 数字内插 | $\uparrow L$ 后低通（截止 $\pi/L$，增益 $L$） |

---

## 参见

- [[Signals and Systems MOC]]
- [[Sampling]]（内插是它的逆操作）
- [[Filtering]]（理想低通不可实现的同一组理由）
- [[Discrete-Time Sampling]]（纯数字域的内插与抽取）
- [[Discrete-Time Processing of Continuous-Time Signals]]（C/D 与 D/C 的完整链路）
- [OCW Lecture 17 notes (PDF)](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec17/)
