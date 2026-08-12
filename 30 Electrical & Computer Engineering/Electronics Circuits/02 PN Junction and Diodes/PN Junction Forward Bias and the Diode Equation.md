---
title: "PN Junction Forward Bias and the Diode Equation"
aliases: ["PN 结正偏", "二极管方程", "少子注入", "肖克利方程"]
tags: [electronic_circuits, ee, pn_junction, diode]
up: "[[Electronic Circuits I MOC]]"
down: ["[[Diode Models and Small-Signal Resistance]]"]
related: ["[[PN Junction in Equilibrium & Reverse Bias]]", "[[Caltech Analog Circuit Design-104N-PN Junction Depletion and Diode Equation]]"]
---
# PN Junction Forward Bias and the Diode Equation

## PN 结（二）：正偏、少子注入与二极管方程

> [!summary] 核心结论
> 正偏把势垒从 $V_0$ 降到 $V_0-V_F$，边界少子浓度按 $e^{V_F/V_T}$ 抬高，扩散流随之指数增长：
> $$I_D=I_S\left(e^{V_D/V_T}-1\right)$$
> 这条指数关系是整门课的核心。它的最实用推论是：**电流每变 10 倍，$V_D$ 只变约 $60\,\mathrm{mV}$** —— 这既解释了「导通压降 $0.7\,\mathrm{V}$」为何在极宽电流范围内都够用，也是后面 $g_m=I_C/V_T$ 的来源。

---
## 1. 正偏做了什么

外加正向电压 $V_F$（$p$ 侧接正）与内建电势反向，势垒降到 $V_0-V_F$。势垒是指数地压制扩散流的，所以势垒降一点，扩散流涨很多。

结果是**少子注入**：大量电子从 $n$ 区越过结进入 $p$ 区，大量空穴反向进入 $n$ 区。

![[ec-pn-junction-forward-bias-and-the-diode-equation-01.svg]]

边界处的少子浓度被抬高到：

$$
p_n(x_n) = p_{n0}\,e^{V_F/V_T},\qquad
n_p(-x_p) = n_{p0}\,e^{V_F/V_T}
$$

这就是**边界条件定律**（law of the junction）。注意这里的指数正是玻尔兹曼因子——势垒降低 $V_F$，能越过去的载流子数就多 $e^{V_F/V_T}$ 倍。

注入进去的超量少子一边向内扩散、一边与多子复合，浓度按扩散长度 $L$ 指数衰减。梯度即扩散流，扩散流即二极管电流。

> [!important] 为什么少子这么关键
> $p_{n0}=n_i^2/N_D$ 小到 $10^4\,\mathrm{cm^{-3}}$ 量级。乘上 $e^{0.7/0.026}\approx 5\times10^{11}$ 后，注入浓度可以逼近甚至超过 $10^{15}$ —— **相对变化有十几个数量级**。多子浓度则几乎纹丝不动。所以「PN 结是少子器件」不是修辞，而是定量事实。

---
## 2. 二极管方程

把两侧的扩散流加起来：

$$
\boxed{\;I_D = I_S\left(e^{V_D/V_T} - 1\right)\;}
$$

其中反向饱和电流

$$
I_S = qA n_i^2\left(\frac{D_n}{L_nN_A} + \frac{D_p}{L_pN_D}\right)
$$

三点值得留意：

1. $I_S \propto n_i^2$，而 $n_i^2$ 对温度极其敏感 —— $I_S$ 大约每升温 $5\,^\circ\mathrm{C}$ 翻一倍。
2. $I_S \propto A$（结面积）。大功率二极管的 $I_S$ 大，同电流下压降更低。
3. $I_S$ 典型值 $10^{-15}\sim10^{-14}\,\mathrm{A}$，所以要达到 mA 电流，指数因子必须到 $10^{11}$ 量级，对应 $V_D\approx0.7\,\mathrm{V}$。

---
## 3. 完整 I–V 曲线

![[ec-pn-junction-forward-bias-and-the-diode-equation-02.svg]]

三个区域：

- **正偏**（$V_D \gtrsim 0.1\,\mathrm{V}$）：$-1$ 项可忽略，$I_D\approx I_Se^{V_D/V_T}$。
- **反偏**：指数项趋于 0，$I_D\approx -I_S$，几乎与电压无关（故名「饱和」）。
- **击穿**（$V_D<-V_{BR}$）：雪崩或齐纳击穿，电流急剧上升。普通二极管应避免；齐纳二极管则专门工作在这里（见 [[Zener Regulators, Limiters and Voltage Doublers]]）。

---
## 4. 60 mV/decade：这门课最有用的一条数字

从 $I_D=I_Se^{V_D/V_T}$ 出发，电流变化 10 倍所需的电压变化：

$$
\Delta V_D = V_T\ln 10 = 0.026\times 2.303 \approx 60\,\mathrm{mV}
$$

这条规律的实际后果：

| 电流 | 近似 $V_D$ |
|---|---|
| $1\,\mathrm{\mu A}$ | $0.52\,\mathrm{V}$ |
| $10\,\mathrm{\mu A}$ | $0.58\,\mathrm{V}$ |
| $100\,\mathrm{\mu A}$ | $0.64\,\mathrm{V}$ |
| $1\,\mathrm{mA}$ | $0.70\,\mathrm{V}$ |
| $10\,\mathrm{mA}$ | $0.76\,\mathrm{V}$ |

跨越 4 个数量级，压降只变 $0.24\,\mathrm{V}$。这就是「恒压降模型」为什么这么好用。

反过来说，这条铁律也是限制：MOS 的亚阈值摆幅同样受 $60\,\mathrm{mV/dec}$ 约束，这是低功耗数字电路降电压的物理下限。

---
## 5. 温度效应

固定电流下，$V_D$ 随温度**下降**约 $-2\,\mathrm{mV/^\circ C}$。

这看起来矛盾（$I_S$ 涨得那么快，$V_D$ 应该降？）——正是如此：温度升高时 $I_S$ 暴涨，为维持同一个 $I_D$，$V_D$ 必须降下来。这个 $-2\,\mathrm{mV/^\circ C}$ 是带隙基准（bandgap reference）的核心机制之一，也是偏置电路必须考虑温漂的原因。

---
## 6. 与其他笔记的关系

- 上一讲建立了 $V_0$ 和耗尽区：[[PN Junction in Equilibrium & Reverse Bias]]。
- 下一讲把这条指数曲线简化成可手算的模型：[[Diode Models and Small-Signal Resistance]]。
- 同一条指数在 BJT 里换了个名字：[[Bipolar Transistor Structure and Operation]]。
