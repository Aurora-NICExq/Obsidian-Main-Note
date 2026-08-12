---
aliases: ["正交向量和正交子空间(orthogonal)", Orthogonal Vectors and Subspaces, Orthogonality]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[Projection Matrices and Least Squares|投影矩阵和最小二乘]], [[Orthogonal Matrices and Gram-Schmidt|正交矩阵和正交化法]], [[Projections and Projection Matrices|投影、投影矩阵]], [[Linear Independence, Basis, and Dimension|向量组的性质]]"
down: "[[Projections and Projection Matrices|投影、投影矩阵]]"
---
# Orthogonal Vectors and Subspaces

> [!summary] 核心结论
> 正交 (orthogonal) 意味着点积为零。四个基本子空间存在自然的正交关系（行空间 ⊥ 零空间）；当 $A\mathbf x=\mathbf b$ 无解时，$A^{\mathsf T}A$ 把它变成可解的正规方程。

前置知识：[[Dot Product|点积]]、[[Vector Spaces and Subspaces|向量空间及其子空间]]。

---

## 向量的正交 (Orthogonality)

$n$ 维空间中两向量夹角 $90^\circ$，即点积为零：$\mathbf x^{\mathsf T}\mathbf y=0$。向量长度平方为 $\mathbf x^{\mathsf T}\mathbf x$。

> [!note] 勾股定理推论
> 正交 ⟺ $\|\mathbf x\|^2+\|\mathbf y\|^2=\|\mathbf x+\mathbf y\|^2$。展开 $\|\mathbf x+\mathbf y\|^2=\mathbf x^{\mathsf T}\mathbf x+2\mathbf x^{\mathsf T}\mathbf y+\mathbf y^{\mathsf T}\mathbf y$，与左式比较得 $2\mathbf x^{\mathsf T}\mathbf y=0$，即 $\mathbf x^{\mathsf T}\mathbf y=0$。

## 2. 正交子空间 (Orthogonal Subspaces)

子空间 $S\perp T$ 指 $S$ 中每个向量都与 $T$ 中每个向量正交。性质：① 二者不交于非零向量；② **行空间 ⊥ 零空间**——由 $A\mathbf x=\mathbf0$ 知 $A$ 的行向量正交于 $\mathbf x$，故 $\mathbf x$ 正交于行向量的线性组合（见 [[Linear Independence, Basis, and Dimension#行空间 (Row Space)|行空间]]）。

## 3. 求解无解方程 $A\mathbf x=\mathbf b$ (Least Squares)

^a72121

对方程过多的长方形矩阵 $A_{m\times n}$，消元常无解。两边左乘 $A^{\mathsf T}$ 得对称矩阵方程： ^47c8b0

$$A\mathbf x=\mathbf b\ \longrightarrow\ A^{\mathsf T}A\,\mathbf x=A^{\mathsf T}\mathbf b.$$

变换后的 $\mathbf x$ 是**最优解**（与原方程的 $\mathbf x$ 不同）。$A^{\mathsf T}A$ 的秩等于 $A$ 的秩，故零空间相同；

$$A^{\mathsf T}A\text{ 可逆}\iff A\text{ 各列线性无关}.$$ ^f5016e

详见 [[Projections and Projection Matrices|投影、投影矩阵]]、[[Projection Matrices and Least Squares|投影矩阵和最小二乘]]。

---

> [!important] 一句话总结
> 正交把空间拆成互不干扰的方向，是投影与最小二乘的基础；行空间与零空间天然正交。
