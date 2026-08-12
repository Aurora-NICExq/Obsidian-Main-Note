---
aliases: [马尔可夫矩阵和傅立叶级数, Markov Matrices and Fourier Series]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[Eigenvalues and Eigenvectors|特征值和特征向量]], [[Similar Matrices and Jordan Form|相似矩阵与若尔当标准型]], [[Linear Algebra and Differential Equations|线性代数与微分方程]], [[Diagonalization and Matrix Powers|对角化和矩阵乘幂]]"
down: ""
---
# Markov Matrices and Fourier Series

> [!summary] 核心结论
> 马尔可夫矩阵 (Markov matrix) 描述状态转移，必有特征值 $\lambda=1$ 且所有 $|\lambda|\le1$，故收敛到稳态。傅里叶级数 (Fourier series) 把"正交基投影"思想搬到无穷维函数空间。

前置知识：[[Eigenvalues and Eigenvectors|特征值和特征向量]]、[[Diagonalization and Matrix Powers|对角化和矩阵乘幂]]。

---

## 1. 马尔可夫矩阵 (Markov Matrices)

**定义**：元素非负、每列之和为 $1$（配合列向量 $u_{k+1}=Au_k$）。

### 两条核心性质

1. **必有 $\lambda=1$**：因每列和为 $1$，$A-I$ 各列和为 $0$，行向量线性相关 ⟹ $\det(A-I)=0$（见 [[Eigenvalues and Eigenvectors#^f0e380|特征值的求解]]）。等价地，$A^{\mathsf T}$ 的全 $1$ 向量满足 $A^{\mathsf T}\mathbf1=\mathbf1$，而 $A,A^{\mathsf T}$ 同特征值。
2. **所有 $|\lambda|\le1$**：由**盖尔圆盘定理 (Gershgorin)**——特征值落在以 $a_{ii}$ 为心、$R_i=\sum_{j\neq i}|a_{ij}|=1-a_{ii}$ 为半径的圆盘内，故 $|z|\le a_{ii}+(1-a_{ii})=1$。

![[tikz-markov-matrices-and-fourier-series-01.svg]]

### 稳态 (Steady State)

把 $u_0=\sum c_ix_i$ 迭代：$u_k=c_1\cdot1^k x_1+\sum_{i\ge2}c_i\lambda_i^k x_i$。因其余 $|\lambda_i|<1$，$k\to\infty$ 时只剩 $u_\infty=c_1x_1$——收敛到 $\lambda=1$ 的特征向量方向。

> [!example] 人口迁移
> $A=\begin{bmatrix}0.9&0.2\\ 0.1&0.8\end{bmatrix}$，解 $(A-I)x=0$ 得稳态 $x_1=\begin{bmatrix}2\\1\end{bmatrix}$：长期加州人口是 Mass 的 2 倍（$\tfrac23$ vs $\tfrac13$）。

## 2. 傅里叶级数 (Fourier Series)

任何周期函数 $f(x)=a_0+\sum_k(a_k\cos kx+b_k\sin kx)$，这是线性代数在**无穷维函数空间**的应用，核心是**投影**。

- **向量空间**：周期函数；**基**：$1,\cos x,\sin x,\cos2x,\dots$；**坐标**：系数 $a_k,b_k$。
- **内积**：$f\cdot g=\int_0^{2\pi}fg\,dx$；基函数**两两正交**（如 $\int_0^{2\pi}\cos nx\cos kx\,dx=0,\ n\neq k$）。

### 求系数 = 投影 (Projection)

正交基下系数 = 投影 = $\dfrac{f\cdot e_k}{e_k\cdot e_k}$：

$$a_k=\frac{1}{\pi}\int_0^{2\pi}f(x)\cos kx\,dx,\quad b_k=\frac{1}{\pi}\int_0^{2\pi}f(x)\sin kx\,dx,\quad a_0=\frac{1}{2\pi}\int_0^{2\pi}f\,dx.$$

> [!note] 为何能"抓出" $a_k$
> 等式两边乘 $\cos kx$ 再积分；由正交性，除"自己乘自己"项外全部为 $0$，剩 $\int f\cos kx=a_k\int(\cos kx)^2=a_k\pi$（用积化和差证正交，正弦/余弦在整周期上积分为 $0$）。

成为"基"还需**完备性**（收敛定理保证不漏任何"方向"）。

---

> [!important] 一句话总结
> 马尔可夫过程看稳态（$\lambda=1$ 主导），傅里叶分析看正交分量（系数即投影）。
