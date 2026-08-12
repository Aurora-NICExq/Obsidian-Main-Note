---
title: "Norton's Theorem"
aliases: ["诺顿等效定理", "Norton's Theorem"]
tags: [basic_circuit_theory, ee]
up: "[[Basic Circuit Theory MOC]]"
down: ["[[Capacitors and Their Properties]]"]
related: ["[[Thevenin's Theorem]]", "[[Source Transformation and Power]]", "[[Kirchhoff's Laws (KCL and KVL)]]", "[[RC Circuit Worked Examples]]"]
---
# Norton's Theorem

## 诺顿定理

> [!theorem] 诺顿定理
> 任何线性有源二端网络都可以用一个理想电流源 $I_N$ 与等效电阻 $R_N$ 的并联来替代。

![[tikz-norton-s-theorem-01.svg]]

---
## 1. 两个核心参数

| 符号 | 名称 | 典型方法 |
|---|---|---|
| $I_N$ | 诺顿电流 | 端口短路电流 $I_{sc}$ |
| $R_N$ | 诺顿电阻 | 独立源置零后从端口看入的等效电阻 |

---
## 2. 求 $I_N$（短路电流）

$$
I_N=I_{sc}=I_{ab}\big|_{\text{short}}
$$

步骤：

1. 断开负载 $R_L$。
2. 将 $a$、$b$ 两端短接。
3. 计算短路电流。

---
## 3. 求 $R_N$（等效内阻）

$R_N$ 是从 $a,b$ 端看入、独立源置零后的等效电阻。

源置零规则：

- 独立电压源 $\to$ 短路，
- 独立电流源 $\to$ 开路。

保留所有受控源，必要时施加测试源。

---
## 4. 接入负载后的分析

对于并联模型，负载电流分配关系为：
$$
I_L=I_N\frac{R_N}{R_N+R_L}
$$

负载电压为：
$$
U_L=I_LR_L=I_N\frac{R_NR_L}{R_N+R_L}
$$

---
## 5. 与戴维南等效的关系

$$
I_N=\frac{U_{th}}{R_{th}},\qquad U_{th}=I_NR_N,\qquad R_N=R_{th}
$$

---
## 6. 总结

> [!attention] 诺顿定理
> 端口短路求 $I_N$，再将源置零求 $R_N$，一个复杂网络就简化为整洁的"电流源并联电阻"模型。

## 参见
- [[Thevenin's Theorem]]
- [[Source Transformation and Power]]
- [[Kirchhoff's Laws (KCL and KVL)]]
- [[RC Circuit Worked Examples#2. Solution Procedure]]
