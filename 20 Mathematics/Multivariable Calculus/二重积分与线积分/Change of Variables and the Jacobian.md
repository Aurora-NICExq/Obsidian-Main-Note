---
aliases: [换元法和雅各比矩阵, Change of Variables and the Jacobian, Jacobian]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Double Integrals in Polar Coordinates and Applications|极坐标的二重积分应用]], [[Double Integrals|二重积分]], [[Triple Integrals (Rectangular and Cylindrical Coordinates)|triple integral（直角坐标与柱坐标）]], [[Spherical Coordinates and Surface Area|球坐标与表面积]]"
down: ""
---
# Change of Variables and the Jacobian

> [!summary] 核心结论
> 多重积分换元不只是把 $x,y$ 改写成 $u,v$：面积元 $dA$ 会被映射局部拉伸/压缩，比例由**雅可比行列式 (Jacobian)** 给出，必须随微元一起改变。极坐标的 $r$ 正是 Jacobian 的特例。

前置知识：[[Double Integrals|二重积分]]、[[Total Differential and the Chain Rule|微分、链式法则]]。

---

## 1. 核心问题 (The Problem)

对任意换元 $u=u(x,y),v=v(x,y)$，如何把 $\iint_R f\,dx\,dy$ 变成 $\iint_{R'}\cdots\,du\,dv$？换元的两个目的：**让区域边界更简单**（奇形 → 矩形/圆盘/常数界），或**让被积函数更简单**。

## 2. 引例：椭圆面积 (Ellipse)

椭圆 $\tfrac{x^2}{a^2}+\tfrac{y^2}{b^2}\le1$ 取 $u=\tfrac xa,v=\tfrac yb$ 变成单位圆盘，$dx\,dy=ab\,du\,dv$，故面积 $=ab\iint_{u^2+v^2\le1}1\,du\,dv=\pi ab$（区域简化 + 面积元只乘常数 $ab$）。

## 3. 雅可比行列式 (Jacobian)

一般换元时 $dx\,dy$ 与 $du\,dv$ 的比例**不是常数**，由局部线性近似的拉伸率决定：

$$J=\frac{\partial(u,v)}{\partial(x,y)}=\begin{vmatrix}u_x&u_y\\ v_x&v_y\end{vmatrix},\qquad du\,dv=\left|\frac{\partial(u,v)}{\partial(x,y)}\right|dx\,dy.$$

做积分常用反向：$dx\,dy=\left|\dfrac{\partial(x,y)}{\partial(u,v)}\right|du\,dv$。行列式可为负（方向翻转），但面积取**绝对值**恒正。两个 Jacobian 互为倒数：$\dfrac{\partial(u,v)}{\partial(x,y)}\cdot\dfrac{\partial(x,y)}{\partial(u,v)}=1$。

## 4. 换元公式："三步走" (The Formula)

$$\iint_R f(x,y)\,dx\,dy=\iint_{R'}f\big(x(u,v),y(u,v)\big)\left|\frac{\partial(x,y)}{\partial(u,v)}\right|du\,dv.$$

1. **改 integrand**：$f(x,y)\to f(x(u,v),y(u,v))$；
2. **乘面积元**：$\times\left|\dfrac{\partial(x,y)}{\partial(u,v)}\right|$；
3. **改区域/设界**：$R\to R'$（$uv$ 平面），写迭代积分。

## 5. 为何极坐标有 $r$ (Polar as a Special Case)

$x=r\cos\theta,y=r\sin\theta$ 算 $\dfrac{\partial(x,y)}{\partial(r,\theta)}=r$，故 $dx\,dy=r\,dr\,d\theta$——极坐标的 $r$ 就是 Jacobian（见 [[Double Integrals in Polar Coordinates and Applications|极坐标的二重积分应用]]）。

> [!note] 为何 Jacobian 是行列式
> 小矩形经线性变换变成平行四边形，其面积 = 两边向量构成的行列式（绝对值），见 [[Cross Product and Determinants|行列式叉积]]。非线性换元时 Jacobian 一般**依赖变量**：如 $u=x,v=xy$ 得 $J=\begin{vmatrix}1&0\\ y&x\end{vmatrix}=x$，即 $du\,dv=x\,dx\,dy$。

## 6. 设新积分界 (New Limits)

- **理想**：$R$ 的边界本就是 $u=$const 或 $v=$const，新界直接是常数；
- **一般**：边界不是等值线，须改写。两法：**消元法**（联立 $u,v$ 定义与边界 $xy$ 方程消去 $x,y$）或**反解代入法**（解出 $x(u,v),y(u,v)$ 代入边界方程）。

---

> [!important] 一句话总结
> 换元三件事：改函数、改区域、乘 Jacobian 绝对值；难点常在把边界翻译到新坐标。
