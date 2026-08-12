---
aliases: [极大极小问题, Maxima and Minima, Optimization in Several Variables]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Partial Differential Equations and Multivariable Differentiation Review|偏微分方程]], [[Dependent Variables and Constrained Partial Derivatives|非独立变量]], [[Lagrange Multipliers|拉格朗日乘数法]], [[Second Derivative Test|二阶导检验]], [[Gradient and Directional Derivative|梯度、方向导数]]"
down: "[[Second Derivative Test|二阶导检验]]"
---
# Maxima and Minima (Several Variables)

> [!summary] 核心结论
> 多元极值问题：先找候选点（$\nabla f=0$），用二阶导检验判断局部性质；**全局最值必须比较内部临界点、边界与无穷远**。约束极值用拉格朗日乘数法。

前置知识：[[Gradient and Directional Derivative|梯度、方向导数]]、[[Second Derivative Test|二阶导检验]]。

---

## 1. 问题分类 (Types)

| 类型 | 条件 | 方法 |
| :-- | :-- | :-- |
| 无约束局部极值 | 开区域内自由 | 解 $\nabla f=\mathbf0$ + [[Second Derivative Test|二阶导检验]] |
| 有约束极值 | $g(x,y,z)=c$ | [[Lagrange Multipliers|拉格朗日乘数法]] 或消元 |
| 全局极值 | 闭/开/无界区域 | 内部临界点 + 边界 + 无穷远 |
| 最小二乘 | 最小化误差平方和 | 对参数求梯度 → 正规方程 |

## 2. 无约束候选点 (Critical Points)

内部局部极值必满足 $\nabla f(x_0,y_0)=\mathbf0$，即 $f_x=f_y=0$。临界点只是候选，可能极大、极小或鞍点。

## 3. 二阶导分类 (Classification)

记 $A=f_{xx},B=f_{xy},C=f_{yy}$，Hessian 判别式 $D=AC-B^2$：

| 条件 | 结论 |
| :-- | :-- |
| $D>0,A>0$ | 局部最小 |
| $D>0,A<0$ | 局部最大 |
| $D<0$ | 鞍点 |
| $D=0$ | 判别失败 |

## 4. 全局最值流程 (Global Extrema)

1. 解 $\nabla f=\mathbf0$ 得内部候选；
2. 检查边界（参数化/分段化为一元）；
3. 区域无界或开边界时检查无穷远/趋边界的极限；
4. 比较所有候选值。

> [!warning] 常见错误
> 只检查 $\nabla f=0$ 只能处理内部局部候选，不能直接回答全局最值。

## 5. 有约束极值 (Constrained)

求 $f$ 在 $g=c$ 下的极值，一般不能直接 $\nabla f=0$；约束面上最优点满足

$$\nabla f=\lambda\nabla g,\qquad g=c.$$

解出候选后仍要比较 $f$ 值并检查约束集的边界/无穷远（详见 [[Lagrange Multipliers|拉格朗日乘数法]]）。

## 6. 最小二乘与正规方程 (Least Squares)

数据 $(x_i,y_i)$，模型 $\hat y=ax+b$，目标 $S(a,b)=\sum(ax_i+b-y_i)^2$。对参数求偏导置零得关于 $a,b$ 的线性方程组。矩阵形式 $\hat y=X\beta$，$S(\beta)=\|X\beta-y\|^2$，

$$\nabla_\beta S=2X^{\top}(X\beta-y)=0\ \Rightarrow\ X^{\top}X\,\beta=X^{\top}y,$$

即**正规方程 (normal equations)**，其几何意义（投影）见 [[Projections and Projection Matrices#^325100|线性代数中的正规方程]]。

---

> [!important] 一句话总结
> 极值的核心不是"求导等于零"本身，而是先找候选点，再用二阶信息、边界与比较确定结论。
