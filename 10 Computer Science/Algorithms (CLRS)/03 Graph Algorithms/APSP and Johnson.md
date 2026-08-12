---
title: "APSP and Johnson"
aliases:
  - "APSP"
  - "全源最短路"
  - "Johnson"
  - "重赋权"
tags:
  - Algorithms
  - Graph
  - MIT6006
up: "[[Algorithms (CLRS) MOC]]"
related:
  - "[[Bellman-Ford]]"
  - "[[Dijkstra]]"
  - "[[Dynamic Programming Part 3]]"
---

# Lec14 APSP and Johnson：全源最短路与重赋权

## 本讲主线
- 从单源最短路（SSSP）升级到**全源最短路（APSP）**。
- 若直接对每个源点都跑 Bellman-Ford，代价太高。
- Johnson 算法的关键想法是：
  - 先用 Bellman-Ford 计算一个势函数
  - 再把所有边重赋权成非负
  - 于是可对每个源点跑 Dijkstra

## APSP 问题
- 对每个源点 `s in V`，求所有 `delta(s, v)`。
- 输出通常是一张距离表，或者对每个源点给一棵最短路径树。

## 朴素做法

```text
对每个源点跑一次:
  Bellman-Ford -> O(|V|^2|E|)
  Dijkstra     -> O(|V|(|V|+|E|)log|V|)
```

- 若存在负边但无负环，希望既保留正确性，又利用 Dijkstra 的速度。

## Johnson 的核心思想
- 给原图加入一个超级源点 `s*`，向所有点连权重为 `0` 的边。
- 从 `s*` 跑一次 Bellman-Ford，得到每个点的势函数 `h(v)`。
- 然后重定义边权：

```text
w'(u,v) = w(u,v) + h(u) - h(v)
```

## 为什么这样有用

### 1. 保持最短路结构
- 任意路径 `P: s -> t` 在新权重下：

```text
w'(P) = w(P) + h(s) - h(t)
```

- 对固定起点终点来说，这只是加上一个常数。
- 因此哪条路径最短不会改变。

### 2. 让边权非负
- 由 Bellman-Ford 得到的 `h` 满足三角不等式形式：

```text
h(v) <= h(u) + w(u,v)
```

- 等价变形后得到：

```text
w'(u,v) >= 0
```

- 这就把问题转换成 Dijkstra 适用的情形。

## Johnson 算法流程
1. 添加超级源点 `s*`
2. 运行 Bellman-Ford，若检测到负环则直接停止
3. 计算势函数 `h(v)`
4. 用 `w'` 重新赋权
5. 对每个源点 `s` 运行一次 Dijkstra
6. 把结果转回原图距离：

```text
delta(s,t) = delta'(s,t) - h(s) + h(t)
```

## 复杂度
- 一次 Bellman-Ford：

```text
O(|V||E|)
```

- 再跑 `|V|` 次 Dijkstra（二叉堆）：

```text
O(|V|(|V|+|E|)log|V|)
```

- 对稀疏图通常优于 `|V|` 次 Bellman-Ford。

## 学习重点
- Johnson 不是“发明了新最短路算法”，而是把旧算法组合起来：
  - Bellman-Ford 负责处理负边与势函数
  - Dijkstra 负责高效求单源最短路
- 关键抽象是**重赋权不改变相对优劣，只改变绝对值**。

## 相关笔记
- [[Algorithms (CLRS) MOC]]
- [[Bellman-Ford]]
- [[Dijkstra]]
- [[Dynamic Programming Part 3]]

## 复习提问
- APSP 与 SSSP 的差别是什么？
- Johnson 为什么要添加超级源点？
- 重赋权为什么不会改变最短路本身？
- Johnson 的优势主要体现在哪类图上？
