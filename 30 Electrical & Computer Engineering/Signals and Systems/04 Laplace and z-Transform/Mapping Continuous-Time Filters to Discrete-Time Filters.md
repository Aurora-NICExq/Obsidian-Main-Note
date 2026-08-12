---
title: "Mapping Continuous-Time Filters to Discrete-Time Filters"
aliases:
  - "模拟滤波器数字化"
  - "冲激不变法"
  - "双线性变换"
  - "频率翘曲"
  - "预畸变"
tags: [signals_and_systems, ee, filter, dsp]
up: "[[Signals and Systems MOC]]"
related:
  - "[[The z-Transform]]"
  - "[[Butterworth Filters]]"
  - "[[Filtering]]"
  - "[[Discrete-Time Processing of Continuous-Time Signals]]"
---
# Mapping Continuous-Time Filters to Discrete-Time Filters

> [!summary] 核心结论
> 模拟滤波器设计已经积累了上百年（巴特沃斯、切比雪夫、椭圆），数字 IIR 设计的主流做法就是**把现成的 $H_c(s)$ 搬过来**。两条路：
> **冲激不变法**保留冲激响应形状，但会**混叠** —— 只适用于本身已充分衰减的低通。
> **双线性变换** $s=\frac{2}{T}\frac{1-z^{-1}}{1+z^{-1}}$ 把整条 $j\omega$ 轴一对一压进单位圆，**绝不混叠**，代价是频率轴被非线性**翘曲**。配合**预畸变**即可保住关键频点，因此是实际的默认选择。

依据：奥本海姆 MIT OCW RES.6-007 [Lecture 23](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-23-mapping-continuous-time-filters-to-discrete-time-filters/)；教材 §7.4、§10。

前置：[[The z-Transform]]、[[Filtering]]。

---

## 1. 一个好的映射要满足什么

把 $H_c(s)$ 变成 $H(z)$，希望：

1. $j\omega$ 轴映到单位圆（这样频率响应才对得上）。
2. 左半平面映到单位圆内（**稳定映成稳定**）。
3. 有理式映成有理式（否则不可实现）。

冲激不变法满足 2、3 但破坏 1（多对一）；双线性变换三条全满足。

---

## 2. 冲激不变法

![[ss-mapping-continuous-time-filters-to-discrete-time-filters-01.svg]]

直接对模拟冲激响应采样：

$$
h[n]=T\,h_c(nT)
$$

由 [[Sampling|采样定理]] 的频域关系：

$$
H(e^{j\Omega})=\sum_{k=-\infty}^{\infty}H_c\left(j\frac{\Omega-2\pi k}{T}\right)
$$

**这就是频谱周期复制** —— 如果 $H_c$ 不是严格带限的（实际滤波器都不是），副本必然重叠。

后果：阻带里混进了折叠回来的成分，实际阻带衰减达不到设计值。

| 适用 | 不适用 |
| ---- | ---- |
| 低通、带通（且阻带衰减已经很深） | 高通、带阻（高频永远不衰减，必然严重混叠） |

好处：时域形状被保留（对需要匹配冲激/阶跃响应的场合有价值），且频率轴是线性的。

极点映射为 $s_k\to e^{s_kT}$，左半平面确实映进单位圆内 —— 稳定性保住了。

---

## 3. 双线性变换

$$
\boxed{\;s=\frac{2}{T}\cdot\frac{1-z^{-1}}{1+z^{-1}}
\qquad\Longleftrightarrow\qquad
z=\frac{1+sT/2}{1-sT/2}\;}
$$

代入 $s=j\omega$ 可以验证 $|z|=1$：整条虚轴恰好映到单位圆，**一对一**（不是多对一），所以**不可能混叠**。

同时 $\mathrm{Re}\{s\}<0$ 映到 $|z|<1$，稳定性保住。

### 频率翘曲

一对一是有代价的：无限长的 $\omega$ 轴要塞进有限长的单位圆，映射必然非线性。

$$
\boxed{\;\omega=\frac{2}{T}\tan\frac{\Omega}{2}\;}
$$

- $\Omega$ 小时 $\omega\approx\Omega/T$，近似线性。
- $\Omega\to\pi$ 时 $\omega\to\infty$ —— 整个高频段被压缩到 $\pi$ 附近。

这叫**频率翘曲（warping）**。后果：直接套用会让截止频率跑偏。

### 预畸变（pre-warping）

补救办法很直接：设计模拟原型时，把要保住的临界频率**先反算过去**：

$$
\omega_{\text{设计}}=\frac{2}{T}\tan\frac{\Omega_{\text{目标}}}{2}
$$

这样经过双线性变换后，它正好落回 $\Omega_{\text{目标}}$。

> [!important] 为什么翘曲基本无害
> 翘曲是**单调**的：通带还是通带，阻带还是阻带，各段的**幅度**指标（纹波、衰减）原样保留 —— 只是频率刻度被拉伸了。
> 预畸变把关键频点钉死之后，剩下的形变通常无关紧要。
>
> 被真正破坏的是**相位线性度**。所以需要严格线性相位时不用双线性变换（改用 FIR 设计）。

---

## 4. 完整设计流程

以数字巴特沃斯低通为例：

1. 给定数字指标：通带边界 $\Omega_p$、阻带边界 $\Omega_s$、纹波 $\delta_p$、衰减 $\delta_s$。
2. **预畸变**：$\omega_p=\frac{2}{T}\tan\frac{\Omega_p}{2}$，$\omega_s=\frac{2}{T}\tan\frac{\Omega_s}{2}$。
3. 用模拟公式定阶数 $N$ 和 $\omega_c$（见 [[Butterworth Filters]]）。
4. 写出模拟原型 $H_c(s)$（左半平面的 $N$ 个极点）。
5. **代入** $s=\frac{2}{T}\frac{1-z^{-1}}{1+z^{-1}}$，化简得 $H(z)$。
6. 分解成二阶节（biquad）级联实现 —— 直接型高阶结构对系数量化极其敏感。

---

## 5. 两种方法对照

| | 冲激不变法 | 双线性变换 |
| ---- | ---- | ---- |
| $j\omega\to$ 单位圆 | 多对一 | **一对一** |
| 混叠 | **有** | 无 |
| 频率轴 | 线性 | 非线性（翘曲） |
| 时域形状 | **保留** | 不保留 |
| 适用滤波器 | 低通、带通 | **全部** |
| 稳定性 | 保持 | 保持 |
| 实际使用 | 少 | **默认选择** |

---

## 6. 速查

| 项目 | 内容 |
| ---- | ---- |
| 冲激不变 | $h[n]=Th_c(nT)$；$s_k\to e^{s_kT}$；会混叠 |
| 双线性 | $s=\frac{2}{T}\frac{1-z^{-1}}{1+z^{-1}}$ |
| 翘曲关系 | $\omega=\frac{2}{T}\tan\frac{\Omega}{2}$ |
| 预畸变 | 设计前把目标 $\Omega$ 按上式换成 $\omega$ |
| 保住的 | 幅度指标、稳定性 |
| 牺牲的 | 相位线性度、时域波形 |

---

## 参见

- [[Signals and Systems MOC]]
- [[The z-Transform]]（$s$ 平面与 $z$ 平面的关系）
- [[Butterworth Filters]]（最常用的模拟原型）
- [[Filtering]]（滤波器指标的定义）
- [[Discrete-Time Processing of Continuous-Time Signals]]（数字滤波器怎么用起来）
- [OCW Lecture 23 notes (PDF)](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec23/)
