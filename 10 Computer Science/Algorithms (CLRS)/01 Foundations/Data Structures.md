---
title: "Data Structures"
aliases:
  - "数据结构"
  - "接口与实现"
  - "动态数组"
  - "摊还分析"
tags:
  - Algorithms
  - DataStructure
  - MIT6006
up: "[[Algorithms (CLRS) MOC]]"
down:
  - "[[Sorting]]"
related:
  - "[[Algorithms and Computation]]"
  - "[[Binary Trees Part 1]]"
  - "[[Binary Heaps]]"
---

# Lec02 Data Structures：接口、数组、链表与动态数组

## 本讲主线
- 先把“数据结构”和“接口”分开：接口规定做什么，数据结构决定怎么做。
- 课程核心接口有两个：`Sequence` 和 `Set`。
- 用三类典型结构比较性能：
  - 数组
  - 链表
  - 动态数组

![[alg-data-structures-01.svg]]

## 两大接口

### 1. Sequence
- 维护一个有外部顺序的序列 `(x0, x1, ..., x(n-1))`。
- 常见操作：
  - `build(X)`, `len()`
  - `iter_seq()`
  - `get_at(i)`, `set_at(i, x)`
  - `insert_at(i, x)`, `delete_at(i)`
  - `insert_first/last`, `delete_first/last`
- 特例：
  - 栈：`insert_last + delete_last`
  - 队列：`insert_last + delete_first`

### 2. Set
- 维护 key 唯一的元素集合，顺序来自 key 的大小。
- 常见操作：
  - `build(X)`, `len()`
  - `find(k)`
  - `insert(x)`, `delete(k)`
  - `find_min/max`
  - `find_next/prev`
- 去掉有序操作后，就是常见的 dictionary 接口。

## 三种序列结构对比

### 1. 普通数组
- 优点：随机访问强。
- `get_at` / `set_at` 是 `Theta(1)`。
- 缺点：动态操作代价高，因为插删会触发：
  - 重分配
  - 元素搬移
- 结论：
  - 静态操作优秀
  - 动态插删通常是 `O(n)`

### 2. 链表
- 每个节点保存：
  - `node.item`
  - `node.next`
- 核心优势是**改指针，不搬元素**。
- 头部插入/删除可达 `Theta(1)`。
- 缺点是随机访问差：
  - `get_at(i)` / `set_at(i, x)` 需要走指针，`O(n)`

### 3. 动态数组
- 目标：保留数组的随机访问优势，同时让尾部动态操作更快。
- 关键思想：**预留额外空间**，不要每次插入都重分配。
- 设填充率 `r = items / capacity`。
- 当数组满了时，额外申请 `Theta(n)` 空间，使填充率降到常数（例如 `1/2`）。
- 虽然单次扩容是 `Theta(n)`，但扩容后要再做 `Theta(n)` 次廉价插入才会再次扩容。

## 摊还分析
- 摊还是把少数昂贵操作的代价，平摊到一长串普通操作中。
- 如果 `k` 次操作总成本最多是 `kT(n)`，就称单次摊还代价是 `T(n)`。
- 因此：
  - 动态数组 `insert_last` 是 `Theta(1)` 摊还时间
  - `delete_last` 也可以做到 `Theta(1)` 摊还时间

## 动态数组删除的关键点
- 只会扩容还不够，因为一直删除会造成空间浪费。
- 不能一空一点就立刻缩容，否则插入/删除交替会频繁抖动。
- 经典办法：
  - 当填充率小于某阈值 `r_d` 时才缩容
  - 缩容后把填充率调回更高的 `r_i`
  - 要求 `r_d < r_i`
- 这样能保证两次昂贵 resize 之间仍有 `Theta(n)` 次便宜操作。

## 复杂度总表

```text
Array:
  build O(n), get/set O(1), 动态插删 O(n)

Linked List:
  build O(n), 头部插删 O(1), 随机访问 O(n)

Dynamic Array:
  build O(n), get/set O(1), 尾部插删 O(1) amortized
```

## 学习上的关键判断
- 需要随机访问：优先考虑数组/动态数组。
- 需要频繁头部插删：链表更自然。
- 需要“尾插很多 + 下标访问很多”：动态数组是主力结构。
- Python `list` 本质上就是动态数组：
  - `append`/`pop` 摊还 `O(1)`
  - 中间/头部插删往往是 `O(n)`

## 相关笔记
- [[Algorithms (CLRS) MOC]]
- [[Sorting]]（下一讲）
- [[Algorithms and Computation]]
- [[Binary Trees Part 1]]
- [[Binary Heaps]]

## 复习提问
- 为什么“接口”和“数据结构”必须区分？
- 数组和链表各自的性能瓶颈是什么？
- 动态数组为什么能把尾插做到摊还 `O(1)`？
- 删除时为什么不能一变空就立刻缩容？
