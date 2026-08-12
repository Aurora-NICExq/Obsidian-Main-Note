---
aliases: [非独立变量, Dependent Variables, Constrained Partial Derivatives]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Lagrange Multipliers|拉格朗日乘数法]], [[Maxima and Minima (Several Variables)|极大极小问题]], [[Total Differential and the Chain Rule|微分、链式法则]], [[Functions of Several Variables, Level Sets, and Partial Derivatives|等值面、偏导数]]"
down: ""
---
# Dependent Variables and Constrained Partial Derivatives

> [!summary] 核心结论
> 当变量被方程约束时，偏导数必须写清"**固定谁**"。最稳的方法是对约束做全微分 $dg=0$，按固定条件令相应微分为零，再消元——这避免了"变量同名 ⟹ 偏导相等"的常见陷阱。

前置知识：[[Total Differential and the Chain Rule|微分、链式法则]]。

---

## 1. 问题：约束下"固定谁" (The Core Question)

许多物理/化学场景变量不自由，如理想气体 $PV=nRT$。讨论"对 $V$ 的偏导"前必须说清"变化时固定了谁"。标准模型：

$$g(x,y,z)=c,$$

局部常把 $z$ 看成由约束决定的 $z(x,y)$。

## 2. 全微分把约束线性化 (Linearize the Constraint)

$$dg=g_x\,dx+g_y\,dy+g_z\,dz=0.$$

它表示：约束面上的小变化 $(dx,dy,dz)$ 不能乱来，必须满足此式。

## 3. 基本约束偏导 (Basic Constrained Partials)

把 $z$ 视为 $z(x,y)$，$\big(\tfrac{\partial z}{\partial x}\big)_y$ 表示动 $x$、固定 $y$（令 $dy=0$）。由 $dg=0$ 解出（$g_z\neq0$）：

$$\left(\frac{\partial z}{\partial x}\right)_y=-\frac{g_x}{g_z},\qquad \left(\frac{\partial z}{\partial y}\right)_x=-\frac{g_y}{g_z}.$$

## 4. 偏导符号的歧义 (Notation Matters)

同一函数换变量后偏导可能不同——不是算错，是固定条件变了。例 $f=x+y$，令 $x=u,\ y=u+v$ 得 $f=2u+v$：

$$\frac{\partial f}{\partial x}=1,\qquad \frac{\partial f}{\partial u}=2,$$

尽管 $x=u$。因为 $\partial/\partial x$ 固定 $y$，而 $\partial/\partial u$ 固定 $v$（即固定 $y-x$）。有歧义时必须写 $\big(\tfrac{\partial f}{\partial x}\big)_y$、$\big(\tfrac{\partial f}{\partial u}\big)_v$。

## 5. 求带约束偏导：两条等价路线 (Two Routes)

设 $f(x,y,z)$ 且约束 $g=c$，求 $\big(\tfrac{\partial f}{\partial z}\big)_y$（固定 $y$、$z$ 为自变量、$x$ 随约束走）。

- **微分消元法**：写 $df=f_x dx+f_y dy+f_z dz$，令 $dy=0$；用 $dg=0$（同样 $dy=0$）解出 $dx$ 用 $dz$ 表示；代回得 $df=\big(\tfrac{\partial f}{\partial z}\big)_y dz$。
- **链式法则法**：$\big(\tfrac{\partial f}{\partial z}\big)_y=f_x\big(\tfrac{\partial x}{\partial z}\big)_y+f_z$，对 $g$ 同样展开得 $\big(\tfrac{\partial x}{\partial z}\big)_y$，代回。

两路线本质相同——都在计算"约束面上的允许方向"。

## 6. 例题 (Worked Example)

三角形面积 $A=\tfrac12 ab\sin\theta$；若为直角三角形、$b$ 为斜边，则约束 $a=b\cos\theta$。"$A$ 对 $\theta$ 的变化率"至少三义：固定 $a,b$；约束下固定 $a$；约束下固定 $b$。约束下固定 $a$ 的结果：

$$\left(\frac{\partial A}{\partial\theta}\right)_a=\frac12 ab\sec\theta.$$

## 7. 易错点 (Pitfalls)

- 不写"固定谁"就算偏导；把"变量同名"当"偏导相等"；忘用约束消元（$x$ 常被约束拖着走）；混淆普通偏导 $f_x$ 与约束偏导。

---

> [!important] 一句话总结
> 约束偏导的可靠流程：写 $df$ 与 $dg=0$，按固定条件令相应微分为零，再消元——先讲清固定谁，再动手。
