---
aliases: ["Green's law", Green's Theorem (Computation and Proof), Green's Theorem Working Version]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Green's Theorem (Circulation Form)|格林定理]], [[Double Integrals|二重积分]], [[Path Independence and Conservative Fields|path independent，conservative]], [[Gradient Fields and Potential Functions|gradient field,potential function]]"
down: ""
---
# Green's Theorem (Computation and Proof)

> [!summary] 核心结论
> 本笔记是 [[Green's Theorem (Circulation Form)|格林定理（环量形式）]] 的**计算与证明**伴侣：给出"看到闭合边界上 $M\,dx+N\,dy$ 就先算 $N_x-M_y$"的实战套路，以及定理的证明骨架（拆项 + 可加性 + 竖直简单区域）。

前置知识：[[Green's Theorem (Circulation Form)|格林定理]]、[[Double Integrals|二重积分]]。

---

## 1. 定理陈述（工作型） (Statement)

$C$ 为正向（逆时针）闭合分段光滑曲线，围成区域 $R$，$\mathbf F=\langle M,N\rangle$：

$$\oint_C M\,dx+N\,dy=\iint_R\left(\frac{\partial N}{\partial x}-\frac{\partial M}{\partial y}\right)dA,\qquad \operatorname{curl}\mathbf F=N_x-M_y.$$

**方向**：沿边界走，$R$ 总在左手边（通常逆时针）；反向则线积分变号。

## 2. 计算套路 (Recipe)

1. 算 $N_x-M_y$；
2. 改写为 $\iint_R(N_x-M_y)\,dA$；
3. 选合适坐标（直角/极坐标/平移）完成面积积分。

**快速化简信号**：边界参数化复杂但 $N_x-M_y$ 简单时，优先用格林定理。

## 3. 代表例题 (Example)

$C$ 为以 $(2,0)$ 为心的单位圆（逆时针）：

$$\oint_C ye^{-x}\,dx+\left(\tfrac12x^2-e^{-x}\right)dy=\iint_R\big((x+e^{-x})-e^{-x}\big)\,dA=\iint_R x\,dA=(\text{面积 }\pi)(\bar x=2)=2\pi.$$

体现"难的边界积分 → 简单的区域量（面积 × 质心坐标）"。

## 4. 推论：梯度场判别 (Corollary)

若 $\mathbf F$ 在 $R$ 及内部 $C^1$ 且 $N_x=M_y$，则对任意闭曲线 $\oint_C\mathbf F\cdot d\mathbf r=0$，即 $\mathbf F$ 保守（见 [[Gradient Fields and Potential Functions|gradient field,potential function]]）。**前提**：$\mathbf F$ 与 $\operatorname{curl}\mathbf F$ 在区域内部处处定义（有奇点/洞时即便 curl=0 也可能非零）。

## 5. 证明骨架 (Proof Sketch)

1. **拆成两条恒等式**：$\oint_C M\,dx=-\iint_R M_y\,dA$，$\oint_C N\,dy=\iint_R N_x\,dA$，相加即得；
2. **可加性 (additivity)**：复杂区域切成 $R_1,R_2$，内部公共边界线积分相互抵消，故只需对简单块成立；
3. **竖直简单区域 (vertically simple)**：对 $a<x<b,\ f_0(x)<y<f_1(x)$ 型区域，边界分四段，竖直边上 $dx=0$，线积分只剩上下两条，与二重积分匹配。

## 6. 用线积分算面积 (Area)

选 $(M,N)$ 使 $N_x-M_y=1$：$\text{Area}(R)=\oint_C x\,dy$（planimeter 测面积仪的原理）。

## 7. 自测清单 (Checklist)

- $C$ 是否闭合？方向是否正向（否则加负号）？$\mathbf F$ 及偏导在 $R$ 内部是否处处光滑（有洞/奇点要小心）？$N_x-M_y$ 是否比参数化更好算？

---

> [!important] 一句话总结
> 看到闭合边界上的 $M\,dx+N\,dy$，先算 $N_x-M_y$，再决定是否用格林定理；其证明 = 拆项 + 可加性 + 简单区域。
