---
title: "Binary Heaps"
aliases:
  - "二叉堆"
  - "优先队列"
  - "堆排序"
  - "建堆"
tags:
  - Algorithms
  - Heap
  - MIT6006
up: "[[Algorithms (CLRS) MOC]]"
related:
  - "[[Data Structures]]"
  - "[[Sorting]]"
  - "[[Dijkstra]]"
---

# Lec08 Binary Heaps：优先队列与堆排序

## 本讲主线
- 从 set 缩到一个更专门的接口：priority queue。
- 目标是：
  - `insert`
  - `find_max`
  - `delete_max`
- 希望结构简单、排序原地、复杂度达到 `O(n log n)`。

![[alg-binary-heaps-01.svg]]

## Priority Queue 接口
- `build(X)`
- `insert(x)`
- `find_max()`
- `delete_max()`

## Priority Queue Sort 视角
- 任何优先队列都可以变成排序算法：
  - 先 build
  - 再重复 `delete_max`
- 这是一种非常有用的统一视角：
  - 无序数组 PQ -> selection sort
  - 有序数组 PQ -> insertion sort
  - AVL PQ -> AVL sort
  - heap PQ -> heap sort

## 两个数组极端

### 无序数组
- `insert` 快：尾插摊还 `O(1)`
- `delete_max` 慢：要扫描找最大值，`O(n)`

### 有序数组
- `delete_max` 快：删末尾摊还 `O(1)`
- `insert` 慢：要把新元素挪到正确位置，`O(n)`

### 启发
- 我们想在两者之间找到折中。

## 把数组看成完全二叉树
- 数组可以隐式表示 complete binary tree。
- 索引关系：

```text
left(i)   = 2i + 1
right(i)  = 2i + 2
parent(i) = floor((i - 1) / 2)
```

- 完全二叉树高度是 `Theta(log n)`，天然足够矮。

## Max-Heap Property
- 对每个节点 `i`：

```text
Q[i] >= Q[left(i)] and Q[i] >= Q[right(i)]
```

- 这个性质只要求“局部父子有序”。
- 但由归纳可推出：任意节点都不小于其子树中的所有节点。
- 特别地，根节点就是全局最大值。

## Heap Insert
- 新元素先追加到数组尾部，对应完全二叉树中新叶子。
- 然后执行 `heapify_up`：
  - 若比父节点大，就交换
  - 直到满足堆性质或到达根
- 因为最多上升一条根路径，所以：

```text
insert = O(log n)
```

## Heap Delete Max
- 最大值在根，但动态数组最容易删除的是尾部。
- 所以先把根和末尾交换，再删除末尾元素。
- 然后对根做 `heapify_down`：
  - 与较大的孩子交换
  - 直到恢复堆性质
- 同理复杂度：

```text
delete_max = O(log n)
```

## Heap Sort
- 把堆接入 priority queue sort：
  - 建堆
  - 反复删除最大值
- 单次删最大是 `O(log n)`，总共 `n` 次，因此：

```text
O(n log n)
```

## In-place Heap Sort
- 把“堆”视为数组前缀 `Q = A[:|Q|]`。
- 每次 `delete_max` 都把当前最大值换到数组尾部未使用区。
- 因此 heap sort 是：
  - 原地
  - `O(n log n)`
- 但通常**不稳定**。

## 线性建堆
- 若逐个插入 `n` 个元素，建堆要 `Omega(n log n)`。
- 更优方法：
  - 直接把整个数组看作完全二叉树
  - 从最后一个内部节点往前做 `heapify_down`
- 结论：

```text
build_heap = O(n)
```

- 虽然这不改变 heap sort 的总体 `O(n log n)`，但会把常数和建堆阶段降下来。

## 这一讲最重要的理解
- 堆并不是“全局有序”，只是“局部有序”。
- 正因为只维护局部有序，才能兼顾：
  - 插入 `O(log n)`
  - 删除最大值 `O(log n)`
  - 原地实现

## 相关笔记
- [[Algorithms (CLRS) MOC]]
- [[Data Structures]]
- [[Sorting]]
- [[Dijkstra]]

## 复习提问
- 为什么堆只需要局部父子有序，就能保证根是全局最大？
- heapify_up 和 heapify_down 分别修复什么破坏？
- 为什么 heap sort 可以原地实现？
- 为什么 bottom-up build heap 是 `O(n)` 而不是 `O(n log n)`？
