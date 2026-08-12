---
title: "BJT Output Characteristics and the Early Effect"
aliases: ["BJT 输出特性", "厄利效应", "Early Effect", "输出电阻 ro"]
tags: [electronic_circuits, ee, bjt]
up: "[[Electronic Circuits I MOC]]"
down: ["[[BJT Operating Regions and Large-Signal Model]]"]
related: ["[[Bipolar Transistor Structure and Operation]]", "[[MOSFET Characteristics and Small-Signal Model]]"]
---
# BJT Output Characteristics and the Early Effect

## BJT（二）：输出特性族、Early 效应与 $r_o$

> [!summary] 核心结论
> 理想模型说 $I_C$ 与 $V_{CE}$ 无关；实际上 $V_{CE}$ 升高会让 BC 结耗尽区侵入基区，基区变薄 $\Rightarrow$ 浓度梯度变陡 $\Rightarrow$ $I_C$ 微升。这就是 **Early 效应**：
> $$I_C = I_Se^{V_{BE}/V_T}\left(1+\frac{V_{CE}}{V_A}\right),\qquad r_o=\frac{V_A}{I_C}$$
> $V_A$（Early 电压）典型 $20\sim 100\,\mathrm{V}$。$r_o$ 是所有共射级增益的上限，也是「本征增益」$g_mr_o=V_A/V_T$ 的来源。

---
## 1. 输出特性族

![[ec-bjt-output-characteristics-and-the-early-effect-01.svg]]

横轴 $V_{CE}$、纵轴 $I_C$，每条曲线对应一个固定的 $V_{BE}$。两个区域：

- **饱和区**（$V_{CE}$ 很小）：BC 结也正偏了，集电极的抽取能力下降，$I_C$ 随 $V_{CE}$ 急剧上升。边界在 $V_{CE}\approx V_{BE}$（严格说是 $V_{CE}$ 使 BC 结开始正偏处）。
- **正向有源区**：曲线接近水平，但有一个小的正斜率——这就是 Early 效应。

把所有曲线的有源段向左延长，它们**交于横轴上同一点** $-V_A$。这个惊人的规律正是 Early 电压的定义方式。

---
## 2. Early 效应的物理

$V_{CE}$ 升高 $\Rightarrow$ BC 结反偏更深 $\Rightarrow$ 耗尽区展宽 $\Rightarrow$ 展宽的一部分**吃进基区**（基区掺杂轻，耗尽区主要往基区扩）$\Rightarrow$ 有效基区宽度 $W_B$ 变小。

而 $I_C \propto 1/W_B$（浓度梯度 = 浓度差 / 宽度）。所以：

$$
W_B\downarrow \;\Rightarrow\; \text{梯度}\uparrow \;\Rightarrow\; I_C\uparrow
$$

这叫**基区宽度调制**（base-width modulation）。修正后的方程：

$$
I_C = I_S e^{V_{BE}/V_T}\left(1 + \frac{V_{CE}}{V_A}\right)
$$

$V_A$ 由基区掺杂和宽度决定：基区越厚、掺杂越重，$V_A$ 越大（但 $\beta$ 越小）。这是工艺上的一对基本矛盾。

> [!note] 极端情况：基区穿通
> $V_{CE}$ 大到耗尽区吃穿整个基区时，E 与 C 直接导通，器件失效。这是 BJT 击穿电压的一个上限。

---
## 3. 输出电阻 $r_o$

在工作点对 $V_{CE}$ 求导：

$$
r_o = \left(\frac{\partial I_C}{\partial V_{CE}}\right)^{-1}_{Q}
= \frac{V_A + V_{CE}}{I_C} \approx \frac{V_A}{I_C}
$$

$$
\boxed{\;r_o \approx \frac{V_A}{I_C}\;}
$$

数值感觉：$V_A=100\,\mathrm{V}$、$I_C=1\,\mathrm{mA}$ $\Rightarrow$ $r_o=100\,\mathrm{k\Omega}$。

$r_o$ 出现在小信号模型里，与集电极负载并联。它是共射级电压增益的天花板。

---
## 4. 本征增益：BJT 最漂亮的一条结论

把 $g_m$ 和 $r_o$ 相乘：

$$
g_m r_o = \frac{I_C}{V_T}\cdot\frac{V_A}{I_C} = \frac{V_A}{V_T}
$$

$$
\boxed{\;g_m r_o = \frac{V_A}{V_T}\;}
$$

**$I_C$ 被完全消掉了。** 这意味着：

- BJT 的最大可能电压增益（用理想电流源做负载时）是一个由工艺决定的常数。
- $V_A=100\,\mathrm{V}$ 时，$g_mr_o \approx 100/0.026 \approx 3800$。
- **烧更多电流不会提高本征增益**，只会提高带宽。

> [!important] 与 MOS 的关键对比
> MOS 的本征增益 $g_mr_o=\dfrac{2}{\lambda V_{ov}}$ 依赖于过驱电压和沟道长度，设计者可以调；而且它的数值通常远低于 BJT（几十量级）。
> 这就是为什么高精度、高增益的模拟电路（运放输入级、带隙基准）至今仍偏爱 BJT 或 BiCMOS。详见 [[MOSFET Characteristics and Small-Signal Model]]。

---
## 5. 关于 $\beta$ 的补充

$\beta$ 并不是常数：

- **小电流区**：BE 结的复合电流占比大，$\beta$ 下降。
- **中电流区**：$\beta$ 平坦，这是设计工作区。
- **大电流区**：高注入效应使基区有效掺杂被注入载流子超过，$\beta$ 明显下降。

加上批次离散和温度系数（约 $+0.5\%/^\circ\mathrm{C}$），实用结论只有一条：**电路不能依赖 $\beta$ 的具体值**。

---
## 6. 与其他笔记的关系

- 理想方程的来源：[[Bipolar Transistor Structure and Operation]]。
- 下一讲把四个工作区讲全：[[BJT Operating Regions and Large-Signal Model]]。
- $r_o$ 进入小信号模型：[[BJT Small-Signal Model]]。
- MOS 里的对应效应（沟道长度调制）：[[MOSFET Characteristics and Small-Signal Model]]。
