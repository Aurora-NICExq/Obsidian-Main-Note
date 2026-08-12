---
title: "Dynamic Programming Part 3"
aliases:
  - "区间 DP"
  - "括号匹配"
  - "Piano"
tags:
  - Algorithms
  - DynamicProgramming
  - MIT6006
up: "[[Algorithms (CLRS) MOC]]"
down:
  - "[[Dynamic Programming Part 4]]"
related:
  - "[[Dynamic Programming Part 1]]"
  - "[[APSP and Johnson]]"
---

# Lec17 Dynamic Programming Part 3：APSP、Parens、Piano

## 本讲主线
- 本讲继续展示“状态约束与扩展”的力量。
- 官方例子包括：
  - Bellman-Ford / APSP 的 DP 视角
  - 算术表达式括号化（Parens）
  - Piano Fingering
- 重点不在背公式，而在看清：
  - 什么时候需要引入额外条件
  - 什么时候需要把状态升维

## Floyd-Warshall：APSP 的 DP 视角
- 设：

```text
D_k(u, v) = 只允许中间点来自 {1..k} 时，u 到 v 的最短距离
```

- 则递推为：

```text
D_k(u, v) = min(
  D_(k-1)(u, v),
  D_(k-1)(u, k) + D_(k-1)(k, v)
)
```

- 本质是问：
  - 最优路径是否经过第 `k` 个点？
- 复杂度：

```text
O(|V|^3)
```

- 这是全源最短路的经典 DP。

## Parenthesization
- 对算术表达式或矩阵链这类问题：
  - 需要决定如何分割一个区间
- 典型状态：

```text
x(i, j) = 子表达式 [i..j] 的最优值
```

- 递推往往是：
  - 枚举最后一次切分位置 `k`
  - 合并左右子问题结果
- 这是标准的**区间 DP + 枚举切分点**模型。

## Piano Fingering
- 给定音符序列，要给每个音符分配手指，使总演奏代价最小。
- 第一反应若只设 `x(i)`，通常信息不够，因为：
  - 下一个状态的代价依赖“当前用了哪根手指”
- 所以必须扩展状态，例如：

```text
x(i, f) = 从第 i 个音开始、且当前起始手指条件为 f 时的最小代价
```

- 这正是“状态不够，就扩展状态”的典型案例。

## 这一讲的统一抽象
- Floyd-Warshall：扩展“允许使用的中间点集合”
- Parens：扩展“当前考虑的区间”
- Piano：扩展“当前附带条件/起始手指”

## 常见信号
- 如果递推里出现一个问号，说明当前状态信息不足。
- 若同一个子问题在不同上下文下最优值不同，就必须把这个上下文纳入状态。
- 状态维度上升后，复杂度通常也会跟着上升，要同时评估可行性。

## 学习重点
- 动态规划往往不是“直接想到最终状态”，而是不断修正状态定义。
- 只要状态把未来决策所需信息装全，局部最优组合才有意义。
- 这也是 DP 最难、最有技巧性的部分。

## 相关笔记
- [[Algorithms (CLRS) MOC]]
- [[Dynamic Programming Part 4]]（下一讲）
- [[Dynamic Programming Part 1]]
- [[APSP and Johnson]]

## 复习提问
- Floyd-Warshall 的第三维 `k` 在控制什么？
- Parenthesization 为什么天然适合区间 DP？
- 为什么钢琴指法问题不能只用 `x(i)` 表示？
- DP 中“状态不够”通常会以什么形式暴露出来？
