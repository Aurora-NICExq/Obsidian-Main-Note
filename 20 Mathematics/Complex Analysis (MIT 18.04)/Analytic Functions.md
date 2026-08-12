---
aliases:
  - 解析函数
  - Analytic Functions
  - Cauchy-Riemann
  - Topic 2 Analytic Functions
tags: [math, complex_analysis]
up: "[[Complex Analysis (MIT 18.04) MOC]]"
related:
  - "[[Complex Algebra and the Complex Plane]]"
  - "[[Total Differential and the Chain Rule]]"
  - "[[Line Integrals and Cauchy's Theorem]]"
down:
  - "[[Line Integrals and Cauchy's Theorem]]"
---
# 解析函数

> [!summary] 核心结论
> 复导数 $f'(z)$ 要求极限**与路径无关**。由此推出 Cauchy–Riemann（CR）方程 $u_x=v_y$、$u_y=-v_x$；在偏导连续时 CR 亦充分。解析（analytic）= 在开集上处处复可微，且解析则“一路可微到底”。$\bar z$ 处处不可微；初等函数的导数公式与实分析同形，但定义域常因**分支 / 零点**而被挖洞。

> 底本：MIT 18.04 Topic 2（Jeremy Orloff）。

---
## 1. 复导数的定义

$$
f'(z_0)=\lim_{z\to z_0}\frac{f(z)-f(z_0)}{z-z_0}
=\lim_{\Delta z\to 0}\frac{f(z_0+\Delta z)-f(z_0)}{\Delta z},
$$
极限必须对**一切**逼近方式相同。若极限存在，称 $f$ 在 $z_0$ **解析 / 可微**；若在开区域 $A$ 上处处可微，称 $f$ 在 $A$ 上解析。

![[ca-limit-paths.svg]]

> [!example] $f(z)=z^2$
> $$
> \frac{(z_0+\Delta z)^2-z_0^2}{\Delta z}=2z_0+\Delta z\to 2z_0.
> $$

> [!example] $f(z)=\bar z$ 在 $0$ 不可微
> $$
> \frac{\overline{\Delta z}}{\Delta z}.
> $$
> 沿实轴 $\Delta y=0$ 得 $1$；沿虚轴 $\Delta x=0$ 得 $-1$。极限不存在。

![[ca-conj-not-analytic.svg]]

---
## 2. 开圆盘与区域

- **开圆盘**：$|z-z_0|<r$
- **去心开圆盘（穿孔圆盘）**：$0<|z-z_0|<r$
- **开区域**：每一点都可放入一个整段落在集合内的开圆盘

![[ca-open-disk.svg]]

极限 $\lim_{z\to z_0}f(z)=L$ 要求：沿任何趋向 $z_0$ 的序列，$f(z)\to L$。连续性：$f$ 在 $z_0$ 连续 $\Leftrightarrow$ $\lim_{z\to z_0}f(z)=f(z_0)$。

写 $f=u+iv$ 时：$f$ 连续 $\Leftrightarrow$ $u,v$ 作为二元函数连续。

常见连续例子：多项式、$e^z$ 整平面连续；主支 $\operatorname{Arg} z$、$\operatorname{Log} z$ 在挖去非正实轴后连续。

---
## 3. 无穷远点（简介）

扩充复平面 $\widehat{\mathbb{C}}=\mathbb{C}\cup\{\infty\}$。约定 $1/\infty=0$。邻域：大圆盘外部可视为 $\infty$ 的邻域（Riemann 球面北极为 $\infty$）。

$$
\lim_{z\to z_0}f(z)=\infty \iff \lim_{z\to z_0}\frac{1}{f(z)}=0.
$$

注意 $\lim_{z\to\infty}e^z$ **不存在**（方向不同结果不同）。

---
## 4. 求导法则

与实变相同（在可微处）：和、积、商、链式、反函数法则。

> [!note]- 证明提纲（积法则）
> $$
> \frac{f g-f_0 g_0}{z-z_0}
> =f\cdot\frac{g-g_0}{z-z_0}+g_0\cdot\frac{f-f_0}{z-z_0}
> \to f'(z_0)g(z_0)+f(z_0)g'(z_0).
> $$
> （商 / 链式同理：写成差商再取极限。）

定理：开圆盘上 $f'\equiv 0$ $\Rightarrow$ $f$ 为常数（后用 CR 证明）。

---
## 5. Cauchy–Riemann 方程

写 $f(z)=u(x,y)+iv(x,y)$。若 $f$ 复可微，则
$$
f'=u_x+iv_x=-i(u_y+iv_y),
$$
从而
$$
u_x=v_y,\qquad u_y=-v_x.
$$

![[ca-cr-directions.svg]]

**充分性（工科常用表述）**：若 $u,v$ 具连续偏导且满足 CR，则 $f$ 复可微。

> [!warning] CR 必要 ≠ 充分
> 可微 $\Rightarrow$ CR 恒成立；但仅有 CR、偏导不连续时，复可微可能失败。工科做题默认检查：CR + 偏导连续（或直接用已知解析函数的代数组合）。

### 5.1 用法

> [!example] $e^z$
> $u=e^x\cos y$，$v=e^x\sin y$。
> $$
> u_x=e^x\cos y=v_y,\quad u_y=-e^x\sin y=-v_x.
> $$
> CR 成立，且 $f'=u_x+iv_x=e^z$。

> [!example] $\bar z=x-iy$
> $u=x$，$v=-y$：$u_x=1\neq -1=v_y$，CR 失败，处处不可微。

