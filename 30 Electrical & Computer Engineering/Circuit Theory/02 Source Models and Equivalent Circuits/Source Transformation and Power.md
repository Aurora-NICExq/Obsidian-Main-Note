---
title: "Source Transformation and Power"
aliases: ["电源变换与功率", "Source Transformation, Power"]
tags: [basic_circuit_theory, ee]
up: "[[Basic Circuit Theory MOC]]"
down: ["[[Thevenin's Theorem]]"]
related: ["[[Voltage and Current Sources]]", "[[Kirchhoff's Laws (KCL and KVL)]]", "[[Thevenin's Theorem]]", "[[Norton's Theorem]]"]
---
# Source Transformation and Power

## 电源变换与功率

> [!definition] 两个常用工具
> 电阻串联的电压源与电阻并联的电流源可以互换；功率的符号表示元件是*吸收*还是*提供*能量。

---
## 1. 电源变换

等效关系：

- 电压源 $V_s$ 串联电阻 $R$，与
- 电流源 $I_s$ 并联同一电阻 $R$ 等效。

转换公式：
$$
I_s=\frac{V_s}{R},\qquad V_s=I_sR
$$

> [!attention] 仅端口等效
> 这种等效仅对*外部端口行为*成立；内部变量不必相同。

---
## 2. 功率与无源符号约定

瞬时功率定义为：
$$
p=ui
$$

在无源符号约定下：

- $p>0$：元件**吸收**功率，
- $p<0$：元件**提供**功率。

---
## 3. 电阻中的功率

对于电阻：
$$
p_R=i^2R=\frac{u^2}{R}\ge 0
$$

因此理想电阻只耗散能量，从不存储能量。

---
## 4. 确定电源功率

电源元件可正可负：

- 电池放电：通常 $p<0$（提供能量），
- 电池充电：可能 $p>0$（吸收能量）。

> [!attention] 安全步骤
> 首先确定电压和电流的一致参考方向，然后直接代入 $p=ui$ 并读取符号。

---
## 5. 总结

> [!attention] 电源变换与功率
> 先用电源变换简化电路，再用 $p=ui$ 判断能量流动方向——这是电路分析中的高频组合操作。

## 参见
- [[Voltage and Current Sources]]
- [[Kirchhoff's Laws (KCL and KVL)]]
- [[Thevenin's Theorem#5. Relation to the Norton Equivalent]]
- [[Norton's Theorem#5. Relation to the Thevenin Equivalent]]
