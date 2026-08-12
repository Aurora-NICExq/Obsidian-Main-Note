---
title: "Zener Regulators, Limiters and Voltage Doublers"
aliases: ["齐纳稳压", "限幅器", "钳位器", "倍压电路", "二极管应用"]
tags: [electronic_circuits, ee, diode]
up: "[[Electronic Circuits I MOC]]"
down: ["[[Bipolar Transistor Structure and Operation]]"]
related: ["[[Half-Wave and Full-Wave Rectifiers]]", "[[Diode Models and Small-Signal Resistance]]"]
---
# Zener Regulators, Limiters and Voltage Doublers

## 二极管应用：齐纳稳压、限幅、钳位与倍压

> [!summary] 核心结论
> 这一讲把二极管的三种「非放大」用法讲完：**稳压**（工作在击穿区，用小的 $r_z$ 把输出钉住）、**限幅/钳位**（用导通阈值切掉或平移波形）、**倍压**（钳位 + 峰值整流串联）。
> 共同的分析套路都一样：先用理想模型判断通断，再用恒压降模型算电平，最后用小信号电阻算残余波动。

---
## 1. 齐纳稳压

![[ec-zener-regulators-limiters-and-voltage-doublers-01.svg]]

齐纳二极管专门设计成在某个反向电压 $V_Z$ 上稳定击穿（$V_Z$ 从 $2.4\,\mathrm{V}$ 到上百伏都有）。反接在负载两端，串一个限流电阻 $R_1$：

- $v_{in}$ 升高 $\Rightarrow$ 齐纳吸走更多电流 $\Rightarrow$ $R_1$ 上压降增大 $\Rightarrow$ $v_{out}$ 几乎不动。
- 负载电流变化时同理，齐纳自动补上差额。

小信号看，齐纳在击穿区的等效电阻是 $r_z$（典型几欧到几十欧），于是输入纹波被分压衰减：

$$
\frac{v_{out}}{v_{in}} = \frac{r_z}{R_1 + r_z}
$$

这个比值就是**线性调整率**。$r_z$ 越小、$R_1$ 越大，稳压越硬。

> [!warning] 设计约束
> $R_1$ 必须同时满足两个极端：
> - **最坏情况一**（$v_{in}$ 最低、负载最重）：齐纳仍需有最小工作电流，否则脱出击穿区，稳压失效。
> - **最坏情况二**（$v_{in}$ 最高、负载最轻）：齐纳自己吸走全部电流，功耗 $V_Z I_Z$ 不能超过额定。
>
> 这两条把 $R_1$ 夹在一个区间里；区间为空就说明齐纳方案不适用，得上串联稳压器。

齐纳稳压效率低（空载时白白烧电流），但零件少、无需反馈补偿，做基准和小电流场合仍然常用。

---
## 2. 限幅器（limiter / clipper）

![[ec-zener-regulators-limiters-and-voltage-doublers-02.svg]]

两条并联支路，各自是「二极管 + 偏置电压」：

- 输入在中间区间时，两个二极管都截止，$v_{out}=v_{in}$，斜率为 1。
- 输入超过 $V_H + V_{D,on}$ 时 $D_1$ 导通，把输出钳在上限。
- 输入低于 $-(V_L + V_{D,on})$ 时 $D_2$ 导通，钳在下限。

传输特性就是一条中间斜率为 1、两端水平的折线。

用途：

- **保护**：把送进 ADC 或运放输入的信号限制在电源轨内。
- **整形**：把正弦削成近似方波。
- **软限幅**：故意让限幅发生在放大器饱和之前，避免恢复时间过长。

把 $V_H$ 或 $V_L$ 设为 0（二极管直接接地）就得到最简单的对称限幅；把其中一条支路去掉就是单边限幅。

---
## 3. 钳位器（clamp / level shifter）

![[ec-zener-regulators-limiters-and-voltage-doublers-03.svg]]

串一个电容、并一个二极管。稳态下电容被充到 $V_p$ 并保持，于是整条波形被**平移**了一个直流量：

$$
v_{out} = v_{in} + V_p
$$

关键区别：限幅器改变波形**形状**，钳位器只改变**直流电平**，形状原封不动。

判断钳位方向：二极管导通时把输出钳在哪个电平，波形就被平移到哪一侧。图中二极管阴极接输出、阳极接地，所以输出的**最低点**被钳在 $0$（严格说是 $-V_{D,on}$），整条波形抬到 $0\sim 2V_p$。

---
## 4. 倍压器

同一张图的右半部分。倍压器就是**钳位器 + 峰值整流**串联：

1. $C_1$、$D_1$ 组成钳位器，把 $\pm V_p$ 的输入变成 $0\sim 2V_p$ 的波形。
2. $D_2$、$C_2$ 组成峰值检波，把这个波形的峰值 $2V_p$ 保持下来。

$$
v_{out} \approx 2V_p - 2V_{D,on}
$$

级联下去可以做三倍压、四倍压（Cockcroft–Walton 倍压链），常见于 CRT 高压、离子泵、以及片上电荷泵（charge pump）——闪存的编程电压就是这么产生的。

代价：输出阻抗随级数急剧变差，只适合极小电流负载。

---
## 5. 分析这类电路的通用套路

1. **判通断**：用理想二极管模型，假设一组状态。
2. **算电平**：换恒压降模型，解出各段的输出。
3. **验假设**：导通支路电流为正、截止支路确实反偏。不自洽就换假设。
4. **画传输特性**：横轴 $v_{in}$、纵轴 $v_{out}$，逐段画出斜率。这一步能立刻暴露分析错误。
5. **算残余波动**：需要精度时用 $r_d=V_T/I_D$ 或 $r_z$ 做小信号分析。

---
## 6. 与其他笔记的关系

- 前置：[[Diode Models and Small-Signal Resistance]]、[[Half-Wave and Full-Wave Rectifiers]]。
- 下一讲进入第一个真正的放大器件：[[Bipolar Transistor Structure and Operation]]。
