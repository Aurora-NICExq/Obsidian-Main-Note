---
title: "Charge, Current, and Voltage"
aliases: ["电荷、电流与电压", "Charge, Current, Voltage"]
tags: [basic_circuit_theory, ee]
up: "[[Basic Circuit Theory MOC]]"
down: ["[[Ohm's Law and I-V Characteristics]]"]
related: ["[[Kirchhoff's Laws (KCL and KVL)]]", "[[Voltage and Current Sources]]", "[[Capacitors and Their Properties]]", "[[Inductors and RL Circuits]]"]
---
# Charge, Current, and Voltage

## 电荷、电流与电压

> [!definition] 三种基本量
> **电荷**是一种*存量*（有多少），**电流**是一种*流量*（变化有多快），
> **电压**是两点之间*单位电荷的能量*。

---
## 1. 电荷

电荷是物质参与电磁相互作用的基本属性。

- 电荷有两种：正电荷和负电荷。
- 同种电荷相互排斥，异种电荷相互吸引。

在微观层面：

- 电子携带负电荷。
- 质子携带正电荷。
- 中子不带电。

物体因得失电子不平衡而带电。

> [!definition] 电荷
> 符号 $Q$ 或 $q$；SI 单位为**库仑**（$\mathrm{C}$）。

---
## 2. 电流

电流是单位时间内通过某一横截面的电荷量：
$$
I=\frac{dQ}{dt}
$$

对于恒定电流：
$$
I=\frac{\Delta Q}{\Delta t}, \qquad 1\ \mathrm A = 1\ \mathrm{C/s}
$$

对应的累积电荷为：
$$
Q=\int_{t_1}^{t_2} i(t)\,dt
$$

几何上，这是在 $i\!-\!t$ 曲线下的有向面积。

---
## 3. 电压

电压是两点之间的电位差，即*单位电荷所做的功*：
$$
u_{AB}=\frac{W_{AB}}{q}
$$

其中：

- $u_{AB}$ — $A$ 点相对于 $B$ 点的电压，
- $W_{AB}$ — 电场力所做的功，
- $q$ — 电荷。

单位关系：
$$
1\ \mathrm V = 1\ \mathrm{J/C}
$$

---
## 4. 关系与求解直觉

1. 电荷 $Q$ 是累积量；电流 $I$ 是其变化率——这是一对微积分关系：
$$
I=\frac{dQ}{dt}, \qquad Q=\int i(t)\,dt
$$
2. 电压反映了驱动电荷运动的势能差。
3. 在电路分析中，这些量与元件方程结合使用：
   - 电阻：$u=iR$（参见 [[Ohm's Law and I-V Characteristics]]）
   - 电容：$i=C\,du/dt$（参见 [[Capacitors and Their Properties]]）
   - 电感：$u=L\,di/dt$（参见 [[Inductors and RL Circuits]]）

---
## 5. 常见陷阱

> [!attention] 注意
> - 将电压视为*某一点的绝对值*：电压始终是两点之间的差值。
> - 混淆 $d$ 和 $\Delta$：瞬时关系使用 $d$，区间平均值使用 $\Delta$。
> - 假设"有电压必有电流"：开路可以保持电压而电流为 $0$。

---
## 6. 总结

> [!attention] 电荷、电流、电压
> 电荷描述*有多少*，电流描述*变化有多快*，电压描述
> *单位电荷的能量差*。

## 参见
- [[Ohm's Law and I-V Characteristics]]
- [[Kirchhoff's Laws (KCL and KVL)]]
- [[Voltage and Current Sources]]
- [[Capacitors and Their Properties]]
- [[Inductors and RL Circuits]]
