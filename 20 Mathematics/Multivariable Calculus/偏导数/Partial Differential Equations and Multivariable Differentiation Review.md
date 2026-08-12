---
aliases: [偏微分方程, Partial Differential Equations, Multivariable Differentiation Review]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Dependent Variables and Constrained Partial Derivatives|非独立变量]], [[Second Derivative Test|二阶导检验]], [[Gradient and Directional Derivative|梯度、方向导数]], [[Maxima and Minima (Several Variables)|极大极小问题]], [[Total Differential and the Chain Rule|微分、链式法则]]"
down: ""
---
# Partial Differential Equations and Multivariable Differentiation Review

> [!summary] 核心结论
> 偏微分方程 (partial differential equation, PDE) 展示偏导数在物理模型中的实际作用。本节不教解 PDE，而是把整套**多元微分工具箱**串成可用的解题流程：图像/等高线、偏导与梯度、线性近似/切平面、方向导数、极值、链式法则、换元、约束偏导。

前置知识：[[Total Differential and the Chain Rule|微分、链式法则]]。

---

## 1. PDE 的"文化介绍" (Why Partial Derivatives Matter)

PDE 是含未知函数偏导数的方程，描述系统随多个变量变化时的规律约束。经典例子是**热方程 (heat equation)**：

$$\frac{\partial f}{\partial t}=k\left(\frac{\partial^2 f}{\partial x^2}+\frac{\partial^2 f}{\partial y^2}+\frac{\partial^2 f}{\partial z^2}\right),$$

其中 $f(x,y,z,t)$ 是位置 $(x,y,z)$ 在时间 $t$ 的温度，$k$ 为导热系数。重点：偏导在物理中频繁、真实地出现。

## 2. 几何直觉：图像与等高线 (Graphs & Contours)

等高线越密，函数变化越快；线条形状反映山脊/盆地/鞍点。用等高线估偏导时，重在**定性判断正负/是否为零**，而非精确读数。

## 3. 偏导与梯度 (Partials & Gradient)

$\nabla f=(f_x,f_y,f_z)$ 指向增大最快方向，并垂直于等值面 $f=$const（给出法向量）。详见 [[Gradient and Directional Derivative|梯度、方向导数]]。

## 4. 线性近似与切平面 (Linearization)

小位移下 $df\approx f_x\,dx+f_y\,dy+f_z\,dz=\nabla f\cdot d\mathbf r$，即切平面近似（见 [[Total Differential and the Chain Rule|微分、链式法则]]、[[Functions of Several Variables, Level Sets, and Partial Derivatives|等值面、偏导数]]）。

## 5. 方向导数 (Directional Derivative)

沿单位向量 $\mathbf u$：$D_{\mathbf u}f=\nabla f\cdot\mathbf u$——一步点积到位。

## 6. 极值复习 (Extrema)

内部临界点 $\nabla f=0$，用 [[Second Derivative Test|二阶导检验]] 区分极大/极小/鞍点；全局最值还须查**边界**与无穷远（见 [[Maxima and Minima (Several Variables)|极大极小问题]]）。

## 7. 链式法则 (Chain Rule)

若 $x,y,z$ 依赖 $u,v$，则 $f$ 间接依赖 $u,v$：$u$ 影响 $x/y/z$ 再影响 $f$，影响量相加。这为换元（极坐标/直角坐标互换）铺路。

## 8. 非独立变量：约束偏导 (Constrained Partials)

设 $f(x,y,z)$ 但约束 $g(x,y,z)=c$。符号 $\big(\tfrac{\partial f}{\partial z}\big)_y$ 意为"动 $z$、固定 $y$，而 $x$ 随约束走"。

**方法一（微分消元）**：写 $df=f_x dx+f_y dy+f_z dz$，令 $dy=0$；再用 $dg=g_x dx+g_y dy+g_z dz=0$ 令 $dy=0$ 解出 $dx=-\tfrac{g_z}{g_x}dz$，代回得

$$\left(\frac{\partial f}{\partial z}\right)_y=-f_x\frac{g_z}{g_x}+f_z.$$

**方法二（链式法则）**：$\big(\tfrac{\partial f}{\partial z}\big)_y=f_x\big(\tfrac{\partial x}{\partial z}\big)_y+f_z$，对 $g$ 同样展开（$g\equiv$const 故为 $0$）得 $\big(\tfrac{\partial x}{\partial z}\big)_y=-\tfrac{g_z}{g_x}$，代回同一公式。两法本质相同（详见 [[Dependent Variables and Constrained Partial Derivatives|非独立变量]]）。

---

> [!important] 一句话总结
> 偏导在 PDE 等物理模型中无处不在；本节重在把多元微分工具串成"读图→梯度→近似→极值→链式→约束"的解题流程。
