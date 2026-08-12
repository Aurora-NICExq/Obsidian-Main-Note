---
aliases:
  - 调和函数
  - Harmonic Functions
  - Laplace equation complex
  - Topic Harmonic Functions
tags: [math, complex_analysis]
up: "[[Complex Analysis (MIT 18.04) MOC]]"
related:
  - "[[Analytic Functions]]"
  - "[[Cauchy's Integral Formula]]"
  - "[[Two-Dimensional Hydrodynamics and Complex Potentials]]"
  - "[[Line Integrals and Cauchy's Theorem]]"
down: []
---
# 调和函数

> [!summary] 核心结论
> 二元实函数 $u(x,y)$ 调和（harmonic）$\Leftrightarrow$ 满足 Laplace 方程 $u_{xx}+u_{yy}=0$。解析函数 $f=u+iv$ 的实部、虚部都调和；在单连通区域上，给定调和 $u$ 可构造共轭调和函数 $v$，使 $f=u+iv$ 解析。水平集 $u=\mathrm{const}$ 与 $v=\mathrm{const}$ **正交**（梯度正交）。调和函数继承均值性质与最大值原理——这是静电、稳态温度与二维理想流体的共同数学骨架。

> 底本：MIT 18.04（Orloff）调和函数专题。工科联系：Laplace 方程、正交网格、与 [[Two-Dimensional Hydrodynamics and Complex Potentials]] 中的势函数 / 流函数。

---
## 1. Laplace 方程与调和

### 1.1 定义

开集上的 $C^2$ 实函数 $u(x,y)$ 称为**调和**，若
$$
\Delta u:=u_{xx}+u_{yy}=0.
$$
$\Delta$ 为 Laplace 算子。

### 1.2 经典物理模型（二维稳态）

| 场 | 调和对象 | 方程含义 |
|----|----------|----------|
| 静电 | 电势 | 无源区 $\nabla\cdot\mathbf{E}=0$ 且无旋 $\Rightarrow$ Laplace |
| 稳态热传导 | 温度 | 无热源时温度调和 |
| 理想流体（不可压无旋） | 速度势 / 流函数 | 见流体专题 |

复分析提供的是：**用解析函数成批制造调和函数**，并用共形映射搬动边界条件（后续）。

---
## 2. 解析 $\Rightarrow$ 实部虚部调和

设 $f=u+iv$ 解析，且 $u,v$ 二阶偏导连续。由 CR：
$$
u_x=v_y,\qquad u_y=-v_x.
$$
对第一式关于 $x$ 求导、第二式关于 $y$ 求导：
$$
u_{xx}=v_{yx},\qquad u_{yy}=-v_{xy}.
$$
混合偏导相等 $\Rightarrow$ $u_{xx}+u_{yy}=0$。同理 $v$ 调和。

> [!example] $f(z)=z^2$
> $u=x^2-y^2$，$v=2xy$。
> $$
> u_{xx}+u_{yy}=2-2=0,\qquad v_{xx}+v_{yy}=0.
> $$

> [!example] $f(z)=e^z$
> $u=e^x\cos y$，$v=e^x\sin y$，均为调和。

> [!example] $u=\log|z|=\ln\sqrt{x^2+y^2}$（在 $\mathbb{C}\setminus\{0\}$）
> 这是 $\operatorname{Re}\operatorname{Log} z$，故在挖去支割线（或穿孔平面上取局部）后调和。在原点有奇异——对应点源（见流体 / 静电）。

---
## 3. 从调和 $u$ 构造共轭 $v$

### 3.1 目标

给定调和 $u$，找 $v$ 使 $f=u+iv$ 解析，即满足 CR：
$$
v_x=-u_y,\qquad v_y=u_x.
$$
这是关于 $v$ 的一阶方程组；可积性条件恰为 $u$ 调和（因为 $v_{xy}=v_{yx}$ $\Leftrightarrow$ $-u_{yy}=u_{xx}$）。

### 3.2 单连通域上的做法（工科流程）

1. 由 $v_y=u_x$，对 $y$ 积分：
   $$
   v(x,y)=\int u_x(x,y)\,dy+g(x).
   $$
2. 用 $v_x=-u_y$ 定出 $g'(x)$，再积分得 $g$。
3. $v$ 差一个实常数；$f$ 差一个纯虚常数。

**关键假设**：区域**单连通**（保证线积分定义的 $v$ 单值）。在环域等有洞区域，绕洞一周可能使 $v$ 多出一个常数（多值共轭）——与 $\arg z$ 作为 $\ln|z|$ 的共轭相同。

> [!example] $u=x^2-y^2$（已知调和）
> $u_x=2x$，$u_y=-2y$。
> $$
> v=\int 2x\,dy+g(x)=2xy+g(x).
> $$
> $v_x=2y+g'(x)=-u_y=2y$ $\Rightarrow$ $g'=0$。取 $g=0$ 得 $v=2xy$，即 $f=z^2$（差常数）。

> [!example] $u=e^x\cos y$
> $u_x=e^x\cos y$，$u_y=-e^x\sin y$。
> $$
> v=\int e^x\cos y\,dy+g(x)=e^x\sin y+g(x).
> $$
> $v_x=e^x\sin y+g'(x)=-u_y=e^x\sin y$ $\Rightarrow$ $g=0$。得 $v=e^x\sin y$，$f=e^z$。

---
## 4. 水平集正交

解析且 $f'\neq 0$ 时，映射局部共形（保角）。特别地：

- 曲线族 $u(x,y)=c$（等势线 / level curves of $u$）
- 曲线族 $v(x,y)=k$（等流线 / level curves of $v$）

