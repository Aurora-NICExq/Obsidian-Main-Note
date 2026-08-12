---
aliases: [向量组的性质, Linear Independence Basis and Dimension, Basis and Dimension]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[Vector Spaces and Subspaces|向量空间及其子空间]], [[Projections and Projection Matrices|投影、投影矩阵]], [[Orthogonal Vectors and Subspaces|正交向量和正交子空间(orthogonal)]]"
down: ""
---
# Linear Independence, Basis, and Dimension

> [!summary] 核心结论
> 线性无关 (linear independence)、基 (basis)、维数 (dimension) 与秩 (rank) 描述同一件事：一组向量到底提供了多少个**独立方向**。

前置知识：[[Vector Spaces and Subspaces|向量空间及其子空间]]。

---

## 1. 线性相关与无关 (Dependence vs Independence)

- **相关 (dependent)**：存在不全为零的 $k_i$ 使 $\sum k_i\alpha_i=0$（零空间有自由变量）。含零向量必相关。
- **无关 (independent)**：仅当所有 $k_i=0$ 时 $\sum k_i\alpha_i=0$（零空间只含 $\mathbf0$）。

列无关 ⟺ 列满秩；矩阵方程视角：$m\times n$ 矩阵若 $m<n$（方程少于未知数），则 $A\mathbf x=\mathbf0$ 有非零解，对应列向量必相关。

## 2. 基 (Basis)

^8403a0

### 列空间 (Column Space)

各列的全部线性组合张成列空间。**基**是一组既能张成空间、又线性无关的向量；其全部线性组合即一个子空间。求基：消元判断主列（pivot columns）。$\mathbb R^n$ 中 $n$ 个向量构成基 ⟺ $n\times n$ 矩阵可逆。基不唯一，但每组基的向量个数相同。

## 3. 维数 (Dimension)

任意基的向量个数相等，即维数。列空间维数 = 秩；零空间维数 = 列数 $-$ 秩（自由变量个数）。

## 4. 四个基本子空间 (Four Fundamental Subspaces)

行空间、列空间、零空间、左零空间。

### 行空间 (Row Space)

$A$ 的行向量的所有线性组合（转置后即列空间处理）。**行秩 = 列秩**。行变换不改变行空间，故行空间的基是 RREF 的前 $r$ 行。

**左零空间 (left null space)**：$A^{\mathsf T}\mathbf y=\mathbf0$ 的解集，由高斯–若尔当 $EA=R$ 中产生零行的行组合给出。

### 初等变换对子空间的影响

- **列互换**改变零空间：解向量分量随之互换（[[Vector Spaces and Subspaces#^6f74a6|改变零空间矩阵]]）；
- **行变换**不改变列的线性关系，但列空间的基须回到原矩阵 $A$ 取对应主列（不能取 $R$ 的列）。不变量：秩、列的线性关系。

## 5. 矩阵空间与秩 1 矩阵 (Matrix Spaces & Rank-1)

$3\times3$ 矩阵空间维数为 $9$；对称阵 $S$ 与反对称阵 $U$ 满足 $\dim S+\dim U=\dim(S+U)+\dim(S\cap U)$。**秩 1 矩阵**都可写成"一列 × 一行"：$A=uv^{\mathsf T}$。

---

> [!important] 一句话总结
> 基是无冗余且能张成空间的向量组，维数是基中向量的个数——它们与秩讲的是同一回事。
