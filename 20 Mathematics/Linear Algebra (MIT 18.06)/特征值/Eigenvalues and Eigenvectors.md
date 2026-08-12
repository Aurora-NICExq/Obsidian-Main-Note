---
aliases: [特征值和特征向量, Eigenvalues and Eigenvectors]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[Symmetric and Positive Definite Matrices|对称矩阵和正定矩阵]], [[Similar Matrices and Jordan Form|相似矩阵与若尔当标准型]], [[Markov Matrices and Fourier Series|马尔可夫矩阵和傅立叶级数]]"
down: "[[Diagonalization and Matrix Powers|对角化和矩阵乘幂]], [[Linear Algebra and Differential Equations|线性代数与微分方程]]"
---
# Eigenvalues and Eigenvectors

> [!summary] 核心结论
> 特征向量 (eigenvector) 是矩阵作用下**方向保持不变**的特殊向量，对应的特征值 (eigenvalue) 给出该方向上的缩放倍数。求特征值归结为解**特征方程 (characteristic equation)** $\det(A-\lambda I)=0$。它把一个矩阵的复杂几何作用，分解为若干条相互独立的"伸缩轴"，是对角化、矩阵幂、微分方程组等一切应用的共同基础。

---

## 1. 定义：方向不变的向量 (Definition)

对于方阵 $A$ 与向量 $x$，乘积 $Ax$ 一般会同时改变 $x$ 的**方向**和**长度**（参见[[The Matrix Viewpoint|矩阵的视角]]）。我们专门寻找这样一类向量：经过 $A$ 作用后**方向不变**，只发生伸缩。这样的向量就是特征向量。 ^5e1c29

这一要求写成方程，就是特征值问题的核心方程：

$$Ax = \lambda x$$

其中标量 $\lambda$ 称为特征值，它正是 $x$ 在该方向上被放大（或缩小、反向）的倍数。注意 $x=0$ 恒满足方程却毫无信息，因此**约定特征向量非零**（$x\neq 0$）。

> [!note] 几何直觉
> $Ax=\lambda x$ 意味着 $x$ 落在一条"特殊的直线"上——这条直线在变换 $A$ 下被映射到自身。求特征向量，就是寻找这些被变换保留的方向；求特征值，就是测量每条方向上的缩放比例。

---

## 2. 如何求解 (Solving the Eigenproblem)

### 2.1 从核心方程到特征方程 (Characteristic Equation)

要把 $\lambda$ 解出来，先把 $Ax=\lambda x$ 移项，使右端为零： ^eb9473

$$(A - \lambda I)x = 0$$

这是一个齐次线性方程组。我们要的是**非零**解 $x$，因此矩阵 $A-\lambda I$ 必须把某个非零向量映为零，即它必须是**奇异矩阵 (singular matrix)**（[[Singular Matrices|不满秩、零空间非平凡]]）。奇异的充要条件是行列式为零，于是得到**特征方程**：

$$\det(A - \lambda I) = 0$$ ^f0e380

