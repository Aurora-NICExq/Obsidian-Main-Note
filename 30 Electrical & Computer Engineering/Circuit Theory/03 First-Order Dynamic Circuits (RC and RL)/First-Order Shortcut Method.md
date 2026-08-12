---
title: "First-Order Shortcut Method"
aliases: ["一阶系统快捷法", "Shortcut Method for First-Order Systems"]
tags: [basic_circuit_theory, ee]
up: "[[Basic Circuit Theory MOC]]"
down: ["[[Inductors and RL Circuits]]"]
related: ["[[RC Circuit Worked Examples]]", "[[Source-Free and Driven RC Response]]", "[[Source-Free and Driven RL Circuits]]"]
---
# First-Order Shortcut Method

## 一阶系统快捷法

> [!theorem] 通用一阶公式
> 任何一阶量 $y(t)$（电容电压、电感电流，或节点电压与支路电流的任意线性组合）都按以下方式演化：
> $$
> y(t)=y_\infty+(y_0-y_\infty)\exp\left(-\frac{t}{\tau}\right)
> $$

---
## 1. 三个要素

应用此公式只需要三个数值：

- $y_0=y(0^+)$ — **初值**，由电容电压或电感电流的连续性求得。
- $y_\infty=y(\infty)$ — **终值**，由直流稳态（电容开路、电感短路）求得。
- $\tau$ — **时间常数**：RC 电路中 $\tau=R_{\text{eq}}C$，RL 电路中 $\tau=L/R_{\text{eq}}$。

---
## 2. 原理说明

任一阶电路的控制方程总可化为以下形式：
$$
\tau\frac{dy}{dt}+y=y_\infty ,
$$
其通解为受迫部分 $y_\infty$ 与衰减自然部分 $(y_0-y_\infty)e^{-t/\tau}$ 之和。快捷法直接读出这些常数，无需每次都重新推导微分方程（参见 [[Source-Free and Driven RC Response#3. Superposition of the Total Response]]）。

---
## 参见
- [[RC Circuit Worked Examples#1. The First-Order Template]]
- [[Source-Free and Driven RC Response#3. Superposition of the Total Response]]
- [[Inductors and RL Circuits#RL Circuits]]
- [[Source-Free and Driven RL Circuits]]
