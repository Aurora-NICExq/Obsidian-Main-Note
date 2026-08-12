---
aliases: [相似矩阵与若尔当标准型, Similar Matrices and Jordan Form, Jordan Canonical Form]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[Eigenvalues and Eigenvectors|特征值和特征向量]], [[Markov Matrices and Fourier Series|马尔可夫矩阵和傅立叶级数]], [[Linear Algebra and Differential Equations|线性代数与微分方程]], [[Symmetric and Positive Definite Matrices|对称矩阵和正定矩阵]], [[Diagonalization and Matrix Powers|对角化和矩阵乘幂]]"
down: ""
---
# Similar Matrices and Jordan Form

> [!summary] 核心结论
> 相似变换 $B=M^{-1}AM$ 表示同一线性变换在**不同基**下的矩阵形式，保留特征值、迹、行列式、秩等不变量。无法对角化的"缺损矩阵"能达到的最简形式是**若尔当标准型 (Jordan form)**。

前置知识：[[Eigenvalues and Eigenvectors|特征值和特征向量]]、[[Diagonalization and Matrix Powers|对角化和矩阵乘幂]]。

---

## 1. 相似矩阵 (Similar Matrices)

若存在可逆 $M$ 使 $B=M^{-1}AM$，则 $A,B$ **相似**——本质是同一线性变换在不同基下的表示，$M$ 是基变换矩阵。对角化是其特例：取 $M=S$（特征向量矩阵）得 $\Lambda=S^{-1}AS$（见 [[Diagonalization and Matrix Powers#^c37711|矩阵与对角矩阵相似]]）。

> [!note] 附：$A^{\mathsf T}A$ 必对称
> $(A^{\mathsf T}A)^{\mathsf T}=A^{\mathsf T}(A^{\mathsf T})^{\mathsf T}=A^{\mathsf T}A$，故 $A^{\mathsf T}A$ 永远对称（与正定性相关，见 [[Symmetric and Positive Definite Matrices|对称矩阵和正定矩阵]]）。

## 2. 不变量 (Invariants)

相似矩阵共享：**特征值**（$Ax=\lambda x\Rightarrow B(M^{-1}x)=\lambda(M^{-1}x)$，特征值同但特征向量变为 $M^{-1}x$）、**迹**、**行列式**、**秩**、**特征多项式**。判断不相似：只要这些不变量有一个不同即可。

## 3. 若尔当标准型 (Jordan Canonical Form)

并非所有矩阵可对角化。**缺损矩阵 (defective)**：特征值重复且几何重数 $<$ 代数重数，特征向量不足。此时最接近对角的形式是分块对角的若尔当型 $J=\operatorname{diag}(J_1,J_2,\dots)$。每个**若尔当块**

$$J_i=\begin{bmatrix}\lambda_i&1&&\\ &\lambda_i&1&\\ &&\ddots&\ddots\\ &&&\lambda_i\end{bmatrix}$$

对角线是特征值、超对角线是 $1$。$1\times1$ 块即 $[\lambda_i]$（对角情形）；非零的"1"正是不可对角化的根源。

## 4. 构造规则 (Construction Rules)

1. 特征值定对角元；
2. **若尔当块数 = 线性无关特征向量数 = 零度 $\dim N(A-\lambda I)$**。块数 $=n$ 则全 $1\times1$（即对角化）；特征向量缺失则块变大。

> [!example] $4\times4$、特征值全为 $0$
> 特征向量 4/3/2/1 个分别对应：零矩阵 / 一个 $2\times2$+两个 $1\times1$ / 两个 $2\times2$ / 一个 $4\times4$。
> 确定块大小看"链长"（幂次）：若 $J^2\neq0$ 但 $J^3=0$，最大块至少 $3\times3$。例 $\operatorname{rank}J=2\Rightarrow$ 零度 $2\Rightarrow$ 2 个块；又 $J^2\neq0$ 排除两个 $2\times2$，故为一个 $3\times3$ + 一个 $1\times1$。

## 5. 地位 (Significance)

数值计算很少直接算若尔当型（重数对扰动敏感、数值不稳），但它是线性代数的理论基石——告诉我们每一类方阵归根结底"长什么样"。

---

> [!important] 一句话总结
> 相似矩阵改变坐标不改变变换本身，故保留特征值/迹/行列式；若尔当型是不可对角化矩阵的最简形式。
