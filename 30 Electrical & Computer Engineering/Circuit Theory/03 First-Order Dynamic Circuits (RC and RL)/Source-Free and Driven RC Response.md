---
title: "Source-Free and Driven RC Response"
aliases: ["一阶 RC 无源与受迫响应", "Source-Free and Driven Circuits"]
tags: [basic_circuit_theory, ee]
up: "[[Basic Circuit Theory MOC]]"
down: ["[[RC Circuit Worked Examples]]"]
related: ["[[Introduction to RC Circuits]]", "[[Capacitors and Their Properties]]", "[[First-Order Shortcut Method]]", "[[LC Circuits and Second-Order ODEs]]"]
---
# Source-Free and Driven RC Response

## 无源响应与受迫响应

> [!definition] 全响应
> 全响应 = **自然响应**（无源）+ **受迫响应**（由外部源驱动）。

---
## 1. 无源电路

无源电路通常指独立源置零后的响应，仅由初始存储能量（电容电压、电感电流）驱动——即**自然响应**。

对于一阶 RC 电路：
$$
v_C(t)=V_0e^{-t/\tau},\qquad \tau=RC
$$

特征：

- 响应随时间衰减，
- 幅度由初始条件确定。

---
## 2. 受迫电路

受迫电路是外部源作用下的响应。

对于直流驱动的一阶 RC 电路：
$$
v_C(t)=V_f+\big[V_0-V_f\big]e^{-t/\tau}
$$

其中 $V_f$ 是由外部源设定的最终稳态值。

![[tikz-source-free-and-driven-rc-response-01.svg]]

受迫 RC 充电方程可写为：
$$
V_1 = R_1C_1\frac{dV_{out}}{dt} + V_{out}
$$

若电容初始电压为零：
$$
V_{out}(0^+) = 0
$$

分离变量并积分：
$$
R_1C_1\frac{dV_{out}}{dt} = -V_{out} + V_1
$$

$$
\int_{0}^{V_{out}} R_1C_1\frac{dv}{-v+V_1} = \int_{0}^{t} dt
$$

$$
-R_1C_1\ln\left(\frac{V_{out}-V_1}{-V_1}\right)=t
$$

$$
\frac{V_{out}-V_1}{-V_1}=\exp\left(-\frac{t}{R_1C_1}\right)
$$

得到：
$$
V_{out}=V_1\left(1-\exp\left(-\frac{t}{R_1C_1}\right)\right)u(t)
$$

![[tikz-source-free-and-driven-rc-response-02.svg]]

---
## 3. 全响应的叠加

在线性时不变电路中：
$$
x(t)=x_n(t)+x_f(t)
$$

- $x_n(t)$ — 自然响应（齐次解），
- $x_f(t)$ — 受迫响应（特解）。

这种分解是后续二阶电路和拉普拉斯方法的统一主线。

---
## 4. 总结

> [!attention] 无源与受迫
> 对于瞬态问题，首先判断变化是由*初始存储能量*驱动还是由*外部源*推动，然后应用对应的一阶模板。

## 参见
- [[Introduction to RC Circuits]]
- [[RC Circuit Worked Examples]]
- [[Capacitors and Their Properties]]
- [[First-Order Shortcut Method]]
- [[LC Circuits and Second-Order ODEs#2nd-Order Differential Equations]]
