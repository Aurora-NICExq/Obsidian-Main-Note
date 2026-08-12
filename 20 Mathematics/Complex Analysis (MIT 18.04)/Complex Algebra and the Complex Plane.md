---
aliases:
  - 复数代数与复平面
  - Complex Algebra
  - Complex Plane
  - Topic 1 Complex Algebra
tags: [math, complex_analysis]
up: "[[Complex Analysis (MIT 18.04) MOC]]"
related:
  - "[[Sinusoidal and Exponential Signals]]"
  - "[[Differential Equations and the Number e]]"
  - "[[Analytic Functions]]"
down:
  - "[[Analytic Functions]]"
---
# 复数代数与复平面

> [!summary] 核心结论
> 复数 $z=x+iy=re^{i\theta}$ 把代数（加减乘除）与几何（缩放+旋转）绑在一起；Euler 公式 $e^{i\theta}=\cos\theta+i\sin\theta$ 是枢纽。$\arg z$ 与 $\log z$ 本质多值，用时必须选定**分支**并避开**支割线**。把 $w=f(z)$ 看成平面到平面的**映射**，是后续解析函数与共形映射的视觉语言。

> 底本：MIT 18.04 Topic 1（Jeremy Orloff）。记号用数学惯例 $i$（工科电路里常写 $j$）。

---
## 1. 动机与代数基本定理

方程 $x^2=-1$ 在实数中无解。引入虚数单位 $i$，满足
$$
i^2=-1.
$$

> [!example] 解 $z^2+z+1=0$
> $$
> z=\frac{-1\pm\sqrt{1-4}}{2}=\frac{-1\pm\sqrt{3}\,i}{2}.
> $$

**代数基本定理**：次数为 $n$ 的多项式恰有 $n$ 个复根（计重数）。后续可用 Cauchy 理论给出简洁证明。

---
## 2. 术语与四则运算

### 2.1 定义

$$
z=x+iy,\qquad x,y\in\mathbb{R},\quad z\in\mathbb{C}.
$$

- 实部：$\operatorname{Re}(z)=x$
- 虚部：$\operatorname{Im}(z)=y$（是**实数**，不含 $i$）

运算只需记住 $i^2=-1$。

### 2.2 共轭、模、除法

共轭：$\overline{x+iy}=x-iy$。关键恒等式：
$$
z\bar z=|z|^2=x^2+y^2.
$$

模（绝对值 / 范数）：
$$
|z|=\sqrt{x^2+y^2}.
$$

除法：分子分母同乘分母的共轭，化成 $a+bi$。

> [!example] $\dfrac{3+4i}{1+2i}$
> $$
> \frac{3+4i}{1+2i}\cdot\frac{1-2i}{1-2i}=\frac{11-2i}{5}=\frac{11}{5}-\frac{2}{5}i.
> $$

![[ca-complex-plane.svg]]

---
## 3. 复平面与三角不等式

把 $z=x+iy$ 看成点 $(x,y)$：$x$ 轴为实轴，$y$ 轴为虚轴。加法即向量加法，故有三角不等式：
$$
|z_1|+|z_2|\ge|z_1+z_2|,
$$
等号当且仅当一方为零，或 $\arg z_1=\arg z_2$（同射线）。

![[ca-triangle-inequality.svg]]

---
## 4. 极坐标与 Euler 公式

### 4.1 极坐标

$$
r=|z|,\qquad \theta=\arg(z),
$$
且 $x=r\cos\theta$，$y=r\sin\theta$。$\theta$ 可加任意 $2\pi$ 整数倍——这是后面分支问题的根源。

### 4.2 Euler 公式（定义）

$$
e^{i\theta}:=\cos\theta+i\sin\theta.
$$

需核验它确像指数：

1. $\dfrac{d}{d\theta}e^{i\theta}=ie^{i\theta}$
2. $e^{i\cdot 0}=1$
3. $e^{i\alpha}e^{i\beta}=e^{i(\alpha+\beta)}$（用角和公式）
4. 与幂级数 $e^w=\sum w^n/n!$ 一致

