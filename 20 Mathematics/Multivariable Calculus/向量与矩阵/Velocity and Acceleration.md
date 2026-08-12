---
aliases: [速度、加速度, Velocity and Acceleration, 运动几何]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Parametric Equations of Curves and Lines|曲线和直线参数方程]], [[Dot Product|点积]], [[Cross Product and Determinants|行列式叉积]]"
down: ""
---
# Velocity and Acceleration

> [!summary] 核心结论
> 参数曲线 (parametric curve) 的导数链 $\mathbf r(t)\to\mathbf v(t)\to\mathbf a(t)$ 给出位置、速度、加速度；切向量 $\mathbf T$、主法向量 $\mathbf N$、面积速度等几何/物理量都由这些导数读出。开普勒第二定律即"面积速度恒定"。

前置知识：[[Parametric Equations of Curves and Lines|曲线和直线参数方程]]。

---

## 1. 位置、速度、加速度 (Position → Velocity → Acceleration)

$$\mathbf r(t)=\langle x,y,z\rangle,\quad \mathbf v(t)=\mathbf r'(t),\quad \mathbf a(t)=\mathbf v'(t)=\mathbf r''(t).$$

- 速率 (speed) $=\|\mathbf v(t)\|=\sqrt{(x')^2+(y')^2+(z')^2}$；
- 某分量恒为 $0$ 时，运动被限制在相应坐标平面/轴上。

## 2. 摆线范例 (Cycloid Example)

对 $\mathbf r(t)=\big(a(t-\sin t),\,a(1-\cos t)\big)$ 求导：

$$\mathbf v(t)=\big(a(1-\cos t),\,a\sin t\big),\qquad \|\mathbf v(t)\|=a\sqrt{2-2\cos t}=2a\big|\sin\tfrac t2\big|.$$

再求导得加速度 $\mathbf a(t)=\big(a\sin t,\,a\cos t\big)$。

## 3. 单位切向量与主法向量 (Unit Tangent & Normal)

$$\mathbf T(t)=\frac{\mathbf r'(t)}{\|\mathbf r'(t)\|},\qquad \mathbf N(t)=\frac{\mathbf T'(t)}{\|\mathbf T'(t)\|}.$$

$\mathbf T$ 指向前进方向，$\mathbf N$ 指向轨道弯曲的内侧。

> [!warning] 奇点
> 若某点 $\|\mathbf r'(t)\|=0$（如摆线尖点），$\mathbf T$ 在该点**不可定义**。

## 4. 面积速度与开普勒第二定律 (Areal Velocity & Kepler's 2nd Law)

太阳在原点，行星轨道 $\mathbf r(t)$。短时间 $dt$ 内位矢扫出的小三角形面积 $dA=\tfrac12\|\mathbf r\times d\mathbf r\|=\tfrac12\|\mathbf r\times\mathbf v\|\,dt$，故

$$\frac{dA}{dt}=\frac12\|\mathbf r\times\mathbf v\|.$$

> [!note] 为何面积速度恒定（角动量守恒）
> 引力是中心力 $\mathbf F=f(r)\mathbf e_r$，与 $\mathbf r$ 共线，故力矩 $\boldsymbol\tau=\mathbf r\times\mathbf F=\mathbf0$。角动量 $\mathbf L=\mathbf r\times(m\mathbf v)$ 满足 $\tfrac{d\mathbf L}{dt}=\boldsymbol\tau=\mathbf0$，恒定。于是 $\|\mathbf r\times\mathbf v\|$ 恒定，得 $\dfrac{dA}{dt}=\dfrac{\|\mathbf L\|}{2m}=$ 常数。**零力矩 ⟹ 角动量守恒 ⟹ 面积速度恒定**。$\blacksquare$

---

> [!important] 一句话总结
> 运动几何的核心链条是 $\mathbf r\to\mathbf v\to\mathbf a$；叉积 $\mathbf r\times\mathbf v$ 的守恒正是开普勒第二定律。
