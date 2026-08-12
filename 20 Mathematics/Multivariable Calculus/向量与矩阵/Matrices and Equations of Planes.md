---
aliases: [矩阵和平面方程, Matrices and Equations of Planes]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Dot Product|点积]], [[Cross Product and Determinants|行列式叉积]], [[Matrices and Inverse Matrices|矩阵与逆矩阵]], [[Vector Spaces and Subspaces|向量空间及其子空间]]"
down: ""
---
# Matrices and Equations of Planes

> [!summary] 核心结论
> 平面方程的系数就是**法向量 (normal vector)**：$ax+by+cz=d$ 中 $\mathbf N=\langle a,b,c\rangle$。一个线性方程组可看成多张平面的交集，解的存在唯一性由系数行列式（法向量是否共面）决定。

前置知识：[[Dot Product|点积]]、[[Cross Product and Determinants|行列式叉积]]。

---

## 1. 平面方程与法向量 (Plane Equation)

一般式 $ax+by+cz=d$ 表达"点 $(x,y,z)$ 在平面上"。系数给出法向量 $\mathbf N=\langle a,b,c\rangle$。

**点积式**：若平面过 $P_0$、法向量 $\mathbf N$，则 $P\in\Pi\iff\mathbf N\cdot(P-P_0)=0$。同一平面有无穷多方程（整体乘常数法向量可缩放）。

## 2. 向量与平面的关系 (Vector vs Plane)

- $\mathbf v\perp\Pi\iff\mathbf v$ 与 $\mathbf N$ 成比例（同向）；
- $\mathbf v\parallel\Pi\iff\mathbf v\cdot\mathbf N=0$。

## 3. 线性系统 = 平面交集 (Linear System as Intersection)

$3\times3$ 系统对应三张平面，"解方程组"即找同时在三张平面上的点。典型情形：前两平面交成一条直线，第三平面与之交于一点，解唯一。

## 4. 齐次系统 $AX=0$ (Homogeneous System)

右端为 $0$，三张平面都过原点，故原点恒为解（平凡解, trivial）。

- $\det A\neq0$：$A$ 可逆，$X=A^{-1}0=0$，**只有零解**；
- $\det A=0$：三法向量 $N_1,N_2,N_3$ 张成体积为 $0$，即**共面 (coplanar)**。此时存在一条过原点、垂直于所有法向量的方向，落在每个平面内，给出**无穷多解（沿一条线）**。

求解方向：若 $N_1,N_2$ 不共线，取 $\mathbf v=N_1\times N_2$，它垂直于 $N_1,N_2$；当 $N_3$ 与它们共面时也自动垂直，即得非零解方向。

## 5. 非齐次系统 $AX=B$ (Nonhomogeneous)

- $\det A\neq0$：唯一解 $X=A^{-1}B$；
- $\det A=0$：几何上"三平面都平行于同一条线"，不可能唯一解，只能**无解或无穷多解**。

完整的解结构（齐次通解 + 特解）见 [[Vector Spaces and Subspaces#^204ad0|线性代数视角下的解的结构]]。

---

> [!important] 一句话总结
> 平面问题的核心是法向量：点在平面上 $\iff$ 法向量与位移向量点积为零；解的结构由行列式判定。
