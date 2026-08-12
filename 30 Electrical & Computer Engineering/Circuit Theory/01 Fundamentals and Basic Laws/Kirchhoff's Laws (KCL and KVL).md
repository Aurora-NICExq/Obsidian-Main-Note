---
title: "Kirchhoff's Laws (KCL and KVL)"
aliases: ["基尔霍夫定律 KCL-KVL", "基尔霍夫定律", "Kirchhoff's Laws"]
tags: [basic_circuit_theory, ee]
up: "[[Basic Circuit Theory MOC]]"
down: ["[[Voltage and Current Sources]]"]
related: ["[[Charge, Current, and Voltage]]", "[[Ohm's Law and I-V Characteristics]]", "[[Thevenin's Theorem]]", "[[Norton's Theorem]]", "[[Source Transformation and Power]]"]
---
# Kirchhoff's Laws (KCL and KVL)

## 基尔霍夫定律（KCL / KVL）

> [!definition] 所有电路方程的骨架
> **KCL** 遵循电荷守恒；**KVL** 遵循能量守恒。
> 它们共同构成了所有电路方程的基础。

---
## 1. KCL：基尔霍夫电流定律

在任何节点上，流入电流之和等于流出电流之和，通常写作：
$$
\sum i = 0
$$

> [!theorem] 基尔霍夫电流定律
> 节点上所有电流的代数和为零，因为节点不存储净电荷——
> 流入的电荷量与流出的电荷量相等（参见 [[Charge, Current, and Voltage#2. Current]]）。

![[tikz-kirchhoff-s-laws-kcl-and-kvl-01.svg]]

物理含义：节点不存储净电荷，因此"流入等于流出"。

---
## 2. KVL：基尔霍夫电压定律

在任意闭合回路中，电压的代数和为零：
$$
\sum u = 0
$$

> [!theorem] 基尔霍夫电压定律
> 电荷沿闭合回路运动一周，其势能净变化为零，因此回路中各支路电压的代数和为零。

![[tikz-kirchhoff-s-laws-kcl-and-kvl-02.svg]]

物理含义：电荷回到起点时净能量变化为零。

---
## 3. 常用联立方法

1. 用 KCL 列写节点方程（节点电压法）。
2. 或用 KVL 列写回路方程（网孔电流法）。
3. 代入元件方程（如 [[Ohm's Law and I-V Characteristics]] 中的 $u=iR$）得到可解的线性方程组。

---
## 4. 快速示例：并联电阻的等效

> [!example] 两个电阻并联
> 对于同一电压 $U$ 下的两个并联支路：
> $$
> I_1=\frac{U}{R_1},\qquad I_2=\frac{U}{R_2}
> $$
> 由 KCL：
> $$
> I=I_1+I_2=U\left(\frac{1}{R_1}+\frac{1}{R_2}\right)
> $$
> 因此：
> $$
> \frac{1}{R_{\text{eq}}}=\frac{1}{R_1}+\frac{1}{R_2}
> $$

---
## 5. 总结

> [!attention] KCL 和 KVL
> KCL 控制*电流守恒*，KVL 控制*能量平衡*；叠加元件方程即可得到完整的电路模型。

## 参见
- [[Charge, Current, and Voltage#2. Current]]
- [[Ohm's Law and I-V Characteristics]]
- [[Thevenin's Theorem]]
- [[Norton's Theorem]]
- [[Source Transformation and Power]]
