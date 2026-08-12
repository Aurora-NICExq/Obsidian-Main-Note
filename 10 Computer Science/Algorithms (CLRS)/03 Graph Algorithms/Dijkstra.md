---
title: "Dijkstra"
aliases:
  - "Dijkstra"
  - "非负权最短路"
  - "贪心"
tags:
  - Algorithms
  - Graph
  - MIT6006
up: "[[Algorithms (CLRS) MOC]]"
down:
  - "[[APSP and Johnson]]"
related:
  - "[[Weighted Shortest Paths]]"
  - "[[Bellman-Ford]]"
  - "[[Binary Heaps]]"
---

# Lec13 Dijkstra：非负权图上的贪心最短路

## 本讲主线
- 若边权都非负，就不必像 Bellman-Ford 那样反复全图扫描。
- 可以用贪心策略：每次确认当前距离估计最小的顶点。
- 这就是 Dijkstra 算法。

![[alg-dijkstra-01.svg]]

## 适用条件
- 所有边权满足：

```text
w(u, v) >= 0
```

- 一旦出现负边，Dijkstra 的贪心正确性就会失效。

## 贪心思想
- 维护两类点：
  - 已确定最短距离的点
  - 尚未确定的点
- 每次从未确定点中取 `d(v)` 最小者，将其“定型”。
- 然后只需用它去松弛相邻边。

## 为什么能定型
- 因为所有边权非负。
- 若某点 `u` 已经是当前未确定点中距离估计最小的，那么任何“绕远后再回来”的路径都不会更短。
- 所以一旦 `u` 被取出，它的 `d(u)` 就已经是真实最短距离。

## 数据结构
- 核心操作是反复取最小距离估计点。
- 因此需要 **min-priority queue**：
  - `extract_min`
  - `decrease_key` 或等价更新

## 算法流程

```text
initialize d(s)=0, others=infinity
put all vertices in min-priority queue
while queue not empty:
  u = extract_min()
  for each (u,v) in Adj(u):
    relax(u,v)
```

- 被 `extract_min` 拿出的点，就加入“已定型集合”。

## 正确性直觉
- 设 `u` 是当前队列里 `d` 最小的点。
- 若存在一条更短路径到 `u`，那么在该路径上，某个尚未定型的前驱点的距离应更小。
- 这与 `u` 是最小估计点矛盾。
- 非负边权是这一步成立的关键。

## 复杂度
- 若图用邻接表，优先队列用二叉堆：

```text
O((|V| + |E|) log |V|)
```

- 相比 Bellman-Ford 的 `O(|V||E|)`，在稀疏图上快得多。

## 与 Bellman-Ford 的对比

```text
Bellman-Ford:
  允许负边
  能检测负环
  O(|V||E|)

Dijkstra:
  要求非负边
  不能处理负边
  O((|V|+|E|)log|V|)
```

## 易错点
- Dijkstra 不是“边权越小先走哪条边”，而是“当前源点到哪个顶点的距离估计最小，就先定哪个点”。
- 负边哪怕只有一条，也可能破坏算法。
- BFS 可以看成“所有边权都等于 1 的 Dijkstra 特例”。

## 相关笔记
- [[Algorithms (CLRS) MOC]]
- [[APSP and Johnson]]（下一讲）
- [[Weighted Shortest Paths]]
- [[Bellman-Ford]]
- [[Binary Heaps]]

## 复习提问
- Dijkstra 的贪心选择到底是什么？
- 为什么非负边是正确性的必要条件？
- 优先队列在 Dijkstra 中承担什么角色？
- BFS 与 Dijkstra 的关系是什么？
