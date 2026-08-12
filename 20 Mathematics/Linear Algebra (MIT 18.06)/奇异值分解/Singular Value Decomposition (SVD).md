---
aliases: [奇异值分解, Singular Value Decomposition, SVD]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[Eigenvalues and Eigenvectors|特征值和特征向量]], [[Symmetric and Positive Definite Matrices|对称矩阵和正定矩阵]], [[Orthogonal Matrices and Gram-Schmidt|正交矩阵和正交化法]], [[Orthogonal Vectors and Subspaces|正交向量和正交子空间(orthogonal)]]"
down: ""
---
# Singular Value Decomposition (SVD)

> [!summary] 核心结论
> SVD 把**任意** $m\times n$ 矩阵分解为 $A=U\Sigma V^{\mathsf T}$：**输入正交旋转 $V^{\mathsf T}$ → 轴向伸缩 $\Sigma$ → 输出正交旋转 $U$**。它用输入、输出**两组正交基**实现"对角化"，是线性代数基本定理的最终形式。

前置知识：[[Symmetric and Positive Definite Matrices|对称矩阵和正定矩阵]]、[[Orthogonal Matrices and Gram-Schmidt|正交矩阵和正交化法]]。

---

## 1. 动机：两组基 (Two Bases)

对称矩阵有 $A=Q\Lambda Q^{\mathsf T}$（正交基 + 实特征值）；一般矩阵的 $A=S\Lambda S^{-1}$ 中 $S$ 列**不正交**。SVD 的突破：在**输入空间**用正交基 $v_1,\dots,v_n$、**输出空间**用另一组正交基 $u_1,\dots,u_m$，对长方形矩阵也成立。

## 2. 几何：圆 → 椭圆 (Circle to Ellipse)

$A$ 把输入空间单位圆变成输出空间的椭圆。SVD 找椭圆主轴：$v_i$（右奇异向量）是输入圆上经 $A$ 落在主轴方向的单位向量；$u_i$（左奇异向量）是输出主轴单位向量；$\sigma_i$（奇异值）是半轴长（伸缩倍率），$Av_i=\sigma_i u_i$。

![[tikz-singular-value-decomposition-svd-01.svg]]

## 3. 代数推导 (Derivation)

把 $Av_i=\sigma_i u_i$ 装成矩阵 $AV=U\Sigma$；因 $V$ 正交（$V^{-1}=V^{\mathsf T}$），右乘 $V^{\mathsf T}$：

$$A=U\Sigma V^{\mathsf T}.$$

- $U$（$m\times m$ 正交，列为左奇异向量）；$\Sigma$（$m\times n$ 对角，$\sigma_1\ge\sigma_2\ge\cdots\ge0$）；$V$（$n\times n$ 正交，列为右奇异向量）。

## 4. 如何求解：转向 $A^{\mathsf T}A$ (Via $A^{\mathsf T}A$)

$A^{\mathsf T}A$ 对称半正定（见 [[Symmetric and Positive Definite Matrices|对称矩阵和正定矩阵]]）：

$$A^{\mathsf T}A=(U\Sigma V^{\mathsf T})^{\mathsf T}(U\Sigma V^{\mathsf T})=V(\Sigma^{\mathsf T}\Sigma)V^{\mathsf T},$$

正是 $A^{\mathsf T}A$ 的特征值分解：**$V$ 是其特征向量，$\sigma_i=\sqrt{\lambda_i}$**。同理 $AA^{\mathsf T}=U(\Sigma\Sigma^{\mathsf T})U^{\mathsf T}$ 给出 $U$。

## 5. 计算步骤 (Algorithm)

1. 算 $A^{\mathsf T}A$；2. 求特征值 $\lambda_i$ → $\sigma_i=\sqrt{\lambda_i}$（降序），单位特征向量构成 $V$；3. 用 **$u_i=\dfrac{Av_i}{\sigma_i}$** 求前 $r$ 个 $u$（保证符号匹配）；4. 用 Gram–Schmidt 补全零空间方向。

> [!example] 例 $A=\begin{bmatrix}4&4\\ -3&3\end{bmatrix}$
> $A^{\mathsf T}A=\begin{bmatrix}25&7\\ 7&25\end{bmatrix}$，$\lambda=32,18$，$\sigma_1=4\sqrt2,\sigma_2=3\sqrt2$；$v_1=\tfrac{1}{\sqrt2}\begin{bmatrix}1\\1\end{bmatrix},v_2=\tfrac{1}{\sqrt2}\begin{bmatrix}-1\\1\end{bmatrix}$；由 $u_i=Av_i/\sigma_i$ 得 $u_1=\begin{bmatrix}1\\0\end{bmatrix}$ 等。

## 6. 关键性质 (Key Properties)

- **秩** $r=$ 非零奇异值个数；
- 四个子空间的标准正交基：$v_{1..r}$ 行空间、$u_{1..r}$ 列空间、$v_{r+1..n}$ 零空间、$u_{r+1..m}$ 左零空间（见 [[Orthogonal Vectors and Subspaces|正交向量和正交子空间(orthogonal)]]）；
- **应用**：$\sigma_1$ 含最多信息，故 SVD 用于图像压缩、去噪与 PCA。

---

> [!important] 一句话总结
> SVD：选输入正交轴 $V$ → 按奇异值 $\Sigma$ 拉伸 → 旋转到输出正交轴 $U$；求解归结为 $A^{\mathsf T}A$ 的特征分解。
