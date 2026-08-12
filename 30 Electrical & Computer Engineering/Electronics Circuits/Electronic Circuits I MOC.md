---
title: "Electronic Circuits I MOC"
aliases: ["Electronic Circuits I", "电子电路 I", "电子电路 MOC", "Razavi 电子电路"]
tags: [electronic_circuits, ee, moc]
down: ["[[Introduction to Microelectronics]]", "[[Basic Physics of Semiconductors]]", "[[Carrier Drift and Diffusion]]", "[[PN Junction in Equilibrium & Reverse Bias]]", "[[PN Junction Forward Bias and the Diode Equation]]", "[[Diode Models and Small-Signal Resistance]]", "[[Half-Wave and Full-Wave Rectifiers]]", "[[Zener Regulators, Limiters and Voltage Doublers]]", "[[Bipolar Transistor Structure and Operation]]", "[[BJT Output Characteristics and the Early Effect]]", "[[BJT Operating Regions and Large-Signal Model]]", "[[BJT Small-Signal Model]]", "[[BJT Biasing Schemes]]", "[[Common-Emitter Stage]]", "[[CE with Emitter Degeneration and Source Resistance]]", "[[Common-Base Stage and Emitter Follower]]", "[[MOSFET Structure and Operation]]", "[[MOSFET Characteristics and Small-Signal Model]]", "[[MOS Biasing and the Common-Source Stage]]", "[[Common-Gate Stage and Source Follower]]"]
related: ["[[Basic Circuit Theory MOC]]", "[[Signals and Systems MOC]]"]
---
# Electronic Circuits I MOC

UCLA · Behzad Razavi《Electronic Circuits I》的学习笔记，共 20 讲。

> [!note] 讲次划分说明
> 讲次编号按 Razavi《Fundamentals of Microelectronics》Ch.1–7 的**章节顺序**组织，
> 用于给自学定一个可靠的先后次序，不对应某个具体视频的编号。

---
## 学习顺序

![[ec-electronic-circuits-i-moc-01.svg]]

---
## 一 · 半导体物理（L01–L03） → `01 Semiconductor Physics/`

- [[Introduction to Microelectronics]]：放大器的三个指标（$A_v$、$R_{in}$、$R_{out}$）、模拟 vs 数字、全课方法论
- [[Basic Physics of Semiconductors]]：能带、本征浓度 $n_i$、掺杂、质量作用定律 $np=n_i^2$
- [[Carrier Drift and Diffusion]]：迁移率与速度饱和、扩散流、爱因斯坦关系 $D/\mu=V_T$

## 二 · PN 结与二极管（L04–L08） → `02 PN Junction and Diodes/`

- [[PN Junction in Equilibrium & Reverse Bias]]：耗尽区四联图、内建电势 $V_0$、结电容 $C_j(V_R)$
- [[PN Junction Forward Bias and the Diode Equation]]：少子注入、$I_D=I_S(e^{V_D/V_T}-1)$、$60\,\mathrm{mV/dec}$
- [[Diode Models and Small-Signal Resistance]]：理想 / 恒压降 / 小信号三种模型、$r_d=V_T/I_D$
- [[Half-Wave and Full-Wave Rectifiers]]：半波、滤波电容与纹波、桥式全波、PIV
- [[Zener Regulators, Limiters and Voltage Doublers]]：齐纳稳压与 $r_z$、限幅器传输特性、钳位与倍压

## 三 · BJT 器件（L09–L13） → `03 BJT Devices/`

- [[Bipolar Transistor Structure and Operation]]：npn 结构、$I_C=I_Se^{V_{BE}/V_T}$、$\beta$、$g_m=I_C/V_T$
- [[BJT Output Characteristics and the Early Effect]]：输出特性族、$V_A$、$r_o=V_A/I_C$、本征增益 $V_A/V_T$
- [[BJT Operating Regions and Large-Signal Model]]：四个工作区、大信号模型、负载线与「增益 × 摆幅」矛盾
- [[BJT Small-Signal Model]]：混合 π 与 T 模型、$g_m/r_\pi/r_o$、两条阻抗速查规则
- [[BJT Biasing Schemes]]：为什么不能依赖 $\beta$、分压偏置 + 射极电阻、自偏置、PNP

## 四 · BJT 放大器（L14–L16） → `04 BJT Amplifiers/`

- [[Common-Emitter Stage]]：$A_v=-g_m(R_C\parallel r_o)$、「增益 = 压降 / 26 mV」
- [[CE with Emitter Degeneration and Source Resistance]]：$A_v=-R_C/(R_E+1/g_m)$、负载反馈换线性度
- [[Common-Base Stage and Emitter Follower]]：CB 低 $R_{in}$ 与 cascode、EF 缓冲、三组态汇总

## 五 · MOSFET 与其放大器（L17–L20） → `05 MOSFET and Amplifiers/`

- [[MOSFET Structure and Operation]]：沟道形成、$V_{TH}$、三极管区与饱和区、夹断
- [[MOSFET Characteristics and Small-Signal Model]]：平方律、$\lambda$、$g_m$ 三种写法、体效应、$g_m/I_D$
- [[MOS Biasing and the Common-Source Stage]]：偏置、共源级的三种负载（电阻 / 二极管接法 / 电流源）
- [[Common-Gate Stage and Source Follower]]：CG 与 cascode、SF 与体效应、**六种组态总表**

---
## 贯穿全课的三条主线

1. **三步法**：大信号定工作点 → 在 $Q$ 点求偏导 → 换线性模型算增益阻抗。二极管、BJT、MOS 各走一遍，一字不改。
2. **$V_T\approx 26\,\mathrm{mV}$**：从爱因斯坦关系到二极管方程到 $g_m=I_C/V_T$，全是同一个 $kT/q$。「电流变 10 倍、电压变 $60\,\mathrm{mV}$」这条铁律在三个器件里通用。
3. **增益 × 摆幅被电源电压卡死**：$|A_v|=V_{R_C}/V_T$ 而 $V_{R_C}+V_{CE}=V_{CC}$。后面所有复杂拓扑（电流源负载、cascode、差分对）都是在绕开这条约束。

---
## 相关

- [[Basic Circuit Theory MOC]]：本课默认已掌握的线性电路工具（KCL/KVL、戴维南、节点法、RC 瞬态）
- [[Signals and Systems MOC]]：频域视角与 LTI 性质
- `Analog Circuit Design/`：同批主题的 Caltech 版讲法，偏 IC 设计视角，可与本系列交叉阅读

---
## 插图（预生成 SVG）

本文件夹的全部插图为 circuitikz / TikZ 预生成的 SVG，存放在
`90 Assets/diagrams/electronic-circuits/`，以 `![[ec-….svg]]` 嵌入。

可编辑源在 `90 Assets/scripts/electronic_circuits/sources/`，重新生成：

```bash
cd "90 Assets/scripts/electronic_circuits" && python3 generate_all.py
```
