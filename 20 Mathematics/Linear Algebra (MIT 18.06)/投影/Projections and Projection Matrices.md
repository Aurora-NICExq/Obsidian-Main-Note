---
aliases: [投影、投影矩阵, Projections and Projection Matrices, Projection Matrix]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[Orthogonal Vectors and Subspaces|正交向量和正交子空间(orthogonal)]], [[Projection Matrices and Least Squares|投影矩阵和最小二乘]], [[Orthogonal Matrices and Gram-Schmidt|正交矩阵和正交化法]]"
down: "[[Projection Matrices and Least Squares|投影矩阵和最小二乘]]"
---
# Projections and Projection Matrices

> [!summary] 核心结论
> 投影 (projection) 把向量分解为子空间内的部分 $\mathbf p$ 与正交误差 $\mathbf e$：$\mathbf b=\mathbf p+\mathbf e$。投影矩阵 $P$ 满足 **$P^{\mathsf T}=P$ 且 $P^2=P$**；当 $A\mathbf x=\mathbf b$ 无解时，投影到列空间给出最优解（正规方程）。

前置知识：[[Orthogonal Vectors and Subspaces|正交向量和正交子空间(orthogonal)]]。

---

## 1. 投影的概念 (Projection)

把 $\mathbf b$ 投影到 $\mathbf a$（或某子空间）即向量分解 $\mathbf b=\mathbf p+\mathbf e$：$\mathbf p$ 与 $\mathbf a$ 平行，**误差 $\mathbf e$ 与 $\mathbf a$ 正交**（见 [[Orthogonal Vectors and Subspaces#向量的正交 (Orthogonality)|向量的正交]]）。本质是找"分身" $\mathbf p$ 使其与 $\mathbf b$ 的距离最小。

### 投影向量的系数 (Projection Coefficient)

由 $\mathbf a^{\mathsf T}\mathbf e=0$ 即 $\mathbf a^{\mathsf T}(\mathbf b-x\mathbf a)=0$ 解出

$$x=\frac{\mathbf a^{\mathsf T}\mathbf b}{\mathbf a^{\mathsf T}\mathbf a},\qquad \mathbf p=\mathbf a x.$$

## 2. 投影矩阵 (Projection Matrix)

内积 $\mathbf a^{\mathsf T}\mathbf a$ 是标量（长度平方）；外积 $\mathbf a\mathbf a^{\mathsf T}$ 是 $n\times n$ 方阵。故

^36ed38

$$P=\frac{\mathbf a\mathbf a^{\mathsf T}}{\mathbf a^{\mathsf T}\mathbf a},\qquad P\mathbf b=\mathbf p.$$ ^a956d5

（$P\mathbf b$ 给出 $\mathbf b$ 在 $\mathbf a$ 上的投影 $\mathbf p=\mathbf a x$，见 [[Projections and Projection Matrices#投影向量的系数 (Projection Coefficient)|投影向量的系数]]。）

**列空间**：$\mathbf a\mathbf a^{\mathsf T}$ 每列都是 $\mathbf a$ 的倍数，故秩 1，列空间是 $\mathbf a$ 所在直线（见 [[Linear Independence, Basis, and Dimension#列空间 (Column Space)|列空间]]）。

**两条性质**：

1. 对称 $P^{\mathsf T}=P$：$(\mathbf a\mathbf a^{\mathsf T})^{\mathsf T}=\mathbf a\mathbf a^{\mathsf T}$（见 [[Matrices (Systems, Elimination, Inverse)#对称矩阵 (Symmetric Matrix)|对称矩阵]]）；
2. 幂等 $P^2=P$：用结合律（见 [[Matrices (Systems, Elimination, Inverse)#乘法的结合律 (Associativity of Multiplication)|乘法的结合律]]），影子再投影还是影子。

## 3. 投影解决可解性问题 (Least-Squares Setup)

当 $\mathbf b\notin C(A)$ 时 $A\mathbf x=\mathbf b$ 无解；把 $\mathbf b$ 投影到 $C(A)$ 得 $\mathbf p$，则 $A\hat{\mathbf x}=\mathbf p$ 必有解，$\hat{\mathbf x}$ 是**最优解**。误差 $\mathbf e=\mathbf b-\mathbf p$ 须垂直于 $C(A)$，即 $A^{\mathsf T}\mathbf e=0$（见 [[Orthogonal Vectors and Subspaces#^47c8b0|正交向量和正交子空间(orthogonal)]]）。

### 正规方程 (Normal Equations)

代入 $\mathbf e=\mathbf b-A\hat{\mathbf x}$：

$$A^{\mathsf T}(\mathbf b-A\hat{\mathbf x})=0\ \Rightarrow\ A^{\mathsf T}A\,\hat{\mathbf x}=A^{\mathsf T}\mathbf b.$$ ^325100

## 4. 投影矩阵公式 (General Projection Matrix)

^102d65

若 $A$ 列无关则 $A^{\mathsf T}A$ 可逆：

$$\hat{\mathbf x}=(A^{\mathsf T}A)^{-1}A^{\mathsf T}\mathbf b,\quad \mathbf p=A\hat{\mathbf x},\quad P=A(A^{\mathsf T}A)^{-1}A^{\mathsf T}.$$

---

> [!important] 一句话总结
> 投影的核心是误差与目标子空间正交；投影矩阵对称且幂等，正规方程 $A^{\mathsf T}A\hat x=A^{\mathsf T}b$ 给出最优解。
