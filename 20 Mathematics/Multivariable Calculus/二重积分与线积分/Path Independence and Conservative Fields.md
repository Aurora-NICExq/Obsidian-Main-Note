---
aliases: ["path independent，conservative", Path Independence and Conservative Fields, Conservative Fields]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Vector Fields and Line Integrals in the Plane|平面向量场和线积分]], [[Gradient Fields and Potential Functions|gradient field,potential function]], [[Double Integrals|二重积分]], [[Green's Theorem (Circulation Form)|格林定理]], [[Stokes' Theorem|斯托克斯定理]]"
down: "[[Gradient Fields and Potential Functions|gradient field,potential function]]"
---
# Path Independence and Conservative Fields

> [!summary] 核心结论
> 一般线积分依赖路径，但**保守场 (conservative field)** 的做功只依赖起点与终点。四个等价说法：梯度场（存在势函数）、路径无关、闭合积分为零、恰当微分。

前置知识：[[Vector Fields and Line Integrals in the Plane|平面向量场和线积分]]、[[Gradient Fields and Potential Functions|gradient field,potential function]]。

---

## 1. 回顾：线积分 (Line Integral)

$$\int_C\mathbf F\cdot d\mathbf r=\int_C\mathbf F\cdot\mathbf T\,ds=\int_C M\,dx+N\,dy.$$

每段位移 $d\mathbf r$ 上只"吃到"力在走路方向上的分量（点乘），沿路累加即总功。

## 2. 示例：某闭合路做功为 0 (A Closed Loop)

$\mathbf F=\langle y,x\rangle$（即 $y\,dx+x\,dy$）绕"x 轴段 + 圆弧段 + 对角线"闭合曲线：三段分别为 $0,\tfrac12,-\tfrac12$，和为 $0$。

> [!warning] 别过度推广
> 这只说明"这条闭合路"为 $0$，**不代表所有闭合路都为 $0$**。需要系统判据，见下。

## 3. 梯度场与线积分基本定理 (Gradient Theorem)

若 $\mathbf F=\nabla f$（$f$ 为**势函数**；物理常用 $\mathbf F=-\nabla f$），则曲线从 $P_0$ 到 $P_1$：

$$\int_C\mathbf F\cdot d\mathbf r=f(P_1)-f(P_0).$$

做功 = "终点势 − 起点势"。

## 4. 四个等价观点 (Four Equivalences)

1. **保守 (conservative)**：任意闭曲线 $\oint_C\mathbf F\cdot d\mathbf r=0$；
2. **路径无关 (path independent)**：同端点的两条路径积分相同；
3. **梯度场**：$\mathbf F=\nabla f$；
4. **恰当微分 (exact differential)**：$M\,dx+N\,dy=df$。

推进逻辑：$\mathbf F=\nabla f\Rightarrow$ 路径无关 $\Rightarrow$ 闭合为 $0$；反向"闭合为 $0$/路径无关 $\Rightarrow$ 存在势函数"在无洞区域成立。

## 5. 反例与物理解释 (Counterexample & Physics)

旋转场 $\mathbf F=\langle-y,x\rangle$ 沿半径 $a$ 圆逆时针积分为 $2\pi a^2\neq0$，故**非**保守。物理直觉：旋转场像永动旋涡，绕一圈能净赚/净亏功，违反"只靠势能差"的保守世界观（对应能量守恒）。

## 6. 做题工作流 (Workflow)

1. 先问：它会不会其实是梯度场？（那样只需端点）
2. 已知 $\mathbf F=\nabla f$：直接 $f(P_1)-f(P_0)$；
3. 暂不知：常规参数化计算，或用"闭合是否为 $0$/是否路径无关"判定保守性。判别与构造 $f$ 见 [[Gradient Fields and Potential Functions|gradient field,potential function]]。

---

> [!important] 一句话总结
> 保守场把路径积分降维为势函数端点差：$\int_C\nabla f\cdot d\mathbf r=f(B)-f(A)$。
