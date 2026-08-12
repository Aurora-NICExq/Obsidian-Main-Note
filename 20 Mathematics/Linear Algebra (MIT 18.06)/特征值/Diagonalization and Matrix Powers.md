---
aliases: [对角化和矩阵乘幂, Diagonalization and Matrix Powers, Diagonalization]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[Eigenvalues and Eigenvectors|特征值和特征向量]], [[Similar Matrices and Jordan Form|相似矩阵与若尔当标准型]], [[Markov Matrices and Fourier Series|马尔可夫矩阵和傅立叶级数]], [[Linear Algebra and Differential Equations|线性代数与微分方程]], [[Symmetric and Positive Definite Matrices|对称矩阵和正定矩阵]]"
down: "[[Linear Algebra and Differential Equations|线性代数与微分方程]]"
---
# Diagonalization and Matrix Powers

> [!summary] 核心结论
> 可对角化矩阵 (diagonalizable matrix) 通过 $A=S\Lambda S^{-1}$ 把高次幂化为特征值的高次幂 $A^k=S\Lambda^k S^{-1}$，从而轻松求解矩阵幂与差分方程。

前置知识：[[Eigenvalues and Eigenvectors|特征值和特征向量]]。

---

## 1. 特征向量矩阵 (Eigenvector Matrix)

把 $n$ 个线性无关的[[Eigenvalues and Eigenvectors#^5e1c29|特征向量]] $x_1,\dots,x_n$ 作列组成 $S$。 ^2d96b0

由 $Ax_i=\lambda_i x_i$ 得 $AS=S\Lambda$，其中 $\Lambda=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$（用[[How Matrix Multiplication Works|列视角]]）。

## 2. 对角化公式 (Diagonalization)

^c37711

$$A=S\Lambda S^{-1},\qquad \Lambda=S^{-1}AS.$$

$\Lambda$ 中特征值的顺序必须与 $S$ 中特征向量列的顺序一一对应。

### 快速求矩阵幂 (Matrix Powers)

$$A^2=(S\Lambda S^{-1})(S\Lambda S^{-1})=S\Lambda^2 S^{-1},\qquad A^k=S\Lambda^k S^{-1}.$$

**稳定性**：$k\to\infty$ 时 $A^k$ 取决于 $|\lambda|$——全 $<1$ 趋于 $0$（稳定），有 $>1$ 发散，$=1$ 临界。

### 对角化条件 (Condition)

^534e80

$A$ 须有 $n$ 个**线性无关**特征向量（$S$ 才可逆，见 [[Matrices (Systems, Elimination, Inverse)#^7ddbcc|矩阵可逆满秩]]）。特征值重复时**可能**（不一定）凑不齐特征向量（见 [[Eigenvalues and Eigenvectors#^34e50d|特征值重复的不同情况]]）。

## 3. 求差分方程 (Difference Equations)

解 $u_{k+1}=Au_k$：把 $u_0=\sum c_i x_i=Sc$，则 $c=S^{-1}u_0$，

$$u_k=S\Lambda^k S^{-1}u_0=\sum_i c_i\lambda_i^k x_i.$$

### 斐波那契数列 (Fibonacci)

^a26777

$F_{k+2}=F_{k+1}+F_k$ 降维为 $\begin{bmatrix}F_{k+2}\\ F_{k+1}\end{bmatrix}=\begin{bmatrix}1&1\\ 1&0\end{bmatrix}\begin{bmatrix}F_{k+1}\\ F_k\end{bmatrix}$。特征值 $\lambda=\tfrac{1\pm\sqrt5}{2}$（黄金比 $\approx1.618$ 与 $\approx-0.618$），由 $u_0=\begin{bmatrix}1\\0\end{bmatrix}$ 得 $c_1=\tfrac{1}{\sqrt5},c_2=-\tfrac{1}{\sqrt5}$，**比内公式**：

$$F_k=\frac{1}{\sqrt5}\left(\frac{1+\sqrt5}{2}\right)^k-\frac{1}{\sqrt5}\left(\frac{1-\sqrt5}{2}\right)^k.$$

$k$ 大时第二项趋于 $0$，故斐波那契以黄金比的指数速度增长。

---

> [!important] 一句话总结
> 只要能对角化，矩阵的高次幂就变成特征值的高次幂——差分方程沿特征向量解耦。