### 4.3 极形式

$$
z=x+iy=r(\cos\theta+i\sin\theta)=re^{i\theta}.
$$

| 运算 | 极形式规则 |
|------|------------|
| 模 | $\|e^{i\theta}\|=1$，$|re^{i\theta}|=r$ |
| 共轭 | $\overline{re^{i\theta}}=re^{-i\theta}$ |
| 乘法 | 模相乘、辐角相加 |
| 除法 | 模相除、辐角相减 |

![[ca-polar-form.svg]]

> [!example] 乘以 $2i$
> $2i=2e^{i\pi/2}$：长度 $\times 2$，逆时针转 $90^\circ$。

![[ca-multiply-by-2i.svg]]

> [!example] $(1+i)^6$
> $1+i=\sqrt{2}\,e^{i\pi/4}$，故
> $$
> (1+i)^6=(\sqrt{2})^6 e^{i\cdot 6\pi/4}=8e^{i\cdot 3\pi/2}=-8i.
> $$
> 亦可：$(1+i)^2=2i$，再 $(2i)^3=8i^3=-8i$。

### 4.4 复化技巧（complex replacement）

计算 $\displaystyle I=\int e^{ax}\cos(bx)\,dx$ 时，令
$$
J=\int e^{ax}e^{ibx}\,dx=\int e^{(a+ib)x}\,dx,
$$
则 $I=\operatorname{Re}(J)$。极形式常比直角形式更干净。

### 4.5 $n$ 次方根

解 $w^n=z$，写 $z=re^{i(\theta+2\pi k)}$，则
$$
w=r^{1/n}\exp\!\left(i\frac{\theta+2\pi k}{n}\right),\quad k=0,1,\ldots,n-1.
$$
$n$ 个根均布在半径 $r^{1/n}$ 的圆周上。

![[ca-nth-roots.svg]]

### 4.6 逆 Euler 与 de Moivre

$$
\cos\theta=\frac{e^{i\theta}+e^{-i\theta}}{2},\qquad
\sin\theta=\frac{e^{i\theta}-e^{-i\theta}}{2i}.
$$

de Moivre：
$$
(\cos\theta+i\sin\theta)^n=\cos(n\theta)+i\sin(n\theta).
$$

### 4.7 矩阵观点（可选）

$z=x+iy$ 对应 $\begin{pmatrix}x&-y\\ y&x\end{pmatrix}$；乘法对应矩阵乘。极形式即“伸缩 × 旋转矩阵”。

---
## 5. 复指数函数 $e^z$

对 $z=x+iy$ 定义
$$
e^z=e^{x+iy}=e^x e^{iy}=e^x(\cos y+i\sin y).
$$

常用性质：$e^{z_1+z_2}=e^{z_1}e^{z_2}$，$e^z\neq 0$，以及
$$
|e^{iy}|=1,\qquad |e^{x+iy}|=e^x.
$$

路径 $t\mapsto e^{it}$（$t\in\mathbb{R}$）沿单位圆逆时针无限绕行。

![[ca-exp-unit-circle.svg]]

---
## 6. 复函数作为映射

$w=f(z)$ 需要 4 维才能“画图”，故改成：$z$-平面的点/曲线映到 $w$-平面。

### 6.1 $w=z^2$

- 射线 $\arg z=\theta$ ↦ 射线 $\arg w=2\theta$（角度加倍）
- 直径两端的射线映到同一条射线
- 上半平面（前两象限）映满整个 $w$-平面

![[ca-map-z-squared.svg]]

### 6.2 $w=e^z$

- 竖直线 $x=\mathrm{const}$ ↦ 圆周 $|w|=e^{x}$
- 水平线 $y=\mathrm{const}$ ↦ 从原点出发的射线
- 任意宽度为 $2\pi$ 的水平带映到**穿孔平面** $\mathbb{C}\setminus\{0\}$

![[ca-map-exp.svg]]

---
## 7. 辐角 $\arg z$ 的分支

