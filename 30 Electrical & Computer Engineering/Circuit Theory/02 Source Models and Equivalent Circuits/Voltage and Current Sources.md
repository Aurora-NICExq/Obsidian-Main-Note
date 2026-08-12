---
title: "Voltage and Current Sources"
aliases: ["电压源与电流源", "Voltage Source, Current Source"]
tags: [basic_circuit_theory, ee]
up: "[[Basic Circuit Theory MOC]]"
down: ["[[Source Transformation and Power]]"]
related: ["[[Charge, Current, and Voltage]]", "[[Ohm's Law and I-V Characteristics]]", "[[Thevenin's Theorem]]", "[[Norton's Theorem]]", "[[Introduction to Op Amps]]"]
---
# Voltage and Current Sources

## 电压源与电流源

> [!definition] 理想源
> 理想**电压源**固定其端*电压*；理想**电流源**固定其*电流*。实际器件总是具有有限的工作范围和内阻效应。

---
## 1. 理想导线模型

在入门电路分析中，理想导线近似为：

- $R=0$，
- 两端电压降 $u=0$，
- 唯一作用是连接同一节点的各点。

因此，任何连续的理想导线都可以视为等电位体。

---
## 2. 电压源

### 2.1 定义

理想电压源在其两端维持一个指定的电压：
$$
u_{ab}(t)=u_s(t)
$$

- 直流源：$u_s(t)=U_0$，
- 交流源：$u_s(t)$ 随时间变化。

---
### 2.2 非理想电压源与电压跌落

实际电压源通常建模为*理想电压源与内阻 $r$ 串联*：
$$
U_{\text{term}}=U_s-Ir
$$

这解释了端电压随负载电流增大而*跌落*的现象。

---
### 2.3 独立源与受控源

**独立电压源**的值由源本身设定。

![[tikz-voltage-and-current-sources-01.svg]]

**受控（非独立）电压源**的值由电路中其他变量决定，例如：
$$
u_s=\mu u_x \quad\text{或}\quad u_s=r_m i_x
$$

![[tikz-voltage-and-current-sources-02.svg]]

---
## 3. 电流源

### 3.1 定义

理想电流源维持一个指定的电流：
$$
i(t)=i_s(t)
$$

- 直流：$i_s(t)=I_0$，
- 交流：$i_s(t)$ 随时间变化。

---
### 3.2 开路极限

![[tikz-voltage-and-current-sources-03.svg]]

在理想模型中，如果外部开路而源仍需维持 $I_s$，则推出：
$$
v_{ab}\to\infty
$$

因此"理想电流源 + 开路"是极限模型，而非可持续的物理状态。

---
### 3.3 实际电流源

实际电流源具有有限的**顺从电压**：

- 低于该极限时，它近似表现为恒流源；
- 超过该极限时，进入饱和状态，电流不再理想恒定。

---
### 3.4 受控电流源

受控电流源一般写作：
$$
i_s=f(v_x\ \text{或}\ i_x)
$$

两种常见类型：

- VCCS（压控电流源）：$i_s=g_m v_x$，
- CCCS（流控电流源）：$i_s=\beta i_x$。

---
## 4. 放大器视角

电压放大器模型通常写作：
$$
v_o=A_v v_i
$$

这本质上是一个受控源模型：输出由输入控制，通过增益缩放（参见 [[Introduction to Op Amps]]）。

---
## 5. 总结

> [!attention] 源模型
> 理想源用于*建立方程*；非理想源用于*解释实际行为*。解题时需区分"理想约束"和"实际工作范围"。

## 参见
- [[Ohm's Law and I-V Characteristics#4. I-V Curves of Ideal Voltage and Current Sources]]
- [[Source Transformation and Power#1. Source Transformation]]
- [[Thevenin's Theorem]]
- [[Norton's Theorem]]
