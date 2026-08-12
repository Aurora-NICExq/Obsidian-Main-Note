---
aliases:
  - 共形变换
  - Conformal Maps
  - Möbius Transformations
  - Topic 11 Conformal Transformations
tags: [math, complex_analysis]
up: "[[Complex Analysis (MIT 18.04) MOC]]"
related:
  - "[[Analytic Functions]]"
  - "[[Harmonic Functions]]"
  - "[[Two-Dimensional Hydrodynamics and Complex Potentials]]"
down: []
---
# 共形变换

> [!summary] 核心结论
> 共形 = 保定向角。$f$ 解析且 $f'(z_0)\neq 0$ $\Rightarrow$ 在 $z_0$ 局部共形（切向量乘以复数 $f'(z_0)$ = 缩放 + 旋转）。Möbius（分式线性）把圆/直线映成圆/直线，并实现 UHP $\leftrightarrow$ 单位圆盘。常用映射画廊：$az+b$、$1/z$、$e^{z}$、$z^{2}$、$z+1/z$。边界上给定 Dirichlet 数据时，可先共形拉直再分离变量；二维流里复势经共形拉回（Milne–Thomson 等）。

> 底本：MIT 18.04 Topic 11（Jeremy Orloff）。

---
## 1. 共形的定义

映射 $f:U\to\mathbb{C}$ 在 $z_0$ 处**共形（conformal）**：它把过 $z_0$ 的光滑曲线的切向夹角（含定向）保持不变。

几何图像：局部上看，$f$ 是相似变换——只缩放与旋转，不剪切。

![[ca-conformal-local.svg]]

反共形（如 $\bar z$）保角但**反转定向**。

---
## 2. 解析 + $f'\neq 0$ $\Rightarrow$ 共形

设 $f$ 在 $z_0$ 解析且 $f'(z_0)\neq 0$。对过 $z_0$ 的曲线 $z(t)$，
$$
\frac{d}{dt}f(z(t))=f'(z(t))z'(t).
$$
在 $z_0$：像切向量 = 原切向量乘以复数 $f'(z_0)$。乘法 = 模 $|f'|$ 缩放 + 辐角 $\arg f'$ 旋转，故两曲线夹角不变且定向保持。

推论：

- $f'\neq 0$ 的解析映射局部一一（反函数定理）。
- $f'(z_0)=0$ 时一般**不**共形：例如 $z\mapsto z^{2}$ 在 $0$ 把角加倍。

> [!warning] $f'=0$ 处不是共形点
> 解析只保证局部共形当且仅当 $f'\neq 0$。在临界点（如 $z^2$ 的原点、$z+1/z$ 的 $\pm 1$）角度被拉伸/折叠，边界对应要单独检查。

> [!tip] CR 视角
> $f'$ 对应的实 Jacobian 是旋转–缩放矩阵 $\begin{pmatrix}u_x&-v_x\\ v_x&u_x\end{pmatrix}$（在 CR 下），行列式 $|f'|^{2}>0$。

---
## 3. Möbius 变换（分式线性变换）

一般形
$$
w=T(z)=\frac{az+b}{cz+d},\qquad ad-bc\neq 0.
$$
（乘以常数不改变映射；可把矩阵 $\begin{pmatrix}a&b\\ c&d\end{pmatrix}$ 归一到行列式 $1$。）

性质：

1. 在 $\widehat{\mathbb{C}}=\mathbb{C}\cup\{\infty\}$ 上是双射；逆仍是 Möbius。
2. 组成群（复合 = 矩阵乘）。
3. **圆/直线定理**：广义圆（圆或直线）映成广义圆。
4. 交比不变；三点决定唯一把它们映到另三点的 Möbius。

特殊情形：

| 形式 | 几何 |
|------|------|
| $az+b$ | 相似：旋转、缩放、平移 |
| $1/z$ | 反演 + 共轭意义下的“圆线互换”（单位圆内外对换） |
| $\dfrac{z-z_1}{z-z_2}$ | 把 $z_1\mapsto 0$、$z_2\mapsto\infty$ |

### 3.1 上半平面 $\leftrightarrow$ 单位圆盘

标准映射
$$
w=\frac{z-i}{z+i}
$$
把上半平面 $\operatorname{Im}z>0$ 映到单位圆盘 $|w|<1$，实轴映到单位圆周，且 $i\mapsto 0$。

![[ca-mobius-uhp-disk.svg]]

逆映射：
$$
z=i\frac{1-w}{1+w}.
$$
一般地，把 UHP 映到单位圆盘且把 $z_0$（$\operatorname{Im}z_0>0$）送到 $0$ 的映射是
$$
e^{i\theta}\frac{z-z_0}{z-\bar z_0}.
$$

验证实轴：$\operatorname{Im}z=0\Rightarrow |z-i|=|z+i|\Rightarrow |w|=1$。

---
## 4. 映射画廊

### 4.1 $w=az+b$

平面的刚体–相似运动：先乘 $a$（转 $\arg a$、缩 $|a|$），再平移 $b$。把直线映直线、圆映圆。

### 4.2 $w=1/z$

极坐标：$re^{i\theta}\mapsto r^{-1}e^{-i\theta}$。单位圆内外互换；过 $0$ 的直线 $\leftrightarrow$ 过 $\infty$ 的直线；不过 $0$ 的圆 $\leftrightarrow$ 圆。常与平移组合成“把圆映成直线”的工具。

