---
title: "Weighted Shortest Paths"
aliases:
  - "加权最短路"
  - "松弛"
  - "relax"
tags:
  - Algorithms
  - Graph
  - MIT6006
up: "[[Algorithms (CLRS) MOC]]"
down:
  - "[[Bellman-Ford]]"
related:
  - "[[Breadth-First Search]]"
  - "[[Depth-First Search]]"
  - "[[Dijkstra]]"
---

# Lec11 Weighted Shortest Paths：加权最短路与松弛框架

## 本讲主线
- 从无权图最短路推广到**带权图最短路**。
- BFS 之所以成立，依赖“每条边代价都相同”；一旦边权不同，就必须改用新框架。
- 本讲建立后续 Bellman-Ford、Dijkstra、Johnson 的共同基础：**松弛（relaxation）**。

![[alg-weighted-shortest-paths-01.svg]]

## 问题定义
- 图 `G = (V, E)`，边权函数 `w(u, v)` 可以是任意实数。
- 路径权重定义为路径上所有边权之和。
- 单源最短路目标：
  - 输入源点 `s`
  - 输出每个点 `v` 的最短距离 `delta(s, v)` 及一棵最短路径树

## BFS 为什么失效
- BFS 最优性来自“路径长度 = 边数”。
- 若一条边权重很大、另一条边权重很小，最少边数不再等于最小总代价。
- 所以图搜索顺序不再是简单的按层推进，而是按**距离估计**推进。

## 松弛（Relaxation）
- 为每个点维护距离估计 `d(v)`：
  - 初始：`d(s) = 0`
  - 其余：`d(v) = infinity`
- 对一条边 `(u, v)` 执行松弛：

```text
if d(v) > d(u) + w(u, v):
  d(v) = d(u) + w(u, v)
  parent(v) = u
```

- 直觉：
  - 若“经过 `u` 再走到 `v`”更优，就更新 `v`
  - 否则保持原估计

## 松弛的核心性质
- `d(v)` 始终是 `delta(s, v)` 的上界，不会低估真正最短路。
- 若一条最短路上的边按正确顺序都被成功松弛过，那么终点距离会收敛到最优值。
- 所以后续算法的区别，本质上是：
  - **边被按什么顺序松弛**
  - **哪些点能被“最终确认”**

## 最短路径树
- 通过 `parent(v)` 记录前驱，不直接存整条路径。
- 所有前驱指针组合成一棵从 `s` 出发的最短路径树。
- 这样能在 `O(|V|)` 空间内表示全部最短路信息。

## DAG 上的加权最短路
- 若图是 DAG，可以先做拓扑排序。
- 然后按拓扑序处理顶点，并对其出边做松弛。
- 因为所有边都从前指向后，最短路依赖天然无环。
- 即使存在负权边，只要没有环，这套方法仍然成立。

## DAG 算法复杂度

```text
Topological Sort: O(|V| + |E|)
Relax all edges once: O(|E|)
Total: O(|V| + |E|)
```

- 这说明：
  - “有负权”本身不是问题
  - 真正麻烦的是“有环且权重可能为负”

## 这一讲最重要的抽象
- BFS 是无权图最短路的特例。
- 带权最短路的统一语言是：
  - 距离估计
  - 前驱树
  - 松弛
- 之后：
  - Bellman-Ford 负责“允许负边”
  - Dijkstra 负责“非负边时更快”
  - Johnson 负责“把 APSP 变成多次 SSSP”

## 相关笔记
- [[Algorithms (CLRS) MOC]]
- [[Bellman-Ford]]（下一讲）
- [[Breadth-First Search]]
- [[Depth-First Search]]
- [[Dijkstra]]

## 复习提问
- 为什么 BFS 不能直接解决带权最短路？
- 松弛操作到底在维护什么不变量？
- 为什么最短路径树只存 `parent` 就够了？
- DAG 上为何只需按拓扑序松弛一遍边？
