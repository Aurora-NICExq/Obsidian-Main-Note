---
aliases: [拉格朗日乘数法, Lagrange Multipliers]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Gradient and Directional Derivative|梯度、方向导数]], [[Total Differential and the Chain Rule|微分、链式法则]], [[Second Derivative Test|二阶导检验]], [[Maxima and Minima (Several Variables)|极大极小问题]], [[Dependent Variables and Constrained Partial Derivatives|非独立变量]]"
down: ""
---
# Lagrange Multipliers

> [!summary] 核心结论
> 约束最值点处，目标函数 $f$ 的等值集与约束集 $g=c$ **相切**，故两梯度平行：$\nabla f=\lambda\nabla g$。再配上约束方程 $g=c$，即得求候选点的拉格朗日方程组。

前置知识：[[Gradient and Directional Derivative|梯度、方向导数]]、[[Maxima and Minima (Several Variables)|极大极小问题]]。

---

## 1. 引入 (Motivation)

在约束 $g(x,y,z)=c$ 下求 $f$ 的极值。变量不再独立，直接 $\nabla f=0$ 往往无效。约束简单时可解出一变量代回；但很多时候约束"解不出来"，需要新方法。

## 2. 几何核心：相切 ⟹ 梯度平行 (Tangency)

在约束曲线 $g=c$ 上找 $f$ 的极值时，最优点对应的 $f$ 等值线会与约束曲线**相切**。相切意味着切线方向相同，故法向量（梯度方向）平行：

$$\nabla f\parallel\nabla g.$$

根据"梯度垂直等值线/等值面"（见 [[Gradient and Directional Derivative|梯度、方向导数]]）：$\nabla f\perp\{f=$const$\}$，$\nabla g\perp\{g=c\}$，相切则两法向量平行。

## 3. 拉格朗日方程 (Lagrange Equations)

"平行"用"成比例"表达，存在标量 $\lambda$（乘数, multiplier）使

$$\nabla f=\lambda\nabla g,\qquad g=c.$$

未知量由 $(x,y)$ 扩为 $(x,y,\lambda)$，加约束方程正好配平。

## 4. 方向导数解释 (Directional-Derivative View)

约束面上最优点沿任何**允许方向**（切向 $\hat u$）移动，$f$ 的一阶变化为零：$\tfrac{df}{ds}=\nabla f\cdot\hat u=0$。故所有切向量都垂直 $\nabla f$，说明 $\nabla f$ 是约束面的法向量；而 $\nabla g$ 也是，于是二者平行。

## 5. 示例：双曲线 $xy=3$ 上的最近点 (Example)

最小化距离平方 $f=x^2+y^2$，约束 $g=xy=3$：

$$2x=\lambda y,\quad 2y=\lambda x,\quad xy=3.$$

解得 $\lambda=2$，候选点 $(\sqrt3,\sqrt3)$ 与 $(-\sqrt3,-\sqrt3)$。

## 6. 注意点 (Caveats)

- 拉格朗日法**只给候选点**，不直接判别 max/min；
- 约束场景下 Hessian 二阶判别不直接适用；
- 须**比较 $f$ 值**并检查"跑到边界/无穷远是否更大/更小"以定全局结论。

## 7. 进阶例子 (Advanced)

体积固定的四面体（底面固定 ⟹ 高 $h$ 固定，因 $V=\tfrac13 A_{\text{base}}h$），顶点在 $z=h$ 上移动以最小化侧面积。换贴合几何的变量（$a_i$ 为底边长，$u_i$ 为顶点投影到各边的距离，侧面积 $\tfrac12 a_i\sqrt{u_i^2+h^2}$），约束 $A_{\text{base}}=\tfrac12(a_1u_1+a_2u_2+a_3u_3)$。拉格朗日乘数给出 $u_1=u_2=u_3$，即顶点投影是底三角形的**内心 (incenter)**。

## 8. 做题模板 (Template)

1. 写目标 $f$ 与约束 $g=c$；
2. 列 $\nabla f=\lambda\nabla g$ + 约束方程；
3. 解所有候选点；
4. 比较 $f$ 值并检查边界/无穷远。

---

> [!important] 一句话总结
> 拉格朗日乘数法的核心方程是 $\nabla f=\lambda\nabla g$ 加约束 $g=c$——约束最优点处梯度被约束面"拦住"而平行。
