---
aliases: [线性代数与微分方程, Linear Algebra and Differential Equations]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[Eigenvalues and Eigenvectors|特征值和特征向量]], [[Similar Matrices and Jordan Form|相似矩阵与若尔当标准型]], [[Markov Matrices and Fourier Series|马尔可夫矩阵和傅立叶级数]], [[Symmetric and Positive Definite Matrices|对称矩阵和正定矩阵]], [[Diagonalization and Matrix Powers|对角化和矩阵乘幂]]"
down: "[[Symmetric and Positive Definite Matrices|对称矩阵和正定矩阵]]"
---
# Linear Algebra and Differential Equations

> [!summary] 核心结论
> 一阶线性微分方程组 $\dfrac{d\mathbf u}{dt}=A\mathbf u$ 的解沿特征向量方向**解耦**为 $e^{\lambda t}x$ 的叠加；长期行为（稳定/稳态/发散）由特征值实部决定。统一写法是矩阵指数 $\mathbf u(t)=e^{At}\mathbf u(0)$。

前置知识：[[Eigenvalues and Eigenvectors|特征值和特征向量]]、[[Diagonalization and Matrix Powers|对角化和矩阵乘幂]]。

---

## 1. 动态问题 (The Dynamic Problem)

$$\frac{d\mathbf u}{dt}=A\mathbf u,\quad \mathbf u(0)\text{ 给定}.$$

类比标量 $\tfrac{dy}{dt}=ay$ 解 $y=e^{at}y(0)$，希望 $\mathbf u(t)=e^{At}\mathbf u(0)$。

## 2. 解法一：特征值解耦 (Decoupling)

设 $\mathbf u=e^{\lambda t}x$ 代入得核心方程 $Ax=\lambda x$。若 $A$ 有 $n$ 个线性无关特征向量，通解（叠加原理）：

$$\mathbf u(t)=\sum_i c_i e^{\lambda_i t}x_i,\qquad c=S^{-1}\mathbf u(0).$$

### 稳定性 (Stability)

| 情况 | 条件 | $t\to\infty$ |
| :-- | :-- | :-- |
| 稳定 | 所有 $\operatorname{Re}\lambda<0$ | $\mathbf u\to\mathbf0$ |
| 稳态 | 一个 $\lambda=0$，其余 $\operatorname{Re}<0$ | $\mathbf u\to$ 常向量 |
| 不稳定 | 任一 $\operatorname{Re}\lambda>0$ | $\mathbf u\to\infty$ |

复特征值 $\lambda=a+bi$：$e^{\lambda t}=e^{at}(\cos bt+i\sin bt)$——实部 $a$ 管增长/衰减，虚部 $b$ 管振荡。

## 3. 解法二：矩阵指数 (Matrix Exponential)

$$e^{At}=I+At+\frac{(At)^2}{2!}+\cdots,\qquad e^{At}=S\,e^{\Lambda t}\,S^{-1},$$

其中 $e^{\Lambda t}=\operatorname{diag}(e^{\lambda_1 t},\dots,e^{\lambda_n t})$。两解法统一：$\mathbf u(t)=Se^{\Lambda t}S^{-1}\mathbf u(0)=Se^{\Lambda t}c$。

## 4. 示例 (Example)

$A=\begin{bmatrix}-2&1\\ 1&-2\end{bmatrix}$：$\lambda_1=-1,\lambda_2=-3$（均 $<0$，稳定），$x_1=\begin{bmatrix}1\\1\end{bmatrix},x_2=\begin{bmatrix}1\\-1\end{bmatrix}$：

$$\mathbf u(t)=c_1e^{-t}\begin{bmatrix}1\\1\end{bmatrix}+c_2e^{-3t}\begin{bmatrix}1\\-1\end{bmatrix}.$$

$\mathbf u(0)=\begin{bmatrix}1\\0\end{bmatrix}$ 给 $c_1=c_2=\tfrac12$。

## 5. 二阶方程降阶 (Reduction to First Order)

$y''+by'+ky=0$ 设 $\mathbf u=\begin{bmatrix}y\\ y'\end{bmatrix}$ 化为 $\mathbf u'=\begin{bmatrix}0&1\\ -k&-b\end{bmatrix}\mathbf u$（类比 [[Diagonalization and Matrix Powers#^a26777|斐波那契数列求解]]，物理见 [[Damped Oscillation|阻尼振动]]）。

---

> [!important] 一句话总结
> 微分方程组沿特征向量解耦：每个方向按 $e^{\lambda t}$ 演化，特征值实部决定稳定性。
