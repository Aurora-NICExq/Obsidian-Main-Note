---
title: "Binary Trees Part 2 AVL"
aliases:
  - "AVL 树"
  - "平衡二叉树"
  - "旋转"
tags:
  - Algorithms
  - Tree
  - MIT6006
up: "[[Algorithms (CLRS) MOC]]"
down:
  - "[[Binary Heaps]]"
related:
  - "[[Binary Trees Part 1]]"
---

# Lec07 Binary Trees, Part 2: AVL：平衡树与旋转

## 本讲主线
- Lec06 已经把很多操作压到 `O(h)`。
- 这一讲解决剩余核心问题：怎样保证 `h = O(log n)`。
- 方案是 AVL 树：通过局部旋转维护高度平衡。

![[alg-binary-trees-part-2-avl-01.svg]]

## AVL 的目标
- 对于 set 和 sequence 两类树结构，都希望动态操作稳定在 `O(log n)`。
- AVL 树是最早提出的平衡二叉树方案之一。

## 旋转（Rotation）
- 旋转的本质：**改变树形，不改变中序顺序**。
- 这点非常关键，因为：
  - 对 BST，它保证 key 的有序性不变
  - 对 sequence tree，它保证序列顺序不变
- 单次旋转只改动 `O(1)` 个指针。

## 为什么旋转足够强
- 任意两棵具有相同中序顺序的二叉树，可以通过 `O(n)` 次旋转互相转换。
- 这说明旋转是“局部修形”的基础操作。

## AVL 平衡条件
- 定义 `skew(x) = height(right) - height(left)`。
- 若某节点满足：

```text
skew in {-1, 0, 1}
```

- 就称它高度平衡。
- AVL 树要求所有节点都高度平衡。

## 为什么高度是 `O(log n)`
- 设高度为 `h` 的 AVL 树最少节点数为 `F(h)`。
- 由于最坏情况下一边高 `h-1`、另一边高 `h-2`，有：

```text
F(h) = 1 + F(h-1) + F(h-2)
```

- 这与 Fibonacci 型增长一致，因此：

```text
F(h) = 2^{Omega(h)}  =>  h = O(log n)
```

## 失衡从哪里来
- 插入/删除一个叶子后，只有该叶到根路径上的祖先可能改变高度。
- 且每个节点高度变化至多 `±1`，所以失衡节点的 `|skew|` 最多到 `2`。
- 这让修复可以局部进行。

## 局部重平衡

### 单旋
- 若某节点 `B` 右重（`skew = 2`），且其右孩子 `F` 的 `skew` 为 `0` 或 `1`：
  - 对 `B` 做一次左旋
- 左重情况完全对称，用右旋。

### 双旋
- 若 `B` 右重，但右孩子 `F` 左重（`skew = -1`）：
  - 先对 `F` 右旋
  - 再对 `B` 左旋
- 左重-右重情形同理。

## 全局重平衡
- 插入/删除后，从受影响节点向上找第一个失衡祖先。
- 对其做局部重平衡。
- 删除可能继续向上传播，因此最坏要一路修到根。
- 但受影响祖先个数至多是树高，因此总代价仍是：

```text
O(log n)
```

## 如何高效知道高度
- 若每次都递归算高度，会退化到 `Omega(n)`。
- 正确做法：把子树高度作为 augmentation 存在节点里。
- 则节点高度可由左右孩子高度 `O(1)` 算出。
- 更新方式：
  - 旋转时更新被重连的少数节点：`O(1)`
  - 插删后沿祖先链回溯更新：`O(h)`

## augmentation 的一般套路
- 若想在树上维护某个子树性质 `P(X)`：
  - 先定义它是什么
  - 再证明能从左右孩子的 augmentation 在 `O(1)` 内算出
- 若成立，就能在不改变大复杂度的前提下维护它。
- 例子：`size` 就是 subtree property，所以 sequence tree 也能与 AVL 结合。

## 结果

```text
Set AVL Tree:
  几乎所有核心操作 O(log n)

Sequence AVL Tree:
  几乎所有核心操作 O(log n)
```

- 这意味着：
  - AVL 树既能做平衡搜索树
  - 也能做支持 rank/select 的平衡序列树

## 相关笔记
- [[Algorithms (CLRS) MOC]]
- [[Binary Heaps]]（下一讲）
- [[Binary Trees Part 1]]

## 复习提问
- 旋转为什么不会破坏中序顺序？
- 为什么 AVL 树高度一定是 `O(log n)`？
- 单旋和双旋分别对应什么失衡模式？
- 为什么“把高度存在节点里”是必要的 augmentation？
