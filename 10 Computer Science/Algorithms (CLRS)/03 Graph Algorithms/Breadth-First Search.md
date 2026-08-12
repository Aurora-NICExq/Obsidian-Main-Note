---
title: "Breadth-First Search"
aliases:
  - "BFS"
  - "广度优先搜索"
  - "无权最短路"
tags:
  - Algorithms
  - Graph
  - MIT6006
up: "[[Algorithms (CLRS) MOC]]"
down:
  - "[[Depth-First Search]]"
related:
  - "[[Weighted Shortest Paths]]"
  - "[[Dijkstra]]"
---

# Lec09 Breadth-First Search：无权图最短路

## 本讲主线
- 图算法单元开始。
- 先统一图的表示，再解决无权图中的最短路问题。
- 目标问题是：

```text
Single Source Shortest Paths (SSSP)
```

![[alg-breadth-first-search-01.svg]]

## 图的基本定义
- 图 `G = (V, E)`：
  - `V` 是顶点集合
  - `E` 是边集合
- 有向图：边是有序对 `(u, v)`
- 无向图：边是无序对 `{u, v}`
- 本课程默认 simple graph：
  - 无重边
  - 无自环

## 邻接与度
- `Adj+(u)`：从 `u` 出发能到达的邻居
- `Adj-(u)`：能到达 `u` 的邻居
- `deg(u)`：邻接点数量

## 图的表示
- 通常用一个映射 `Adj` 把顶点映射到邻接表。
- 顶点编号连续时可用数组；否则常用哈希表。
- 总空间：

```text
Theta(|V| + |E|)
```

- 因此图算法中的“线性时间”通常指：

```text
Theta(|V| + |E|)
```

## 路径与距离
- path：顶点序列，相邻顶点之间都有边
- path length：边数
- `delta(u, v)`：从 `u` 到 `v` 的最短路径长度
- 若不可达，则记作 `infinity`

## 重要问题层次
- Single Pair Reachability
- Single Pair Shortest Path
- Single Source Shortest Paths

本讲直接给出能解决最强版本的算法：BFS。

## 最短路径树（Shortest Paths Tree）
- 若要为源点 `s` 到每个点都返回一条最短路，不能真的把所有路径完整存下来，否则可能爆到 `Omega(|V|^2)`。
- 更好的表示：
  - 存 `P(v)`：最短路中 `v` 的前驱
  - 存 `delta(s, v)`：最短距离
- 这些 parent 指针组成一棵最短路径树。

## BFS 的核心思想
- 按照“与源点距离递增”的顺序扩展顶点。
- 可以理解成逐层扫描 level sets：

```text
L0 = {s}
L1 = 与 s 距离为 1 的点
L2 = 与 s 距离为 2 的点
...
```

- 实现上通常等价于队列版 BFS。

## BFS 不变式
- 当准备处理第 `i` 层时：
  - 所有更浅层 `L0 ... L(i-1)` 的距离和父指针都已经正确
- 处理 `Li` 的方法：
  - 枚举 `L(i-1)` 中每个点 `u`
  - 对每个尚未访问的邻居 `v`：
    - 设 `delta(s, v) = i`
    - 设 `P(v) = u`
    - 加入 `Li`

## 为什么 BFS 求得的是最短路
- BFS 第一次发现一个点 `v` 时，必然是通过最少边数到达的。
- 因为它是按层扩展的：
  - 先把距离 0 的点处理完
  - 再处理距离 1
  - 再处理距离 2
- 所以“第一次到达”就已经是最短距离。

## 复杂度
- 每个顶点最多入队/入层一次。
- 每条边最多被扫描常数次。
- 因此：

```text
BFS = O(|V| + |E|)
```

## 应用范围
- 无权图最短路
- 单源可达性
- 构造最短路径树
- 分层遍历图

## 易混点
- BFS 解决的是**无权图**或**等权边图**上的最短路。
- 一旦边权不同，就不能直接用 BFS。

## 相关笔记
- [[Algorithms (CLRS) MOC]]
- [[Depth-First Search]]（下一讲）
- [[Weighted Shortest Paths]]
- [[Dijkstra]]

## 复习提问
- 为什么图通常用邻接表而不是邻接矩阵？
- BFS 的“层”为什么对应最短距离？
- 为什么第一次访问一个点时就能确定它的最短距离？
- BFS 的 `O(|V| + |E|)` 是怎么数出来的？
