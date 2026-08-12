---
title: "Sorting"
aliases:
  - "排序"
  - "归并排序"
  - "插入排序"
  - "比较排序下界"
tags:
  - Algorithms
  - Sorting
  - MIT6006
up: "[[Algorithms (CLRS) MOC]]"
down:
  - "[[Hashing]]"
  - "[[Linear Sorting]]"
related:
  - "[[Data Structures]]"
  - "[[Binary Heaps]]"
---

# Lec03 Sorting：排序、递归分析与三种基础排序

## 本讲主线
- 如果把集合按 key 排序存放，就能用二分查找把 `find(k)` 加速到 `O(log n)`。
- 因此问题变成：**如何高效构造有序数组**。
- 本讲用排序问题引入：
  - 递归算法设计
  - 递推式分析
  - 选择排序、插入排序、归并排序

![[alg-sorting-01.svg]]

## 排序问题定义
- 输入：长度为 `n` 的数组 `A`
- 输出：一个数组 `B`，满足：
  - `B` 是 `A` 的一个排列
  - `B` 非降序排列

## 术语
- destructive sort：直接覆盖原数组
- in-place sort：只用 `O(1)` 额外空间

## 为什么排序重要
- 无序数组实现 set：
  - `find` 慢
  - `find_min/max` 也不理想
- 有序数组实现 set：
  - `find(k)` 可二分到 `O(log n)`
  - `find_min/max` 很快
  - 但 `insert/delete` 仍需搬移，通常是 `O(n)`

## 从最笨的方法开始：Permutation Sort
- 枚举所有 `n!` 个排列，检查哪个是有序的。
- 正确性简单，因为“全试一遍”。
- 复杂度是指数级：

```text
Omega(n! * n)
```

- 作用不是实用，而是提醒我们：暴力法通常只适合拿来做对照。

## 递推分析工具
- 代入法（substitution）
- 递归树（recurrence tree）
- 主定理（Master Theorem，课程后续展开）

## Selection Sort

### 思想
- 在前缀 `A[:i+1]` 中找最大值，交换到位置 `i`。
- 然后递归排序更短的前缀。

### 正确性抓手
- 一个已排好序数组的最后一个元素，一定是当前范围中的最大值。
- 每轮把最大值放到最终位置，问题规模减 1。

### 复杂度
- 找前缀最大值：`Theta(n)`
- 递推：

```text
T(n) = T(n-1) + Theta(n)
```

- 结论：

```text
T(n) = Theta(n^2)
```

### 特点
- 原地
- 交换次数少
- 但整体仍是平方级

## Insertion Sort

### 思想
- 先递归排好前缀 `A[:i]`
- 再把 `A[i]` 通过不断左交换插入到正确位置

### 正确性抓手
- 假设前缀已排序
- 若最后一个元素比前一个小，就不断交换，直到恢复有序

### 复杂度
- `insert_last` 代价最坏 `Theta(n)`
- 递推同样是：

```text
T(n) = T(n-1) + Theta(n)
```

- 所以：

```text
T(n) = Theta(n^2)
```

### 特点
- 原地
- 稳定
- 对“几乎有序”的输入更友好

## Merge Sort

### 思想
- 分治：
  - 递归排序左半边
  - 递归排序右半边
  - 再把两个有序子数组 merge

### merge 的核心
- 两个子数组都已有序
- 比较当前候选元素，把较小/较大者放入结果
- 这就是典型的 two-finger / two-pointer 思路

### 复杂度
- 合并代价：`Theta(n)`
- 递推：

```text
T(n) = 2T(n/2) + Theta(n)
```

- 结论：

```text
T(n) = Theta(n log n)
```

### 特点
- 稳定
- 不是原地（标准实现需要额外空间）
- 是后续比较排序的性能基线

## 三种排序对比

```text
Selection Sort: Theta(n^2), 原地, 不强调稳定
Insertion Sort: Theta(n^2), 原地, 稳定
Merge Sort:     Theta(n log n), 非原地, 稳定
```

## 这一讲最该建立的感觉
- 递归排序的正确性证明几乎总是靠归纳。
- 递归排序的效率分析几乎总是落到递推式。
- 分治真正强的地方在于：虽然递归层数变多，但每层总工作量可能维持在线性级，从而得到 `n log n`。

## 相关笔记
- [[Algorithms (CLRS) MOC]]
- [[Hashing]]（下一讲）
- [[Linear Sorting]]（下一讲）
- [[Data Structures]]
- [[Binary Heaps]]

## 复习提问
- 为什么 permutation sort 正确但没价值？
- 选择排序和插入排序的 `Theta(n^2)` 本质原因是什么？
- 归并排序的 `Theta(n log n)` 从哪两部分来？
- 哪些排序是原地的？哪些是稳定的？
