---
title: "Binary Trees Part 1"
aliases:
  - "二叉树"
  - "遍历序"
  - "有序集合"
tags:
  - Algorithms
  - Tree
  - MIT6006
up: "[[Algorithms (CLRS) MOC]]"
down:
  - "[[Binary Trees Part 2 AVL]]"
related:
  - "[[Data Structures]]"
  - "[[Hashing]]"
---

# Lec06 Binary Trees, Part 1：从高度 `h` 到有序集合与序列

## 本讲主线
- 之前我们想要一种结构，同时支持 set/sequence 的动态操作。
- 二叉树给出统一框架：许多操作可以在 `O(h)` 内完成。
- 真正的目标不是只要树，而是要让树高 `h = O(log n)`。

## 为什么引入二叉树
- 数组/链表各有短板。
- 我们希望对 set 和 sequence 都做到：
  - 查询快
  - 插删也快
- 二叉树是 pointer-based 结构，每个节点有：
  - `item`
  - `parent`
  - `left`
  - `right`

## 术语与基本性质
- root：无父节点
- leaf：无子节点
- depth：到根的路径长度
- height：某节点子树中的最大深度
- 若所有操作都能做到 `O(h)`，那只要树高可控，就能获得好复杂度。

## 中序遍历（Traversal Order）
- 左子树全部在当前节点之前
- 右子树全部在当前节点之后
- 中序遍历顺序：
  - 递归左子树
  - 访问自己
  - 递归右子树
- 整体时间 `O(n)`。

## Tree Navigation

### first / last
- 某节点子树中的第一个元素：一路向左找。
- 对称地可求最后一个元素。
- 代价 `O(h)`。

### successor / predecessor
- 若节点有右子树，successor 是右子树里的第一个节点。
- 否则向上找第一个把当前节点放在其左子树中的祖先。
- predecessor 完全对称。
- 代价 `O(h)`。

## 动态操作

### 插入
- 按遍历顺序在某节点前/后插入一个叶子。
- 本质是：
  - 要么挂到某个空孩子位置
  - 要么挂到 predecessor/successor 的相应位置
- 代价 `O(h)`。

### 删除
- 删除叶子最简单，直接摘掉。
- 若不是叶子：
  - 与 predecessor 或 successor 交换 item
  - 把问题递归下推到叶子
- 整体仍是 `O(h)`。

## 应用一：Set = Binary Search Tree
- 给遍历顺序赋予语义：**中序遍历就是 key 的升序**。
- 这等价于 BST 性质：
  - 左子树 key 不大于当前节点
  - 右子树 key 不小于当前节点
- 于是：
  - `find(k)` 像二分一样沿树走，`O(h)`
  - `find_min/max/prev/next/insert/delete` 也都可基于导航完成

## 应用二：Sequence Tree
- 若中序遍历顺序就是序列顺序，就能实现 sequence。
- 关键问题：如何在 `O(h)` 找到第 `i` 个节点？

### subtree_at(i) 的思路
- 给每个节点维护 `size = 子树节点数`。
- 设左子树大小为 `n_L`：
  - 若 `i < n_L`，去左子树
  - 若 `i = n_L`，当前节点就是答案
  - 若 `i > n_L`，去右子树查 `i - n_L - 1`
- 因此 `get_at(i)` 可做到 `O(h)`。

### augmentation 的意义
- 插入一个叶子后，祖先的 `size` 全部 `+1`
- 删除叶子后，祖先的 `size` 全部 `-1`
- 维护代价仍是 `O(h)`。

## 当前结论

```text
Binary Tree:
  Set 操作:      O(h)
  Sequence 操作: O(h)
```

- 问题只剩一个：
  - 如果树退化成链，`h = Theta(n)`，所有优势消失。
- 这正是下一讲 AVL 的出发点。

## 相关笔记
- [[Algorithms (CLRS) MOC]]
- [[Binary Trees Part 2 AVL]]（下一讲）
- [[Data Structures]]
- [[Hashing]]

## 复习提问
- 为什么 successor 可以只靠局部结构和祖先关系求出？
- BST 的“有序性”为什么正好对应中序遍历？
- Sequence tree 为什么必须维护子树大小？
- 这讲所有操作的瓶颈为什么都落在 `h` 上？
