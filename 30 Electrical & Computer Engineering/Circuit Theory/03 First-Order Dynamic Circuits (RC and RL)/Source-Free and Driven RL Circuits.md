---
title: "Source-Free and Driven RL Circuits"
aliases: ["RL 无源与受迫响应", "Source-Free and Driven RL Response"]
tags: [basic_circuit_theory, ee]
up: "[[Basic Circuit Theory MOC]]"
down: ["[[Driven Circuits with Initial Conditions]]"]
related: ["[[Inductors and RL Circuits]]", "[[First-Order Shortcut Method]]", "[[Source-Free and Driven RC Response]]", "[[Introduction to RLC Circuits]]"]
---
# Source-Free and Driven RL Circuits

## 无源与受迫 RL 电路

> [!definition] RL 是 RC 的对偶
> RL 电路由电感关系 $v_L=L\,di/dt$ 支配。其自然响应是**电流**的指数衰减，恰好与[[Source-Free and Driven RC Response|RC 电路]]中**电压**的指数衰减对偶。

---
## 1. 无源 RL 响应

将独立源置零，使电感携带初始电流 $I_0$。在电感 $L$ 两端接单个电阻 $R$ 的情况下：

![[tikz-source-free-and-driven-rl-circuits-01.svg]]

回路 KVL 给出一个一阶齐次方程：
$$
L\frac{di}{dt}+Ri=0
$$

因此：
$$
\frac{di}{dt}=-\frac{R}{L}\,i,\qquad \tau=\frac{L}{R}
$$

由 $i(0)=I_0$ 得解为衰减指数：
$$
i(t)=I_0\,e^{-t/\tau}=I_0\,e^{-(R/L)t}
$$

> [!attention] 电感电流连续性
> 电感电流不能跃变，因此 $i(0^+)=i(0^-)=I_0$。从开关*前*的电路确定 $I_0$（参见 [[Inductors and RL Circuits#Setting Initial Conditions in RL Circuits]]）。

---
## 2. 受迫 RL 响应

现在施加直流源，使电流趋近于非零终值 $I_f$。利用[[First-Order Shortcut Method|一阶模板]]：
$$
i(t)=I_f+\big(I_0-I_f\big)e^{-t/\tau},\qquad \tau=\frac{L}{R_{\text{eq}}}
$$

- $I_0=i(0^+)$ — 初始电感电流（连续），
- $I_f=i(\infty)$ — 终值，在直流稳态下将电感视为*短路*求得，
- $R_{\text{eq}}$ — 从电感端看入、源置零后的电阻。

---
## 3. 算例

> [!example] RL 支路阶跃接通
> 电源 $V_1$ 驱动 $R_1$ 与 $L_1$ 串联，在 $t=0$ 时合闸，$i(0^-)=0$。
> $$
> I_f=\frac{V_1}{R_1},\qquad \tau=\frac{L_1}{R_1}
> $$
> $$
> i(t)=\frac{V_1}{R_1}\left(1-e^{-t/\tau}\right)u(t)
> $$
> 电流从 $0$ 上升至 $V_1/R_1$，在 $t=\tau$ 时达到约 $63\%$ 的终值。

---
## 参见
- [[Inductors and RL Circuits#RL Circuits]]
- [[First-Order Shortcut Method]]
- [[Source-Free and Driven RC Response]]
- [[Introduction to RLC Circuits]]
