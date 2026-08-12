---
title: "Driven Circuits with Initial Conditions"
aliases: ["含初始条件的受迫电路", "Driven Circuits with Initial Conditions"]
tags: [basic_circuit_theory, ee]
up: "[[Basic Circuit Theory MOC]]"
down: ["[[Introduction to RLC Circuits]]"]
related: ["[[Source-Free and Driven RC Response]]", "[[Source-Free and Driven RL Circuits]]", "[[First-Order Shortcut Method]]", "[[RC Circuit Worked Examples]]"]
---
# Driven Circuits with Initial Conditions

## 含初始条件的受迫电路

> [!definition] 一般一阶情况
> 具有非零初始条件的受迫电路是自然响应（由存储能量确定）与受迫响应（由外部源确定）的*叠加*。这是最一般的一阶情况，涵盖[[Source-Free and Driven RC Response|RC]]和[[Source-Free and Driven RL Circuits|RL]]电路。

---
## 1. $t=0^-$ 和 $t=0^+$ 的作用

开关时刻分为"前"和"后"：

- $t=0^-$ — 开关*前*的电路；求解得到存储状态（$v_C$ 或 $i_L$）。
- $t=0^+$ — 开关*后*的电路；状态变量在开关瞬间**连续**：
$$
v_C(0^+)=v_C(0^-),\qquad i_L(0^+)=i_L(0^-)
$$

其他所有量（电阻电流、源电流）可能跃变；只有电容电压和电感电流保证连续。

![[tikz-driven-circuits-with-initial-conditions-01.svg]]

---
## 2. 一般解

一旦已知初值 $x(0^+)$、终值 $x(\infty)$ 和时间常数 $\tau$，响应遵循[[First-Order Shortcut Method|通用模板]]：
$$
x(t)=x(\infty)+\big[x(0^+)-x(\infty)\big]e^{-t/\tau}
$$

非零初始条件仅通过 $x(0^+)$ 体现；源设定 $x(\infty)$。

---
## 3. 算例

> [!example] 电容已充电至 $V_0$，再由 $V_s$ 驱动
> 预充电至 $v_C(0^-)=V_0$ 的电容在 $t=0$ 时通过电阻 $R$ 切换到电源 $V_s$。
> $$
> x(0^+)=V_0,\qquad x(\infty)=V_s,\qquad \tau=RC
> $$
> $$
> v_C(t)=V_s+(V_0-V_s)e^{-t/\tau}
> $$
> 若 $V_0<V_s$ 则电容充电；若 $V_0>V_s$ 则放电趋向 $V_s$。无源情况（$V_s=0$）和零初始情况（$V_0=0$）都是此单一公式的特例。

---
## 参见
- [[Source-Free and Driven RC Response]]
- [[Source-Free and Driven RL Circuits]]
- [[Inductors and RL Circuits#Setting Initial Conditions in RL Circuits]]
- [[RC Circuit Worked Examples#2. Solution Procedure]]
- [[First-Order Shortcut Method]]
