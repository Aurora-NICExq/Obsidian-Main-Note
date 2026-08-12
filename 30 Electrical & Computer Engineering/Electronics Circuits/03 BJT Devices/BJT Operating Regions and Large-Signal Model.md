---
title: "BJT Operating Regions and Large-Signal Model"
aliases: ["BJT 工作区", "饱和区", "大信号模型", "负载线"]
tags: [electronic_circuits, ee, bjt]
up: "[[Electronic Circuits I MOC]]"
down: ["[[BJT Small-Signal Model]]"]
related: ["[[BJT Output Characteristics and the Early Effect]]", "[[BJT Biasing Schemes]]"]
---
# BJT Operating Regions and Large-Signal Model

## BJT（三）：四个工作区、大信号模型与负载线

> [!summary] 核心结论
> 工作区完全由两个 pn 结各自的偏置方向决定，不需要背表。放大器只用**正向有源区**；开关只用**截止**与**饱和**。
> 大信号模型：输入侧是一个二极管，输出侧是一个受 $V_{BE}$ 控制的电流源。
> 负载线把器件特性和外部电阻画在同一张图上，工作点就是两者的交点 —— 这是理解「增益 vs 摆幅」权衡的最好工具。

---
## 1. 四个工作区

![[ec-bjt-operating-regions-and-large-signal-model-01.svg]]

| 区 | BE 结 | BC 结 | 行为 |
|---|---|---|---|
| 截止 | 反偏 | 反偏 | 三个电流都≈0，相当于断开 |
| **正向有源** | 正偏 | 反偏 | $I_C=I_Se^{V_{BE}/V_T}$，理想电流源 |
| 饱和 | 正偏 | 正偏 | $V_{CE}$ 被压到 $\approx0.2\,\mathrm{V}$，$I_C<\beta I_B$ |
| 反向有源 | 反偏 | 正偏 | 能工作但 $\beta$ 极低，几乎不用 |

判据只有一句话：**看两个 pn 结各自正偏还是反偏**。不需要死记 $V_{CE}$ 的门限。

### 饱和区细节

BC 结一旦正偏，集电结也开始向基区注入载流子，与正向注入相抵消。后果：

- $I_C$ 不再由 $V_{BE}$ 独自决定，$\beta$ 「失效」（$I_C < \beta I_B$）。
- $V_{CE,sat}\approx 0.1\sim0.3\,\mathrm{V}$，功耗低 —— 这是 BJT 做开关的价值。
- **但基区里积累了大量超量少子**，关断时必须先把它们抽走，造成**存储时间**（storage time），限制开关速度。

> [!note] 为什么数字电路最终选了 CMOS 而不是 BJT
> 除了静态功耗，饱和区的电荷存储正是 TTL 速度上不去的关键。后来的肖特基 TTL 就是靠加一个肖特基二极管把管子钳在饱和边缘之外来提速的。

---
## 2. 大信号模型

同一张图的右半部分：

- **输入侧**：B–E 之间是一个二极管，饱和电流为 $I_S/\beta$（因为 $I_B=I_C/\beta$）。
- **输出侧**：C–E 之间是一个受控电流源 $I_Se^{V_{BE}/V_T}$。

这个「电压进、电流出」的结构就是**跨导器件**的定义，也是 BJT 能做放大的全部理由。MOS 的大信号模型结构完全一样，只是输入侧连二极管都没有（栅极直流开路）。

---
## 3. 负载线

![[ec-bjt-operating-regions-and-large-signal-model-02.svg]]

外部电路（$V_{CC}$ 与 $R_C$）给出一条直线约束：

$$
I_C = \frac{V_{CC} - V_{CE}}{R_C}
$$

它在图上是一条从 $(0,\ V_{CC}/R_C)$ 到 $(V_{CC},\ 0)$ 的直线，斜率 $-1/R_C$。器件特性族与这条直线的交点就是工作点 $Q$。

$V_{BE}$ 变化时，$Q$ 沿着负载线移动。所以：

- **$Q$ 太靠近饱和端**：输出往下摆不了多少就进饱和，波形被削底。
- **$Q$ 太靠近截止端**：输出往上摆不了多少，且 $g_m=I_C/V_T$ 很小，增益低。
- **合适的 $Q$**：$V_{CE}$ 大约留在 $V_{CC}$ 的一半附近，上下摆幅对称。

### 摆幅与增益的根本矛盾

共射级的增益（忽略 $r_o$）：

$$
|A_v| = g_m R_C = \frac{I_C R_C}{V_T} = \frac{V_{R_C}}{V_T}
$$

其中 $V_{R_C}$ 是 $R_C$ 上的直流压降。要增益大就要 $V_{R_C}$ 大，但 $V_{R_C}$ 大意味着留给 $V_{CE}$ 的电压少，输出摆幅就小。

$$
V_{R_C} + V_{CE} = V_{CC}
$$

**电源电压把「增益 × 摆幅」的乘积卡死了。** 这条约束是整个模拟设计的第一性矛盾，也是后面引入电流源负载、cascode、差分对等一系列技巧的动机。

> [!example] 数字感觉
> $V_{CC}=3\,\mathrm{V}$，把一半电压给 $R_C$：$|A_v|=1.5/0.026\approx 58$。
> 想要 $|A_v|=200$，需要 $V_{R_C}=5.2\,\mathrm{V}$ —— 在 $3\,\mathrm{V}$ 电源下**根本做不到**。只能改用电流源负载（直流压降小但交流电阻大）。

---
## 4. BJT 做开关

- **输入低**：BE 结不导通，截止，$I_C=0$，$V_{out}=V_{CC}$。
- **输入高**：基极电流足够大（$I_B > I_{C,sat}/\beta$，工程上取 $2\sim10$ 倍余量称为 overdrive），进入饱和，$V_{out}=V_{CE,sat}\approx0.2\,\mathrm{V}$。

过驱动越深，导通越可靠，但存储的电荷越多、关断越慢。这是一个实打实的速度/裕量权衡。

---
## 5. 与其他笔记的关系

- 特性族与 $r_o$：[[BJT Output Characteristics and the Early Effect]]。
- 下一讲把工作点线性化：[[BJT Small-Signal Model]]。
- 怎么把 $Q$ 稳定地放在想要的位置：[[BJT Biasing Schemes]]。
