---
title: "Ohm's Law and I-V Characteristics"
aliases: ["欧姆定律与 I-V 特性", "Ohm's law, IV characteristics"]
tags: [basic_circuit_theory, ee]
up: "[[Basic Circuit Theory MOC]]"
down: ["[[Kirchhoff's Laws (KCL and KVL)]]"]
related: ["[[Charge, Current, and Voltage]]", "[[Voltage and Current Sources]]", "[[Source Transformation and Power]]"]
---
# Ohm's Law and I-V Characteristics

## 欧姆定律与 I-V 特性

> [!definition] 两个互补的概念
> **欧姆定律**描述了*线性电阻*的比例关系；**I-V 特性**
> 描述了*任意*元件的端口关系。

---
## 1. 欧姆定律（线性电阻）

对于线性电阻元件：
$$
u=iR
$$
等效形式：
$$
i=\frac{u}{R},\qquad R=\frac{u}{i}
$$

变量含义：

- $u$ — 电阻两端的电压（$\mathrm V$），
- $i$ — 通过电阻的电流（$\mathrm A$），
- $R$ — 电阻值（$\Omega$）。

> [!theorem] 欧姆定律
> 在线性电阻中，端电压与通过它的电流成正比，比例常数为 $R$。

---
## 2. 电阻与材料参数

对于均匀导体：
$$
R=\rho\frac{L}{A}
$$

- $\rho$ — 电阻率（$\Omega\cdot m$），
- $L$ — 导体长度（越长 ⇒ 电阻 $R$ 越大），
- $A$ — 横截面积（越大 ⇒ 电阻 $R$ 越小）。

---
## 3. I-V 特性的定义

I-V 特性是元件端口电流与电压之间的函数关系：
$$
i=f(u)\quad\text{或}\quad u=g(i)
$$

线性电阻是最简单的情况：一条过原点的直线。

![[tikz-ohm-s-law-and-i-v-characteristics-01.svg]]

---
## 4. 理想电压源和电流源的 I-V 曲线

理想[[Voltage and Current Sources|电压源]]：
$$
u=U_s
$$
在 $i\!-\!u$ 平面中为一条垂直线。

理想电流源：
$$
i=I_s
$$
在 $i\!-\!u$ 平面中为一条水平线。

结论：理想源一般并不满足电阻关系 $u=iR$。

---
## 5. 何时使用欧姆定律

1. 已知三个量中的任意两个，求第三个：
$$
u=iR,\quad i=\frac{u}{R},\quad R=\frac{u}{i}
$$
2. 结合[[Kirchhoff's Laws (KCL and KVL)|KCL/KVL]]求解复杂电路。
3. 在线性化近似下估算支路电压和电流。

---
## 6. 关于非线性元件的说明

许多器件的电阻随温度、电压或电流变化而*不是*恒定的（例如灯丝）。其 I-V 曲线是一条曲线而非固定的直线。

![[tikz-ohm-s-law-and-i-v-characteristics-02.svg]]

---
## 7. 总结

> [!attention] 欧姆定律与 I-V 特性
> 欧姆定律是*线性电阻模型*，而 I-V 特性是*更一般的元件模型*。始终先判断元件是线性还是非线性的。

## 参见
- [[Charge, Current, and Voltage]]
- [[Kirchhoff's Laws (KCL and KVL)]]
- [[Voltage and Current Sources#2. Voltage Source]]
- [[Source Transformation and Power]]
