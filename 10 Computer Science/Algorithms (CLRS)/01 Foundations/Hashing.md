---
title: "Hashing"
aliases:
  - "哈希"
  - "散列表"
  - "链地址法"
  - "全域哈希"
tags:
  - Algorithms
  - Hashing
  - MIT6006
up: "[[Algorithms (CLRS) MOC]]"
related:
  - "[[Sorting]]"
  - "[[Linear Sorting]]"
  - "[[Binary Trees Part 1]]"
---

# Lec04 Hashing：为什么哈希能快过比较搜索

## 本讲主线
- 比较模型下，搜索做不到比 `Omega(log n)` 更快。
- 要突破这个下界，必须利用 Word-RAM 的随机访问能力。
- 直接寻址太耗空间，于是引出哈希表。

![[alg-hashing-01.svg]]

## 比较搜索下界

### 决策树视角
- 任意比较算法都可以看成一棵二叉决策树。
- 每个内部节点是一次比较。
- 每个叶子对应一个最终输出。

### 为什么有 `Omega(log n)`
- 搜索问题至少要区分 `n+1` 种输出情形。
- 二叉树有这么多叶子，树高至少是 `Omega(log n)`。
- 所以比较模型中：

```text
find(k) = Omega(log n)
```

- 有序数组的二分查找正好达到这个下界。

## 直接寻址数组（Direct Access Array）
- 若 key 是 `0..u-1` 内的整数，可以把元素直接放在下标 `k` 上。
- 好处：
  - `find/insert/delete` 最坏 `O(1)`
- 代价：
  - 空间是 `O(u)`
- 当 `u >> n` 时完全不划算。

## 哈希的核心思想
- 用一个函数 `h(k)` 把大范围 `u` 映射到小范围 `m = Theta(n)`。
- 用大小为 `m` 的数组充当哈希表。
- 必然出现**冲突**，因为当 `m < u` 时，函数不可能单射。

## 冲突处理
- 两大思路：
  - open addressing：冲突元素还放在表内其他位置
  - chaining：每个桶挂一个链
- 本讲核心分析对象是 chaining。

## Chaining 的性能关键
- 若元素在桶中分布足够均匀，则平均链长约为：

```text
alpha = n / m
```

- 当 `m = Theta(n)` 时，`alpha = O(1)`。
- 这时查找、插入、删除的期望时间就能做到 `O(1)`。

## 为什么普通取模不够稳
- 例子：`h(k) = k mod m`
- 若输入 key 带有模式或对称性，可能集中落入少数桶。
- 所以固定哈希函数无法防止“坏输入”。

## Universal Hashing
- 课程给出的典型族：

```text
h_ab(k) = ((a*k + b) mod p) mod m
```

- 其中：
  - `p > u` 是素数
  - `a != 0`
  - `a, b` 随机选取

### 关键性质
- 对任意不同 key `ki != kj`：

```text
Pr[h(ki) = h(kj)] <= 1/m
```

- 于是某个元素所在桶的期望链长为：

```text
1 + (n-1)/m = O(1)
```

## 动态哈希表
- 当装载因子 `n/m` 偏离常数范围时，需要重建表。
- 做法与动态数组类似：
  - 扩/缩容
  - 重选随机哈希函数
  - 重新散列全部元素
- 因此动态操作可以做到：

```text
expected amortized O(1)
```

## 能做什么，不能做什么
- 哈希表非常适合 dictionary / membership 问题。
- 但不擅长 order 操作：
  - `find_min/max`
  - `find_prev/next`
- 因为哈希破坏了顺序结构。

## 复杂度总结

```text
Sorted Array:
  find O(log n), insert/delete O(n)

Direct Access Array:
  find/insert/delete O(1), 空间 O(u)

Hash Table:
  build O(n) expected
  find O(1) expected
  insert/delete O(1) expected amortized
  order 操作不高效
```

## 相关笔记
- [[Algorithms (CLRS) MOC]]
- [[Sorting]]
- [[Linear Sorting]]
- [[Binary Trees Part 1]]

## 复习提问
- 为什么比较模型下搜索不可能优于 `Omega(log n)`？
- 直接寻址为什么快？为什么不实用？
- chaining 的期望 `O(1)` 依赖什么条件？
- universal hashing 为什么比固定取模更稳健？
