---
title: "Thevenin's Theorem"
aliases: ["戴维南等效定理", "Thevenin's Theorem"]
tags: [basic_circuit_theory, ee]
up: "[[Basic Circuit Theory MOC]]"
down: ["[[Norton's Theorem]]"]
related: ["[[Source Transformation and Power]]", "[[Kirchhoff's Laws (KCL and KVL)]]", "[[RC Circuit Worked Examples]]"]
---
# Thevenin's Theorem

## 戴维南定理

> [!theorem] 戴维南定理
> 任何线性有源二端网络都可以用一个理想电压源 $U_{th}$ 与等效电阻 $R_{th}$ 的串联来替代。

![[tikz-thevenin-s-theorem-01.svg]]

---
## 1. 两个核心参数

| 符号 | 名称 | 典型方法 |
|---|---|---|
| $U_{th}$ | 戴维南电压 | 端口开路电压 $U_{ab}$ |
| $R_{th}$ | 戴维南电阻 | 独立源置零后从端口看入的等效电阻 |

---
## 2. 求 $U_{th}$（开路电压）

$$
U_{th}=U_{ab}\big|_{\text{open}}
$$

步骤：

1. 断开负载 $R_L$。
2. 计算 $a$、$b$ 两端之间的电压。

---
## 3. 求 $R_{th}$（等效内阻）

$R_{th}$ 是从 $a,b$ 端看入、独立源置零后的等效电阻。

源置零规则：

- 独立电压源 $\to$ 短路，
- 独立电流源 $\to$ 开路。

当存在受控源时，保留受控源并施加测试源来求等效电阻。

---
## 4. 接入负载后的分析

简化后得到一个简单的串联回路：
$$
I=\frac{U_{th}}{R_{th}+R_L}
$$
$$
U_L=IR_L=U_{th}\frac{R_L}{R_{th}+R_L}
$$

---
## 5. 与诺顿等效的关系

$$
I_N=\frac{U_{th}}{R_{th}},\qquad U_{th}=I_NR_N,\qquad R_{th}=R_N
$$

---
## 6. 总结

> [!attention] 戴维南定理
> 开路求 $U_{th}$，再将源置零求 $R_{th}$，一个复杂网络就简化为整洁的"电压源串联电阻"模型。

## 参见
- [[Norton's Theorem]]
- [[Source Transformation and Power]]
- [[Kirchhoff's Laws (KCL and KVL)]]
- [[RC Circuit Worked Examples#2. Solution Procedure]]
