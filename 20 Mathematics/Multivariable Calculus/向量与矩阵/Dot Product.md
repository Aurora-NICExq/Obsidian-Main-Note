---
aliases: [点积, Dot Product]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Cross Product and Determinants|行列式叉积]], [[Matrices and Equations of Planes|矩阵和平面方程]], [[Gradient and Directional Derivative|梯度、方向导数]]"
down: "[[Cross Product and Determinants|行列式叉积]]"
---
# Dot Product

> [!summary] 核心结论
> 点积 (dot product) 同时编码**夹角、投影与正交**：$\mathbf u\cdot\mathbf v=\|\mathbf u\|\|\mathbf v\|\cos\theta$。方向导数、切向/法向判断、线积分与通量都建立在它之上。

---

## 1. 两种视角 (Two Views)

| 视角 | 含义 | 用途 |
| :-- | :-- | :-- |
| 几何 (geometric) | 向量是带方向和长度的箭头 | 判断夹角、投影、平行/垂直 |
| 代数 (algebraic) | 向量是有序坐标数组 | 用分量计算点积、方程与矩阵运算 |

## 2. 定义 (Definition)

- 几何定义：$\mathbf u\cdot\mathbf v=\|\mathbf u\|\,\|\mathbf v\|\cos\theta$；
- 坐标计算：$\mathbf u\cdot\mathbf v=u_1v_1+u_2v_2+u_3v_3$。

直观理解：一个向量在另一个方向上的**投影长度**乘以后者长度。

> [!note] 两种定义为何一致（余弦定理证明）
> 对三角形（边为 $\mathbf u,\mathbf v,\mathbf u-\mathbf v$）用余弦定理：$\|\mathbf u-\mathbf v\|^2=\|\mathbf u\|^2+\|\mathbf v\|^2-2\|\mathbf u\|\|\mathbf v\|\cos\theta$。左边按坐标展开 $\|\mathbf u\|^2+\|\mathbf v\|^2-2(u_1v_1+u_2v_2+u_3v_3)$。两式相消即得 $\|\mathbf u\|\|\mathbf v\|\cos\theta=\sum u_iv_i$。$\blacksquare$

## 3. 夹角与正交 (Angle & Orthogonality)

| 条件 | 几何意义 |
| :-- | :-- |
| $\mathbf u\cdot\mathbf v>0$ | 夹角 $<90^\circ$ |
| $\mathbf u\cdot\mathbf v=0$ | 两向量正交 (orthogonal) |
| $\mathbf u\cdot\mathbf v<0$ | 夹角 $>90^\circ$ |

## 4. 投影公式 (Projection)

设 $\mathbf v\neq\mathbf0$。$\mathbf u$ 在 $\mathbf v$ 方向上的**标量投影 (scalar projection)** 与**向量投影 (vector projection)**：

$$\operatorname{comp}_{\mathbf v}(\mathbf u)=\frac{\mathbf u\cdot\mathbf v}{\|\mathbf v\|},\qquad \operatorname{proj}_{\mathbf v}(\mathbf u)=\frac{\mathbf u\cdot\mathbf v}{\mathbf v\cdot\mathbf v}\,\mathbf v.$$

## 5. 在多变量微积分中的作用 (Roles)

| 场景 | 点积的作用 |
| :-- | :-- |
| 方向导数 (directional derivative) | $D_{\hat{\mathbf u}}f=\nabla f\cdot\hat{\mathbf u}$ |
| 切向/法向判断 | 法向量与切向量点积为 $0$ |
| 线积分 (line integral) | $\mathbf F\cdot d\mathbf r$ 取切向分量 |
| 通量 (flux) | $\mathbf F\cdot\mathbf n$ 取法向分量 |

---

> [!important] 一句话总结
> 点积把"一个向量在另一方向上的分量"化为可计算的代数量——夹角、投影、正交一网打尽。
