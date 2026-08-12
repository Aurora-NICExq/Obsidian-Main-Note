---
aliases: [二阶导检验, Second Derivative Test, Hessian Test]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Maxima and Minima (Several Variables)|极大极小问题]], [[Lagrange Multipliers|拉格朗日乘数法]], [[Functions of Several Variables, Level Sets, and Partial Derivatives|等值面、偏导数]], [[Total Differential and the Chain Rule|微分、链式法则]]"
down: ""
---
# Second Derivative Test

> [!summary] 核心结论
> 临界点 (critical point) 由一阶偏导同时为零给出；局部形状由 Hessian 判别式 $D=AC-B^2$ 决定。$D>0$ 时同向弯曲（看 $A$ 定极大/极小），$D<0$ 为鞍点，$D=0$ 判别失败。

前置知识：[[Maxima and Minima (Several Variables)|极大极小问题]]。

---

## 1. 临界点 (Critical Points)

二元函数 $f(x,y)$ 满足 $f_x=f_y=0$ 处为临界点，此时切平面水平。但**全局**最值还可能在**边界**或变量趋于无穷远处取得（见 [[Maxima and Minima (Several Variables)|极大极小问题]]）。

## 2. 二次型分析 (Quadratic Form)

临界点附近形状形如二次型 $w=ax^2+bxy+cy^2$（在原点）。判别式 $4ac-b^2$：

- $>0$：同号弯曲，$a>0$ 极小、$a<0$ 极大；
- $<0$：可正可负 → **鞍点 (saddle)**；
- $=0$：退化 (degenerate)，某方向无变化。

直觉同一元二次函数"是否有实根、抛物线整条在 $x$ 轴上/下方"。

## 3. 二阶导数判别法 (The Test)

临界点处记 $A=f_{xx},\ B=f_{xy}=f_{yx},\ C=f_{yy}$，定义

$$D=AC-B^2=\det\begin{pmatrix}A&B\\ B&C\end{pmatrix}.$$

| 条件 | 结论 |
| :-- | :-- |
| $D>0,\ A>0$ | 局部最小 (local min) |
| $D>0,\ A<0$ | 局部最大 (local max) |
| $D<0$ | 鞍点 (saddle) |
| $D=0$ | 判别失败（需更高阶项） |

> [!note] 为何判别式起作用（二阶泰勒近似）
> 临界点附近形状由二阶项主导：$\Delta f\approx\tfrac12 f_{xx}\Delta x^2+f_{xy}\Delta x\Delta y+\tfrac12 f_{yy}\Delta y^2$（一阶项因 $f_x=f_y=0$ 消失）。这是一个二次型，其正定/负定/不定恰由 $D=AC-B^2$ 与 $A$ 的符号刻画——这正是判别法的来历。

## 4. 全局最值：边界 + 无穷远 (Global Extrema)

找全局最值须三步：①内部临界点分类；②检查边界（参数化为一元/分段）；③检查无穷远或趋于边界的极限。

> [!example] 局部最小但无最大
> 在 $x>0,y>0$ 上 $f=x+y+\dfrac{1}{xy}$，唯一临界点 $(1,1)$ 满足 $D>0,A>0$（局部最小）；但 $x\to0^+$ 或 $x,y\to\infty$ 时 $f\to\infty$，故**无全局最大**。

## 5. 解题流程 (Workflow)

1. 解 $\nabla f=0$ 求临界点；
2. 算 $A,B,C$；
3. 算 $D=AC-B^2$ 并分类；
4. 若问全局最值，补查边界与无穷远。

---

> [!important] 一句话总结
> 二阶导检验只分类内部临界点；全局最值还必须检查边界和无穷远。
