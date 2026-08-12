---
title: "Introduction to RC Circuits"
aliases: ["RC 电路入门", "RC Transient"]
tags: [basic_circuit_theory, ee]
up: "[[Basic Circuit Theory MOC]]"
down: ["[[Source-Free and Driven RC Response]]"]
related: ["[[Capacitors and Their Properties]]", "[[RC Circuit Worked Examples]]", "[[First-Order Shortcut Method]]"]
---
# Introduction to RC Circuits

## RC 电路入门：电容瞬态响应

> [!definition] 一阶 RC 行为
> 一阶 RC 电路遵循一阶微分方程；其特征解为指数衰减或指数趋近于终值。

---
## 1. 电容的电流-电压关系

电容电流与其电压变化率成正比：
$$
I=C\frac{dV}{dt}
$$

采用相反的参考方向时写作：
$$
I=-C\frac{dV}{dt}
$$

两种形式仅符号约定不同；物理本质相同。

![[tikz-introduction-to-rc-circuits-01.svg]]

---
## 2. 简单 RC 放电模型

设电容器 $C_1$ 初始电压为 $V_0$，与电阻 $R_1$ 构成回路；记输出电压为 $V_{out}(t)$。

![[tikz-introduction-to-rc-circuits-02.svg]]

---
## 3. 建立方程并积分

结合电阻和电容的关系：
$$
\frac{V_{out}}{R_1}=-C_1\frac{dV_{out}}{dt}
$$

分离变量：
$$
dt=-R_1C_1\frac{dV_{out}}{V_{out}}
$$

积分（$t:0\to t,\;V_{out}:V_0\to V_{out}$）：
$$
\int_0^t dt=-R_1C_1\int_{V_0}^{V_{out}}\frac{dV_{out}}{V_{out}}
$$

得到：
$$
t=-R_1C_1\left[\ln V_{out}-\ln V_0\right]
$$
$$
t=-R_1C_1\ln\left(\frac{V_{out}}{V_0}\right)
$$

整理为显式解：
$$
V_{out}=V_0\exp\left(-\frac{t}{R_1C_1}\right)
$$

---
## 4. 时间常数与物理含义

定义时间常数：
$$
\tau=R_1C_1
$$

于是：
$$
V_{out}(t)=V_0e^{-t/\tau}
$$

关键点：

- $t=0$：$V_{out}=V_0$
- $t=\tau$：$V_{out}=V_0/e\approx0.368V_0$
- $t\to\infty$：$V_{out}\to0$
- 工程实践中 $t\approx5\tau$ 是接近稳态的经验法则。

电流大小也呈指数衰减：
$$
|i(t)|=\frac{V_0}{R_1}e^{-t/\tau}
$$

---
## 5. 波形草图

![[tikz-introduction-to-rc-circuits-03.svg]]

---
## 6. 总结

> [!attention] RC 瞬态
> RC 电路本质上是一个*带时间常数的一阶系统*；变化率由 $\tau=RC$ 决定。

## 参见
- [[Capacitors and Their Properties#2. Current-Voltage Relation]]
- [[RC Circuit Worked Examples#1. The First-Order Template]]
- [[Source-Free and Driven RC Response]]
- [[First-Order Shortcut Method]]
