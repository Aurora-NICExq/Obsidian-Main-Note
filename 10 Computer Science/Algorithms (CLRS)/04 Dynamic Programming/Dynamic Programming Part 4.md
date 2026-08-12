---
title: "Dynamic Programming Part 4"
aliases:
  - "背包"
  - "Subset Sum"
  - "伪多项式"
tags:
  - Algorithms
  - DynamicProgramming
  - MIT6006
up: "[[Algorithms (CLRS) MOC]]"
related:
  - "[[Dynamic Programming Part 1]]"
  - "[[Complexity]]"
---

# Lec18 Dynamic Programming Part 4：Rods、Subset Sum 与伪多项式

## 本讲主线
- 前三讲讲的是“怎样做 DP”。
- 这一讲开始问更细的问题：
  - 为什么有些 DP 看起来像多项式，其实并不是真多项式？
- 关键词是：
  - Rods
  - Subset Sum
  - Pseudopolynomial Time

## Rods / Cut Rod
- 给定一根长度为 `n` 的杆，以及不同长度切段的收益。
- 目标是决定如何切分，使总收益最大。
- 典型状态：

```text
x(i) = 长度为 i 的杆可获得的最大收益
```

- 递推：

```text
x(i) = max_{1 <= j <= i} { price(j) + x(i-j) }
```

- 复杂度通常是 `O(n^2)`。
- 这是“枚举第一刀切在哪里”的典型一维 DP。

## Subset Sum
- 输入一组整数和目标和 `T`。
- 问是否存在某个子集，使元素和恰好为 `T`。
- 典型状态：

```text
S(i, t) = 是否能用前 i 个数凑出和 t
```

- 递推：

```text
S(i, t) = S(i-1, t) or S(i-1, t-a_i)
```

- 时间复杂度常写为：

```text
O(nT)
```

## 为什么 `O(nT)` 不一定是“多项式”
- 输入目标值 `T` 时，输入长度不是 `T`，而是 `log T` 位。
- 因此 `O(nT)` 对数值本身是线性的，但对输入长度却可能是指数级。
- 这种时间复杂度称为：

```text
pseudopolynomial
```

## 伪多项式时间
- 若复杂度对输入中“数值大小”多项式，而不是对“编码长度”多项式，就叫伪多项式。
- 对应直觉：
  - 算法利用了数值很小这一事实
  - 但当数值很大、编码仍很短时，算法会爆炸

## 与复杂性理论的连接
- Subset Sum 是著名 NP-complete 问题之一。
- 它之所以还能写出 `O(nT)` 的 DP，是因为它是**弱 NP 完全**问题。
- 这也解释了：
  - 为什么某些 NP-hard/NP-complete 问题仍能写出看似“不错”的 DP
  - 但这些算法未必是真正多项式时间

## 本讲的关键意识
- 不是所有 DP 都是“高效”的。
- 做完一个 DP 后必须追问：
  - 复杂度是对什么量多项式？
  - 状态空间是否依赖于数值大小？

## 学习重点
- Rod Cutting 练的是“枚举第一步决策”的递推写法。
- Subset Sum 练的是“真假可达性 DP”。
- 伪多项式概念把 DP 与复杂性理论连了起来。

## 相关笔记
- [[Algorithms (CLRS) MOC]]
- [[Dynamic Programming Part 1]]
- [[Complexity]]

## 复习提问
- Rod Cutting 的状态和递推为什么自然？
- Subset Sum 的 `O(nT)` 为什么不是严格意义上的多项式时间？
- 什么叫伪多项式时间？
- 为什么 Subset Sum 被称为“弱 NP 完全”很重要？
