---
title: "Linear Sorting"
aliases:
  - "线性时间排序"
  - "计数排序"
  - "基数排序"
tags:
  - Algorithms
  - Sorting
  - MIT6006
up: "[[Algorithms (CLRS) MOC]]"
related:
  - "[[Sorting]]"
  - "[[Hashing]]"
---

# Lec05 Linear Sorting：计数排序与基数排序

## 本讲主线
- 比较排序有 `Omega(n log n)` 下界。
- 但如果 key 不是“只能比较的黑箱”，而是可以按位/按值访问的整数，就可能更快。
- 核心结果：
  - counting sort：`O(n + u)`
  - radix sort：`O(cn)`

## 比较排序下界
- 排序要区分 `n!` 个排列。
- 比较模型的决策树是二叉树。
- 所以最坏时间至少：

```text
Omega(log(n!)) = Omega(n log n)
```

- 这说明 merge sort 在比较模型下已经是最优量级。

## Direct Access Sort
- 若 key 是互异的非负整数，且范围是 `0..u-1`：
  - 把每个元素放到直接寻址数组对应位置
  - 再按下标顺序读出
- 复杂度：

```text
Theta(n + u)
```

- 当 `u = Theta(n)` 时，它就是线性时间。
- 限制也很明显：
  - key 范围不能太大
  - 不能直接处理重复 key

## 从整数到元组
- 若 `u` 比 `n` 大很多，可以把整数拆成 base-`n` 的多位表示。
- 比如 `k = an + b`，就可写成二元组 `(a, b)`。
- 更一般地，任意 key 都可写成 `c` 位 base-`n` 数。

## Tuple Sort 的关键思想
- 想按字典序对元组排序。
- 正确做法不是先排最高位，而是：

```text
从最低位到最高位依次排序
```

- 这样前面排好的低位顺序，才能在后面继续被保留。

## Stability 为什么关键
- 若两个元素当前位相同，排序后它们原先的先后关系必须保留。
- 否则之前按低位建立的顺序会被破坏。
- 所以 radix sort 的辅助排序必须是**稳定排序**。

## Counting Sort

### 思想
- 不是在每个 key 位置只放一个元素，而是放一条“链”。
- 元素按出现顺序追加到对应桶尾部。
- 最后按 key 从小到大遍历所有桶，并在桶内保持原顺序输出。

### 正确性来源
- 桶顺序保证 key 有序。
- 桶内追加顺序保证稳定性。

### 复杂度

```text
O(n + u)
```

- 当 `u = O(n)` 时就是线性。

## Radix Sort

### 思想
- 把整数拆成 `c` 位 base-`n` 数字。
- 对每一位使用 counting sort。
- 顺序是：**从最低位到最高位**。

### 复杂度
- 每一位排序代价 `O(n)`。
- 共 `c` 位：

```text
O(cn)
```

- 若 `u = O(n^c)` 且 `c` 为常数，就得到线性时间。

## 本讲算法对比

```text
Insertion Sort: O(n^2), 原地, 稳定
Selection Sort: O(n^2), 原地, 不稳定
Merge Sort:     O(n log n), 非原地, 稳定
Counting Sort:  O(n + u), 非原地, 稳定
Radix Sort:     O(cn), 非原地, 稳定
```

## 学习重点
- 线性排序不是“推翻了下界”，而是**跳出了比较模型**。
- counting sort 的本质是：
  - 利用 key 可直接索引
  - 用桶把重复 key 组织起来
- radix sort 的本质是：
  - 把“大 key 排序”降成“多轮小 key 稳定排序”

## 相关笔记
- [[Algorithms (CLRS) MOC]]
- [[Sorting]]
- [[Hashing]]

## 复习提问
- 为什么比较排序下界不能约束 counting sort / radix sort？
- counting sort 为什么必须稳定？
- radix sort 为什么一定要从低位到高位排？
- 在什么条件下 radix sort 可以看作线性时间？
