---
aliases: [梯度、方向导数, Gradient and Directional Derivative, Gradient]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Functions of Several Variables, Level Sets, and Partial Derivatives|等值面、偏导数]], [[Total Differential and the Chain Rule|微分、链式法则]], [[Lagrange Multipliers|拉格朗日乘数法]], [[Gradient Fields and Potential Functions|gradient field,potential function]]"
down: "[[Maxima and Minima (Several Variables)|极大极小问题]]"
---
# Gradient and Directional Derivative

> [!summary] 核心结论
> 梯度 (gradient) $\nabla w=\langle w_x,w_y,w_z\rangle$ 把所有一阶偏导打包成一个向量；它**垂直于等值面**、指向**增长最快的方向**，其长度即最陡斜率。方向导数 (directional derivative) 是梯度在单位方向上的投影 $\nabla w\cdot\hat{\mathbf u}$。

前置知识：[[Functions of Several Variables, Level Sets, and Partial Derivatives|等值面、偏导数]]、[[Total Differential and the Chain Rule|微分、链式法则]]。

---

## 1. 梯度的定义 (Definition)

由链式法则，若 $w=w(x,y,z)$ 且 $\mathbf r(t)=(x(t),y(t),z(t))$，则

$$\frac{dw}{dt}=w_x\frac{dx}{dt}+w_y\frac{dy}{dt}+w_z\frac{dz}{dt}=\nabla w\cdot\frac{d\mathbf r}{dt},\qquad \nabla w=\langle w_x,w_y,w_z\rangle.$$

梯度把"各方向偏导"打包成一个向量。

## 2. 几何意义：垂直等值面 (Perpendicular to Level Sets)

> [!important] 定理
> $\nabla w$ 在每点垂直于过该点的等值面 $w=c$。

**证明.** 取完全落在等值面上的曲线 $\mathbf r(t)$，则 $w(\mathbf r(t))\equiv c$，故 $\tfrac{dw}{dt}=0$。由向量链式法则 $\nabla w\cdot\mathbf v=0$（$\mathbf v=d\mathbf r/dt$ 为切向量）。$\mathbf v$ 是任意沿等值面的切向量，故 $\nabla w$ 垂直于切平面内一切切向量，即为法向量。$\blacksquare$

**三例**：$w=ax+by+cz$ 等值面是平面，法向量 $\langle a,b,c\rangle=\nabla w$；$w=x^2+y^2$ 等值线是圆，$\nabla w=\langle2x,2y\rangle$ 径向外指、垂直圆；$w=x^2-y^2$ 梯度随点变化（强调梯度是**向量场**）。

![[tikz-gradient-and-directional-derivative-01.svg]]

## 3. 应用：等值面的切平面 (Tangent Plane via Gradient)

隐式曲面 $w(x,y,z)=c$ 在 $P$ 处法向量为 $\nabla w(P)$。例：$x^2+y^2-z^2=4$ 在 $(2,1,1)$ 处 $\nabla w=\langle4,2,-2\rangle$，切平面

$$4(x-2)+2(y-1)-2(z-1)=0\iff 4x+2y-2z=8.$$

也可由微分/线性近似得到：$dw\approx4\Delta x+2\Delta y-2\Delta z$，等值面上 $\Delta w=0$ 给出同一切平面（见 [[Total Differential and the Chain Rule#^aa8e28|线性近似得到切平面]]）。

## 4. 方向导数 (Directional Derivative)

取单位向量 $\hat{\mathbf u}=\langle a,b\rangle$，沿它以单位速度走 $x(s)=x_0+as,\ y(s)=y_0+bs$（$s$ 为弧长）。方向导数

$$\left.\frac{dw}{ds}\right|_{\hat{\mathbf u}}=\nabla w\cdot\hat{\mathbf u},$$

几何上是用"含该方向的竖直平面"切图像所得切线斜率。

## 5. 三条结论：最陡方向 (Steepest Direction)

写成夹角形式 $\nabla w\cdot\hat{\mathbf u}=|\nabla w|\cos\theta$：

1. **最大上升方向**：$\theta=0$（$\hat{\mathbf u}\parallel\nabla w$）——梯度方向是增长最快方向；
2. **最大上升率**：等于 $|\nabla w|$——梯度长度是最陡斜率；
3. **不变方向**：$\theta=90^\circ$（$\hat{\mathbf u}\perp\nabla w$）——沿等值线切向走函数值不变。

看等高线图时，**梯度永远垂直等值线，并指向数值更大的一侧**。

---

> [!important] 一句话总结
> 梯度指向最大增长方向、垂直等值面；方向导数就是 $\nabla f\cdot\hat{\mathbf u}$——它是 [[Maxima and Minima (Several Variables)|极值]] 与 [[Lagrange Multipliers|约束优化]] 的几何引擎。
