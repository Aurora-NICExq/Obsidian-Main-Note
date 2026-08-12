---
aliases: [球坐标与表面积, Spherical Coordinates and Surface Area, Spherical Coordinates]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Triple Integrals (Rectangular and Cylindrical Coordinates)|triple integral（直角坐标与柱坐标）]], [[Change of Variables and the Jacobian|换元法和雅各比矩阵]], [[Divergence Theorem (Gauss's Theorem)|散度定理（高斯定理）]], [[Vector Fields, Surface Integrals, and Flux in 3D|三维向量场、曲面积分与通量]]"
down: "[[Vector Fields, Surface Integrals, and Flux in 3D|三维向量场、曲面积分与通量]]"
---
# Spherical Coordinates and Surface Area

> [!summary] 核心结论
> 球坐标 (spherical coordinates) 适合球/锥对称区域，体积元 $dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta$。曲面面积用参数化叉积 $dS=\|\mathbf r_u\times\mathbf r_v\|\,du\,dv$ 计算。

前置知识：[[Triple Integrals (Rectangular and Cylindrical Coordinates)|triple integral（直角坐标与柱坐标）]]、[[Change of Variables and the Jacobian|换元法和雅各比矩阵]]。

---

## 1. 球坐标：变量与几何 (Variables)

- $\rho$：到原点距离；$\theta$：$xy$ 平面方位角（$0\le\theta<2\pi$）；$\phi$：与正 $z$ 轴夹角（$0\le\phi\le\pi$）。

$$x=\rho\sin\phi\cos\theta,\quad y=\rho\sin\phi\sin\theta,\quad z=\rho\cos\phi.$$

## 2. 体积元 $\rho^2\sin\phi$ (Volume Element)

$$dV=\rho^2\sin\phi\,d\rho\,d\phi\,d\theta.$$

这是 [[Change of Variables and the Jacobian|Jacobian]] 在三维的同一件事（局部体积缩放，亦联系 [[Applications of Determinants#^3bbccb|行列式求体积]]）：

$$\iiint_E f\,dV=\iiint_{E'}f(\rho\sin\phi\cos\theta,\rho\sin\phi\sin\theta,\rho\cos\phi)\,\rho^2\sin\phi\,d\rho\,d\phi\,d\theta.$$

## 3. 何时用球坐标 (When)

出现 $x^2+y^2+z^2$、球面、球壳/球冠，或圆锥（$\phi=$const）与"到原点距离"组合。边界翻译：$x^2+y^2+z^2=\rho^2$，$z=\rho\cos\phi$，$\sqrt{x^2+y^2}=\rho\sin\phi$。

## 4. 表面积元素：参数化叉积 (Surface Area)

对参数曲面 $\mathbf r(u,v)$：

$$dS=\|\mathbf r_u\times\mathbf r_v\|\,du\,dv,\qquad \iint_S g\,dS=\iint_D g(\mathbf r(u,v))\,\|\mathbf r_u\times\mathbf r_v\|\,du\,dv.$$

$\mathbf r_u\times\mathbf r_v$ 是法向的"有向面积向量"（对照 [[Cross Product and Determinants|行列式叉积]]）。

## 5. 主例：球面面积 (Sphere Area)

半径 $a$ 的球面 $\mathbf r(\phi,\theta)=\langle a\sin\phi\cos\theta,a\sin\phi\sin\theta,a\cos\phi\rangle$，可算 $\|\mathbf r_\phi\times\mathbf r_\theta\|=a^2\sin\phi$：

![[tikz-spherical-coordinates-and-surface-area-01.svg]]

$$\mathrm{Area}(S)=\int_0^{2\pi}\int_0^{\pi}a^2\sin\phi\,d\phi\,d\theta=4\pi a^2.$$

## 6. Checklist

1. 球/锥对称先想球坐标，边界翻译成 $\rho,\phi,\theta$；
2. 三重积分别漏 Jacobian $\rho^2\sin\phi$；
3. 表面积题先参数化，再套 $dS=\|\mathbf r_u\times\mathbf r_v\|\,du\,dv$。

---

> [!important] 一句话总结
> 球坐标体积元与表面积公式同源：都来自参数化后的局部伸缩因子。
