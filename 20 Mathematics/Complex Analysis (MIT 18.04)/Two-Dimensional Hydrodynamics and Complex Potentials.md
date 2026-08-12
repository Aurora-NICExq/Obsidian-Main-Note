---
aliases:
  - 二维流体与复势
  - Complex Potentials
  - Two-Dimensional Hydrodynamics
  - 复势
  - Topic Hydrodynamics
tags: [math, complex_analysis]
up: "[[Complex Analysis (MIT 18.04) MOC]]"
related:
  - "[[Harmonic Functions]]"
  - "[[Analytic Functions]]"
  - "[[Complex Algebra and the Complex Plane]]"
  - "[[Cauchy's Integral Formula]]"
down: []
---
# 二维流体与复势

> [!summary] 核心结论
> 二维不可压（incompressible）且无旋（irrotational）流存在速度势 $\varphi$ 与流函数 $\psi$，二者调和且满足 CR，故复势 $\Phi=\varphi+i\psi$ 解析。复速度满足
> $$
> \Phi'(z)=U-iV,
> $$
> 其中 $(U,V)$ 为速度场；流线即 $\psi=\mathrm{const}$。基本积木：均匀流、源汇 $\propto\log z$、涡旋 $\propto -i\log z$、拐角 / 停滞流 $\propto z^n$，再叠加。正交网格 $\varphi,\psi$ 与 [[Harmonic Functions]] 完全同一套几何。

> 底本：MIT 18.04（Orloff）二维流体与复势。工科重点：从 $\Phi$ 读出速度与流线；会叠加热门基本解。

---
## 1. 二维理想流的假设

平面速度场 $\mathbf{v}=(U(x,y),V(x,y))$。

### 1.1 不可压

$$
\nabla\cdot\mathbf{v}=U_x+V_y=0.
$$
（体积守恒 / 密度恒定。）

### 1.2 无旋

$$
\nabla\times\mathbf{v}\ \text{的}z\text{分量}=V_x-U_y=0.
$$
（有速度势：$\mathbf{v}=\nabla\varphi$。）

在单连通流场区域上，不可压 + 无旋 $\Rightarrow$ 存在 $\varphi,\psi$ 满足
$$
U=\varphi_x=\psi_y,\qquad V=\varphi_y=-\psi_x,
$$
即 $\varphi,\psi$ 满足 CR，且
$$
\Delta\varphi=0,\qquad\Delta\psi=0.
$$
于是
$$
\Phi(z):=\varphi(x,y)+i\psi(x,y)
$$
为**复势（complex potential）**，在流场区域内解析（奇点除外：源、涡等）。

![[ca-harmonic-orthogonal.svg]]

---
## 2. 复速度公式

