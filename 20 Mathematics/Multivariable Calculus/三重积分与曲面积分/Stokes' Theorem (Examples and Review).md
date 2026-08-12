---
aliases: [斯托克斯定理（例题与总复习）, Stokes' Theorem Examples and Review]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Stokes' Theorem|斯托克斯定理]], [[Divergence Theorem (Gauss's Theorem)|散度定理（高斯定理）]], [[Vector Fields, Surface Integrals, and Flux in 3D|三维向量场、曲面积分与通量]], [[Topological Subtleties and Maxwell's Equations|拓扑注意事项与麦克斯韦方程组]], [[Triple Integrals (Rectangular and Cylindrical Coordinates)|triple integral（直角坐标与柱坐标）]]"
down: "[[Topological Subtleties and Maxwell's Equations|拓扑注意事项与麦克斯韦方程组]]"
---
# Stokes' Theorem (Examples and Review)

> [!summary] 核心结论
> 斯托克斯的"换面"技巧来自**同一边界的 curl 通量相等**。多变量微积分四大积分定理（梯度定理、格林、散度、斯托克斯）可统一为"内部微分算子的积分 = 边界上的积分"。

前置知识：[[Stokes' Theorem|斯托克斯定理]]。

---

## 1. "换面等价"何时成立 (Surface Independence)

两张曲面 $S_1,S_2$ 同一边界 $C$，$\mathbf F$ 在其张成区域内光滑，则

$$\iint_{S_1}(\nabla\times\mathbf F)\cdot\mathbf n\,dS=\iint_{S_2}(\nabla\times\mathbf F)\cdot\mathbf n\,dS=\oint_C\mathbf F\cdot d\mathbf r.$$

曲面可不同、边界相同；curl 总通量只由边界环量决定。

## 2. 方向速记 (Orientation)

给定 $\mathbf n$，边界 $C$ 正向由右手法则定：在图上标法向箭头，从箭头方向看过去，边界逆时针为正。

## 3. 四大定理总表 (The Four Theorems)

统一范式"边界积分 = 内部积分"：

1. **梯度定理**：$\displaystyle\int_C\nabla f\cdot d\mathbf r=f(B)-f(A)$；
2. **格林定理**（2D Stokes，见 [[Green's Theorem (Circulation Form)|格林定理]]）：$\displaystyle\oint_{\partial R}M\,dx+N\,dy=\iint_R(N_x-M_y)\,dA$；
3. **散度定理**（3D Gauss，见 [[Divergence Theorem (Gauss's Theorem)|散度定理（高斯定理）]]）：$\displaystyle\iint_{\partial E}\mathbf F\cdot\mathbf n\,dS=\iiint_E\operatorname{div}\mathbf F\,dV$；
4. **斯托克斯定理**（3D curl，见 [[Stokes' Theorem|斯托克斯定理]]）：$\displaystyle\oint_{\partial S}\mathbf F\cdot d\mathbf r=\iint_S(\nabla\times\mathbf F)\cdot\mathbf n\,dS$。

统一视角：内部某微分算子（$\nabla,\nabla\times,\nabla\cdot$）的积分 = 边界上的积分。

## 4. 两个必会恒等式 (Two Identities)

$$\nabla\times(\nabla f)=\mathbf0\quad(\text{梯度场无旋}),\qquad \nabla\cdot(\nabla\times\mathbf F)=0\quad(\text{curl 通过闭曲面总为 }0).$$

背后仍是"混合偏导可交换"与"内部面抵消"的结构（几何上同 [[Applications of Determinants#^3bbccb|体积/取向]] 的局部线性化思路）。

## 5. Checklist

1. 见 $\oint_C\mathbf F\cdot d\mathbf r$ 且 $C$ 闭合：优先 Stokes/Green（先算 curl）；
2. 见 $\iint_{\partial E}\mathbf F\cdot\mathbf n\,dS$ 且闭曲面：优先散度定理（先算 div）；
3. 每题先画图写清取向——方向错就是整题 $-1$。

---

> [!important] 一句话总结
> 后半段主线是 grad、curl、div 与它们对应的边界积分定理；换面技巧源于同一边界 curl 通量相等。
