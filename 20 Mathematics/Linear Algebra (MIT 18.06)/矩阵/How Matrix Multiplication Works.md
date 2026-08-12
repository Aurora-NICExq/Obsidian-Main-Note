---
aliases: [矩阵乘法的原理, How Matrix Multiplication Works]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[The Matrix Viewpoint|矩阵的视角]], [[Matrices (Systems, Elimination, Inverse)|矩阵]], [[Singular Matrices|singular矩阵]]"
down: ""
---
# How Matrix Multiplication Works

> [!summary] 核心结论
> 矩阵乘法 $C=AB$ 有三个等价视角：**行乘列**（元素层面）、**列的线性组合**（$AB$ 的列是 $A$ 作用于 $B$ 的列）、**线性变换复合**（先 $B$ 后 $A$）。

---

## 1. 行乘列视角 (Row × Column)

$$c_{ij}=\text{row}_i(A)\cdot\text{col}_j(B).$$

## 2. 列组合视角 (Column Combination)

$AB$ 的第 $j$ 列 $=A\,b_j$：

$$AB=\begin{bmatrix}Ab_1&Ab_2&\cdots&Ab_n\end{bmatrix},$$

即 $Ab_j$ 是 $A$ 的列按 $b_j$ 的系数作线性组合。

## 3. 变换复合视角 (Composition)

$ABx=A(Bx)$——$AB$ 表示**先做 $B$、再做 $A$**。顺序不可随意交换（$AB\neq BA$）。

---

> [!important] 一句话总结
> $AB$ 的每一列都是 $A$ 对 $B$ 对应列的作用；乘法即变换的复合。
