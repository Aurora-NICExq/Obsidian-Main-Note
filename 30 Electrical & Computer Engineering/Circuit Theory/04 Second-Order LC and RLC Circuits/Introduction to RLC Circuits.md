---
title: "Introduction to RLC Circuits"
aliases: ["驱动 RL 与 RLC 电路引入", "Introduction to RLC Circuits"]
tags: [basic_circuit_theory, ee]
up: "[[Basic Circuit Theory MOC]]"
down: ["[[LC Circuits and Second-Order ODEs]]"]
related: ["[[Inductors and RL Circuits]]", "[[Source-Free and Driven RL Circuits]]", "[[Driven Circuits with Initial Conditions]]", "[[First-Order Shortcut Method]]"]
---
# Introduction to RLC Circuits

## RLC 电路入门

> [!definition] 从一阶到二阶
> 受迫 RL 支路仍是一阶问题；增加第二个储能元件（$L$ 与 $C$ 共存）将电路提升至**二阶**，产生振荡行为。

---
## 1. 受迫 RL 电路

$$
I_{out}(0^-)=\frac{V_1}{R_1}
$$

$$
I_{out}(0^+)=\frac{V_1}{R_1}
$$

$$
I_{out}(\infty)=\frac{V_1}{R_1\parallel R_2}
$$

$$
\tau=\frac{L_1}{R_1\parallel R_2},\quad t>0
$$

$$
I_{out}(t)=\frac{V_1}{R_1\parallel R_2}+\left(\frac{V_1}{R_1}-\frac{V_1}{R_1\parallel R_2}\right)\exp\!\left(-\frac{t}{\tau}\right),\quad t>0
$$

![[tikz-introduction-to-rlc-circuits-01.svg]]

开关在 $t=0$ 断开后，$R_2$ 与 $R_1$ 并联呈现给电感：

![[tikz-introduction-to-rlc-circuits-02.svg]]

---
## 2. 总结表：R、C、L

| 量 | $R$ | $C$ | $L$ |
|---|---|---|---|
| 基本方程 | $V=IR$ | $I=C\dfrac{dV}{dt}$ | $V=L\dfrac{dI}{dt}$ |
| 存储能量 | — | $\tfrac{1}{2}CV^2$ | $\tfrac{1}{2}LI^2$ |
| 初始条件 | — | $V_0$ | $I_0$ |

---
## 3. RLC 电路

### 3.1 LC 电路示例

当已充电的电容连接到电感时，能量在两者之间来回交换：
$$
E_{cap}=\frac{1}{2}C_1V_0^2
$$

$$
E_{cap}=0
$$

$$
E_m=\frac{1}{2}C_1V_0^2=\frac{1}{2}L_1I^2
$$

![[tikz-introduction-to-rlc-circuits-03.svg]]

无损输出电压为持续振荡：

![[tikz-introduction-to-rlc-circuits-04.svg]]

---
## 参见
- [[Inductors and RL Circuits#RL Circuits]]
- [[Capacitors and Their Properties#4. Energy Storage and Power]]
- [[LC Circuits and Second-Order ODEs#Simple Parallel LC Circuit]]
- [[First-Order Shortcut Method]]
