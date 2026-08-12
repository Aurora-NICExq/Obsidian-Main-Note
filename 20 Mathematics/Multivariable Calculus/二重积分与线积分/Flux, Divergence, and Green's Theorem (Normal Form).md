---
aliases: [通量与散度（格林定理法向形式）, Flux Divergence and Green's Theorem Normal Form, 2D Divergence Theorem]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Green's Theorem (Circulation Form)|格林定理]], [[Gradient Fields and Potential Functions|gradient field,potential function]], [[Vector Fields and Line Integrals in the Plane|平面向量场和线积分]], [[Line Integrals in Space, Curl, and Potential Functions|空间线积分、旋度与势函数]]"
down: ""
---
# Flux, Divergence, and Green's Theorem (Normal Form)

> [!summary] 核心结论
> 把"沿边界切向的做功线积分"平移到"沿边界法向的通量 (flux) 线积分"，得到格林定理的**法向形式**（即二维散度定理）：**边界总通量 = 区域内散度 (divergence) 的二重积分**。

前置知识：[[Vector Fields and Line Integrals in the Plane|平面向量场和线积分]]、[[Green's Theorem (Circulation Form)|格林定理]]。

---

## 1. 通量的定义 (Flux)

把 $\mathbf F$ 视作二维流体速度场。对弧长 $ds$、单位法向量 $\mathbf n$，穿过该小段的瞬时流量 $\approx\mathbf F\cdot\mathbf n\,ds$，累加得通量线积分 $\int_C\mathbf F\cdot\mathbf n\,ds$。通量取**法向分量**（对比做功取**切向分量** $\int_C\mathbf F\cdot\mathbf T\,ds$）；$\mathbf n\perp\mathbf T$ 是点积正交结构（见 [[Orthogonal Vectors and Subspaces|正交向量和正交子空间(orthogonal)]]）。

## 2. 通量的 $dx,dy$ 公式 (Differential Form)

$C$ 取正向（逆时针），外法向指向行进方向右侧。参数化 $\mathbf r(t)=(x,y)$：

$$\mathbf T\,ds=\langle dx,dy\rangle,\qquad \mathbf n\,ds=\langle dy,-dx\rangle.$$

故对 $\mathbf F=\langle P,Q\rangle$：

$$\int_C\mathbf F\cdot\mathbf n\,ds=\int_C(P\,dy-Q\,dx)=\int_C(-Q\,dx+P\,dy).$$

("把切向微元旋转 $90^\circ$ 得法向微元"是线性变换，见 [[The Matrix Viewpoint|矩阵的视角]]。)

## 3. 法向形式 = 2D 散度定理 (Normal Form)

定义散度 $\operatorname{div}\mathbf F:=P_x+Q_y$。对正向简单闭曲线 $C$ 及所围区域 $R$（$P,Q$ 在含 $R$ 开集上 $C^1$）：

$$\oint_C\mathbf F\cdot\mathbf n\,ds=\iint_R\operatorname{div}\mathbf F\,dA.$$

**散度直观**：$>0$ 为源（流出），$<0$ 为汇（吸收），$=0$ 无净源汇（不可压缩流）。

## 4. 单连通与"洞" (Simply Connected & Holes)

法向形式右边是对整个 $R$ 的积分，故要求 $\mathbf F$ 及偏导在 $R$ **内部处处**定义——不能只看边界。**单连通 (simply connected)**：连通且无洞（圆盘、矩形是；挖去原点的平面不是）。

**典型反例**：$\mathbf F=\left\langle\dfrac{x}{x^2+y^2},\dfrac{y}{x^2+y^2}\right\rangle$ 在 $\mathbb R^2\setminus\{0\}$ 上 $\operatorname{div}\mathbf F=0$，但绕单位圆通量 $=\int_0^{2\pi}1\,d\theta=2\pi\neq0$——因为圆盘含原点而 $\mathbf F$ 在原点无定义。

## 5. 带洞区域 (Regions with Holes)

外边界 $C_{\text{out}}$ 逆时针、内边界 $C_{\text{in}}$ 顺时针。若都按逆时针参数化：

$$\oint_{C_{\text{out}}}\mathbf F\cdot\mathbf n\,ds-\oint_{C_{\text{in}}}\mathbf F\cdot\mathbf n\,ds=\iint_R\operatorname{div}\mathbf F\,dA.$$

## 6. 例题 (Example)

$\mathbf F=\langle x,y\rangle$：$\operatorname{div}\mathbf F=2$，故 $\oint_C\mathbf F\cdot\mathbf n\,ds=\iint_R 2\,dA=2\,\text{Area}(R)$。半径 $a$ 圆盘通量 $=2\pi a^2$。

## 7. 线性代数视角 (Linear-Algebra View)

若 $\mathbf F(\mathbf x)=A\mathbf x$ 为线性场（$A$ 为 $2\times2$），则 $\operatorname{div}\mathbf F=\mathrm{tr}(A)$，即散度等于矩阵的迹。可联系 [[Eigenvalues and Eigenvectors#特征值与迹 (Eigenvalues and the Trace)|迹]]：迹是线性变换"总体伸缩"的不变量。

---

> [!important] 一句话总结
> 通量形式关注法向分量：边界净流出 = 内部散度总和；用前务必确认内部无奇点。
