---
title: "Signals and Systems MOC"
aliases: ["Signals and Systems", "信号与系统 MOC", "信号与系统", "奥本海姆"]
tags: [signals_and_systems, ee, moc]
down: ["[[Sinusoidal and Exponential Signals]]", "[[Unit Step and Unit Impulse Signals]]", "[[System Interconnection and Basic Properties]]", "[[Convolution]]", "[[Analog and Digital Signal Processing]]", "[[Systems Represented by Differential and Difference Equations]]", "[[Continuous-Time Fourier Series]]", "[[Continuous-Time Fourier Transform]]", "[[Fourier Transform Properties]]", "[[Discrete-Time Fourier Series]]", "[[Discrete-Time Fourier Transform]]", "[[Filtering]]", "[[Continuous-Time Modulation]]", "[[Discrete-Time Modulation]]", "[[Sampling]]", "[[Interpolation]]", "[[Discrete-Time Processing of Continuous-Time Signals]]", "[[Discrete-Time Sampling]]", "[[The Laplace Transform]]", "[[Continuous-Time Second-Order Systems]]", "[[The z-Transform]]", "[[Mapping Continuous-Time Filters to Discrete-Time Filters]]", "[[Butterworth Filters]]", "[[Feedback]]", "[[Feedback Example - The Inverted Pendulum]]"]
related: ["[[Basic Circuit Theory MOC]]", "[[Electronic Circuits I MOC]]", "[[Differential Equations and the Number e]]", "[[Signals Systems and Inference (MIT 6.011) MOC]]"]
---
# Signals and Systems MOC

MIT · Alan V. Oppenheim《Signals and Systems》（[OCW RES.6-007](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/)）的学习笔记，对应 26 讲，共 25 篇。

---

## 一 · 信号与系统基础（L1–L6） → `01 Signals and Systems/`

- [[Sinusoidal and Exponential Signals]]：正弦与复指数、连续/离散的周期性差别
- [[Unit Step and Unit Impulse Signals]]：$u$ 与 $\delta$、筛选性质、二者的微积分关系
- [[System Interconnection and Basic Properties]]：串/并联、线性、时不变、因果、稳定、记忆
- [[Convolution]]：脉冲分解、卷积和与卷积积分、flip–slide–sum
- [[Analog and Digital Signal Processing]]：用 $h$ 判无记忆/因果/BIBO、积分器与累加器、逆系统
- [[Systems Represented by Differential and Difference Equations]]：LCCDE、初始松弛、积分器/延迟器实现、IIR 的由来

## 二 · 傅里叶分析（L7–L12） → `02 Fourier Analysis/`

- [[Continuous-Time Fourier Series]]：谐波复指数、$a_k$、奇方波、吉布斯与收敛
- [[Continuous-Time Fourier Transform]]：包络采样、$T_0\to\infty$ 得 CTFT、波特图例
- [[Fourier Transform Properties]]：卷积/相乘/尺度/时移、对偶性、帕塞瓦尔
- [[Discrete-Time Fourier Series]]：只有 $N$ 个谐波、有限和、无收敛性问题
- [[Discrete-Time Fourier Transform]]：$2\pi$ 周期性、Dirichlet 核、**四种傅里叶表示全景**
- [[Filtering]]：理想 LP/HP/BP、理想滤波器为何不可实现、实际指标的四方牵制

## 三 · 调制与采样（L13–L19） → `03 Modulation and Sampling/`

- [[Continuous-Time Modulation]]：频谱搬移、同步解调与相位失配、带载波 AM、频分复用
- [[Discrete-Time Modulation]]：同样的搬移 + $2\pi$ 的硬约束、复调制与 I/Q
- [[Sampling]]：冲激串采样 $\Rightarrow$ 频谱周期复制、**采样定理**、混叠与防混叠
- [[Interpolation]]：sinc 内插、零阶保持的下垂与泄漏、过采样
- [[Discrete-Time Processing of Continuous-Time Signals]]：C/D–$H(e^{j\Omega})$–D/C 的等效连续系统、频率归一化
- [[Discrete-Time Sampling]]：抽取与内插、多相实现、有理倍率采样率转换

## 四 · 拉普拉斯与 z 变换（L20–L24） → `04 Laplace and z-Transform/`

- [[The Laplace Transform]]：ROC、极点零点、**稳定 $\Leftrightarrow$ ROC 含 $j\omega$ 轴**
- [[Continuous-Time Second-Order Systems]]：$\zeta$ 与 $\omega_n$、极点位置的几何读法、$Q$
- [[The z-Transform]]：ROC 是圆环、单位圆、$s\to z$ 映射、**稳定 $\Leftrightarrow$ 极点在单位圆内**
- [[Mapping Continuous-Time Filters to Discrete-Time Filters]]：冲激不变法 vs 双线性变换、频率翘曲与预畸变
- [[Butterworth Filters]]：最大平坦、极点半圆分布、四大家族对照

## 五 · 反馈（L25–L26） → `05 Feedback/`

- [[Feedback]]：$\dfrac{G}{1+GH}$、灵敏度 $1/(1+T)$、增益带宽积、相位裕度
- [[Feedback Example - The Inverted Pendulum]]：右半平面极点、比例不够、PD 镇定

---

## 贯穿全课的三条主线

1. **复指数是 LTI 系统的特征函数。** $e^{st}$ 进去出来还是 $H(s)e^{st}$。这一条撑起了全部四种傅里叶表示、拉普拉斯和 z 变换 —— 它们只是「把信号拆成复指数」的不同版本。
2. **一个域离散 $\Leftrightarrow$ 另一个域周期。** 采样定理、频谱周期复制、DTFT 的 $2\pi$ 周期、循环卷积，全是这条对偶律的不同侧面（见 [[Discrete-Time Fourier Transform#7. 四种傅里叶表示的全景|全景表]]）。
3. **时域卷积 $\Leftrightarrow$ 频域相乘。** 滤波、调制、采样三大应用都是它（或它的对偶）的直接兑现。

---

## 相关

- [[Basic Circuit Theory MOC]]：电路中的指数衰减与正弦振荡、RC/RLC 瞬态
- [[Electronic Circuits I MOC]]：把这些系统真正用晶体管做出来
- [[Differential Equations and the Number e]]：实指数与虚指数
- [[Signals Systems and Inference (MIT 6.011) MOC]]：S&S 后续——状态空间、估计、WSS/PSD、Wiener 与检测（MIT 6.011）

---

## 插图（预生成 SVG）

全部插图存放在 `90 Assets/diagrams/signals-and-systems/`，以 `![[ss-….svg]]` 嵌入。两套生成器并存：

| 生成器 | 覆盖 | 依赖 |
| ---- | ---- | ---- |
| `generate_all.py` | 原有 20 张 `ss-<topic>.svg` | matplotlib（需 venv） |
| `generate_tikz.py` | 新增 18 张 `ss-<note-slug>-NN.svg` | 本机 TeX Live，**全离线** |

重新生成（TikZ 那套，无需任何安装）：

```bash
cd "90 Assets/scripts/signals_and_systems" && python3 generate_tikz.py
```
