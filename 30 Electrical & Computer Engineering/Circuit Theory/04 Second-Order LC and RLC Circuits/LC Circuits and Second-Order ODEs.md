---
title: "LC Circuits and Second-Order ODEs"
aliases: ["LC 电路与二阶微分方程", "Simple LC Circuit; 2nd-Order Diff. Equations"]
tags: [basic_circuit_theory, ee]
up: "[[Basic Circuit Theory MOC]]"
down: ["[[Ideal and Lossy LC Tanks]]"]
related: ["[[Introduction to RLC Circuits]]", "[[Inductors and RL Circuits]]", "[[Capacitors and Their Properties]]"]
---
# 简单 LC 电路与二阶微分方程

> [!definition] 二阶电路
> 具有两个独立储能元件（$L$ 和 $C$）的电路由*二阶*微分方程支配，其解可能为过阻尼、临界阻尼或欠阻尼。

## 简单并联 LC 电路

![[tikz-lc-circuits-and-second-order-odes-01.svg]]

能量在电容和电感之间振荡：初始全部存储在 $C$ 中，四分之一周期后全部转移到 $L$，然后返回：
$$
E_C=\frac{1}{2}C_1V_0^2
$$

$$
E_C=0
$$

$$
E_L=\frac{1}{2}L_1I_1^2=\frac{1}{2}C_1V_0^2
$$

![[tikz-lc-circuits-and-second-order-odes-02.svg]]

## 二阶微分方程

一般齐次二阶方程及其初始条件：
$$
a\frac{d^2y}{dt^2}+b\frac{dy}{dt}+cy=0
$$

$$
y(0)=K_1,\quad \frac{dy}{dt}(0)=K_2
$$

尝试指数试探解：
$$
y(t)=Ae^{st}
$$

$$
as^2Ae^{st}+bsAe^{st}+cAe^{st}=0
$$

得到**特征方程**：
$$
as^2+bs+c=0
$$

$$
s_{1,2}=\frac{-b\pm\sqrt{b^2-4ac}}{2a}
$$

> [!attention] 三种阻尼情况
> 判别式 $b^2-4ac$ 决定响应类型：
> $$
> \text{情况 1： } s_1\neq s_2,\ \text{均为实数},\ (b^2-4ac>0)
> $$
> $$
> \text{情况 2： } s_1=s_2=-\frac{b}{2a},\ (b^2=4ac)
> $$
> $$
> \text{情况 3： } s_1\neq s_2,\ \text{均为复数},\ (b^2-4ac<0)
> $$
> 分别对应**过阻尼**、**临界阻尼**和**欠阻尼**（振荡）响应。

对于不同的根，通解及其常数为：
$$
y(t)=A_1e^{s_1t}+A_2e^{s_2t}
$$

$$
K_1=A_1+A_2
$$

$$
K_2=A_1s_1+A_2s_2
$$

## 参见
- [[Introduction to RLC Circuits#3. RLC Circuits]]
- [[Inductors and RL Circuits#1. The Fundamental Inductor Relation]]
- [[Capacitors and Their Properties#4. Energy Storage and Power]]
- [[Ideal and Lossy LC Tanks]]
