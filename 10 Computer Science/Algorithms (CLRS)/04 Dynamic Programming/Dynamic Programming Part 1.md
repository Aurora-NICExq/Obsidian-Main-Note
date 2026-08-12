---
title: "Dynamic Programming Part 1"
aliases:
  - "动态规划"
  - "SRTBOT"
  - "子问题 DAG"
  - "记忆化"
tags:
  - Algorithms
  - DynamicProgramming
  - MIT6006
up: "[[Algorithms (CLRS) MOC]]"
down:
  - "[[Dynamic Programming Part 2]]"
related:
  - "[[Depth-First Search]]"
  - "[[Bellman-Ford]]"
---

# Lec15 Dynamic Programming Part 1：递归算法、子问题 DAG 与 SRTBOT

## 本讲主线
- 课程从图算法切到动态规划。
- 动态规划不是“背表格”，而是把指数级递归，压缩成对子问题 DAG 的一次求值。
- 本讲重点是建立统一模板：

```text
Subproblems
Relation
Topological order
Base case
Original problem
Time
```

![[alg-dynamic-programming-part-1-01.svg]]

## 动态规划在解决什么
- 许多问题天然满足：
  - 最优解可由更小子问题组合而成
  - 朴素递归会重复求解相同子问题
- 解决办法：
  - 识别重复子问题
  - 让每个子问题只算一次

## 从递归到 DP
- 朴素递归：表达清晰，但可能指数爆炸。
- memoization：自顶向下，只在第一次访问时计算。
- tabulation：自底向上，按依赖顺序填表。
- 两者本质相同，都是在一张**子问题 DAG** 上做动态规划。

## Fib 例子
- 递归定义：

```text
F(n) = F(n-1) + F(n-2)
```

- 朴素递归会重复计算大量相同子问题，时间指数级。
- 用 memoization 或 bottom-up 表填充后：

```text
Time = O(n)
```

- 这是动态规划最基础的“去重”动机。

## DAG 例子
- 加权 DAG 最短路也可视为动态规划：
  - 子问题是“到某点的最短距离”
  - 依赖只来自拓扑序更早的顶点
- 这说明：
  - 动态规划与图算法并不分家
  - 很多 DP 本质上就是 DAG 上的路径问题

## SRTBOT 模板
- 官方用 `SRTBOT` 组织 DP 设计过程。
- 对做题最有用的不是记名字，而是记顺序：
  - 先想子问题如何缩小
  - 再写递推
  - 再确认依赖无环
  - 再给 base case
  - 最后读出原问题答案并算复杂度

## Bowling 例子
- 这类一维 DP 的典型特征：
  - 决策只影响后续一个有限窗口
  - 子问题通常可设计成前缀/后缀最优值
- 做题时优先问自己：
  - 当前位是“选”还是“不选”？
  - 选了之后会把状态推进到哪里？

## 动态规划的本质理解
- DP 不是某个具体算法，而是一类设计范式。
- 真正困难通常不在“填表”，而在：
  - 子问题怎么定义
  - 递推怎么写
  - 需要额外记录什么状态

## 本讲最该掌握的能力
- 看见指数级递归，先怀疑是否存在重复子问题。
- 能把递归关系画成子问题 DAG。
- 明白“按拓扑序求值”就是 DP 的计算核心。

## 相关笔记
- [[Algorithms (CLRS) MOC]]
- [[Dynamic Programming Part 2]]（下一讲）
- [[Depth-First Search]]
- [[Bellman-Ford]]

## 复习提问
- 动态规划和普通递归的根本区别是什么？
- 为什么 Fibonacci 是 DP 的经典入门例子？
- 为什么很多 DP 都可以看成对子问题 DAG 的求值？
- 设计 DP 时，SRTBOT 六步里哪一步最关键？