常数导数定理：若 $f'\equiv 0$，则由 CR 得 $u_x=u_y=v_x=v_y=0$，故 $u,v$ 常数，$f$ 常数。

### 5.2 与 Jacobian 的联系

$f'$ 作为复数对应矩阵 $\begin{pmatrix}u_x&u_y\\ v_x&v_y\end{pmatrix}$；在 CR 下它正是 $(u,v)$ 的 Jacobian，且等于 $\begin{pmatrix}u_x&-v_x\\ v_x&u_x\end{pmatrix}$。可用此记忆 CR。

### 5.3 解析则高阶可微

若二阶偏导连续且 $f$ 解析，则 $f'$ 也满足 CR，故 $f'$ 解析——“一路可微到底”。（完整理论稍后由 Cauchy 积分公式给出：$C^\infty$ 且局部可展成幂级数。）

---
## 6. 函数画廊（定义域 · 导数）

**整函数（entire）**：在全平面解析。

| 函数 | 定义域 | 导数 |
|------|--------|------|
| $e^z$ | $\mathbb{C}$（整） | $e^z$ |
| 常数、$z^n$（$n\ge 0$）、多项式 | $\mathbb{C}$ | 同实分析 |
| $1/z$ | $\mathbb{C}\setminus\{0\}$ | $-1/z^2$ |
| 有理函数 $p/q$ | 挖掉 $q$ 的根 | 商法则 |
| $\sin z,\cos z$ | $\mathbb{C}$ | $\cos z,-\sin z$ |
| $\cosh z,\sinh z$ | $\mathbb{C}$ | $\sinh z,\cosh z$ |
| $\log z$ | 挖掉所选支割线 | $1/z$ |
| $z^a=e^{a\log z}$ | 一般挖支割；非负整数幂则整 | $a z^{a-1}$ |

定义（与实变一致）：
$$
\cos z=\frac{e^{iz}+e^{-iz}}{2},\qquad
\sin z=\frac{e^{iz}-e^{-iz}}{2i},
$$
$$
\cosh z=\frac{e^{z}+e^{-z}}{2},\qquad
\sinh z=\frac{e^{z}-e^{-z}}{2}.
$$

要点：

- $\cos^2 z+\sin^2 z=1$；$\cosh^2 z-\sinh^2 z=1$
- $\sin,\cos$ 仍以 $2\pi$ 为周期，但**无界**（虚部方向指数增长）
- $\sin z=0\Leftrightarrow z=n\pi$；$\cos z=0\Leftrightarrow z=\pi/2+n\pi$（仅实零点）
- $\cosh(iz)=\cos z$，$\sinh(iz)=i\sin z$
- $\log$ 的导数 $1/z$ 在穿孔平面解析，定义域可比 $\log$ 本身更大

直角分解（常用）：
$$
\begin{aligned}
\cos(x+iy)&=\cos x\cosh y-i\sin x\sinh y,\\
\sin(x+iy)&=\sin x\cosh y+i\cos x\sinh y.
\end{aligned}
$$

---
## 7. 复合与支割线移动

链式法则照旧，但要跟踪**分母零点**与**内层分支割线的原像**。

> [!example] $\sqrt{1-z}$（主支平方根）
> $\sqrt{w}$ 在 $w\le 0$（实）处割开。令 $w=1-z$，则割线条件 $1-z\le 0$ 且实 $\Leftrightarrow$ $z\ge 1$ 且实。故 $\sqrt{1-z}$ 在挖去射线 $[1,+\infty)$ 后解析。

![[ca-sqrt-branch-composition.svg]]

> [!example] $1/(e^z-1)$
> 分母为零当 $e^z=1\Leftrightarrow z=2\pi in$。解析于 $\mathbb{C}\setminus\{2\pi in:n\in\mathbb{Z}\}$。

---
## 8. 自检

1. 复极限“与路径无关”——这是整门课比实分析更强的起点。
2. 会写 / 验 CR，会用 $f'=u_x+iv_x$ 算导数。
3. 记住整函数与带洞定义域的典型例子；复合时会**搬移支割线**。

> [!success]- 参考答案
> 1. $f'(z_0)$ 的差商极限必须对一切逼近路径相同；$\bar z$ 沿实/虚轴得 $1$ 与 $-1$，故不可微。
> 2. $u_x=v_y$、$u_y=-v_x$；可微时 $f'=u_x+iv_x$。充分性还要偏导连续（见上文 warning）。
> 3. 整：$e^z$、多项式、$\sin/\cos$；带洞：$1/z$、$\log z$。复合 $\sqrt{1-z}$：内层割线 $w\le 0$ 拉回为 $z\ge 1$。

> [!example] 练习：CR 与定义域
> （1）用 CR 判断 $f=z\bar z$ 何处可微；（2）主支下 $\sqrt{1-z}$ 的解析域是什么？

> [!success]- 练习参考答案
> （1）$u=x^2+y^2$，$v=0$：$u_x=2x=v_y=0\Rightarrow x=0$；$u_y=2y=-v_x=0\Rightarrow y=0$。仅在 $0$ 处 CR 成立，且可直接验证差商 $\to 0$，故**仅在原点**可微（非开集上解析）。
> （2）$\sqrt{w}$ 主支割 $w\le 0$；令 $w=1-z$，得割线 $z\ge 1$（实）。解析于 $\mathbb{C}\setminus[1,+\infty)$。

下一讲：线积分与 Cauchy 定理——解析性开始“变成积分恒等式”。

## 参考

- Jeremy Orloff, *18.04 Topic 2: Analytic functions*, MIT OCW Spring 2018
- https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/
