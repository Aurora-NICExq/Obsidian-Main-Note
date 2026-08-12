---
title: "Dynamic Programming Part 2"
aliases:
  - "LCS"
  - "LIS"
  - "状态扩展"
tags:
  - Algorithms
  - DynamicProgramming
  - MIT6006
up: "[[Algorithms (CLRS) MOC]]"
down:
  - "[[Dynamic Programming Part 3]]"
related:
  - "[[Dynamic Programming Part 1]]"
---

# Lec16 Dynamic Programming Part 2：LCS、LIS 与状态扩展

## 本讲主线
- 这一讲在 DP 基础模板上继续推进：
  - 从单序列走向多序列
  - 从前缀问题走向子串/区间问题
  - 从“只求值”走向“恢复解”
- 官方例子是：
  - LCS
  - LIS
  - Coins

## LCS：Longest Common Subsequence
- 输入两个序列 `A` 和 `B`。
- 子问题常定义为：

```text
L(i, j) = A[:i] 与 B[:j] 的最长公共子序列长度
```

- 递推：

```text
if A[i-1] == B[j-1]:
  L(i,j) = 1 + L(i-1,j-1)
else:
  L(i,j) = max(L(i-1,j), L(i,j-1))
```

- 复杂度：

```text
O(nm)
```

- 这是典型的二维 DP。

## Parent Pointers
- 只算最优值不够时，要记录“最优解来自哪一步”。
- 对 LCS，通常额外记录：
  - 是来自左上
  - 还是上方
  - 还是左方
- 然后可从终点反向恢复一条具体最优解。

## LIS：Longest Increasing Subsequence
- 目标：找一个严格递增的最长子序列。
- 经典 DP 设计：

```text
x(i) = 以第 i 个元素结尾的 LIS 长度
```

- 递推：

```text
x(i) = 1 + max{x(j) | j < i and A[j] < A[i]}
```

- 总复杂度 `O(n^2)`。
- 这一例子说明：
  - 子问题不一定是“前缀整体最优”
  - 也可以是“带约束的局部最优”

## Coins：区间状态
- 课程中的 coins 例子强调：
  - 状态有时不能只用一个下标表示
  - 必须把“剩余区间”也编码进状态
- 例如对区间 `[i, j]` 定义最优值：

```text
x(i, j)
```

- 这是从前缀 DP 迈向区间 DP 的关键一步。

## 状态扩展的含义
- 若现有状态不足以写出正确递推，就要**扩展状态**。
- 典型症状：
  - 递推式里出现“未知的上下文”
  - 你需要知道前一个选择、当前区间、起始条件等额外信息

## 本讲建立的两个能力
- 会设计二维状态：
  - 双序列 DP
  - 区间 DP
- 会记录 parent pointers：
  - 不只求最优值
  - 还能恢复一条最优解

## 学习重点
- DP 的难点常在“怎么定义状态”，不是“怎么写循环”。
- 一旦状态正确定义，递推和拓扑顺序通常会自然出现。
- 父指针思想和图最短路中的前驱树是同一类结构。

## 相关笔记
- [[Algorithms (CLRS) MOC]]
- [[Dynamic Programming Part 3]]（下一讲）
- [[Dynamic Programming Part 1]]

## 复习提问
- LCS 的二维状态为什么自然？
- LIS 为什么不能只看“前缀最优值”？
- 什么情况下应该扩展 DP 状态？
- parent pointers 在 DP 中和在图算法中有什么共性？
