---
aliases: [散度定理（应用与陷阱）, Divergence Theorem Applications and Pitfalls]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Divergence Theorem (Gauss's Theorem)|散度定理（高斯定理）]], [[Topological Subtleties and Maxwell's Equations|拓扑注意事项与麦克斯韦方程组]], [[Vector Fields, Surface Integrals, and Flux in 3D|三维向量场、曲面积分与通量]], [[Flux, Divergence, and Green's Theorem (Normal Form)|通量与散度（格林定理法向形式）]], [[Stokes' Theorem|斯托克斯定理]]"
down: "[[Topological Subtleties and Maxwell's Equations|拓扑注意事项与麦克斯韦方程组]]"
---
# Divergence Theorem (Applications and Pitfalls)

> [!summary] 核心结论
> 散度定理常用于"省曲面积分"与"反算体积"，但两类坑最常见：**曲面是否真闭合**、**区域内是否有奇点（场不光滑/未定义）**。有奇点必须先"挖洞"处理。

前置知识：[[Divergence Theorem (Gauss's Theorem)|散度定理（高斯定理）]]。

---

## 1. 用途一：算闭曲面通量 (Compute Flux)

把 $\iint_{\partial E}\mathbf F\cdot\mathbf n\,dS$ 改写为 $\iiint_E\operatorname{div}\mathbf F\,dV$，在体积分端用对称性 + 合适坐标（[[Triple Integrals (Rectangular and Cylindrical Coordinates)|柱坐标]]、[[Spherical Coordinates and Surface Area|球坐标]]）。

## 2. 用途二：反算体积/平均值 (Compute Volume)

若构造 $\mathbf F$ 使 $\operatorname{div}\mathbf F\equiv1$，则 $\mathrm{Vol}(E)=\iint_{\partial E}\mathbf F\cdot\mathbf n\,dS$。常用 $\mathbf F=\tfrac13\langle x,y,z\rangle$（散度为 $1$）。

## 3. 抵消机制 (Why Only the Outer Boundary)

把 $E$ 切成小盒子，相邻盒子共享面一次取外法向、一次取内法向，通量符号相反，**内部面全抵消**，只剩外边界 $\partial E$。

## 4. 关键陷阱：奇点 (Singularities)

散度定理要求 $\mathbf F$ 在区域内光滑。若区域含奇点，需先"挖洞 (puncture)"，对挖空区域用定理，再分析小洞边界贡献。

> [!warning] "div = 0 但通量 ≠ 0"
> 点源场 $\mathbf F(\mathbf r)=\dfrac{\mathbf r}{\|\mathbf r\|^3}$ 在 $\mathbf0$ 处未定义；对 $\mathbf r\neq0$ 有 $\operatorname{div}\mathbf F=0$，但绕原点的任意球面 $\iint_{S_a}\mathbf F\cdot\mathbf n\,dS=4\pi$。原点"藏了一个源"，普通意义下的 $\operatorname{div}$ 捕捉不到（需 $\delta$ 分布）。

## 5. Checklist

1. **闭合性**：是"侧面"还是"完整封闭曲面"？缺盖先补上再减回；
2. **光滑性**：区域内是否含 $\mathbf F$ 未定义点（尤其分母含 $x^2+y^2+z^2$）；
3. 体积分端用对称性 + 选坐标 + 简化被积函数。

---

> [!important] 一句话总结
> 用散度定理前先问：曲面闭合吗？场在内部光滑吗？有奇点就先挖洞处理（详见 [[Topological Subtleties and Maxwell's Equations|拓扑注意事项与麦克斯韦方程组]]）。
