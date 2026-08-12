---
title: "The z-Transform"
aliases:
  - "z 变换"
  - "单位圆"
  - "z 平面"
  - "离散系统函数"
tags: [signals_and_systems, ee, ztransform]
up: "[[Signals and Systems MOC]]"
related:
  - "[[The Laplace Transform]]"
  - "[[Discrete-Time Fourier Transform]]"
  - "[[Systems Represented by Differential and Difference Equations]]"
  - "[[Mapping Continuous-Time Filters to Discrete-Time Filters]]"
---
# The z-Transform

> [!summary] 核心结论
> $$X(z)=\sum_{n=-\infty}^{\infty}x[n]z^{-n}$$
> 对 DTFT 的推广，正如拉普拉斯之于 CTFT：把单位圆 $z=e^{j\Omega}$ 推广到整个复平面。
> ROC 是**圆环**（不是半平面）—— 收敛只取决于 $|z|$。右边序列 $\Rightarrow$ 最外极点**以外**；左边序列 $\Rightarrow$ 最内极点**以内**。
> 两条判据：**ROC 含单位圆 $\Leftrightarrow$ BIBO 稳定**；因果 + 稳定 $\Leftrightarrow$ **全部极点在单位圆内**。

依据：奥本海姆 MIT OCW RES.6-007 [Lecture 22](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-22-the-z-transform/)；教材 §10。

前置：[[Discrete-Time Fourier Transform]]、[[The Laplace Transform]]。

---

## 1. 定义与动机

DTFT 要求 $\sum|x[n]|<\infty$。同样的补救办法：先乘一个衰减因子 $r^{-n}$：

$$
\sum_n x[n]r^{-n}e^{-j\Omega n}=\sum_n x[n]\big(re^{j\Omega}\big)^{-n}
$$

令 $z=re^{j\Omega}$：

$$
\boxed{\;X(z)=\sum_{n=-\infty}^{\infty}x[n]\,z^{-n}\;}
$$

**DTFT 是 z 变换在单位圆上的取值**：

$$
X(e^{j\Omega})=X(z)\big|_{z=e^{j\Omega}}\quad(\text{当单位圆在 ROC 内时})
$$

---

## 2. ROC 是圆环

收敛与否只取决于 $|z|=r$，所以 ROC 总是以原点为中心的**圆环** $R_1<|z|<R_2$。

![[ss-the-z-transform-01.svg]]

| 序列类型 | ROC |
| ---- | ---- |
| 右边序列（$n<N_1$ 时为 0） | 最外极点**以外** $\lvert z\rvert>R_{\max}$ |
| 左边序列（$n>N_2$ 时为 0） | 最内极点**以内** $\lvert z\rvert<R_{\min}$ |
| 双边序列 | 圆环 $R_1<\lvert z\rvert<R_2$ |
| 有限长序列 | 整个 $z$ 平面（可能除 0 和/或 $\infty$） |

ROC 内不含极点。同一个 $X(z)$ 配不同 ROC 对应完全不同的序列 —— 与拉普拉斯完全同构的陷阱。

> [!example] 经典对照
> $$X(z)=\frac{1}{1-az^{-1}}$$
> - ROC $|z|>|a|$ $\Rightarrow$ $x[n]=a^nu[n]$（右边，因果）
> - ROC $|z|<|a|$ $\Rightarrow$ $x[n]=-a^nu[-n-1]$（左边，反因果）

---

## 3. $s$ 平面到 $z$ 平面的映射

同一张图的右半部分。采样把 $s$ 平面按 $z=e^{sT}$ 卷成 $z$ 平面：

| $s$ 平面 | $z$ 平面 |
| ---- | ---- |
| $j\omega$ 轴 | **单位圆** $\lvert z\rvert=1$ |
| 左半平面 $\mathrm{Re}\{s\}<0$ | **单位圆内** $\lvert z\rvert<1$ |
| 右半平面 | 单位圆外 |
| 原点 $s=0$ | $z=1$ |
| $s=\pm j\pi/T$（奈奎斯特） | $z=-1$ |

因为 $e^{sT}$ 对 $s$ 有 $j2\pi/T$ 的周期，$s$ 平面里每一条宽 $\omega_s$ 的水平带都映到整个 $z$ 平面 —— 这就是 DTFT $2\pi$ 周期性和混叠的几何来源。

于是所有判据都平移过来：

$$
\text{左半平面}\ \longrightarrow\ \text{单位圆内}
$$

---

## 4. 稳定性与因果性

