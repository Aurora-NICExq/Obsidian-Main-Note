---
title: "Inductors and RL Circuits"
aliases: ["电感与 RL 电路", "Inductor Circuits"]
tags: [basic_circuit_theory, ee]
up: "[[Basic Circuit Theory MOC]]"
down: ["[[Source-Free and Driven RL Circuits]]"]
related: ["[[Capacitors and Their Properties]]", "[[Source-Free and Driven RC Response]]", "[[Introduction to RLC Circuits]]", "[[First-Order Shortcut Method]]"]
---
## 电感

> [!definition] 电感
> 电感两端的电压与其电流的*变化率*成正比；电感从根本上*阻碍电流的突变*。

---
## 1. 电感的基本关系

按图所示的参考方向和极性，电感满足：
$$
V_1=L_1\frac{dI_1}{dt}
$$

等效积分形式：
$$
I_1(t)=I_1(t_0)+\frac{1}{L_1}\int_{t_0}^{t}V_1(\tau)\,d\tau
$$

这表明电感电流由电压的*积分*决定，因此连续变化，在理想情况下不能跃变。

![[tikz-inductors-and-rl-circuits-01.svg]]

---
## 2. 示例：线性增长电流

给定电流：
$$
I_1=\alpha t
$$

则：
$$
V_1=L_1\frac{dI_1}{dt}=L_1\alpha
$$

结论：当电流以斜率 $\alpha$ 线性上升时，电感电压为常数。

![[tikz-inductors-and-rl-circuits-02.svg]]

---
## 3. 电路与电压波形

当 $dI_1/dt$ 为常数时，电感电压保持恒定，因此 $V_1\!-\!t$ 图为一条水平线。

![[tikz-inductors-and-rl-circuits-03.svg]]

![[tikz-inductors-and-rl-circuits-04.svg]]

---
## 4. 本节总结

> [!attention] 关键点
> - $V=L\,dI/dt$ 是电感电路分析的核心理念。
> - 电感阻碍*电流的变化*，而非电流本身。
> - 电流斜率越大，电感电压越大。
> - 恒定的电感电压对应线性变化的电流。

# RL 电路

## 无源（零输入）响应

![[tikz-inductors-and-rl-circuits-05.svg]]

$$
L_1\frac{dI_{out}}{dt}=-R_1I_{out}
$$

$$
I_{out}(0^+)=-I_0
$$

$$
\frac{L_1}{R_1}\frac{dI_{out}}{dt}+I_{out}=0
$$

$$
\tau=\frac{L_1}{R_1}
$$

## RL 电路的响应特性

电感电流在开关瞬间是连续的，因此必须先从开关前电路确定初始值，然后用于开关后的微分方程。

![[tikz-inductors-and-rl-circuits-06.svg]]

![[tikz-inductors-and-rl-circuits-07.svg]]

## RL 电路初始条件的设定

电感维持其电流的趋势可建模为初始电流在短接回路中持续流动：

![[tikz-inductors-and-rl-circuits-08.svg]]

## 参见
- [[Charge, Current, and Voltage#2. Current]]
- [[Source-Free and Driven RC Response#3. Superposition of the Total Response]]
- [[Introduction to RLC Circuits]]
- [[LC Circuits and Second-Order ODEs]]
- [[First-Order Shortcut Method]]
