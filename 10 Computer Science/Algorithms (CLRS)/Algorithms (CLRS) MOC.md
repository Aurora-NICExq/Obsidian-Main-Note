---
title: "Algorithms (CLRS) MOC"
aliases:
  - "Algorithms MOC"
  - "算法导论 MOC"
  - "MIT 6.006"
  - "算法导论"
tags:
  - Algorithms
  - MIT6006
  - MOC
down:
  - "[[Algorithms and Computation]]"
  - "[[Data Structures]]"
  - "[[Sorting]]"
  - "[[Hashing]]"
  - "[[Linear Sorting]]"
  - "[[Binary Trees Part 1]]"
  - "[[Binary Trees Part 2 AVL]]"
  - "[[Binary Heaps]]"
  - "[[Breadth-First Search]]"
  - "[[Depth-First Search]]"
  - "[[Weighted Shortest Paths]]"
  - "[[Bellman-Ford]]"
  - "[[Dijkstra]]"
  - "[[APSP and Johnson]]"
  - "[[Dynamic Programming Part 1]]"
  - "[[Dynamic Programming Part 2]]"
  - "[[Dynamic Programming Part 3]]"
  - "[[Dynamic Programming Part 4]]"
  - "[[Complexity]]"
  - "[[Course Review]]"
  - "[[Algorithms Next Steps]]"
related:
  - "[[C_DataStruct MOC]]"
  - "[[Rust MOC]]"
---

# Algorithms (CLRS) MOC

MIT 6.006 *Introduction to Algorithms*（[OCW Spring 2020](https://ocw.mit.edu/courses/6-006-introduction-to-algorithms-spring-2020/)）的学习笔记，共 21 讲。教材对应 CLRS。

## 学习顺序

![[alg-algorithms-clrs-moc-01.svg]]

## 一 · 基础（L01–L05） → `01 Foundations/`

- [[Algorithms and Computation]]：问题 vs 算法、Word-RAM 模型、渐进复杂度、归纳法证正确性
- [[Data Structures]]：接口 vs 实现、静态数组/链表/动态数组、摊还分析
- [[Sorting]]：选择/插入/归并、递归树、比较排序的 `Omega(n log n)` 下界
- [[Hashing]]：链地址法、全域哈希、期望 `O(1)` 的代价与前提
- [[Linear Sorting]]：计数排序与基数排序 —— 放弃比较才能突破下界

## 二 · 树与堆（L06–L08） → `02 Trees and Heaps/`

- [[Binary Trees Part 1]]：遍历序、子树大小、从高度 `h` 到有序集合与序列接口
- [[Binary Trees Part 2 AVL]]：平衡条件、四种旋转、为什么高度是 `O(log n)`
- [[Binary Heaps]]：数组隐式表示、下沉、建堆为何是 `O(n)`、堆排序

## 三 · 图算法（L09–L14） → `03 Graph Algorithms/`

- [[Breadth-First Search]]：按层扩展、FIFO 与最短路的对应
- [[Depth-First Search]]：边的四种分类、环检测、拓扑排序 = 完成时间逆序
- [[Weighted Shortest Paths]]：松弛框架、五类图对应五种算法
- [[Bellman-Ford]]：按边数分层的 DP、`|V|-1` 轮、负环检测
- [[Dijkstra]]：非负权下的贪心、为什么负权会破坏它、优先队列的选择
- [[APSP and Johnson]]：全源最短路、超级源点与重赋权

## 四 · 动态规划（L15–L18） → `04 Dynamic Programming/`

- [[Dynamic Programming Part 1]]：SRTBOT 六步、子问题 DAG、记忆化 vs 填表
- [[Dynamic Programming Part 2]]：LCS、LIS、状态扩展
- [[Dynamic Programming Part 3]]：区间 DP —— APSP、Parens、Piano
- [[Dynamic Programming Part 4]]：Rods、Subset Sum、伪多项式的含义

## 五 · 复杂度与回顾（L19–L21） → `05 Complexity and Review/`

- [[Complexity]]：`P`/`NP`/`EXP`/`R`、规约的方向、NP-hard 与 NP-complete
- [[Course Review]]：把整门课串成一条线
- [[Algorithms Next Steps]]：从课程方法到算法研究、6.046 的入口

## 贯穿全课的三条主线

1. **先定接口，再选数据结构。** 「要支持哪些操作」决定「用什么结构」，而不是反过来。排序、树、堆、图、DP 全都是这套框架的实例；`Data Structures` 那一讲给出的操作代价表，是整门课的原点。
2. **最短路只有一个动作：松弛。** BFS、DAG 松弛、Dijkstra、Bellman-Ford 的差别**只在松弛的顺序和次数**。图的性质（有无权、有无负边、有无环）决定用哪个，而不是「哪个更快」。
3. **SRTBOT 六步里只有第一步难。** 子问题定对了，递推、拓扑序、边界、原问题、复杂度都几乎是自动的。DP 的本质是在子问题 DAG 上做记忆化的 DFS —— 与图算法是同一件事。

## 相关

- [[C_DataStruct MOC]]：同样的数据结构，用 C 从零实现的版本
- [[Rust MOC]]：所有权模型下这些结构的写法差异
- `Complexity.md` 里的 NP-hard 讨论可接 6.046 *Design and Analysis of Algorithms*

## 插图（预生成 SVG）

全部插图为 TikZ 预生成的 SVG，存放在 `90 Assets/diagrams/algorithms/`，以 `![[alg-….svg]]` 嵌入。
可编辑源在 `90 Assets/scripts/algorithms/sources/`，重新生成（本机 TeX Live，全离线）：

```bash
cd "90 Assets/scripts/algorithms" && python3 generate_all.py
```
