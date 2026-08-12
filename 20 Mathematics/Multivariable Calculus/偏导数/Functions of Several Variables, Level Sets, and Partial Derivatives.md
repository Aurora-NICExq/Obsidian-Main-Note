---
aliases: [等值面、偏导数, Functions of Several Variables, Level Sets and Partial Derivatives, Partial Derivatives]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Total Differential and the Chain Rule|微分、链式法则]], [[Gradient and Directional Derivative|梯度、方向导数]], [[Second Derivative Test|二阶导检验]], [[Maxima and Minima (Several Variables)|极大极小问题]], [[Dependent Variables and Constrained Partial Derivatives|非独立变量]]"
down: "[[Total Differential and the Chain Rule|微分、链式法则]]"
---
# Functions of Several Variables, Level Sets, and Partial Derivatives

> [!summary] 核心结论
> 多变量函数 (function of several variables) 可通过图像、等值集 (level set) 与偏导数 (partial derivative) 理解。偏导数是曲面沿坐标方向的瞬时坡度；当 $f$ 可微 (differentiable) 时，这些坡度合成**切平面 (tangent plane)** 给出一阶线性近似。

前置知识：[[Differentiation|求导]]。

---

## 1. 定义 (Definition)

定义域 $D\subseteq\mathbb R^n$ 上的多变量函数是映射 $f:D\to\mathbb R$，把输入向量 $\mathbf x=(x_1,\dots,x_n)$ 对应到实数 $y=f(\mathbf x)$。$n\ge2$ 时称"多变量"。若输出为向量 $\mathbb R^m$，则是**向量值函数 (vector-valued function)** $\mathbf F:D\to\mathbb R^m$。

## 2. 空间中的图像 (Graph)

![[tikz-functions-of-several-variables-level-sets-and-part-01.svg]]

相关：二次型曲面见 [[Quadratic Forms|线性代数二次型]]。

## 3. 等值面 (Level Sets)

对三元函数 $f(x,y,z)$，取常数 $c$，满足 $f(x,y,z)=c$ 的所有点构成**等值面 (level surface)**。维数随之：

- 二元 $f(x,y)=c$ → **等值线 (level curve)**（平面曲线）；
- 三元 $f(x,y,z)=c$ → **等值面**（空间曲面）；
- $n$ 元 $f(\mathbf x)=c$ → **等值超曲面**（$\mathbb R^n$ 中 $n-1$ 维对象）。

梯度与等值面的垂直关系见 [[Gradient and Directional Derivative|与梯度的联系]]。

## 4. 偏导数：极限定义 (Partial Derivatives)

对 $x_i$ 求偏导，就只让 $x_i$ 变化、其余固定。对二元函数 $f(x,y)$ 在 $(x_0,y_0)$：

$$\frac{\partial f}{\partial x}=\lim_{h\to0}\frac{f(x_0+h,y_0)-f(x_0,y_0)}{h},\qquad \frac{\partial f}{\partial y}=\lim_{h\to0}\frac{f(x_0,y_0+h)-f(x_0,y_0)}{h}.$$

> [!warning] 有偏导 ≠ 可微
> 函数在某点偏导数存在，**不保证**在该点可微（甚至不保证连续）。可微是更强的条件，它要求一阶线性近似的误差是高阶无穷小——这正是切平面成立的前提。

## 5. 计算规则与几何意义 (Computation & Geometry)

求 $\partial/\partial x$ 时把 $y$ 当常数，反之亦然，按一元法则求导。例：$f=x^2y+3y^2$ 得 $f_x=2xy$，$f_y=x^2+6y$。

几何上，$f_x(x_0,y_0)$ 是用平面 $y=y_0$ 切曲面所得曲线 $z=f(x,y_0)$ 在 $x_0$ 处的切线斜率；$f_y$ 同理。即**偏导数 = 曲面沿坐标方向的瞬时坡度**。

## 6. 切平面近似 (Tangent Plane Approximation)

^0abe80

当 $f$ 在 $(a,b)$ **可微**时，同时让 $x,y$ 各动一点点，有一阶线性近似：

$$f(a+\Delta x,b+\Delta y)\approx f(a,b)+f_x(a,b)\Delta x+f_y(a,b)\Delta y.$$

![[tikz-functions-of-several-variables-level-sets-and-part-02.svg]]

## 7. 切平面方程 (Tangent Plane Equation)

$x,y$ 两条偏导切线张成切平面：

$$z\approx f(a,b)+f_x(a,b)(x-a)+f_y(a,b)(y-b).$$

也可用等值面法向量 $\nabla f$（参数式得法向量）表示同一切平面（见 [[Gradient and Directional Derivative|梯度、方向导数]]）。

---

> [!important] 一句话总结
> 偏导数是坐标方向的瞬时坡度；可微时它们合成切平面，给出多元一阶线性近似。
