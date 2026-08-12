---
aliases: [矩阵, Matrices, Gaussian Elimination, LU Decomposition]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[The Matrix Viewpoint|矩阵的视角]], [[How Matrix Multiplication Works|矩阵乘法的原理]], [[Singular Matrices|singular矩阵]], [[Vector Spaces and Subspaces|向量空间及其子空间]]"
down: "[[Vector Spaces and Subspaces|向量空间及其子空间]]"
---
# Matrices (Systems, Elimination, Inverse)

> [!summary] 核心结论
> 矩阵 (matrix) 同时表示**线性方程组、线性变换与列向量的线性组合**。求解的主线是：消元 (elimination) → $LU$ 分解 → 逆矩阵 (inverse) → 转置与置换。

---

## 1. 线性方程组 (Linear Systems)

每个方程是一个"线性几何对象"，解集是它们的交集（二维是直线、三维是平面）；秩 (rank) 是独立约束的个数。矩阵形式：

$$A\mathbf x=\mathbf b,\quad A\in\mathbb R^{m\times n},\ \mathbf x\in\mathbb R^n,\ \mathbf b\in\mathbb R^m,$$

其中 $A$ 是系数矩阵（[[The Matrix Viewpoint#^631678|矩阵的结构视角]]）。

### 线性组合 (Linear Combination)

$A\mathbf x$ 的本质是**对 $A$ 的列向量加权求和**：$\sum_i x_i\,\alpha_i$。满足 $A\mathbf x=0$ 的 $\mathbf x$ 张成零空间（[[Vector Spaces and Subspaces#^ac1101|零空间的理解]]）。增广矩阵 $[\,A\mid\mathbf b\,]$ 把右端并入便于消元。

### 矩阵初等变换 (Elementary Row Operations)

由单位矩阵经一次初等变换得到**初等矩阵 (elementary matrix)**：互换、倍乘、倍加三类。**左乘**初等矩阵做行变换，**右乘**做列变换。矩阵方程的化简见 [[Vector Spaces and Subspaces#^0abc1a|行最简矩阵]]。

## 2. 回代 (Back Substitution)

高斯消元把 $A\mathbf x=\mathbf b$ 化为上三角 $U\mathbf x=\mathbf y$ 后，从最后一个未知数往回算：

$$x_i=\frac{y_i-\sum_{j>i}u_{ij}x_j}{u_{ii}},\qquad i=n,n-1,\dots,1.$$

## 3. 矩阵乘法 (Matrix Multiplication)

### 乘法的结合律 (Associativity of Multiplication)

$(AB)C=A(BC)$——括号可增减；但一般**不可交换** $AB\neq BA$。乘法可按行视角、列视角或分块 (block) 进行：

$$AB=\begin{pmatrix}A_{11}B_{11}+A_{12}B_{21}&A_{11}B_{12}+A_{12}B_{22}\\ A_{21}B_{11}+A_{22}B_{21}&A_{21}B_{12}+A_{22}B_{22}\end{pmatrix}.$$

## 4. 矩阵的逆 (Matrix Inverse)

^7ddbcc

方阵的逆满足 $A^{-1}A=AA^{-1}=I$。要点：

1. 不可逆（奇异, singular）⟺ 至少一列无贡献（[[Singular Matrices|singular矩阵]]）；
2. 方阵的左逆 = 右逆；$(A^{-1})^{\mathsf T}=(A^{\mathsf T})^{-1}$；
3. **"鞋袜定理"**：$(AB)^{-1}=B^{-1}A^{-1}$（穿脱顺序相反）。

**高斯–若尔当法**：$[\,A\mid I\,]\xrightarrow{\text{Gauss–Jordan}}[\,I\mid A^{-1}\,]$。

## 5. 消元与 $LU$ 分解 (Elimination & LU)

每次行变换等价于左乘初等矩阵 $E_{ij}$（见 [[Matrices (Systems, Elimination, Inverse)#矩阵初等变换 (Elementary Row Operations)|矩阵初等变换]]）。多步消元 $(E_{32}E_{31}E_{21})A=U$，移到右边得

$$A=LU,$$

- $L$（下三角）记录消元乘数（变号填回）；$U$（上三角）含主元 (pivots)。

应用：解方程 $LUx=b$（先 $Ly=b$ 再 $Ux=y$）；行列式 $\det A=\det L\det U$；时间复杂度上高斯消元 $O(n^3)$、$LU$ 回代 $O(n^2)$。

## 6. 转置与置换 (Transpose & Permutation)

### 置换矩阵 P (Permutation Matrix)

行重排的单位矩阵；$n$ 阶有 $n!$ 个。性质：通过左乘做行变换；$P^{-1}=P^{\mathsf T}$（变换后再变回）；用于把 $0$ 从主元位置换走。

### 转置 (Transpose)

$(A^{\mathsf T})_{ij}=a_{ji}$。

#### 对称矩阵 (Symmetric Matrix)

若 $A^{\mathsf T}=A$ 则对称。重要事实：任意 $R$ 与其转置之积 $RR^{\mathsf T}$ 必对称——

$$(RR^{\mathsf T})^{\mathsf T}=(R^{\mathsf T})^{\mathsf T}R^{\mathsf T}=RR^{\mathsf T}.$$

---

> [!important] 一句话总结
> 矩阵组织线性关系，并通过消元、乘法与逆进行求解；$A=LU$ 是这套机器的核心分解。