由 CR 与 $\Phi'=\varphi_x+i\psi_x$，
$$
\Phi'(z)=\varphi_x+i\psi_x=U+i(-V)=U-iV.
$$
因此
$$
U-iV=\Phi'(z),\qquad
U=\operatorname{Re}\Phi',\quad
V=-\operatorname{Im}\Phi'.
$$
也常写 $\overline{\Phi'(z)}=U+iV$（共轭后直接得到速度向量的复形式）。

> [!tip] 计算步骤
> 1. 写出 $\Phi(z)$
> 2. 求导 $\Phi'(z)$
> 3. 读出 $U-iV$，或写 $U+iV=\overline{\Phi'(z)}$
> 4. 流线：解 $\psi=\operatorname{Im}\Phi=\mathrm{const}$；等势线：$\varphi=\operatorname{Re}\Phi=\mathrm{const}$

速度大小 $|\mathbf{v}|=|\Phi'(z)|$。停滞点（stagnation）：$\Phi'(z)=0$。

---
## 3. 流线与流量

- **流线（streamline）**：$\psi=\mathrm{const}$。流体质点轨迹（稳态）与流线重合；速度切于流线。
- **等势线**：$\varphi=\mathrm{const}$，与流线正交（$\Phi$ 解析且 $\Phi'\neq 0$ 处）。
- 两条流线 $\psi=c_1$、$c_2$ 之间的流量（单位厚度）为 $|c_2-c_1|$（适当定向）。

固壁边界：取为一条流线（$\psi=\mathrm{const}$），因为流体不能穿过壁面。

---
## 4. 基本流场画廊

![[ca-flow-gallery.svg]]

### 4.1 均匀流（uniform flow）

$$
\Phi(z)=Az,\qquad A>0\text{ 实}\quad\Rightarrow\quad
\Phi'=A,\quad U=A,\ V=0.
$$
流线：水平直线 $\psi=Ay=\mathrm{const}$。更一般 $A=Ue^{-i\alpha}$ 给出与实轴夹角 $\alpha$ 的均匀流。

### 4.2 源 / 汇（source / sink）：$\log z$

取主支或在挖支割线的平面上，
$$
\Phi(z)=k\log z=k\ln r+ik\theta,\qquad k\in\mathbb{R}.
$$
- $\varphi=k\ln r$：等势线为同心圆
- $\psi=k\theta$：流线为从原点出发的射线
- $\Phi'=k/z$ $\Rightarrow$ 速度径向，$|\mathbf{v}|=|k|/r$

$k>0$ 为源，$k<0$ 为汇。绕原点一小圆的流量 $\propto 2\pi k$（与辐角跳变一致）。原点是奇点。

### 4.3 涡旋（vortex）：$-i\log z$

$$
\Phi(z)=-i\kappa\log z=\kappa\theta-i\kappa\ln r
$$
（$\kappa$ 实；符号约定因教材而异，这里取一种常见形）。
- 流线：$\psi=-\kappa\ln r=\mathrm{const}$ $\Rightarrow$ 同心圆
- 等势线：射线
- 速度沿圆周切向，$|\mathbf{v}|\propto 1/r$

环量与 $\kappa$ 相关；原点仍是奇点。源与涡的线性组合给出螺旋流线（对数螺线）。

### 4.4 停滞流 / 拐角流：$z^2$（及 $z^n$）

$$
\Phi(z)=z^2= (x^2-y^2)+i(2xy).
$$
- 流线 $xy=\mathrm{const}$（双曲线）
- $\Phi'=2z=0$ 于原点 $\Rightarrow$ **停滞点**
- 正实、正虚轴附近可理解为直角拐角内的流（壁取为流线 $xy=0$）

更一般 $\Phi=z^{n}$ 或 $\Phi=z^{\pi/\alpha}$ 描述张角为 $\alpha$ 的楔形拐角流（需分支）。

### 4.5 偶极子（dipole）预告

$$
\Phi(z)=\frac{\mu}{z}
$$
可视为源汇对靠近后的极限；流线是过原点的圆族。绕圆柱的均匀流经典解含均匀流 + 偶极子（及可选环量项）。

---
## 5. 叠加原理

Laplace / 解析在线性运算下封闭：若干复势相加仍为复势，速度场叠加。

> [!example] 均匀流 + 源
> $$
> \Phi(z)=Az+k\log z.
> $$
> 远处近似均匀流；原点附近源主导。可画出被“吹偏”的流线。

> [!example] 均匀流绕圆柱（经典形，无环量）
> $$
> \Phi(z)=U\left(z+\frac{a^2}{z}\right),\qquad |z|>a.
> $$
> 在 $|z|=a$ 上 $\psi=0$（圆柱为流线）。$\Phi'=U(1-a^2/z^2)$，停滞点 $z=\pm a$。这是共形映射 / 镜像思想的流体版。

> [!example] 加环量
> $$
> \Phi(z)=U\left(z+\frac{a^2}{z}\right)-i\kappa\log z.
> $$
> 停滞点移动；$\kappa$ 足够大时两停滞点在圆柱上合并再离开——与升力（Kutta–Joukowski）叙事衔接。

---
## 6. 与调和 / 共形的接口

| 复分析对象 | 流体读法 |
|------------|----------|
| $\varphi=\operatorname{Re}\Phi$ | 速度势 |
| $\psi=\operatorname{Im}\Phi$ | 流函数 |
| $\varphi,\psi$ 调和 + CR | 不可压 + 无旋 |
| $\Phi'$ | 给出 $U-iV$ |
| $\Phi'\neq 0$ 处保角 | 等势线 ⊥ 流线 |
| $\log z$、$-i\log z$、$z^n$ | 源、涡、拐角积木 |
| 共形映射 $w=f(z)$ | 把简单流搬到复杂几何（后续专题） |

边界值问题：在固壁上指定 $\psi=\mathrm{const}$，在远场指定均匀流，等——先猜积木叠加，再靠共形映射系统化。

---
## 7. 注意事项（工科易错）

1. **多值**：$\log z$ 的虚部是 $\arg$；跨支割线 $\psi$ 跳变对应源的流量。物理上常在剖开的平面上取单值支。
2. **奇点**：源、涡、偶极子处模型破裂；真实流体有核或粘性区。
3. **停滞点**：$\Phi'=0$ 处正交网格图像“坏掉”，局部像 $z^2$ 映射。
4. **三维 / 有旋 / 可压**：本课框架不适用；这是二维理想流的专用语言。
5. **符号约定**：$U-iV=\Phi'$ 与 $\overline{\Phi'}=U+iV$ 等价；写清即可，勿混用。

> [!warning] $U-iV$ 还是 $\overline{\Phi'}$？
> 速度场 $(U,V)$ 满足 $U-iV=\Phi'$（本课约定）。写成 $\overline{\Phi'}$ 时得到 $U+iV$——同一物理场的两种打包方式。混用两种约定会把环量/源强符号搞反。

---
## 8. 自检

1. 记住不可压 + 无旋 $\Rightarrow$ 复势 $\Phi=\varphi+i\psi$ 解析，且 $\Phi'=U-iV$。
2. 会从 $\Phi$ 读流线（$\psi=\mathrm{const}$）与速度。
3. 会默写均匀流、源 $\log z$、涡 $-i\log z$、停滞流 $z^2$，并理解叠加。
4. 把正交网格图与 [[Harmonic Functions]] 对照；为共形映射绕流做准备。

> [!success]- 参考答案
> 1. 不可压 $\Rightarrow\Delta\varphi=0$（或等价散度为零）；无旋 $\Rightarrow$ 有势。合起来 $\Phi=\varphi+i\psi$ 解析，$\Phi'=U-iV$。
> 2. 流线 = $\psi$ 水平集；速度由 $\Phi'$ 读出；固壁常取为一条流线。
> 3. 均匀流 $Az$；源 $k\log z$；涡 $-i\kappa\log z$；拐角/停滞 $z^n$。线性叠加仍为复势。
> 4. $\varphi,\psi$ 调和共轭 $\Leftrightarrow$ 正交网格；共形映射把简单流拉到复杂边界。

> [!example] 练习：读速度
> $\Phi(z)=U(z+a^2/z)$（$|z|>a$）。求 $\Phi'$，并指出停滞点。

> [!success]- 练习参考答案
> $\Phi'=U(1-a^2/z^2)=0\Rightarrow z=\pm a$（在圆柱上）。这是无环量绕圆柱的经典复势。

后续：Taylor / Laurent、留数——把“奇点贡献”算成积分；共形映射专门搬边界。

## 参考

- Jeremy Orloff, *18.04* two-dimensional hydrodynamics / complex potentials, MIT OCW Spring 2018
- https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/
