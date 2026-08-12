---
aliases: [线性代数与图论, Linear Algebra and Graph Theory]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[Vector Spaces and Subspaces|向量空间及其子空间]], [[Linear Independence, Basis, and Dimension|向量组的性质]]"
down: ""
---
# Linear Algebra and Graph Theory

> [!summary] 核心结论
> 图论 (graph theory) 的**关联矩阵 (incidence matrix)** 把边与节点连接起来；线性代数用零空间、列空间与秩描述网络的流、环路与可解性，欧拉公式 (Euler's formula) 正是维度公式的体现。

---

## 1. 图与关联矩阵 (Graphs & Incidence Matrix)

图是结点 (node) 与边 (edge) 的集合（边连通结点）；"小世界图"中结点间最远距离即六度分离。$m$ 条边、$n$ 个结点的图对应 $m\times n$ 的**关联矩阵 (incidence matrix)**，每行恰有两个非零数（一条边的两端）。

## 2. 回路与树 (Loops & Trees)

- **回路 (loop)**：图中的子图；其对应的行**线性相关**。故"线性无关 ⟺ 没有回路"。
- **树 (tree)**：没有回路的图。

## 3. 维度公式与欧拉公式 (Euler's Formula)

左零空间维数

$$\dim N(A^{\mathsf T})=m-r$$

给出独立回路数。整理即**欧拉公式**：

$$(\text{结点数})-(\text{边数})+(\text{回路数})=1.$$

---

> [!important] 一句话总结
> 图的结构转化为关联矩阵后，网络问题就能用零空间、列空间与秩来分析——欧拉公式是其维度推论。
