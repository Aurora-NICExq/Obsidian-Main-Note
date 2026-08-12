---
title: "Capacitors and Their Properties"
aliases: ["电容及其基本性质", "Capacitor"]
tags: [basic_circuit_theory, ee]
up: "[[Basic Circuit Theory MOC]]"
down: ["[[Introduction to RC Circuits]]"]
related: ["[[Charge, Current, and Voltage]]", "[[RC Circuit Worked Examples]]", "[[Inductors and RL Circuits]]"]
---
# Capacitors and Their Properties

## 电容及其基本性质

> [!definition] 电容
> 电容器*存储*能量而不耗散能量；其电压*连续*变化，电流由电压的*变化率*决定。

---
## 1. 定义与单位

电容定义为：
$$
C=\frac{Q}{V}
$$

单位是法拉（$\mathrm F$）：
$$
1\ \mathrm F = 1\ \mathrm{C/V}
$$

---
## 2. 电流-电压关系

定义关系：
$$
i(t)=C\frac{dv(t)}{dt}
$$

及其积分形式：
$$
v(t)=v(t_0)+\frac{1}{C}\int_{t_0}^{t}i(\tau)\,d\tau
$$

---
## 3. 物理性质

> [!attention] 三条规则
> 1. 电容电压不能突变（在理想模型中）。
> 2. 在直流稳态下，理想电容表现为*开路*（$dv/dt=0\Rightarrow i=0$）。
> 3. 在高频下，电容更易"导通"交流。

---
## 4. 能量存储与功率

存储能量：
$$
W_C=\frac{1}{2}Cv^2
$$

瞬时功率：
$$
p(t)=v(t)i(t)
$$

理想电容既能吸收也能释放能量；平均而言它不是纯粹的耗能元件。

---
## 5. 总结

> [!attention] 电容元件
> 电容本质上是一个*电荷-电压映射加能量存储*；瞬态分析必须使用其微分/积分关系。

## 参见
- [[Charge, Current, and Voltage#2. Current]]
- [[Introduction to RC Circuits#1. The Capacitor's Current-Voltage Relation]]
- [[RC Circuit Worked Examples]]
- [[Source-Free and Driven RC Response]]
