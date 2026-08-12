---
aliases: [对称矩阵和正定矩阵, Symmetric and Positive Definite Matrices, Positive Definite]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[Eigenvalues and Eigenvectors|特征值和特征向量]], [[Similar Matrices and Jordan Form|相似矩阵与若尔当标准型]], [[Quadratic Forms|线性代数二次型]], [[Diagonalization and Matrix Powers|对角化和矩阵乘幂]]"
down: "[[Similar Matrices and Jordan Form|相似矩阵与若尔当标准型]]"
---
# Symmetric and Positive Definite Matrices

> [!summary] 核心结论
> 实对称矩阵 (real symmetric matrix) 必可**正交对角化** $A=Q\Lambda Q^{\mathsf T}$（谱定理）。**正定矩阵 (positive definite)** 有四个等价判据：所有特征值 / 主元 / 顺序主子式为正，或对任意 $x\neq0$ 有 $x^{\mathsf T}Ax>0$（能量）。

前置知识：[[Eigenvalues and Eigenvectors|特征值和特征向量]]。

---

## 1. 对称矩阵的性质 (Properties)

^d38018

实对称矩阵 $A=A^{\mathsf T}$：① 特征值**全为实数**；② 特征向量**相互正交**（可选标准正交基）。

### 谱定理 (Spectral Theorem)

特征向量矩阵可取正交矩阵 $Q$（见 [[Symmetric and Positive Definite Matrices#^d38018|对称矩阵性质2]]）：

$$A=Q\Lambda Q^{\mathsf T}=\lambda_1 q_1q_1^{\mathsf T}+\cdots+\lambda_n q_nq_n^{\mathsf T}.$$

因 $q_iq_i^{\mathsf T}$ 是投影到 $q_i$ 直线上的投影矩阵（见 [[Projections and Projection Matrices#^36ed38|投影矩阵]]），故 **$A$ 是 $n$ 个投影矩阵的线性组合，系数即特征值**。

> [!note] 为何特征值为实（证明）
> 设 $Ax=\lambda x$。取共轭转置并点积得 $\lambda x^{H}x=\bar\lambda x^{H}x$；因 $x^{H}x=\|x\|^2>0$，故 $\lambda=\bar\lambda$，即 $\lambda$ 为实数。实对称是 Hermitian（$A=\bar A^{\mathsf T}$）在实域的特例。主元符号与特征值符号一致，主元之积 = 特征值之积 $=\det A$。

## 2. 正定矩阵的四个判据 (Four Tests)

| 视角 | 条件 |
| :-- | :-- |
| 特征值 | 所有 $\lambda_i>0$ |
| 能量（定义） | 对任意 $x\neq0$，$x^{\mathsf T}Ax>0$ |
| 行列式 | 所有顺序主子式 $>0$ |
| 消元 | 所有主元 (pivots) $>0$ |

**二次型 (quadratic form)**：$x^{\mathsf T}Ax=ax_1^2+2bx_1x_2+cx_2^2$（纯量）。正定的"真正定义"是它对所有非零 $x$ 为正。

## 3. 几何：碗与马鞍 (Bowl vs Saddle)

正定 ⟹ $x^{\mathsf T}Ax$ 是向上开口的"碗"，唯一最低点在原点；特征值是各方向的曲率（$\lambda_{\max}$ 最陡、$\lambda_{\min}$ 最平）。

![[tikz-symmetric-and-positive-definite-matrices-01.svg]]

不定矩阵（特征值一正一负）⟹ 马鞍面：

![[tikz-symmetric-and-positive-definite-matrices-02.svg]]

**水平截面**：$x^{\mathsf T}Ax=1$ 对正定是椭圆（封闭，$ac-b^2>0,a>0$），对不定是双曲线（$ac-b^2<0$）。**主轴定理**：特征向量给椭圆长短轴方向，特征值给轴长（$\lambda$ 越大轴越短，$x=1/\sqrt\lambda$）。

## 4. 与多元极值的联系 (Optimization)

临界点 $\nabla f=\mathbf0$ 后，$\Delta f\approx\tfrac12 x^{\mathsf T}Hx$（$H$ 为 Hessian，对称）。局部极小 ⟺ $H$ 正定。对照表：一元 $f''>0$ ↔ 多元 $H$ 正定；$f''<0$ ↔ 负定；拐点 ↔ 不定（见 [[Quadratic Forms|线性代数二次型]]、[[Second Derivative Test|二阶导检验]]）。条件数（$\lambda_{\max}/\lambda_{\min}$）大时碗变"峡谷"，梯度下降收敛慢。

## 5. 配方 = 高斯消元 (Completing the Square = Elimination)

对二次型配方等价于做高斯消元：括号外系数 = **主元**，括号内变量系数 = **乘数**。例 $A=\begin{bmatrix}2&6\\6&20\end{bmatrix}$：

$$f=2(x+3y)^2+2y^2\quad\Longleftrightarrow\quad U=\begin{bmatrix}2&6\\0&2\end{bmatrix},\ l_{21}=3.$$

即分解 $A=LDL^{\mathsf T}$。**所有主元为正 ⟺ 正定**（配方后是正系数平方和）。

---

> [!important] 一句话总结
> 正定矩阵的代数条件与几何条件一致：二次型在所有非零方向上恒正，图像是向上开口的碗。
