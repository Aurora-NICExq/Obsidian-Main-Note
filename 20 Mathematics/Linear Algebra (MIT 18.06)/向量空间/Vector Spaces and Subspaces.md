---
aliases: [向量空间及其子空间, Vector Spaces and Subspaces, Four Fundamental Subspaces]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[Linear Independence, Basis, and Dimension|向量组的性质]], [[Matrices (Systems, Elimination, Inverse)|矩阵]], [[Singular Matrices|singular矩阵]]"
down: "[[Linear Independence, Basis, and Dimension|向量组的性质]]"
---
# Vector Spaces and Subspaces

> [!summary] 核心结论
> 子空间 (subspace) 必须**含零向量**并对加法、数乘**封闭**。列空间 (column space)、零空间 (null space)、行空间、左零空间构成矩阵的四个基本子空间，决定 $A\mathbf x=\mathbf b$ 的可解性与解的结构。

前置知识：[[Matrices (Systems, Elimination, Inverse)|矩阵]]。

---

## 1. 向量空间与子空间 (Spaces & Subspaces)

向量空间是一组遵循加法、数乘规则的对象（向量）的集合。子集 $W$ 是**子空间**当且仅当：① 含零向量；② 对加法封闭；③ 对数乘封闭。一句话：**过原点的、平直的线性结构**。$\mathbb R^3$ 中过原点的直线/平面、$\{\mathbf0\}$、$\mathbb R^3$ 本身都是子空间。

## 2. 列空间和零空间 (Column Space and Null Space)

| 子空间 | 符号 | 描述 |
| :-- | :-- | :-- |
| 列空间 | $C(A)$ | $A$ 各列张成的空间 |
| 零空间 | $N(A)$ | 所有满足 $A\mathbf x=\mathbf0$ 的 $\mathbf x$ |

### 列空间与矩阵方程解的关系

$A\mathbf x=x_1a_1+\cdots+x_na_n$ 是列的加权和，故 **$A\mathbf x=\mathbf b$ 有解 ⟺ $\mathbf b\in C(A)$**（$\mathbf b$ 是各列的线性组合）。

### 零空间 (Null Space)

矩阵方程 $A\mathbf x=\mathbf 0$ 即"存在列向量的组合结果为零列"。 ^ac1101

三条性质：① 它是子空间（含 $\mathbf0$、对线性组合封闭）；② 它是齐次方程 $A\mathbf x=\mathbf0$ 的解集 ^0ed6c9 ；③ 秩-零度定理 $n=r+\dim N(A)$。

## 3. 主变量、自由变量与阶梯形 (Pivots & Echelon Form)

### 阶梯形矩阵 (Row Echelon Form)

零行在最下方；每个非零行的首非零元（**主元 pivot**）的列标随行递增。主元个数 = 秩 $r$；自由变量个数 $=n-r$。求 $N(A)$：消元→给自由变量赋值→回解主变量得**特解 (special solution)**。

### 行最简形 (RREF)

主元为 $1$ 且其所在列其余为 $0$：

$$R=\begin{bmatrix}I&F\\ 0&0\end{bmatrix}$$ ^0abc1a

### 零空间矩阵 (Null-Space Matrix)

^6f74a6

各列由特解构成，满足 $RN=0$：

$$N=\begin{bmatrix}-F\\ I\end{bmatrix}.$$

$N$ 的各列是**基础解系**（每列对应一个自由变量），其行须按 $x_1,x_2,\dots$ 的顺序排列。

## 4. $A\mathbf x=\mathbf b$ 的可解性与解的结构 (Solvability)

^204ad0

若左侧某些行的线性组合为零，右侧常数也必须为零。求解步骤：写增广矩阵 → 消元为阶梯形 → 取特解 $x_p$（自由变量置零，解主变量）→ 通解 $=x_p+x_n$：

$$Ax_p=b,\ Ax_n=0\ \Rightarrow\ A(x_p+x_n)=b.$$ ^981165

几何上解集是零空间经 $x_p$ 平移的**仿射空间 (affine space)**（不过原点）。有解条件：$\mathbf b\in C(A)$（见 [[Vector Spaces and Subspaces#列空间与矩阵方程解的关系|列空间与矩阵方程解的关系]]）。

## 5. 秩 (Rank)

$r\le m,\ r\le n$；秩 = 主列数 = 列空间维数。**列满秩**（$r=n$）：零空间只含 $\mathbf0$，解唯一或无解。**行满秩**（$r=m$）：必有解。**满秩方阵**：RREF 是 $I$，零空间为 $\{\mathbf0\}$，唯一解。

---

> [!important] 一句话总结
> 判断子空间先查含零向量、再查线性组合封闭；四个基本子空间撑起 $A\mathbf x=\mathbf b$ 的全部解结构。