### 4.3 $w=e^{z}$

$z=x+iy\mapsto e^{x}e^{iy}$：水平带 $0<\operatorname{Im}z<\alpha$ 映成张角 $\alpha$ 的扇形；竖直线映成圆周。周期 $2\pi i$，故带域宽 $>2\pi$ 时不再单叶。

![[ca-map-exp.svg]]

### 4.4 $w=z^{2}$

$re^{i\theta}\mapsto r^{2}e^{i2\theta}$：角加倍。右半平面映到挖去负实轴的平面；第一象限映到上半平面。在 $0$ 处 $f'=0$，不共形。

![[ca-map-z-squared.svg]]

### 4.5 $w=z+1/z$（Joukowski）

单位圆外部（或内部）可映成机翼剖面型曲线；实轴区间 $[-2,2]$ 外的椭圆/双曲线族是经典图像。流动问题里把绕圆柱的流拉成绕翼型的流。

> [!example] 组合拳
> 要解半平面上的边值问题：先 Möbius 拉到单位圆盘，再分离变量或 Poisson 核；或把多边形用 Schwarz–Christoffel（了解即可）拉到半平面。

---
## 5. Dirichlet 问题与辐角组合（简介）

平面区域 $\Omega$ 上 Laplace 方程 $\Delta u=0$，边界 $\partial\Omega$ 给 $u|_{\partial\Omega}=g$，称 **Dirichlet 问题**。二维时调和 $u$ 是某解析 $f=u+iv$ 的实部（单连通且适当正则时）。

共形映射的用法：

1. 找共形 $\varphi:\Omega\to\mathbb{D}$（或 UHP）。
2. 把边界数据推到标准区域，解标准 Dirichlet（圆盘 Poisson 公式 / 半平面）。
3. 拉回：$u=u_{\text{std}}\circ\varphi$。

**辐角构造**：若边界由若干射线/圆弧组成，且边界值分段常数，常取
$$
u(z)=A+B\operatorname{Arg}(z-z_{1})+C\operatorname{Arg}(z-z_{2})+\cdots
$$
或 $\operatorname{Arg}\bigl(\dfrac{z-a}{z-b}\bigr)$（两射线之间的调和函数）。$\operatorname{Arg}$ 沿支割跳跃 $\pi$ 或 $2\pi$，正好匹配分段常数边界。

---
## 6. 复势与 Milne–Thomson（点到为止）

二维不可压无旋流：复势 $w(z)=\phi+i\psi$（$\phi$ 速度势，$\psi$ 流函数），速度 $\overline{w'(z)}$。共形映射 $\zeta=\varphi(z)$ 下，若在 $\zeta$ 平面有复势 $W(\zeta)$，则
$$
w(z)=W(\varphi(z))
$$
给出 $z$ 平面流（流线 $\psi=\mathrm{const}$ 被拉回）。

**Milne–Thomson 圆定理**：在均匀流等已知流中插入圆柱 $|z|=a$，可通过
$$
w(z)=f(z)+\overline{f(a^{2}/\bar z)}
$$
（$f$ 为无柱时的复势，在柱外解析）自动让圆周成为流线。与 $z+a^{2}/z$ 型映射密切相关——共形把“直线边界”思想搬到圆上。

细节见 [[Two-Dimensional Hydrodynamics and Complex Potentials]]。

---
## 7. 自检

1. 共形 = 保定向角；$f$ 解析且 $f'\neq 0$ 则局部共形。
2. Möbius：圆/直线定理；UHP $\leftrightarrow$ 盘用 $(z-i)/(z+i)$。
3. 画廊：$az+b$、$1/z$、$e^{z}$、$z^{2}$、$z+1/z$ 的区域对应。
4. Dirichlet：共形拉到标准域；分段常数边界可用 $\operatorname{Arg}$ 组合。
5. 复势在共形下复合；Milne–Thomson 是圆边界的标准招。

> [!success]- 参考答案
> 1. 切向量乘以 $f'(z_0)$ = 缩放+旋转；需 $f'\neq 0$。
> 2. Möbius 保广义圆；$(z-i)/(z+i)$ 把上半平面映到单位盘（或逆映射）。
> 3. 平移旋转缩放；$1/z$ 反演；$e^z$ 带→扇/半平面；$z^2$ 角加倍；$z+1/z$ 圆柱绕流经典形。
> 4. 先映到圆盘/半平面再分离变量；分段常值边界常用 $\operatorname{Arg}((z-a)/(z-b))$。
> 5. $w(z)=W(\varphi(z))$；Milne–Thomson 用 $f(z)+\overline{f(a^2/\bar z)}$ 强制圆周为流线。

> [!example] 练习：是否共形
> $f(z)=z^2$ 在 $z=1$ 与 $z=0$ 是否局部共形？简述理由。

> [!success]- 练习参考答案
> $f'=2z$：$z=1$ 处 $f'\neq 0$，局部共形；$z=0$ 处 $f'=0$，角加倍，不共形。

## 参考

- Jeremy Orloff, *18.04 Topic 11: Conformal transformations*, MIT OCW Spring 2018
- https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/