$$
\boxed{\;\text{BIBO 稳定}\iff\text{ROC 包含单位圆}\;}
$$

$$
\boxed{\;\text{因果}\iff\text{ROC 是最外极点以外的区域（且 } X(z) \text{ 在 } z=\infty \text{ 处有限）}\;}
$$

$$
\text{因果 + 稳定}\iff\text{全部极点在单位圆内 } (|p_k|<1)
$$

对一阶 $h[n]=a^nu[n]$：极点在 $z=a$，稳定要求 $|a|<1$ —— 与 [[Systems Represented by Differential and Difference Equations|差分方程那一讲]] 直接给出的条件一致。

---

## 5. 有理系统函数

对 LCCDE $\sum a_ky[n-k]=\sum b_kx[n-k]$：

$$
H(z)=\frac{\sum_kb_kz^{-k}}{\sum_ka_kz^{-k}}
$$

FIR（$N=0$，无反馈）：分母是常数，**极点全在原点** $\Rightarrow$ 恒稳定。这是 FIR 滤波器最大的工程优势。

IIR：有非平凡极点，必须检查是否都在单位圆内。

---

## 6. 常用变换对

| $x[n]$ | $X(z)$ | ROC |
| ---- | ---- | ---- |
| $\delta[n]$ | $1$ | 全平面 |
| $u[n]$ | $\dfrac{1}{1-z^{-1}}$ | $\lvert z\rvert>1$ |
| $a^nu[n]$ | $\dfrac{1}{1-az^{-1}}$ | $\lvert z\rvert>\lvert a\rvert$ |
| $-a^nu[-n-1]$ | $\dfrac{1}{1-az^{-1}}$ | $\lvert z\rvert<\lvert a\rvert$ |
| $na^nu[n]$ | $\dfrac{az^{-1}}{(1-az^{-1})^2}$ | $\lvert z\rvert>\lvert a\rvert$ |
| $\delta[n-m]$ | $z^{-m}$ | 全平面（除 0 或 $\infty$） |

---

## 7. 性质

| 性质 | 时域 | $z$ 域 |
| ---- | ---- | ---- |
| 线性 | $ax_1+bx_2$ | $aX_1+bX_2$ |
| **时移** | $x[n-n_0]$ | $z^{-n_0}X(z)$ |
| $z$ 域尺度 | $a^nx[n]$ | $X(z/a)$ |
| 时间反转 | $x[-n]$ | $X(1/z)$ |
| **卷积** | $x*h$ | $XH$ |
| $z$ 域微分 | $nx[n]$ | $-z\dfrac{dX}{dz}$ |
| 初值（因果） | $x[0]$ | $\lim_{z\to\infty}X(z)$ |

**$z^{-1}$ 就是「延迟一拍」** —— 这就是为什么方框图里延迟单元直接标 $z^{-1}$（见 [[Systems Represented by Differential and Difference Equations]] 的实现图）。

---

## 8. 逆变换

三种常用方法：

1. **部分分式展开**：把 $H(z)$ 拆成一阶项之和，逐项查表。注意按 ROC 决定每项取右边还是左边形式。
2. **长除法**：直接展开成 $z^{-1}$ 的幂级数，系数就是 $h[n]$。适合快速看前几项。
3. **围道积分**（留数定理）：$x[n]=\frac{1}{2\pi j}\oint X(z)z^{n-1}dz$。理论上完备，手算少用。

---

## 9. 速查

| 项目 | 拉普拉斯 | z 变换 |
| ---- | ---- | ---- |
| 定义 | $\int x e^{-st}dt$ | $\sum x[n]z^{-n}$ |
| 对应的傅里叶 | $s=j\omega$（虚轴） | $z=e^{j\Omega}$（**单位圆**） |
| ROC 形状 | 半平面 / 带状 | **圆环** |
| 稳定 | ROC 含 $j\omega$ 轴 | ROC 含**单位圆** |
| 因果+稳定 | 极点在**左半平面** | 极点在**单位圆内** |
| 基本算子 | 微分 $\to s$ | 延迟 $\to z^{-1}$ |

---

## 参见

- [[Signals and Systems MOC]]
- [[Discrete-Time Fourier Transform]]（单位圆上的特例）
- [[The Laplace Transform]]（连续时间的对应物）
- [[Systems Represented by Differential and Difference Equations]]（有理 $H(z)$ 的来源）
- [[Mapping Continuous-Time Filters to Discrete-Time Filters]]（$s\to z$ 的具体做法）
- [OCW Lecture 22 notes (PDF)](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec22/)