$\arg z$ 多值：$\arg z=\theta_0+2\pi k$。**分支** = 选定一个区间使函数单值；**支割线** = 从定义域挖掉不连续处（通常从 $0$ 到 $\infty$ 的一条射线）。

常见选择：

| 分支 | 区间 | 支割线 |
|------|------|--------|
| 主支 $\operatorname{Arg} z$ | $(-\pi,\pi]$ | 负实轴 |
| 常用另一支 | $[0,2\pi)$ | 正实轴 |

![[ca-arg-branches.svg]]

> [!warning] 穿越支割线
> 无论怎么选，绕原点一周辐角必跳 $2\pi$。需要连续性时，定义域必须挖掉支割线。

---
## 8. 对数 $\log z$ 与复幂

### 8.1 定义

$$
\log z=\ln|z|+i\arg z
$$
（$\ln$ 为普通正实对数）。多值；选定 $\arg$ 的分支即选定 $\log$ 的分支。主支写作 $\operatorname{Log} z$（或 $\mathrm{Log}\,z$）：
$$
\operatorname{Log} z=\ln|z|+i\operatorname{Arg} z,\qquad -\pi<\operatorname{Arg} z\le\pi.
$$

性质核对：$e^{\log z}=z$（在选定分支上）。$\log 0$ 无定义。

![[ca-log-principal.svg]]

映射直觉（主支）：

- 圆周 $|z|=r$ ↦ 竖直线段 $\operatorname{Re} w=\ln r$
- 射线 $\arg z=\theta$ ↦ 水平线 $\operatorname{Im} w=\theta$
- 穿孔平面 ↦ 水平带 $-\pi<\operatorname{Im} w\le\pi$

### 8.2 复幂

$$
z^{a}:=e^{a\log z}
$$
一般多值；取主支即得主值。

> [!example] $\sqrt{i}$（主支）
> $\operatorname{Arg} i=\pi/2$，故
> $$
> i^{1/2}=e^{\frac12\operatorname{Log} i}=e^{i\pi/4}=\frac{\sqrt{2}}{2}(1+i).
> $$

---
## 9. 自检

1. 熟练直角 ↔ 极形式互化，以及乘法=缩放+旋转。
2. 会用 Euler / 逆 Euler，会算 $n$ 次方根。
3. 理解 $e^z$、$z^2$ 的映射图。
4. **分支与支割线**：后续 $\sqrt{z}$、$\log z$、多值反函数全部建立在此上。

> [!success]- 参考答案
> 1. $z=x+iy=re^{i\theta}$；乘积模相乘、辐角相加（= 缩放+旋转）。
> 2. $e^{i\theta}=\cos\theta+i\sin\theta$；逆之 $\cos\theta=(e^{i\theta}+e^{-i\theta})/2$。$n$ 次方根：$r^{1/n}e^{i(\theta+2\pi k)/n}$，$k=0,\ldots,n-1$。
> 3. $e^z$：水平线→射线、竖直线→圆周；$z^2$：辐角加倍、模平方（$1/4$ 平面→半平面等）。
> 4. $\arg/\log$ 多值；选定连续分支必须挖掉支割线；绕原点一周辐角跳 $2\pi$。

> [!example] 练习：主支方根与对数
> （1）主支下求 $\sqrt{-1}$；（2）求 $\operatorname{Log}(-1)$。说明二者与“穿越负实轴”的关系。

> [!success]- 练习参考答案
> （1）$\operatorname{Arg}(-1)=\pi$，故 $\sqrt{-1}=e^{i\pi/2}=i$（主支；另一值 $-i$ 属另一支）。
> （2）$\operatorname{Log}(-1)=\ln 1+i\pi=i\pi$。沿负实轴割线，上沿 $\operatorname{Arg}\to\pi$、下沿 $\to-\pi$，故 $\operatorname{Log}$ 在割线两侧差 $2\pi i$。

## 参考

- Jeremy Orloff, *18.04 Topic 1: Complex algebra and the complex plane*, MIT OCW Spring 2018
- 课程主页：https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/
