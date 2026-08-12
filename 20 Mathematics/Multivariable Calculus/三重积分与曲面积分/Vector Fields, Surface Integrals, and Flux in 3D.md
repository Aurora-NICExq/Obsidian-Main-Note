---
aliases: [三维向量场、曲面积分与通量, Vector Fields Surface Integrals and Flux in 3D, Surface Integrals]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Spherical Coordinates and Surface Area|球坐标与表面积]], [[Stokes' Theorem (Examples and Review)|斯托克斯定理（例题与总复习）]], [[Divergence Theorem (Applications and Pitfalls)|散度定理（应用与陷阱）]], [[Line Integrals in Space, Curl, and Potential Functions|空间线积分、旋度与势函数]], [[Topological Subtleties and Maxwell's Equations|拓扑注意事项与麦克斯韦方程组]]"
down: "[[Divergence Theorem (Gauss's Theorem)|散度定理（高斯定理）]]"
---
# Vector Fields, Surface Integrals, and Flux in 3D

> [!summary] 核心结论
> 曲面积分 (surface integral) 的核心是面积元素 $dS=\|\mathbf r_u\times\mathbf r_v\|\,du\,dv$；通量 (flux) 用**带方向的面积向量** $\mathbf n\,dS=\pm(\mathbf r_u\times\mathbf r_v)\,du\,dv$。这是二维线积分/通量思想在三维曲面上的推广。

前置知识：[[Spherical Coordinates and Surface Area|球坐标与表面积]]、[[Cross Product and Determinants|行列式叉积]]。

---

## 1. 三维向量场与曲面 (Fields & Surfaces)

$\mathbf F(x,y,z)=\langle P,Q,R\rangle$。曲面 $S$ 两种表示：**参数化** $\mathbf r(u,v)$，或**图像型** $z=g(x,y)$。

## 2. 标量曲面积分 (Scalar Surface Integral)

$$dS=\|\mathbf r_u\times\mathbf r_v\|\,du\,dv,\qquad \iint_S g\,dS=\iint_D g(\mathbf r(u,v))\,\|\mathbf r_u\times\mathbf r_v\|\,du\,dv.$$

叉积给出"带方向的面积向量"（见 [[Cross Product and Determinants|行列式叉积]]），其模长是面积缩放因子（同 [[Applications of Determinants#^3bbccb|行列式求体积]] 的几何思想）。图像型 $z=g(x,y)$ 取 $\mathbf r=\langle x,y,g\rangle$ 得常用公式 $dS=\sqrt{1+g_x^2+g_y^2}\,dx\,dy$。

## 3. 通量 (Flux)

通量衡量"场穿过曲面"的总量，取单位法向 $\mathbf n$（需选定方向）：$\displaystyle\iint_S\mathbf F\cdot\mathbf n\,dS$。

![[tikz-vector-fields-surface-integrals-and-flux-in-3d-01.svg]]

## 4. 参数化计算模板 (Parametric Template)

取与选定方向一致的"面积向量" $\mathbf n\,dS=\pm(\mathbf r_u\times\mathbf r_v)\,du\,dv$，则

$$\iint_S\mathbf F\cdot\mathbf n\,dS=\iint_D\mathbf F(\mathbf r(u,v))\cdot(\pm\,\mathbf r_u\times\mathbf r_v)\,du\,dv.$$

**方向选反，结果整体变号。**

**示例：圆柱侧面** $S:x^2+y^2=a^2,\ 0\le z\le h$，外向，$\mathbf F=\langle x,y,0\rangle$。

![[tikz-vector-fields-surface-integrals-and-flux-in-3d-02.svg]]

计算：$\mathbf r(\theta,z)=\langle a\cos\theta,a\sin\theta,z\rangle$，$\mathbf r_\theta\times\mathbf r_z=\langle a\cos\theta,a\sin\theta,0\rangle=a\mathbf e_r$，$\mathbf F\cdot(\mathbf r_\theta\times\mathbf r_z)=a^2$，故

$$\iint_S\mathbf F\cdot\mathbf n\,dS=\int_0^h\int_0^{2\pi}a^2\,d\theta\,dz=2\pi a^2 h.$$

## 5. 图像型曲面快速公式 (Graph Surface)

$S:z=g(x,y)$，向上取向（$\mathbf n$ 的 $k$ 分量正）：

$$\mathbf n\,dS=\langle -g_x,-g_y,1\rangle\,dx\,dy,\qquad \iint_S\mathbf F\cdot\mathbf n\,dS=\iint_D\mathbf F(x,y,g)\cdot\langle -g_x,-g_y,1\rangle\,dx\,dy.$$

向下取向取负号。

## 6. 与二维的对应 (2D Correspondence)

二维通量 $\int_C\mathbf F\cdot\mathbf n\,ds$ → 三维 $\iint_S\mathbf F\cdot\mathbf n\,dS$；二维法向微元 $\langle dy,-dx\rangle$ → 三维"向量面积元" $\mathbf r_u\times\mathbf r_v$。

## 7. Checklist

1. 先定取向（向上/向外/向下）——否则符号错一整题；
2. 优先参数化，算 $\mathbf r_u\times\mathbf r_v$；
3. 图像型用 $\langle -g_x,-g_y,1\rangle$（向上）模板。

---

> [!important] 一句话总结
> 曲面通量的稳定模板：参数化曲面 → 算 $\mathbf r_u\times\mathbf r_v$ → 与场点乘；取向决定符号。
