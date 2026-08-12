---
aliases: [空间线积分、旋度与势函数, Line Integrals in Space Curl and Potential Functions, Curl]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Topological Subtleties and Maxwell's Equations|拓扑注意事项与麦克斯韦方程组]], [[Stokes' Theorem|斯托克斯定理]], [[Vector Fields, Surface Integrals, and Flux in 3D|三维向量场、曲面积分与通量]], [[Divergence Theorem (Gauss's Theorem)|散度定理（高斯定理）]], [[Gradient Fields and Potential Functions|gradient field,potential function]]"
down: "[[Stokes' Theorem|斯托克斯定理]]"
---
# Line Integrals in Space, Curl, and Potential Functions

> [!summary] 核心结论
> 三维线积分仍是沿曲线做功。旋度 (curl) $\nabla\times\mathbf F$ 刻画**局部环量密度**，是斯托克斯定理的被积函数；恒等式 $\nabla\times(\nabla f)=\mathbf0$ 说明梯度场必无旋。

前置知识：[[Vector Fields and Line Integrals in the Plane|平面向量场和线积分]]、[[Gradient Fields and Potential Functions|gradient field,potential function]]。

---

## 1. 空间曲线的线积分 (3D Line Integral)

$$\int_C\mathbf F\cdot d\mathbf r=\int_a^b\mathbf F(\mathbf r(t))\cdot\mathbf r'(t)\,dt=\int_C P\,dx+Q\,dy+R\,dz.$$

仍是"代入 → 求导 → 点乘 → 一元积分"；反向走变号。

## 2. 梯度场与势函数（3D） (Potential)

若 $\mathbf F=\nabla f=\langle f_x,f_y,f_z\rangle$，则保守，$\int_C\mathbf F\cdot d\mathbf r=f(P_1)-f(P_0)$，只依赖端点。

## 3. 旋度 (Curl)

$$\nabla\times\mathbf F=\operatorname{curl}\mathbf F=\langle R_y-Q_z,\ P_z-R_x,\ Q_x-P_y\rangle.$$

**环量密度直觉**：对一点附近的小回路 $C$（法向 $\mathbf n$、面积 $\Delta S$），$(\operatorname{curl}\mathbf F)\cdot\mathbf n\approx\dfrac{1}{\Delta S}\oint_C\mathbf F\cdot d\mathbf r$。基本恒等式 $\nabla\times(\nabla f)=\mathbf0$，故梯度场必有 $\operatorname{curl}\mathbf F=\mathbf0$（必要条件）。

## 4. 求势函数 (Exactness)

解 $f_x=P,\ f_y=Q,\ f_z=R$：

1. 由 $f_x=P$ 积分 $f=\int P\,dx+g(y,z)$；
2. 对 $y$ 求偏导令 $=Q$ 解出 $g_y$；
3. 用 $f_z=R$ 作一致性检查补齐。

判别：$\operatorname{curl}\mathbf F=\mathbf0$ 必要；充分性取决于定义域是否有洞（见 [[Topological Subtleties and Maxwell's Equations|拓扑注意事项与麦克斯韦方程组]]）。

## 5. Jacobian 视角 (Jacobian View)

把一阶偏导打包成 Jacobian $\nabla\mathbf F=[\,\partial F_i/\partial x_j\,]$：

- **div** 是对角线和：$\operatorname{div}\mathbf F=\mathrm{tr}(\nabla\mathbf F)$（见 [[Eigenvalues and Eigenvectors#特征值与迹 (Eigenvalues and the Trace)|迹]]）；
- **curl** 由非对角项的差组成（Jacobian 的反对称部分），对应局部旋转（对照 [[The Matrix Viewpoint|矩阵的视角]]）。

## 6. Checklist

1. 线积分能否用势函数化简？先试 $\operatorname{curl}\mathbf F=\mathbf0$；
2. 找 $f$ 用"积分 + 补函数 + 一致性检查"，别同时硬解三式；
3. 留意定义域：场在某轴/点未定义时 $\operatorname{curl}=0$ 也可能不保守。

---

> [!important] 一句话总结
> 三维保守场先看 $\nabla\times\mathbf F$，再看定义域；求势函数用积分加补函数。
