---
title: "MOS Biasing and the Common-Source Stage"
aliases: ["MOS 偏置", "共源级", "Common-Source", "二极管接法负载", "电流源负载"]
tags: [electronic_circuits, ee, mosfet, amplifier]
up: "[[Electronic Circuits I MOC]]"
down: ["[[Common-Gate Stage and Source Follower]]"]
related: ["[[MOSFET Characteristics and Small-Signal Model]]", "[[Common-Emitter Stage]]", "[[Caltech Analog Circuit Design-123N-MOS Stages (1)-Common-Source Source Degeneration and Impedances]]"]
---
# MOS Biasing and the Common-Source Stage

## MOSFET（三）：偏置与共源级的三种负载

> [!summary] 核心结论
> 共源级与共射级完全同构：$A_v=-g_m(R_D\parallel r_o)$，$R_{in}=\infty$，$R_{out}=R_D\parallel r_o$。
> 真正的设计内容在**负载的选择**：电阻负载受电源电压限制；二极管接法负载给出 $-\sqrt{(W/L)_1/(W/L)_2}$ 的可预测但偏低的增益；电流源负载逼近本征增益 $g_mr_o$，是 IC 里的默认选择。
> 偏置上 MOS 比 BJT 简单一点（栅极不吃电流），但麻烦在 $V_{TH}$ 的工艺离散。

---
## 1. MOS 偏置

栅极直流电流为零，所以分压器可以用**极大**的电阻（MΩ 级），不必像 BJT 那样担心基极电流把分压点拉偏。

标准结构仍是分压偏置 + 源极电阻：

$$
V_G = V_{DD}\frac{R_2}{R_1+R_2},\qquad
V_{GS} = V_G - I_DR_S
$$

联立饱和区方程解出 $I_D$（一个二次方程，取使 $V_{GS}>V_{TH}$ 的根）。

$R_S$ 的负反馈作用与 BJT 的 $R_E$ 完全一样：$I_D\uparrow\Rightarrow V_S\uparrow\Rightarrow V_{GS}\downarrow\Rightarrow I_D\downarrow$，把 $V_{TH}$ 和 $\mu C_{ox}$ 的工艺离散压下去。

> [!note] 分立 vs 集成的分野
> 上面这套（大电阻分压 + 源极退化）是**分立电路**的做法。集成电路里几乎不这么干 —— 片上大电阻又贵又不准。IC 的标准做法是**电流镜**：用一个基准电流复制到各级。这是 Electronic Circuits II 的内容，但值得现在就知道分野在哪。

---
## 2. 共源级：三种负载

![[ec-mos-biasing-and-the-common-source-stage-01.svg]]

### (a) 电阻负载

$$
A_v = -g_m(R_D\parallel r_o) \approx -g_mR_D
$$

代入 $g_m=2I_D/V_{ov}$：

$$
|A_v| = \frac{2I_DR_D}{V_{ov}} = \frac{2V_{R_D}}{V_{ov}}
$$

与共射级的 $V_{R_C}/V_T$ 对照：分母从 $26\,\mathrm{mV}$ 变成了 $V_{ov}/2$（典型 $100\,\mathrm{mV}$）。**同样的直流压降，MOS 的增益只有 BJT 的 1/4 左右。**

同样受电源电压卡死：$V_{R_D}+V_{DS}=V_{DD}$，要增益就没摆幅。

### (b) 二极管接法负载

把负载管的栅漏短接。此时它的小信号阻抗是 $1/g_{m2}$（并上 $r_{o2}$，通常可忽略）：

$$
A_v = -\frac{g_{m1}}{g_{m2}}
= -\sqrt{\frac{(W/L)_1}{(W/L)_2}}\cdot\sqrt{\frac{I_{D1}}{I_{D2}}}
= -\sqrt{\frac{(W/L)_1}{(W/L)_2}}
$$

（同一支路电流相等，根号内的电流比为 1。）

**优点**：增益只由**尺寸比**决定 —— 不依赖 $\mu$、$C_{ox}$、$V_{TH}$、温度、电流。在工艺离散面前极其鲁棒，线性度也好。

**缺点**：增益天花板低。要 $|A_v|=10$ 就需要 $(W/L)$ 比达到 100，面积代价大；而且负载管上要压 $V_{GS2}$，摆幅被吃掉。

### (c) 电流源负载

PMOS 栅接固定偏压，工作在饱和区，等效为一个大电阻 $r_{o2}$：

$$
A_v = -g_{m1}(r_{o1}\parallel r_{o2})
$$

这就逼近了本征增益 $g_mr_o$（约 $50\sim 200$）。

**关键优势**：$r_{o2}$ 可以做到几百 kΩ，但它的**直流压降只需要 $V_{ov2}$**（一两百 mV）。「交流电阻大、直流压降小」—— 这正是电阻负载做不到的，也是为什么 IC 里几乎全用电流源负载。

**代价**：
- 输出直流电平由两个管子的电流是否精确匹配决定 —— 稍有失配输出就会贴到某条轨上。所以电流源负载的共源级**必须**放在反馈环里（共模反馈或整体负反馈）。
- 输出摆幅被两个管子的 $V_{ov}$ 挤压。

---
## 3. 三种负载对照

| | (a) 电阻 | (b) 二极管接法 | (c) 电流源 |
|---|---|---|---|
| $A_v$ | $-g_mR_D$ | $-\sqrt{(W/L)_1/(W/L)_2}$ | $-g_m(r_{o1}\parallel r_{o2})$ |
| 典型值 | $10\sim 30$ | $2\sim 10$ | $50\sim 200$ |
| 精度 | 依赖 $g_m$（差） | 尺寸比（**极好**） | 依赖 $r_o$（差） |
| 摆幅 | 差（压降大） | 中 | 好（压降 $=V_{ov}$） |
| 需要反馈定直流点 | 否 | 否 | **是** |
| 片上可行性 | 差（大电阻贵） | 好 | 好 |

---
## 4. 源极退化

与 BJT 的射极退化同构，但更简洁（$\beta\to\infty$）：

$$
A_v = -\frac{R_D}{R_S + 1/g_m}
$$

$$
R_{out} = r_o(1+g_mR_S) + R_S \approx g_mr_oR_S
$$

输入阻抗仍是无穷大（栅极不吃电流），所以 MOS 里没有 BJT 那条「$R_{in}=r_\pi+(\beta+1)R_E$」的规则 —— **规则简化成了「栅极永远是无穷大阻抗，源极看进去是 $1/g_m$」**。

$R_{out}$ 被 $(1+g_mR_S)$ 放大这条，正是 MOS cascode 的原理。

> [!warning] 别忘了体效应
> 源极退化使源极电位浮起来，于是 $V_{SB}\ne 0$，$g_{mb}$ 登场：
> $$R_{out}\approx r_o\left[1+(g_m+g_{mb})R_S\right]$$
> 实际增益比不考虑体效应时低 $10\%\sim30\%$。

---
## 5. 与其他笔记的关系

- 器件参数：[[MOSFET Characteristics and Small-Signal Model]]。
- 完全同构的 BJT 版本：[[Common-Emitter Stage]]、[[CE with Emitter Degeneration and Source Resistance]]。
- 另外两种 MOS 组态：[[Common-Gate Stage and Source Follower]]。
- IC 视角的更细讨论：[[Caltech Analog Circuit Design-123N-MOS Stages (1)-Common-Source Source Degeneration and Impedances]]。
