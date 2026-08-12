---
title: "Bellman-Ford"
aliases:
  - "Bellman-Ford"
  - "负权边"
  - "负环检测"
tags:
  - Algorithms
  - Graph
  - MIT6006
up: "[[Algorithms (CLRS) MOC]]"
down:
  - "[[Dijkstra]]"
related:
  - "[[Weighted Shortest Paths]]"
  - "[[APSP and Johnson]]"
  - "[[Dynamic Programming Part 1]]"
---

# Lec12 Bellman-Ford：负权边、边数分层与负环检测

## 本讲主线
- 上一讲建立了松弛框架，这一讲处理**带环且允许负权边**的情形。
- Bellman-Ford 的关键不是贪心，而是“按边数逐步逼近最短路”。
- 它还能顺带检测**负权环**。

![[alg-bellman-ford-01.svg]]

## 使用前提
- 可以有负权边。
- 但若从源点可达的负权环存在，则“最短路”根本没有定义：
  - 因为可以反复绕环让路径代价无限下降。

## 核心思想
- 任何最短简单路径最多只包含 `|V| - 1` 条边。
- 因此只要我们逐轮放宽“允许使用的边数”，最终就会覆盖所有最短简单路径。

## 动态规划视角
- 定义 `d_i(v)`：
  - 从 `s` 到 `v`、最多使用 `i` 条边的最短距离
- 则有递推：

```text
d_i(v) = min(
  d_(i-1)(v),
  min_{(u,v) in E} d_(i-1)(u) + w(u,v)
)
```

- Bellman-Ford 的原地实现，就是把这套递推压缩成反复扫描所有边。

## 算法流程

```text
initialize d(s)=0, others=infinity
repeat |V|-1 times:
  for each edge (u,v):
    relax(u,v)
```

- 最后再多扫一轮所有边：
  - 如果还能继续松弛，说明存在从 `s` 可达的负权环

## 为什么 `|V|-1` 轮足够
- 若一条最短路径是简单路径，则边数最多 `|V|-1`。
- 每一轮相当于允许再多用一条边。
- 所以 `|V|-1` 轮后，所有最短简单路径的影响都已传播完成。

## 正确性抓手
- 上界性质：`d(v)` 永远不会小于真实最短路。
- 路径松弛性质：若某条最短路上的边按顺序被成功松弛，终点会变成最优值。
- 经过足够轮数后，每条最短简单路径上的边都等价于被“按顺序传播”了一次。

## 负环检测
- 如果第 `|V|` 轮还能改进某个 `d(v)`，说明存在一条更短路径使用了至少 `|V|` 条边。
- 根据抽屉原理，这条路径必然重复顶点，包含一个环。
- 又因为距离还能继续下降，这个环必须是负权环。

## 复杂度

```text
Time: O(|V||E|)
Space: O(|V|)
```

- 比 Dijkstra 慢，但适用范围更广。

## 适用场景
- 图中存在负边。
- 需要判断是否存在负环。
- Johnson 算法中的第一步也要调用 Bellman-Ford。

## 学习重点
- Bellman-Ford 不是“盲扫边”，而是在做一种**按路径长度分层的动态规划**。
- 负权边不可怕；真正危险的是负权环。
- 只要问题仍然有定义，Bellman-Ford 就能稳定工作。

## 相关笔记
- [[Algorithms (CLRS) MOC]]
- [[Dijkstra]]（下一讲）
- [[Weighted Shortest Paths]]
- [[APSP and Johnson]]
- [[Dynamic Programming Part 1]]

## 复习提问
- 为什么最短简单路径最多只有 `|V|-1` 条边？
- Bellman-Ford 的每一轮在“多允许”什么？
- 为什么多扫一轮还能更新，就意味着有负环？
- Bellman-Ford 与 DAG 最短路在思想上有什么共同点？
