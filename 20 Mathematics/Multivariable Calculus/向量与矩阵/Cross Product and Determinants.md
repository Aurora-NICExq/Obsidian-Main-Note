---
aliases: [行列式叉积, Cross Product and Determinants, Cross Product]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Dot Product|点积]], [[Matrices and Equations of Planes|矩阵和平面方程]], [[Parametric Equations of Curves and Lines|曲线和直线参数方程]], [[Applications of Determinants|行列式的应用]]"
down: "[[Matrices and Equations of Planes|矩阵和平面方程]]"
---
# Cross Product and Determinants

> [!summary] 核心结论
> 行列式 (determinant) 给出线性变换对面积/体积的**缩放因子**；叉积 (cross product) 给出一个**带方向的面积向量 (oriented area vector)**：$\mathbf a\times\mathbf b$ 垂直于二者所张平面，长度等于平行四边形面积，方向由右手定则决定。

前置知识：[[Dot Product|点积]]。

---

## 1. 平行四边形面积与行列式 (2D Determinant = Area)

以 $A=(a_1,a_2)$、$B=(b_1,b_2)$ 为邻边的平行四边形，面积为 $|\det[A\ B]|=|a_1b_2-a_2b_1|$。

> [!note] 为何是 $a_1b_2-a_2b_1$
> 通过剪切/旋转把 $A$ 转到 $x$ 轴上：面积 $=$ 底 $\|A\|$ × 高（$B$ 在垂直于 $A$ 方向的分量）。代数上 $|a_1b_2-a_2b_1|$ 恰等于 $\|A\|\times(\text{垂直分量})$，与几何面积一致。

## 2. 行列式求体积 (3D Determinant = Volume)

行列式衡量线性变换对"体积"的缩放因子，$3\times3$ 行列式的绝对值即平行六面体体积，参见 [[Applications of Determinants#^3bbccb|行列式求体积]]。

## 3. 叉积：带方向的面积向量 (Cross Product)

给两个三维向量 $\mathbf a,\mathbf b$，叉积 $\mathbf a\times\mathbf b$ 产生一个**新向量**，满足：

1. **垂直**于 $\mathbf a,\mathbf b$ 所张平面（同时垂直于两者）；
2. **长度**等于以 $\mathbf a,\mathbf b$ 为邻边的平行四边形面积（故三角形面积 $A_\triangle=\tfrac12\|\mathbf a\times\mathbf b\|$）；
3. **方向**由右手定则 (right-hand rule) 决定。

故叉积本质是"带方向的面积向量"。它**反交换 (anticommutative)**：$\mathbf a\times\mathbf b=-(\mathbf b\times\mathbf a)$，换序方向翻转。

![[tikz-cross-product-and-determinants-01.svg]]

## 4. 行列式计算公式 (Determinant Formula)

若 $\mathbf a=(a_1,a_2,a_3)$、$\mathbf b=(b_1,b_2,b_3)$，则

$$\mathbf a\times\mathbf b=\big(a_2b_3-a_3b_2,\ a_3b_1-a_1b_3,\ a_1b_2-a_2b_1\big)=\begin{vmatrix}\mathbf i&\mathbf j&\mathbf k\\ a_1&a_2&a_3\\ b_1&b_2&b_3\end{vmatrix},$$

其中 $\mathbf i,\mathbf j,\mathbf k$ 为标准基向量。

## 5. 共面与平面方程的两种判定 (Coplanarity Tests)

设平面 $\Pi$ 过不共线三点 $A,B,C$，边向量 $\vec{AB}=B-A$、$\vec{AC}=C-A$。

- **体积（行列式）判定**：把 $\vec{AB},\vec{AC},\vec{AP}$ 看作平行六面体三棱，$P$ 在平面内 $\iff$ 三向量共面 $\iff$ 体积为 $0$：

$$P\in\Pi\iff \det[\vec{AB}\ \vec{AC}\ \vec{AP}]=(\vec{AB}\times\vec{AC})\cdot\vec{AP}=0.$$

- **法向量（点积）判定**：取法向量 $\mathbf n=\vec{AB}\times\vec{AC}$，则平面内任意点 $P$ 满足 $\vec{AP}\perp\mathbf n$：

$$P\in\Pi\iff \mathbf n\cdot(P-A)=0.$$

这两种判定本质相同（混合积 = 行列式），是 [[Matrices and Equations of Planes|平面方程]] 的几何根据。

---

> [!important] 一句话总结
> 叉积把"垂直方向"与"面积大小"合成一个向量，行列式负责计算这种有向面积/体积。
