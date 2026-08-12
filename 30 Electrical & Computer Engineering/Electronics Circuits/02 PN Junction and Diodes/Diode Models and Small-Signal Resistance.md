---
title: "Diode Models and Small-Signal Resistance"
aliases: ["二极管模型", "恒压降模型", "小信号电阻", "理想二极管"]
tags: [electronic_circuits, ee, diode, small_signal]
up: "[[Electronic Circuits I MOC]]"
down: ["[[Half-Wave and Full-Wave Rectifiers]]"]
related: ["[[PN Junction Forward Bias and the Diode Equation]]", "[[BJT Small-Signal Model]]"]
---
# Diode Models and Small-Signal Resistance

## 二极管模型：理想、恒压降与小信号

> [!summary] 核心结论
> 同一个器件有三套模型，选哪个取决于你在问什么问题：判断通断用**理想开关**，算直流工作点用**恒压降**（$0.7\,\mathrm{V}$），算小信号增益用**小信号电阻** $r_d=V_T/I_D$。
> 这一讲第一次演示了本课的通用方法：**大信号定工作点，小信号取切线**。后面 BJT 和 MOS 完全照搬这套流程。

---
## 1. 为什么需要模型

精确方程 $I_D=I_S(e^{V_D/V_T}-1)$ 是超越方程，接一个电阻就解不出闭式：

$$
\frac{V_{DD}-V_D}{R} = I_Se^{V_D/V_T}
$$

工程上有两条路：迭代求数值解，或者换一个够用的近似模型。绝大多数手算走第二条。

---
## 2. 三种大信号模型

![[ec-diode-models-and-small-signal-resistance-01.svg]]

| 模型 | 导通时 | 截止时 | 适用场合 |
|---|---|---|---|
| 理想开关 | 短路（$V_D=0$） | 开路 | 判断哪个二极管导通、逻辑分析 |
| 恒压降 | $V_D=V_{D,on}\approx0.7\,\mathrm{V}$ | 开路 | 90% 的手算直流分析 |
| 指数 | $I_D=I_Se^{V_D/V_T}$ | 同左 | 需要精确工作点、或分析非线性时 |

**用法要点**：先假设一组通断状态，用假设解出电路，再回头验证假设自洽（导通支路电流为正、截止支路反偏）。不自洽就换一组假设重来。

### 迭代法（需要精度时）

$$
V_D^{(k+1)} = V_T\ln\frac{I_D^{(k)}}{I_S},\qquad
I_D^{(k+1)} = \frac{V_{DD}-V_D^{(k+1)}}{R}
$$

由于指数的强压缩性，通常两三轮就收敛到 mV 以内。

---
## 3. 小信号电阻

![[ec-diode-models-and-small-signal-resistance-02.svg]]

当二极管上叠加一个小的交流扰动时，工作点附近可以线性化：

$$
r_d = \left(\frac{\partial I_D}{\partial V_D}\right)^{-1}_{Q}
= \left(\frac{I_S}{V_T}e^{V_D/V_T}\right)^{-1}
= \frac{V_T}{I_D}
$$

$$
\boxed{\;r_d = \frac{V_T}{I_D} = \frac{26\,\mathrm{mV}}{I_D}\;}
$$

数值感觉：

| $I_D$ | $r_d$ |
|---|---|
| $10\,\mathrm{\mu A}$ | $2.6\,\mathrm{k\Omega}$ |
| $100\,\mathrm{\mu A}$ | $260\,\Omega$ |
| $1\,\mathrm{mA}$ | $26\,\Omega$ |
| $10\,\mathrm{mA}$ | $2.6\,\Omega$ |

> [!important] 这个式子的地位
> $r_d=V_T/I_D$ 与后面 BJT 的 $g_m=I_C/V_T$ 是同一件事的两种写法（$r_d = 1/g_m$）。整门课里凡是看到 $V_T/I$ 或 $I/V_T$，背后都是同一条指数曲线在工作点求导。

### 成立条件

线性化要求扰动足够小。展开二阶项可以看出，当 $v_d$ 超过约 $10\,\mathrm{mV}$ 时二次项开始不可忽略，出现明显失真。工程上常用的判据就是

$$
v_d \ll V_T \approx 26\,\mathrm{mV}
$$

---
## 4. 一个完整例子

$V_{DD}=3\,\mathrm{V}$，$R=2\,\mathrm{k\Omega}$，二极管 $I_S=10^{-15}\,\mathrm{A}$。求工作点和小信号电阻。

**第一步（恒压降）**：假设 $V_D=0.7\,\mathrm{V}$，

$$
I_D=\frac{3-0.7}{2\,\mathrm{k}}=1.15\,\mathrm{mA}
$$

**第二步（回代精化）**：

$$
V_D = V_T\ln\frac{I_D}{I_S}=0.026\times\ln\frac{1.15\times10^{-3}}{10^{-15}}\approx 0.72\,\mathrm{V}
$$

再代回得 $I_D\approx1.14\,\mathrm{mA}$ —— 已经收敛。

**第三步（小信号）**：

$$
r_d = \frac{26\,\mathrm{mV}}{1.14\,\mathrm{mA}} \approx 22.8\,\Omega
$$

若在 $V_{DD}$ 上叠加一个小纹波 $v_{in}$，则二极管上的纹波为

$$
v_d = v_{in}\cdot\frac{r_d}{R+r_d} \approx \frac{v_{in}}{88}
$$

—— 这正是齐纳稳压电路的工作原理，只不过那里用的是击穿区的 $r_z$。

---
## 5. 与其他笔记的关系

- 模型来源：[[PN Junction Forward Bias and the Diode Equation]]。
- 大信号模型的应用：[[Half-Wave and Full-Wave Rectifiers]]、[[Zener Regulators, Limiters and Voltage Doublers]]。
- 同一套线性化方法用在 BJT 上：[[BJT Small-Signal Model]]。
