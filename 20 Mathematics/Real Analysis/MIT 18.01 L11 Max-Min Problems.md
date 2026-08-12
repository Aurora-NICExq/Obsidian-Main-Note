---
aliases: [MIT18.1-Lec11-最大最小（Max-min Problems）, 最大最小, Max-Min Problems, Optimization]
tags: [math, single-variable-calculus]
up: "[[Single-Variable Calculus (MIT 18.01) MOC]]"
related: "[[MIT 18.01 L10 Curve Sketching]], [[MIT 18.01 L12 Related Rates]], [[Maxima and Minima (Several Variables)|极大极小问题]]"
down: "[[MIT 18.01 L12 Related Rates]]"
---
# Max-Min Problems

> [!summary] 核心结论
> 优化问题 (optimization) 的套路：建模 → 用约束消元化为单变量 → 在临界点与端点之间比较取最值。闭区间上连续函数必取得最大最小（极值定理）。

> 关键词：建模、约束消元、端点、全局最值、检验。

---

## 1. 优化问题的"骨架" (Skeleton)

1. 设变量（明确含义）；
2. 写目标函数 $f$；
3. 用约束消元，化为单变量；
4. 给定义域（端点关键）；
5. 找临界点：$f'=0$ 或不可导；
6. 比较端点与临界点的函数值。

## 2. 局部 vs 全局 (Local vs Global)

- 局部极值 (local extremum)：邻域内最值；
- 全局极值 (global extremum)：整个定义域最值；
- **极值定理 (Extreme Value Theorem)**：闭区间上连续函数必取得最大、最小值。

## 3. 例题：固定周长矩形的最大面积 (Worked Example)

约束 $2x+2y=P$，面积 $A=xy=x\big(\tfrac P2-x\big)$。由 $A'(x)=\tfrac P2-2x=0$ 得 $x=\tfrac P4$，故 $x=y$——**最优是正方形**。

## 4. 技巧：最短距离用平方 (Minimize the Square)

距离最小化常转化为"距离平方"最小化（二者单调等价），免去根号求导。

## 5. 易错点 (Pitfalls)

- 忽略端点；忘记变量非负/区间限制；得到极值点不回代解释（单位/可行性）。

> [!tip] 多元推广
> 多变量下的同类问题用偏导数与 [[Maxima and Minima (Several Variables)|二阶导检验]]、[[Lagrange Multipliers|拉格朗日乘数法]] 处理。

---

> [!important] 一句话总结
> 优化 = 建模消元 + 在临界点与端点间比较；闭区间连续性保证最值存在。
