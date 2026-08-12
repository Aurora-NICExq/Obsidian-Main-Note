---
aliases: [斯托克斯定理, Stokes' Theorem]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Line Integrals in Space, Curl, and Potential Functions|空间线积分、旋度与势函数]], [[Triple Integrals (Rectangular and Cylindrical Coordinates)|triple integral（直角坐标与柱坐标）]], [[Divergence Theorem (Gauss's Theorem)|散度定理（高斯定理）]], [[Vector Fields, Surface Integrals, and Flux in 3D|三维向量场、曲面积分与通量]], [[Green's Theorem (Circulation Form)|格林定理]]"
down: "[[Stokes' Theorem (Examples and Review)|斯托克斯定理（例题与总复习）]]"
---
# Stokes' Theorem

> [!summary] 核心结论
> 斯托克斯定理 (Stokes' theorem) 把**闭曲线上的环量（线积分）**与**任意张成曲面上的旋度通量**联系起来：$\displaystyle\oint_{\partial S}\mathbf F\cdot d\mathbf r=\iint_S(\nabla\times\mathbf F)\cdot\mathbf n\,dS$。这是三维版的旋度观点（格林定理的推广）。

前置知识：[[Line Integrals in Space, Curl, and Potential Functions|空间线积分、旋度与势函数]]。

---

## 1. 定理陈述 (Statement)

$S$ 为定向光滑曲面，边界 $C=\partial S$ 取与 $S$ **右手相容**的正向，则

$$\oint_{\partial S}\mathbf F\cdot d\mathbf r=\iint_S(\nabla\times\mathbf F)\cdot\mathbf n\,dS.$$

**右手法则**：右手四指沿 $C$ 正向弯曲，拇指指向 $\mathbf n$。$C$ 反向或 $\mathbf n$ 反向，两侧同时变号。

## 2. 直觉：curl 是环量密度 (Intuition)

$(\operatorname{curl}\mathbf F)\cdot\mathbf n$ 是单位面积的净环量；斯托克斯把这些微小环量在曲面上积分，得到边界总环量。

## 3. 用法：选最好算的曲面 (Pick the Best Surface)

要算 $\oint_C\mathbf F\cdot d\mathbf r$：先算 $\nabla\times\mathbf F$，再选一个**边界同为 $C$** 的曲面 $S$（可换曲面），使 $(\nabla\times\mathbf F)\cdot\mathbf n$ 或 $dS$ 好算。$C$ 是圆/椭圆时优先取其平面圆盘；$C$ 在某平面内则降为 [[Green's Theorem (Circulation Form)|格林定理]]。

## 4. 格林定理是特例 (Green as a Special Case)

$S$ 取 $xy$ 平面区域 $R$、$\mathbf n=\mathbf k$、$\mathbf F=\langle M,N,0\rangle$，则 $\nabla\times\mathbf F=\langle0,0,N_x-M_y\rangle$，斯托克斯化为

$$\oint_{\partial R}M\,dx+N\,dy=\iint_R(N_x-M_y)\,dA.$$

## 5. 例题 (Example)

$\mathbf F=\langle-y,x,0\rangle$，$C$ 半径 $a$ 圆（逆时针，向上法向）。$\nabla\times\mathbf F=\langle0,0,2\rangle$，取 $S$ 为圆盘 $\mathbf n=\mathbf k$：

$$\oint_C\mathbf F\cdot d\mathbf r=\iint_S 2\,dS=2\pi a^2.$$

## 6. Checklist

1. $C$ 必须闭合（$=\partial S$）；
2. $C$ 与 $\mathbf n$ 须右手相容（否则符号错）；
3. 先算 curl，再选最好算的 $S$。

---

> [!important] 一句话总结
> 斯托克斯定理可换成更好算的曲面，但边界方向必须与法向右手相容（综合演练见 [[Stokes' Theorem (Examples and Review)|斯托克斯定理（例题与总复习）]]）。