求解步骤因此分两步：**先**由特征方程解出全部特征值 $\lambda$，**再**对每个 $\lambda$ 回代 $(A-\lambda I)x=0$，求其零空间[[Vector Spaces and Subspaces#^0ed6c9|（特征向量张成该零空间）]]得到对应的特征向量。

### 2.2 二阶情形：迹与行列式 (2×2 Case)

对 $2\times 2$ 矩阵，特征方程展开后总可写成：

$$\lambda^2 - (\text{Trace})\,\lambda + (\text{Determinant}) = 0$$

由韦达定理 (Vieta's formulas) 立即得到两个极有用的关系：

- $\lambda_1 + \lambda_2 = \text{Trace}(A)$（迹，即对角线元素之和）
- $\lambda_1 \cdot \lambda_2 = \det(A)$（行列式）

### 2.3 推广到 $n\times n$ (General Case)

一般地，特征多项式 (characteristic polynomial) $P(\lambda)=\det(A-\lambda I)$ 是 $\lambda$ 的 $n$ 次多项式：

$$P(\lambda) = (-1)^n\lambda^n + c_{n-1}\lambda^{n-1} + \dots + c_1\lambda + c_0$$

它的两端系数最具几何意义：

- **次高次项系数** $c_{n-1}=(-1)^{n-1}\,\text{Trace}(A)$，这解释了为何**特征值之和等于迹**；
- **常数项** $c_0=\det(A)$。原因很直接：令 $\lambda=0$，则 $P(0)=\det(A-0\cdot I)=\det(A)$，而多项式中令 $\lambda=0$ 只剩常数项，故 $c_0=\det(A)$。这解释了为何**特征值之积等于行列式**。

> [!tip] 推论
> 由于 $\det(A-\lambda I)=\det\big((A-\lambda I)^{\mathsf T}\big)=\det(A^{\mathsf T}-\lambda I)$，矩阵 $A$ 与其转置 $A^{\mathsf T}$ 有**完全相同的特征值**。

---

## 3. 特征值的基本性质 (Basic Properties)

### 3.1 个数与线性无关性 (Count & Independence)

$n\times n$ 矩阵在复数域上恰有 $n$ 个特征值（含重数）。若这些特征值**两两不同 (distinct)**，则对应的 $n$ 个特征向量必然线性无关，从而[[Diagonalization and Matrix Powers#^2d96b0|特征向量矩阵可逆]]——这是矩阵可对角化的充分条件。

> [!note]- 证明：相异特征值对应的特征向量线性无关
> 设 $\lambda_1,\dots,\lambda_k$ 两两不同，对应特征向量 $x_1,\dots,x_k$，对 $k$ 用归纳法。$k=1$ 时 $x_1\neq0$ 显然无关。设前 $k-1$ 个线性无关，若 $x_k$ 可由它们线性表出，记 $x_k=\sum_{i<k}c_i x_i$。
> 两边左乘 $A$，利用 $Ax_i=\lambda_i x_i$ 得 $\lambda_k x_k=\sum_{i<k}c_i\lambda_i x_i$；又把 $x_k=\sum_{i<k}c_i x_i$ 两边乘以 $\lambda_k$ 得 $\lambda_k x_k=\sum_{i<k}c_i\lambda_k x_i$。两式相减：
> $$\sum_{i<k}c_i(\lambda_i-\lambda_k)\,x_i = 0.$$
> 由归纳假设 $x_1,\dots,x_{k-1}$ 线性无关，故每个系数 $c_i(\lambda_i-\lambda_k)=0$；又 $\lambda_i\neq\lambda_k$，于是 $c_i=0$，从而 $x_k=0$，与特征向量非零矛盾。故 $x_1,\dots,x_k$ 线性无关。$\blacksquare$

### 特征值与迹 (Eigenvalues and the Trace)

全部特征值之和等于矩阵的**迹 (trace)**，即对角线元素之和：

$$\sum_{i} \lambda_i = \text{Trace}(A)$$

迹是线性变换"总体伸缩量"的一个不变量，在散度、雅可比矩阵等场合反复出现。

### 3.2 行列式与可逆性 (Determinant & Invertibility)

全部特征值之积等于行列式 $\prod_i \lambda_i = \det(A)$。由此立刻得到一个判据：**矩阵奇异 $\iff$ 它有一个特征值为 $0$**。此时 $Ax=0\cdot x=0$，特征向量正是零空间中的非零向量。

---

## 4. 特殊矩阵的特征结构 (Special Matrices)

### 4.1 投影矩阵 (Projection Matrix)

投影矩阵 $P$ 满足 $P^2=P$，其特征值只能是 $0$ 或 $1$，对应两类几何清晰的特征向量：

- **位于投影平面内的向量**：投影不改变它，$Px = 1\cdot x$（[[Projections and Projection Matrices#^a956d5|向量的投影]]），故 $\lambda=1$；
- **垂直于投影平面的向量**（属于左零空间）：被投影压成零，$Px = 0\cdot x$，故 $\lambda=0$。

代数上也能验证：由 $Px=\lambda x$ 与 $P^2=P$ 得 $\lambda x = \lambda^2 x$，因 $x\neq 0$ 故 $\lambda=\lambda^2$，解得 $\lambda\in\{0,1\}$。

### 4.2 复数特征值：旋转与反对称矩阵 (Complex Eigenvalues)

当矩阵含有"旋转"成分（即非对称）时，可能没有实特征值。例如逆时针旋转 $90^\circ$ 的矩阵 ^fa8cf9

$$Q = \begin{bmatrix} 0 & -1 \\ 1 & 0 \end{bmatrix}$$

没有任何**实**向量在它作用下方向不变，因此它没有实特征值，特征值为纯虚数 $\pm i$。一般规律是：

- **对称矩阵 (symmetric, $A=A^{\mathsf T}$)**：特征值全为**实数**；
- **反对称矩阵 (skew-symmetric, $A=-A^{\mathsf T}$)**：特征值全为**纯虚数**。

> [!note]- 证明：实对称矩阵的特征值为实数
> 设实对称矩阵 $A=A^{\mathsf T}$，$Ax=\lambda x$（$x\neq0$，允许 $x,\lambda$ 取复值）。左乘共轭转置 $\bar x^{\mathsf T}$：
> $$\bar x^{\mathsf T}Ax=\lambda\,\bar x^{\mathsf T}x=\lambda\lVert x\rVert^2.$$
> 另一方面，对 $Ax=\lambda x$ 取共轭转置得 $\bar x^{\mathsf T}\bar A^{\mathsf T}=\bar\lambda\,\bar x^{\mathsf T}$；因 $A$ 为**实**矩阵 $\bar A=A$ 且对称 $A^{\mathsf T}=A$，故 $\bar A^{\mathsf T}=A$，右乘 $x$ 得
> $$\bar x^{\mathsf T}Ax=\bar\lambda\,\lVert x\rVert^2.$$
> 两式左端相同，且 $\lVert x\rVert^2>0$，故 $\lambda=\bar\lambda$，即 $\lambda$ 为实数。对反对称矩阵 $A^{\mathsf T}=-A$，同样推演给出 $\lambda=-\bar\lambda$，即 $\lambda$ 为纯虚数。$\blacksquare$

由于实矩阵的特征多项式系数为实数，根据代数基本定理 (Fundamental Theorem of Algebra)，复特征值必**共轭成对 (conjugate pairs)** 出现。

### 4.3 矩阵平移 $A+cI$ (Matrix Shift)

把矩阵加上单位矩阵的倍数，是少数能简单预测特征值变化的运算：**特征向量完全不变，特征值整体平移 $+c$**。证明只需一行：

$$(A+cI)x = Ax + cIx = \lambda x + cx = (\lambda + c)x$$

> [!warning] 适用范围
> 该规律**只**对 $A+cI$（加单位矩阵的倍数）成立。对一般的 $A+B$，特征值通常**不会**相加，特征向量也会改变——除非 $A$ 与 $B$ 恰好共享同一组特征向量。

---

## 5. 特征值重复与可对角化性 (Repeated Eigenvalues & Diagonalizability)

当特征值出现重复时，能否凑齐足够多的线性无关特征向量，决定了矩阵是否可对角化。 ^34e50d

这里需要区分两个"重数 (multiplicity)"：

- **代数重数 (algebraic multiplicity)**：$\lambda$ 作为特征方程根的重数；
- **几何重数 (geometric multiplicity)**：$\lambda$ 对应特征空间的维数（即线性无关特征向量个数）。

二者的关系决定矩阵的"好坏"（详见[[Diagonalization and Matrix Powers#^534e80|对角化条件]]）：

- **可对角化（"好"矩阵）**：每个特征值的几何重数 $=$ 代数重数。对称矩阵、对角矩阵、单位矩阵都属此类。
- **不可对角化（"坏"矩阵）**：存在几何重数 $<$ 代数重数的特征值，例如剪切矩阵 (shear matrix)，特征向量不足，无法对角化（需用[[Similar Matrices and Jordan Form|若尔当标准型]]处理）。

---

## 6. 应用 (Applications)

1. **判断可逆性 (invertibility)**：若 $A$ 有特征值 $0$ 则 $A$ 奇异；但 $A+I$ 的对应特征值变为 $0+1=1$，矩阵随即可逆。这一"平移使其可逆"的技巧在数值算法中很常见（如 Google 的 PageRank 通过类似手段保证良态）。
2. **求解微分方程组 (systems of ODEs)**：解 $\dfrac{du}{dt}=Au$ 时，沿特征向量方向解耦为标量方程，通解形如 $e^{\lambda t}$ 的叠加（详见[[Linear Algebra and Differential Equations|线性代数与微分方程]]）。这正是特征值连接线性代数与微积分的桥梁。

---

> [!important] 一句话总结
> 特征值问题的本质，是寻找矩阵作用下**方向不变**的特殊向量——它把矩阵对角化为一组独立的伸缩轴，从而让矩阵幂、指数与动力学问题都变得透明。
