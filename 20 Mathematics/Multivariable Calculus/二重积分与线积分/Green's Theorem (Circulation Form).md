---
aliases: [格林定理, Green's Theorem, Green's Theorem (Circulation Form)]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Vector Fields and Line Integrals in the Plane|平面向量场和线积分]], [[Double Integrals|二重积分]], [[Flux, Divergence, and Green's Theorem (Normal Form)|通量与散度（格林定理法向形式）]], [[Path Independence and Conservative Fields|path independent，conservative]]"
down: "[[Flux, Divergence, and Green's Theorem (Normal Form)|通量与散度（格林定理法向形式）]]"
---
# Green's Theorem (Circulation Form)

> [!summary] 核心结论
> 格林定理 (Green's theorem) 把**沿边界的线积分**与**区域内的二重积分**联系起来：边界总环量 (circulation) 等于区域内旋度 (curl) 的总和。这是二维版的斯托克斯观点。

前置知识：[[Vector Fields and Line Integrals in the Plane|平面向量场和线积分]]、[[Double Integrals|二重积分]]。

---

## 1. 环量形式 (Circulation Form)

设 $\mathbf F=\langle M(x,y),N(x,y)\rangle$，$C$ 是**简单闭合**、取**正向（逆时针）**的边界，$R$ 为所围区域，$M,N$ 在含 $R$ 的开集上 $C^1$，则

$$\oint_C M\,dx+N\,dy=\iint_R\left(\frac{\partial N}{\partial x}-\frac{\partial M}{\partial y}\right)dA.$$

记 $\operatorname{curl}\mathbf F:=N_x-M_y$，则

$$\oint_C\mathbf F\cdot d\mathbf r=\iint_R\operatorname{curl}\mathbf F\,dA.$$

若 $C$ 改为顺时针，则左侧取负。

## 2. 关键推论：curl = 0 ⟹ 保守 (Conservative)

若 $\operatorname{curl}\mathbf F=0$ 且 $\mathbf F$ 在**无洞 (simply connected)** 区域内光滑，则对任意闭曲线 $\oint_C\mathbf F\cdot d\mathbf r=0$，从而 $\mathbf F$ 是梯度场（存在势函数）。这与保守场判据一致：$\operatorname{curl}\mathbf F=0\iff M_y=N_x$（见 [[Path Independence and Conservative Fields|path independent，conservative]]）。

## 3. 用格林定理换算计算 (Worked Example)

直接参数化很麻烦的线积分：

$$\oint_C ye^{-x}\,dx+\left(\tfrac12x^2-e^{-x}\right)dy,\quad C:\text{以 }(2,0)\text{ 为心、半径 1 的圆（逆时针）}.$$

取 $M=ye^{-x},\ N=\tfrac12x^2-e^{-x}$，则 $N_x-M_y=(x+e^{-x})-e^{-x}=x$，故

$$\oint_C M\,dx+N\,dy=\iint_R x\,dA=(\text{质心横坐标 }2)\times(\text{面积 }\pi)=2\pi.$$

## 4. 面积公式 (Area via Boundary)

选 $M,N$ 使 $N_x-M_y\equiv1$，把面积写成边界线积分：

$$\text{Area}(R)=\oint_C x\,dy=-\oint_C y\,dx=\frac12\oint_C(x\,dy-y\,dx).$$

其中 $x\,dy-y\,dx$ 是有向面积元的边界表达，可对照 [[Applications of Determinants#^3bbccb|行列式的几何意义]]（面积/体积缩放与取向）。

## 5. 使用前的 Checklist

1. 必须是**闭合曲线**（$\oint$），取向明确（正向 = 逆时针）；
2. $M,N$ 在区域及邻域内足够光滑；若区域内有奇点（"有洞"情形）需额外处理；
3. 先算 $\operatorname{curl}\mathbf F=N_x-M_y$，再做二重积分（常配合对称性/几何量）。

---

> [!important] 一句话总结
> 格林定理：边界环量 = 内部旋度总和；使用前必查闭合、取向与光滑性。
