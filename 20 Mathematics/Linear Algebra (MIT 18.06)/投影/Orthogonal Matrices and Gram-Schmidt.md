---
aliases: [正交矩阵和正交化法, Orthogonal Matrices and Gram-Schmidt, QR Decomposition]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[Orthogonal Vectors and Subspaces|正交向量和正交子空间(orthogonal)]], [[Projection Matrices and Least Squares|投影矩阵和最小二乘]], [[Projections and Projection Matrices|投影、投影矩阵]]"
down: ""
---
# Orthogonal Matrices and Gram-Schmidt

> [!summary] 核心结论
> 标准正交基把计算大大简化：投影矩阵变成 $QQ^{\mathsf T}$、最小二乘解变成 $\hat x_i=q_i^{\mathsf T}b$。**Gram–Schmidt** 把线性无关向量组整理成标准正交基，对应矩阵分解 $A=QR$。

前置知识：[[Projections and Projection Matrices|投影、投影矩阵]]。

---

## 1. 标准正交向量 (Orthonormal Vectors)

满足 $q_i^{\mathsf T}q_j=\delta_{ij}$（正交且单位长）。把它们作列组成 $Q$，则

$$Q^{\mathsf T}Q=I.$$

> [!note] 正交矩阵 (Orthogonal Matrix)
> 严格定义下，只有 $Q$ 为**方阵**时才叫正交矩阵，此时 $Q^{\mathsf T}=Q^{-1}$（转置等于逆）。例：旋转矩阵、置换矩阵。

## 2. $Q$ 简化计算 (Simplification)

- **投影**：$P=A(A^{\mathsf T}A)^{-1}A^{\mathsf T}$（见 [[Projections and Projection Matrices#^102d65|投影矩阵公式]]），$A\to Q$ 且 $Q^{\mathsf T}Q=I$，得 $P=QQ^{\mathsf T}$；
- **最小二乘**：$A^{\mathsf T}A\hat x=A^{\mathsf T}b\to I\hat x=Q^{\mathsf T}b$，即 $\hat x=Q^{\mathsf T}b$，分量 $x_i=q_i^{\mathsf T}b$（只需点积，不必解方程组）。

## 3. Gram–Schmidt 正交化 (Gram-Schmidt)

给定线性无关 $a,b,c$，构造标准正交 $q_1,q_2,q_3$，张成空间不变。**核心**：减去在已有方向上的投影，只留垂直部分。

$$A=a,\ q_1=\tfrac{A}{\|A\|};\quad B=b-(b^{\mathsf T}q_1)q_1,\ q_2=\tfrac{B}{\|B\|};\quad C=c-(c^{\mathsf T}q_1)q_1-(c^{\mathsf T}q_2)q_2,\ q_3=\tfrac{C}{\|C\|}.$$

## 4. $A=QR$ 分解 (QR Decomposition)

Gram–Schmidt 可写成 $A=QR$：$Q$ 列为 $q_i$，$R$ 为**上三角**（因构造 $a_k$ 只用到 $q_1,\dots,q_k$）。捷径：两边左乘 $Q^{\mathsf T}$ 得

$$R=Q^{\mathsf T}A.$$

---

> [!important] 一句话总结
> 正交化保留张成空间，把基变成长度 1、互相垂直；任何满秩 $A$ 都可分解为 $A=QR$。
