---
aliases: [线性代数二次型, Quadratic Forms]
tags: [math, linear-algebra]
up: "[[Linear Algebra (MIT 18.06) MOC]]"
related: "[[Symmetric and Positive Definite Matrices|对称矩阵和正定矩阵]], [[Eigenvalues and Eigenvectors|特征值和特征向量]], [[Second Derivative Test|二阶导检验]], [[Maxima and Minima (Several Variables)|极大极小问题]]"
down: ""
---
# Quadratic Forms

> [!summary] 核心结论
> 多元函数在临界点附近的几何形状由 Hessian 给出的**二次型 (quadratic form)** $h^{\mathsf T}Hh$ 决定，而二次型的形状（碗/倒碗/马鞍）由 Hessian 特征值的符号决定。这把多元微积分的极值问题转化为线性代数的正定性问题。

前置知识：[[Eigenvalues and Eigenvectors|特征值和特征向量]]、[[Symmetric and Positive Definite Matrices|对称矩阵和正定矩阵]]。

---

## 1. 泰勒展开中的二次型 (Taylor Expansion)

$$f(a+h)\approx f(a)+\nabla f(a)^{\mathsf T}h+\tfrac12 h^{\mathsf T}H(a)h,\qquad H(a)=\Big[\tfrac{\partial^2 f}{\partial x_i\partial x_j}(a)\Big].$$

关键项 $\tfrac12 h^{\mathsf T}H(a)h$ 正是二次型。

## 2. 临界点的局部形状 (Local Shape)

$\nabla f(a)=0$ 时形状由 $h^{\mathsf T}Hh$ 决定：

- $H$ 正定 → 杯形 → 局部极小；$H$ 负定 → 倒杯 → 局部极大；
- $H$ 不定 → 马鞍点；$H$ 半定 → 二阶判别不够，需更高阶项。

## 3. 特征值分解与主轴 (Principal Axes)

Hessian 对称，可正交对角化 $H=Q\Lambda Q^{\mathsf T}$。令 $z=Q^{\mathsf T}h$：

$$h^{\mathsf T}Hh=z^{\mathsf T}\Lambda z=\sum_i\lambda_i z_i^2.$$

$Q$ 给主轴方向，$\lambda_i$ 给该方向的曲率正负与强度——**特征值全正 ⟺ 正定 ⟺ 极小**（见 [[Symmetric and Positive Definite Matrices|对称矩阵和正定矩阵]]）。

## 4. 二元判别式 (2D Test)

$H=\begin{pmatrix}f_{xx}&f_{xy}\\ f_{yx}&f_{yy}\end{pmatrix}$，$D=\det H=f_{xx}f_{yy}-f_{xy}^2$：$D>0,f_{xx}>0$ 极小；$D>0,f_{xx}<0$ 极大；$D<0$ 马鞍；$D=0$ 判别不够（与 [[Second Derivative Test|二阶导检验]] 一致）。

## 5. 水平集直觉 (Level Sets)

$f(a+h)=f(a)+c$ 给 $h^{\mathsf T}Hh\approx2c$：正定二次型水平集是椭圆，不定是双曲线，有零特征值则退化。

---

> [!important] 一句话总结
> Hessian 把局部极值问题转化为二次型的正定性问题——特征值符号决定碗、倒碗或马鞍。
