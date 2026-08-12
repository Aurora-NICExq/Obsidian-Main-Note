---
aliases: ["gradient field,potential function", Gradient Fields and Potential Functions]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Vector Fields and Line Integrals in the Plane|平面向量场和线积分]], [[Path Independence and Conservative Fields|path independent，conservative]], [[Green's Theorem (Circulation Form)|格林定理]], [[Line Integrals in Space, Curl, and Potential Functions|空间线积分、旋度与势函数]], [[Stokes' Theorem|斯托克斯定理]]"
down: ""
---
# Gradient Fields and Potential Functions

> [!summary] 核心结论
> 判别向量场是否为梯度场 (gradient field)：先看旋度 $\operatorname{curl}\mathbf F=N_x-M_y$，再看定义域。若 $\mathbf F=\nabla f$，则线积分降维为端点差 $f(P_1)-f(P_0)$，闭合积分为零。

前置知识：[[Vector Fields and Line Integrals in the Plane|平面向量场和线积分]]、[[Gradient and Directional Derivative|梯度、方向导数]]。

---

## 1. 梯度场、势函数与线积分基本定理 (Gradient Theorem)

若存在标量 $f$ 使 $\mathbf F=\nabla f=\langle f_x,f_y\rangle$，则 $\mathbf F$ 是**梯度场/保守场**，$f$ 是**势函数 (potential)**。**线积分基本定理**：曲线 $C$ 从 $P_0$ 到 $P_1$ 时

$$\int_C\mathbf F\cdot d\mathbf r=f(P_1)-f(P_0),\qquad\text{故}\quad\oint_C\mathbf F\cdot d\mathbf r=0.$$

## 2. 判别准则：$M_y=N_x$ ⟺ curl = 0 (Test)

若 $\mathbf F=\nabla f$，则混合偏导可交换 $f_{xy}=f_{yx}$，故 $M_y=N_x$。定义二维旋度

$$\operatorname{curl}\mathbf F:=N_x-M_y,\qquad\text{于是}\quad M_y=N_x\iff\operatorname{curl}\mathbf F=0.$$

- $\operatorname{curl}\mathbf F\neq0$ ⟹ 一定不是梯度场；
- $\operatorname{curl}\mathbf F=0$ ⟹ 还需看定义域：在**无洞 (simply connected)** 区域上才足以推出 $\mathbf F$ 是梯度场。

## 3. 旋度的直觉 (Intuition)

curl 衡量局部旋转成分（vorticity）。纯平移 $\langle a,b\rangle$ 与径向扩张 $\langle x,y\rangle$ 均 $\operatorname{curl}=0$；旋转场 $\langle-y,x\rangle$ 有 $\operatorname{curl}=2$（一般 $\langle-\omega y,\omega x\rangle$ 给 $2\omega$）。故 $\operatorname{curl}=0$ 不是"没运动"，而是"没局部旋转"。

**有洞反例**：$\mathbf F=\left\langle-\dfrac{y}{x^2+y^2},\dfrac{x}{x^2+y^2}\right\rangle$ 在 $\mathbb R^2\setminus\{0\}$ 上满足 $M_y=N_x$，但绕单位圆积分 $=2\pi\neq0$，无全局势函数。

## 4. 构造势函数：两种方法 (Constructing $f$)

- **方法 A（线积分定义）**：选基点 $P_0$，定义 $f(P)=f(P_0)+\int_{P_0}^P\mathbf F\cdot d\mathbf r$；保守时与路径无关，常取"先水平后竖直"折线。
- **方法 B（积分 + 补函数，最常用）**：由 $f_x=M$ 得 $f=\int M\,dx+g(y)$，再令 $f_y=N$ 解出 $g'(y)$ 并积分。

## 5. 例题（判别 + 求势函数） (Worked Example)

$\mathbf F=\langle 4x^2+a\,xy,\ 3y^2+4x^2\rangle$。判别：$M_y=ax,\ N_x=8x\Rightarrow a=8$。取 $a=8$ 用方法 B：

$$f=\int(4x^2+8xy)\,dx=\tfrac43x^3+4x^2y+g(y),$$

$$f_y=4x^2+g'(y)=3y^2+4x^2\Rightarrow g(y)=y^3+C,\qquad f=\tfrac43x^3+4x^2y+y^3+C.$$

## 6. 做题 Checklist

1. 算 $\operatorname{curl}\mathbf F=N_x-M_y$；
2. $\neq0$：非梯度场，止；
3. $=0$：检查定义域是否有洞、是否处处光滑；
4. 可判为梯度场：用方法 B 求 $f$，再用端点差秒算线积分（见 [[Path Independence and Conservative Fields|path independent，conservative]]）。

---

> [!important] 一句话总结
> 二维场 $N_x-M_y=0$ 只是局部条件；无洞定义域上它才通常推出全局势函数。
