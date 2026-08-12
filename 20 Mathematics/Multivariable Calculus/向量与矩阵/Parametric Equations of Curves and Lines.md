---
aliases: [曲线和直线参数方程, Parametric Equations of Curves and Lines]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Velocity and Acceleration|速度、加速度]], [[Dot Product|点积]], [[Matrices and Equations of Planes|矩阵和平面方程]], [[Differentiation|求导]]"
down: "[[Velocity and Acceleration|速度、加速度]]"
---
# Parametric Equations of Curves and Lines

> [!summary] 核心结论
> 用参数 $t$ 描述曲线/直线：$\mathbf r(t)$ 由参数生成位置，导数 $\mathbf r'(t)$ 给出切向量与速率。消参 (eliminating the parameter) 只是一种可选表达，并非总可行或必要。

前置知识：[[Differentiation|求导]]。

---

## 1. 摆线 (Cycloid)

半径为 $a$ 的圆在直线上**无滑动滚动**时，圆周上一固定点描出的轨迹叫摆线。

![[tikz-parametric-equations-of-curves-and-lines-01.svg]]

以转角 $t$ 为参数，标准参数方程为

$$\begin{cases}x(t)=a(t-\sin t),\\ y(t)=a(1-\cos t),\end{cases}\quad t\in\mathbb R,\qquad \mathbf r(t)=\big(a(t-\sin t),\,a(1-\cos t)\big).$$

## 2. 参数曲线的基本表示 (Parametric Curves)

- 平面曲线 $x=x(t),y=y(t)$；空间曲线再加 $z=z(t)$；向量形式 $\mathbf r(t)=\langle x,y,z\rangle$；
- 消参：若能从 $x(t),y(t)$ 消去 $t$ 得 $F(x,y)=0$，但消参不总可行或必要。

## 3. 切向量与斜率 (Tangent & Slope)

切向量 $\mathbf r'(t)=\langle x',y',z'\rangle$ 给出切线方向，速率 $\|\mathbf r'(t)\|$（详见 [[Velocity and Acceleration|速度、加速度]]）。平面曲线斜率：

$$\frac{dy}{dx}=\frac{dy/dt}{dx/dt}\quad(dx/dt\neq0);$$

当 $dx/dt=0$ 而 $dy/dt\neq0$ 时切线竖直。

## 4. 参数化的几何意义 (Reparametrization)

改变参数不改变轨迹，但改变"走法"（方向、速度）。若 $t=\phi(s),\phi'(s)\neq0$，则 $\mathbf r(\phi(s))$ 与 $\mathbf r(t)$ 同一轨迹；$\phi'(s)<0$ 时方向反向。

## 5. 直线的参数方程 (Lines)

- 向量形式：给定点 $\mathbf r_0$ 与方向 $\mathbf v$，$\mathbf r(t)=\mathbf r_0+t\mathbf v$；
- 分量形式：$x=x_0+at,\ y=y_0+bt,\ z=z_0+ct$；
- 过两点：$\mathbf r(t)=\mathbf r_1+t(\mathbf r_2-\mathbf r_1)$；
- 二维斜率：$a\neq0$ 时 $m=b/a$，$a=0$ 为竖直线。

## 6. 直线与平面的位置关系 (Line–Plane Relation)

把直线代入平面 $\Pi:Ax+By+Cz+D=0$（法向量 $\mathbf n=(A,B,C)$）：

$$(Aa+Bb+Cc)\,t+(Ax_0+By_0+Cz_0+D)=0\ \Longrightarrow\ kt+m=0,$$

其中 $k=\mathbf n\cdot\mathbf v$。位置关系完全由 $k,m$ 决定（$k\neq0$ 交于一点；$k=0,m\neq0$ 平行；$k=m=0$ 直线在平面内）。

## 7. 常见参数化 (Common Examples)

圆 $\langle a\cos t,a\sin t\rangle$；椭圆 $\langle a\cos t,b\sin t\rangle$；抛物线 $y=x^2$ 取 $x=t,y=t^2$；线段取 $t\in[0,1]$。

---

> [!important] 一句话总结
> 参数方程的核心是 $\mathbf r(t)$：位置由参数生成，方向由 $\mathbf r'(t)$ 给出，消参可有可无。
