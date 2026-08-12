---
title: "Depth-First Search"
aliases:
  - "DFS"
  - "深度优先搜索"
  - "拓扑排序"
  - "环检测"
tags:
  - Algorithms
  - Graph
  - MIT6006
up: "[[Algorithms (CLRS) MOC]]"
down:
  - "[[Weighted Shortest Paths]]"
related:
  - "[[Breadth-First Search]]"
  - "[[Dynamic Programming Part 1]]"
---

# Lec10 Depth-First Search：可达性、拓扑排序与环检测

## 本讲主线
- BFS 解决单源最短路。
- DFS 解决的不是最短路，而是更广义的**图结构分析**问题：
  - 可达性
  - 连通分量
  - 拓扑排序
  - 环检测

![[alg-depth-first-search-01.svg]]

## DFS 的基本思想
- 从源点 `s` 出发：
  - 沿一条路一直走到底
  - 走不动就回溯
  - 再找新的未探索分支
- 递归形式最自然：

```text
visit(u):
  for v in Adj(u):
    if v 未访问:
      P(v) = u
      visit(v)
```

- `P(s) = None`

## DFS 解决什么问题
- Single Source Reachability
- 返回一棵 parent tree
- 但**不保证最短路**

## 正确性直觉
- 对“从 `s` 可达且距离不超过 `k` 的点都能被访问”做归纳。
- 若点 `v` 距离为 `k+1`，则在某条最短路上存在前驱 `u`，其距离为 `k`。
- 当 DFS 访问到 `u` 时，会检查边 `(u, v)`，从而最终访问到 `v`。

## 复杂度
- 单源 DFS：
  - 每个已访问顶点只 visit 一次
  - 每条被扫描到的邻边只处理常数次
- 课程笔记把它写成 `O(|E|)`，因为它不额外给所有未达顶点填距离。
- 更常见的统一写法是：

```text
O(|V| + |E|)
```

## Full-DFS
- 若想探索整张图，而不是只看一个源点可达部分：
  - 反复从任意未访问点启动一次 DFS
- 这叫 Full-DFS。
- 总复杂度仍是：

```text
O(|V| + |E|)
```

## 连通性与连通分量
- 无向图连通：任意两点之间都存在路径。
- Connected Components：把图划分成若干极大连通块。
- 做法：
  - 运行 Full-DFS
  - 每次新启动的一轮 DFS 所访问到的点，就是一个连通分量

## 拓扑排序

### DAG
- Directed Acyclic Graph：有向无环图。

### Topological Order
- 一个顶点顺序 `f`，满足每条边 `(u, v)` 都有：

```text
f(u) < f(v)
```

### DFS 与拓扑序
- 定义 finishing order：Full-DFS 完成访问各顶点的顺序。
- 结论：

```text
若 G 是 DAG，则 finishing order 的逆序就是一个拓扑序
```

### 直觉
- 若有边 `(u, v)`：
  - 若先访问到 `u`，那么在 `u` 完成前一定会先完成 `v`
  - 若先访问到 `v`，在 DAG 中 `v` 不可能再回到 `u`
- 因此 `v` 总比 `u` 更早 finish，所以逆 finishing order 满足拓扑约束。

## 环检测
- 若 reverse finishing order 不是合法拓扑序，则图中一定有环。
- 另一种 DFS 视角：
  - 若在 DFS 过程中碰到一条指向当前祖先的边，就发现了环
- 课程中的关键命题：
  - 若图中有环，Full-DFS 一定会遍历到一条“指向祖先”的边

## 这一讲的定位
- BFS 更像“按距离推进”。
- DFS 更像“按结构深入”，因此特别适合做：
  - 拓扑排序
  - 环检测
  - 连通块划分

## 相关笔记
- [[Algorithms (CLRS) MOC]]
- [[Weighted Shortest Paths]]（下一讲）
- [[Breadth-First Search]]
- [[Dynamic Programming Part 1]]

## 复习提问
- 为什么 DFS 不能保证最短路？
- Full-DFS 为什么能求连通分量？
- 为什么 DAG 的 reverse finishing order 一定是拓扑序？
- DFS 中“遇到指向祖先的边”为什么意味着有环？
