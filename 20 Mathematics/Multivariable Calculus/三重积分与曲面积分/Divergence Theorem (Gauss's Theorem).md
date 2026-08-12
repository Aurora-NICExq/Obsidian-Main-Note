---
aliases: [散度定理（高斯定理）, Divergence Theorem, Gauss's Theorem]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Divergence Theorem (Applications and Pitfalls)|散度定理（应用与陷阱）]], [[Stokes' Theorem (Examples and Review)|斯托克斯定理（例题与总复习）]], [[Line Integrals in Space, Curl, and Potential Functions|空间线积分、旋度与势函数]], [[Triple Integrals (Rectangular and Cylindrical Coordinates)|triple integral（直角坐标与柱坐标）]], [[Spherical Coordinates and Surface Area|球坐标与表面积]]"
down: "[[Divergence Theorem (Applications and Pitfalls)|散度定理（应用与陷阱）]]"
---
# Divergence Theorem (Gauss's Theorem)

> [!summary] 核心结论
> 散度定理 (Divergence / Gauss theorem) 把**闭曲面上的通量**转化为**区域内散度的体积分**：把"边界总流出"变成"内部源汇总量"。$\displaystyle\iint_{\partial E}\mathbf F\cdot\mathbf n\,dS=\iiint_E\operatorname{div}\mathbf F\,dV$。

前置知识：[[Vector Fields, Surface Integrals, and Flux in 3D|三维向量场、曲面积分与通量]]、[[Triple Integrals (Rectangular and Cylindrical Coordinates)|triple integral（直角坐标与柱坐标）]]。

---

## 1. 通量与散度 (Flux & Divergence)

通量 $\iint_S\mathbf F\cdot\mathbf n\,dS$；散度 $\operatorname{div}\mathbf F:=P_x+Q_y+R_z$，直觉是"单位体积净流出率"（源为正、汇为负）。

**线性代数视角**：线性场 $\mathbf F(\mathbf x)=A\mathbf x$ 时 $\operatorname{div}\mathbf F=\mathrm{tr}(A)$（Jacobian 的迹），参见 [[Eigenvalues and Eigenvectors#特征值与迹 (Eigenvalues and the Trace)|迹]]。

## 2. 散度定理 (The Theorem)

立体区域 $E$，边界闭曲面 $S=\partial E$ 取**外法向**，$\mathbf F$ 在含 $E$ 的开集上光滑：

$$\iint_{\partial E}\mathbf F\cdot\mathbf n\,dS=\iiint_E\operatorname{div}\mathbf F\,dV.$$

关键词：**闭曲面、外法向、光滑无奇点**。

## 3. 计算套路 (Recipe)

$S$ 复杂但 $\operatorname{div}\mathbf F$ 简单时，散度定理比直接算曲面积分更快。

## 4. 例题 (Example)

$\mathbf F=\langle x,y,z\rangle$ 通过半径 $a$ 球面的外通量：$\operatorname{div}\mathbf F=3$，故

$$\iint_S\mathbf F\cdot\mathbf n\,dS=\iiint_E 3\,dV=3\cdot\tfrac43\pi a^3=4\pi a^3.$$

## 5. 证明思路 (Proof Idea)

1. 先对长方体盒子证：$\iiint_E P_x\,dV$ 用一维基本定理化为两张 $x=$const 面上的 $P$ 差；$Q_y,R_z$ 同理，三方向相加得六面总通量；
2. 一般区域用小盒子逼近取极限：相邻小盒子公共面通量符号相反相互抵消，只剩外边界。

## 6. Checklist

1. 是否闭曲面（有无"盖子"）？法向是否向外？
2. 区域内是否有奇点/不连续（有则先别套，见 [[Divergence Theorem (Applications and Pitfalls)|散度定理（应用与陷阱）]]）；
3. 体积分选何坐标最省事（直角/柱/球，注意 Jacobian）。

---

> [!important] 一句话总结
> 散度定理只适用于闭曲面 + 内部光滑场；它把边界净流出改写成内部源汇总量。