二者在交点处**正交**：
$$
\nabla u\cdot\nabla v=u_x v_x+u_y v_y=u_x(-u_y)+u_y u_x=0
$$
（用了 CR：$v_x=-u_y$，$v_y=u_x$）。

![[ca-harmonic-orthogonal.svg]]

> [!tip] 作图习惯
> 画出 $u=\mathrm{const}$ 与 $v=\mathrm{const}$ 的正交网格，就是解析函数（以及二维理想流）的视觉语言。$|f'|$ 控制局部缩放：网格疏密反映速度大小。

> [!example] $z^2$ 的网格
> $u=x^2-y^2=c$ 是双曲线；$v=2xy=k$ 是另一族双曲线；二者正交。原点 $f'=0$ 是停滞点，正交性 / 保角性在该点失效（夹角变为 $2$ 倍）。

---
## 5. 均值性质与最大值原理

### 5.1 均值性质

若 $u$ 在含闭圆盘 $|z-z_0|\le R$ 的区域上调和，则
$$
u(z_0)=\frac{1}{2\pi}\int_0^{2\pi}u(z_0+Re^{i\theta})\,d\theta.
$$
来源：局部构造解析 $f=u+iv$，对 $f$ 用 CIF 的均值形式，再取实部。也有纯实变量的圆均值证明。

### 5.2 最大值 / 最小值原理

在有界区域 $A$ 上调和、在 $\overline{A}$ 上连续的 $u$：最大值与最小值都在**边界**取得。若 $u$ 在内点取到最大或最小，则 $u$ 常数。

> [!warning] 与最大模的关系
> 解析 $f$ 的最大模原理 $\approx$ 对 $\log|f|$（在无零点处调和）或对 $|f|$ 的相关论证。调和函数的极值原理更“直接”：温度的最高点只可能在边界加热处。

### 5.3 唯一性（Dirichlet 直觉）

若两个调和函数在 $\partial A$ 上相同，则其差在边界为零；由最大值原理，差在内部也为零。故**边界值决定内部调和函数**（Dirichlet 问题在合适区域上解唯一）。共形映射的用途之一：把怪边界变成圆盘再求解。

---
## 6. 与 CR 的再联系

写梯度与法向：

- $\nabla u=(u_x,u_y)$
- 由 CR，$\nabla v=(-u_y,u_x)$，恰为 $\nabla u$ 旋转 $90^\circ$（逆时针）

因此沿 $v=\mathrm{const}$ 的切向与 $\nabla u$ 平行——等流线上速度势变化最快的方向，等。流体语言见下一讲。

还可写复导数：
$$
f'=u_x+iv_x=u_x-iu_y
$$
（因为 $v_x=-u_y$）。若速度势为 $u$，则速度场与 $\overline{f'}$ 相关——正是复速度 $U-iV=\Phi'$ 的由来。

---
## 7. 常见调和函数速查

| $u(x,y)$ | 对应解析 $f$（示意） | 奇点 / 定义域 |
|----------|----------------------|---------------|
| $x$ | $z$ | 整 |
| $x^2-y^2$ | $z^2$ | 整 |
| $e^x\cos y$ | $e^z$ | 整 |
| $\ln\sqrt{x^2+y^2}$ | $\log z$ | $0$；需分支 |
| $\arg$ 的一支 | $-i\log z$ 的实部相关 | 支割线 |
| $\dfrac{x}{x^2+y^2}$ | $\operatorname{Re}(1/z)$ | $0$ |

线性组合仍调和（Laplace 算子线性）；解析函数的实部虚部、以及 $\operatorname{Re}(f)$、$\operatorname{Im}(f)$、$|f|$ 一般**不**调和（$|f|$ 通常不调和），但 $\log|f|$ 在 $f\neq 0$ 处调和。

---
## 8. 自检

1. 会验证 / 使用 $\Delta u=0$；记住解析 $\Rightarrow$ $u,v$ 调和。
2. 会在单连通域上由 $u$ 积分构造共轭 $v$。
3. 理解 $u=\mathrm{const}$ 与 $v=\mathrm{const}$ 正交网格。
4. 会陈述调和函数的均值性质与最大 / 最小值原理。

> [!success]- 参考答案
> 1. $\Delta u=u_{xx}+u_{yy}=0$。解析 $f=u+iv$ $\Rightarrow$ CR + 偏导可交换 $\Rightarrow$ $u,v$ 调和。
> 2. 由 CR：$v_x=-u_y$、$v_y=u_x$，沿路径积分得 $v$（单连通保证路径无关）；差一个实常数。
> 3. $\nabla u\cdot\nabla v=0$（CR），故等势线 $u=\mathrm{const}$ 与等流线 $v=\mathrm{const}$ 正交。
> 4. 圆均值；$u$ 的最大/最小在有界域的边界取得（非常数则内点取不到）。

> [!example] 练习：找调和共轭
> $u=x^2-y^2$。验证调和，并在单连通域上求共轭 $v$（取 $v(0,0)=0$）。

> [!success]- 练习参考答案
> $\Delta u=2-2=0$。$v_x=-u_y=2y$，$v_y=u_x=2x$ $\Rightarrow$ $v=2xy+C$。$v(0,0)=0\Rightarrow C=0$，即 $v=2xy$，对应 $f=z^2$。

下一讲：二维流体——把 $u,v$ 读成速度势与流函数，用复势 $\Phi=\varphi+i\psi$ 解流场。

## 参考

- Jeremy Orloff, *18.04* harmonic functions notes, MIT OCW Spring 2018
- https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/
