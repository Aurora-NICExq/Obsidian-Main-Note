---
title: "Introduction to Op Amps"
aliases: ["运算放大器入门", "Introduction to Op Amps"]
tags: [basic_circuit_theory, ee]
up: "[[Basic Circuit Theory MOC]]"
down: []
related: ["[[Voltage and Current Sources]]", "[[Kirchhoff's Laws (KCL and KVL)]]", "[[Ohm's Law and I-V Characteristics]]", "[[Source Transformation and Power]]"]
---
# Introduction to Op Amps

## 运算放大器入门

> [!definition] 运算放大器
> 运放放大两个输入端之间的*电压差*。在负反馈电路中，输出自动调整以使两个输入电压近似相等。

---
## 1. 基本放大器概念

电压增益是输出电压与输入电压的比值：
$$
A_o=\frac{V_{out}}{V_{in}}
$$

理想放大器的输入端近乎开路，因此输入电流可视为零。

![[tikz-introduction-to-op-amps-01.svg]]

---
## 2. 运放模型

运放有两个输入端：

- 同相输入端：$+$
- 反相输入端：$-$

输出电压与两个输入电压之差成正比：
$$
V_{out}=A_o(V_+-V_-)
$$

理想输入电流：
$$
i_+=i_-=0
$$

![[tikz-introduction-to-op-amps-02.svg]]

---
## 3. 两种输入配置

驱动同相输入端时，输出与输入同相：
$$
V_{out}=A_oV_{in1}
$$

驱动反相输入端时，输出相对于输入反相：
$$
V_{out}=-A_oV_{in2}
$$

由于开环增益 $A_o$ 非常大而输出摆幅受电源电压限制，实际电路使用**负反馈**来保持 $V_+$ 和 $V_-$ 接近相等。

![[tikz-introduction-to-op-amps-03.svg]]

---
## 4. 单位增益缓冲器

单位增益缓冲器将输出直接反馈至反相输入端。

负反馈迫使：
$$
V_-\approx V_+
$$

因此：
$$
V_{out}\approx V_{in}
$$

![[tikz-introduction-to-op-amps-04.svg]]

---
## 5. 同相放大器

同相放大器将输入信号接到 $+$ 端，通过 $R_1$–$R_2$ 分压器将输出反馈到 $-$ 端。

分压关系：
$$
V_- = V_{out}\frac{R_2}{R_1+R_2}
$$

负反馈近似：
$$
V_-\approx V_+=V_{in}
$$

因此闭环增益为：
$$
V_{out}\approx \left(1+\frac{R_1}{R_2}\right)V_{in}
$$

![[tikz-introduction-to-op-amps-05.svg]]

---
## 6. 总结

> [!attention] 运放
> 运放问题的关键：*输入端无电流流入*，且*负反馈下两个输入电压近似相等*；结合外部电阻网络建立方程。

## 参见
- [[Voltage and Current Sources#4. The Amplifier Viewpoint]]
- [[Kirchhoff's Laws (KCL and KVL)]]
- [[Ohm's Law and I-V Characteristics]]
- [[Source Transformation and Power]]
