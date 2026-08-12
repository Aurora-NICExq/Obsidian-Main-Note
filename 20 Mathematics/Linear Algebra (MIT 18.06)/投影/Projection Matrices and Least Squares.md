---
aliases: [投影矩阵和最小二乘, Projection Matrices and Least Squares, Least Squares]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[Orthogonal Vectors and Subspaces|正交向量和正交子空间(orthogonal)]], [[Orthogonal Matrices and Gram-Schmidt|正交矩阵和正交化法]], [[Projections and Projection Matrices|投影、投影矩阵]]"
down: ""
---
# Projection Matrices and Least Squares

> [!summary] 核心结论
> 最小二乘 (least squares) 用投影解决 $A\mathbf x=\mathbf b$ 不可解时的"最近可解"问题：核心方程是正规方程 $A^{\mathsf T}A\hat{\mathbf x}=A^{\mathsf T}\mathbf b$。

前置知识：[[Projections and Projection Matrices|投影、投影矩阵]]、[[Orthogonal Vectors and Subspaces|正交向量和正交子空间(orthogonal)]]。

---

## 1. 最小二乘问题 (The Problem)

当 $A\mathbf x=\mathbf b$ 无解时 $\mathbf b\notin C(A)$。改为找 $\hat{\mathbf x}$ 使 $A\hat{\mathbf x}$ 是 $\mathbf b$ 在 $C(A)$ 上的投影：

$$A\hat{\mathbf x}=\mathbf p,\quad \mathbf e=\mathbf b-\mathbf p,\quad \mathbf e\perp C(A).$$

## 2. 正规方程 (Normal Equations)

误差 $\mathbf e=\mathbf b-A\hat{\mathbf x}$ 与 $A$ 各列正交，故 $A^{\mathsf T}(\mathbf b-A\hat{\mathbf x})=0$：

$$A^{\mathsf T}A\,\hat{\mathbf x}=A^{\mathsf T}\mathbf b.$$

## 3. 投影矩阵 (Projection Matrix)

若 $A$ 列无关：

$$\hat{\mathbf x}=(A^{\mathsf T}A)^{-1}A^{\mathsf T}\mathbf b,\quad \mathbf p=A\hat{\mathbf x},\quad P=A(A^{\mathsf T}A)^{-1}A^{\mathsf T},$$

满足 $P^2=P$ 且 $P^{\mathsf T}=P$。当列为标准正交时简化为 $P=QQ^{\mathsf T}$（见 [[Orthogonal Matrices and Gram-Schmidt|正交矩阵和正交化法]]）。

---

> [!important] 一句话总结
> 最小二乘不是让 $A\mathbf x=\mathbf b$ 真可解，而是让 $A\hat{\mathbf x}$ 成为 $\mathbf b$ 在列空间中的最佳近似。
