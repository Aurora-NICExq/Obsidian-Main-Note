---
aliases: [平面向量场和线积分, Vector Fields and Line Integrals in the Plane, Line Integrals]
tags: [math, multivariable-calculus]
up: "[[Multivariable Calculus MOC]]"
related: "[[Path Independence and Conservative Fields|path independent，conservative]], [[Gradient Fields and Potential Functions|gradient field,potential function]], [[Green's Theorem (Circulation Form)|格林定理]], [[Flux, Divergence, and Green's Theorem (Normal Form)|通量与散度（格林定理法向形式）]], [[Line Integrals in Space, Curl, and Potential Functions|空间线积分、旋度与势函数]]"
down: "[[Green's Theorem (Circulation Form)|格林定理]]"
---
# Vector Fields and Line Integrals in the Plane

> [!summary] 核心结论
> 线积分 (line integral) $\int_C\mathbf F\cdot d\mathbf r$ 把向量场沿曲线的**切向分量**累加，物理上是力沿路径做的**功 (work)**。两种等价理解：参数化计算 $\int_a^b\mathbf F(\mathbf r(t))\cdot\mathbf r'(t)\,dt$ 与几何视角 $\int_C\mathbf F\cdot\mathbf T\,ds$。

前置知识：[[Parametric Equations of Curves and Lines|曲线和直线参数方程]]、[[Dot Product|点积]]。

---

## 1. 平面向量场 (Vector Field)

平面每点 $(x,y)$ 放一个向量 $\mathbf F(x,y)=\langle M(x,y),N(x,y)\rangle$，整张平面是"一片箭头草原"。

![[tikz-vector-fields-and-line-integrals-in-the-plane-01.svg]]

典型例子：常向量场 $\langle2,1\rangle$；径向发散 $\langle x,y\rangle$；旋转场 $\langle-y,x\rangle$。它们决定线积分（做功）的正负。

## 2. 线积分：把"做功"数学化 (Work)

小位移下 $\Delta W\approx\mathbf F\cdot\Delta\mathbf r$，分段求和取极限：

$$W=\int_C\mathbf F\cdot d\mathbf r=\lim_{\max|\Delta\mathbf r_i|\to0}\sum_i\mathbf F(\text{点}_i)\cdot\Delta\mathbf r_i.$$

## 3. 参数化计算 (Parametric Computation)

给曲线参数化 $\mathbf r(t)=\langle x(t),y(t)\rangle,\ t\in[a,b]$，则 $d\mathbf r=\mathbf r'(t)\,dt$，线积分化为一元积分：

$$\int_C\mathbf F\cdot d\mathbf r=\int_a^b\mathbf F(\mathbf r(t))\cdot\mathbf r'(t)\,dt.$$

肌肉记忆：**代入 → 求导 → 点乘 → 一元积分**。

## 4. 微分形式记号 (Differential Form)

$\mathbf F=\langle M,N\rangle$，形式上 $d\mathbf r=\langle dx,dy\rangle$，故

$$\int_C\mathbf F\cdot d\mathbf r=\int_C M\,dx+N\,dy.$$

> [!warning] 不是两个独立积分
> $\int_C M\,dx+N\,dy$ 是**沿曲线 $C$** 的同一个积分，$x,y$ 联动；最终必须把 $x,y,dx,dy$ 都化为同一参数。

## 5. 例题 (Example)

旋转场 $\mathbf F=\langle-y,x\rangle$，$C:x=t,y=t^2,\ 0\le t\le1$。则 $\mathbf r'=\langle1,2t\rangle$，$\mathbf F(\mathbf r(t))=\langle-t^2,t\rangle$：

$$\int_C\mathbf F\cdot d\mathbf r=\int_0^1\langle-t^2,t\rangle\cdot\langle1,2t\rangle\,dt=\int_0^1 t^2\,dt=\frac13.$$

## 6. 几何视角：切向分量 × 弧长 (Tangential Component)

$d\mathbf r=\mathbf T\,ds$（$\mathbf T$ 单位切向量），故

$$\int_C\mathbf F\cdot d\mathbf r=\int_C\mathbf F\cdot\mathbf T\,ds,$$

$\mathbf F\cdot\mathbf T$ 是力在运动方向上的分量。两个"眼算"例子（圆 $x^2+y^2=a^2$ 逆时针）：径向 $\langle x,y\rangle$ 处处垂直切向 ⟹ 功为 $0$；旋转 $\langle-y,x\rangle$ 与切向同向、长度 $a$ ⟹ $\int_C a\,ds=a\cdot2\pi a=2\pi a^2$。

> [!note] 参数化不变性
> 线积分依赖几何路径与方向，不依赖参数名；但换**路径**结果一般改变，反向走则变号。

---

> [!important] 一句话总结
> 线积分的稳定算法：参数化曲线 → 代入向量场 → 点乘 $\mathbf r'(t)$ → 一元积分；几何上是切向分量沿弧长的累加。
