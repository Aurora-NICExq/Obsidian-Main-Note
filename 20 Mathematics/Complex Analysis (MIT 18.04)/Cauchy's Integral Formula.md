---
aliases:
  - Cauchy 积分公式
  - Cauchy's Integral Formula
  - CIF
  - Topic 4 Cauchy Integral Formula
tags: [math, complex_analysis]
up: "[[Complex Analysis (MIT 18.04) MOC]]"
related:
  - "[[Line Integrals and Cauchy's Theorem]]"
  - "[[Analytic Functions]]"
  - "[[Harmonic Functions]]"
down: []
---
# Cauchy 积分公式

> [!summary] 核心结论
> 若 $f$ 在简单闭围道 $C$ 内部及边界上解析，$z_0$ 在内部，则
> $$
> f(z_0)=\frac{1}{2\pi i}\oint_C\frac{f(z)}{z-z_0}\,dz.
> $$
> 对 $z$ 求导得高阶公式：$f$ 自动 $C^\infty$，且导数仍由围道积分给出。配合 ML 估计推出 Cauchy 估计、Liouville（有界整函数为常数）与代数基本定理。均值性质与最大模原理是解析函数的“刚性”体现。

> 底本：MIT 18.04 Topic 4（Jeremy Orloff）。工科重点：会套 CIF / 导数 CIF 算围道积分；理解“解析 $\Rightarrow$ 无穷可微”；会用 Liouville 证 FTA。

---
## 1. Cauchy 积分公式（CIF）

### 1.1 陈述

设 $C$ 为（正定向）简单闭围道，$f$ 在 $C$ 上及其内部解析，$z_0$ 在 $C$ 内部。则
$$
f(z_0)=\frac{1}{2\pi i}\oint_C\frac{f(z)}{z-z_0}\,dz,
$$
或
$$
\oint_C\frac{f(z)}{z-z_0}\,dz=2\pi i\,f(z_0).
$$

> [!warning] 点必须在“内部”
> CIF 要求 $z_0$ 在 $C$ 内部且 $f$ 在闭围道及其内部解析。$z_0$ 在外部时左侧积分为 $0$（被积对 $z$ 解析）；漏掉 $2\pi i$ 或把定向弄反是常见算术错。

![[ca-cif.svg]]

### 1.2 直觉

把 $C$ 变形到以 $z_0$ 为心的小圆 $|z-z_0|=\varepsilon$。在小圆上 $z=z_0+\varepsilon e^{i\theta}$，$dz=i\varepsilon e^{i\theta}\,d\theta$，
$$
\oint\frac{f(z)}{z-z_0}\,dz
=\int_0^{2\pi}f(z_0+\varepsilon e^{i\theta})\,i\,d\theta
\to 2\pi i\,f(z_0)\quad(\varepsilon\to 0),
$$
因为 $f$ 连续。变形合法是因为 $f(z)/(z-z_0)$ 在两圆之间的环域上解析（奇点只在 $z_0$）。

### 1.3 立刻能算的积分

> [!example] $\displaystyle\oint_{|z|=2}\dfrac{e^z}{z-1}\,dz$
> $f(z)=e^z$ 整，$z_0=1$ 在圆内 $\Rightarrow$ 积分 $=2\pi i\,e$。

> [!example] $\displaystyle\oint_{|z|=1}\dfrac{\cos z}{z}\,dz$
> $=2\pi i\cos 0=2\pi i$。

> [!example] 奇点在外
> $\displaystyle\oint_{|z|=1}\dfrac{e^z}{z-2}\,dz=0$（被积函数在闭圆盘上解析，Cauchy 定理）。

---
## 2. 导数的 CIF

在 CIF 下可对 $z_0$ 求导（积分号下求导，工科课程通常直接使用）：
$$
f'(z_0)=\frac{1}{2\pi i}\oint_C\frac{f(z)}{(z-z_0)^2}\,dz,
$$
$$
f^{(n)}(z_0)=\frac{n!}{2\pi i}\oint_C\frac{f(z)}{(z-z_0)^{n+1}}\,dz.
$$
等价写法：
$$
\oint_C\frac{f(z)}{(z-z_0)^{n+1}}\,dz=\frac{2\pi i}{n!}\,f^{(n)}(z_0).
$$

> [!example] $\displaystyle\oint_{|z|=1}\dfrac{\sin z}{z^2}\,dz$
> $=2\pi i\cdot(\sin z)'|_{0}=2\pi i\cos 0=2\pi i$。

> [!example] $\displaystyle\oint_{|z|=2}\dfrac{e^z}{(z-1)^3}\,dz$
> $n=2$，$f=e^z$，$z_0=1$：
> $$
> =\frac{2\pi i}{2!}\,e^1=\pi i\,e.
> $$

### 2.1 无穷可微

解析函数不仅有一阶复导数，而且**任意阶**导数都存在且仍解析（“一路可微到底”）。这比实分析强得多：实函数可微不必二阶可微；复解析则自动 $C^\infty$，且局部可展成幂级数（Taylor 专题）。

---
## 3. ML 估计（长度估计）

### 3.1 不等式

若在路径 $\gamma$ 上 $|f(z)|\le M$，且 $\gamma$ 长度为 $L$，则
$$
\left|\int_\gamma f(z)\,dz\right|\le M L.
$$
证明骨架：$|\int f\gamma'\,dt|\le\int |f||\gamma'|\,dt\le M\int|\gamma'|\,dt=ML$。

### 3.2 用途

- 估计积分上界（数值 / 证明中“让半径 $\to\infty$ 或 $\to 0$”）
- 推导 Cauchy 估计与 Liouville

> [!example] 大圆上的衰减
> 若 $|f(z)|\le K/|z|^2$ 在 $|z|=R$ 上，则
> $$
> \left|\oint_{|z|=R}f\,dz\right|\le \frac{K}{R^2}\cdot 2\pi R=\frac{2\pi K}{R}\to 0\quad(R\to\infty).
> $$

---
## 4. Cauchy 估计

取 $C$ 为圆 $|z-z_0|=R$，并设在圆上 $|f|\le M$。由导数 CIF：
$$
\big|f^{(n)}(z_0)\big|
=\left|\frac{n!}{2\pi i}\oint_C\frac{f(z)}{(z-z_0)^{n+1}}\,dz\right|
\le\frac{n!}{2\pi}\cdot\frac{M}{R^{n+1}}\cdot 2\pi R
=\frac{n!\,M}{R^n}.
$$
即
$$
\big|f^{(n)}(z_0)\big|\le\frac{n!\,M}{R^n}.
$$

> [!tip] 读法
> 圆越大（$R$ 大）或函数在圆上越小（$M$ 小），中心处导数越小。整函数若全局有界，则所有 $n\ge 1$ 的导数在每点为零——这就是 Liouville。

---
## 5. Liouville 定理与代数基本定理

### 5.1 Liouville

**有界整函数必为常数。**

> [!note]- 证明提纲（Liouville）
> 全局 $|f|\le M$。Cauchy 估计 $n=1$：$|f'(z_0)|\le M/R$，对任意 $R$。令 $R\to\infty$ 得 $f'(z_0)=0$；点任意 $\Rightarrow f'\equiv 0\Rightarrow f$ 常数。

> [!example] $e^z$ 无界
> $|e^{x+iy}|=e^x$，沿正实轴可任意大——与“非常数整函数”一致。$\sin z$、多项式（次数 $\ge 1$）同样无界。

### 5.2 代数基本定理（FTA）

次数 $n\ge 1$ 的多项式 $p(z)=a_n z^n+\cdots+a_0$（$a_n\neq 0$）在 $\mathbb{C}$ 中至少有一根。

> [!tip] 反证法（经典）
> 若 $p$ 无根，则 $f=1/p$ 为整函数。又 $|z|\to\infty$ 时 $|p(z)|\to\infty$，故 $f$ 在无穷远处趋于 $0$，从而 $f$ 有界。Liouville $\Rightarrow f$ 常数 $\Rightarrow p$ 常数，矛盾。

由此用因式分解可推出恰有 $n$ 个根（计重数）——与 Topic 1 的宣言闭合。

---
## 6. 均值性质（Mean Value）

在 CIF 中取 $C:|z-z_0|=R$，参数化得
$$
f(z_0)=\frac{1}{2\pi}\int_0^{2\pi}f(z_0+Re^{i\theta})\,d\theta.
$$
即：$f(z_0)$ 等于圆周上的**平均值**。

对实部 $u=\operatorname{Re}f$ 取实部，得调和函数的均值性质（见 [[Harmonic Functions]]）。

---
## 7. 最大模原理（Maximum Modulus）

### 7.1 陈述

设 $f$ 在有界区域 $A$ 上解析，在闭包 $\overline{A}$ 上连续。则 $|f|$ 的最大值在**边界** $\partial A$ 上取得。若 $f$ 非常数，则 $|f|$ 在 $A$ 内部取不到最大值。

等价：非常数解析函数的模不能在内点有局部最大。

### 7.2 直觉与推论

- 来自均值性质：若内点 $|f(z_0)|$ 最大，则圆周上 $|f|$ 只能处处等于 $|f(z_0)|$，再推 $f$ 常数。
- **最小模**：若 $f$ 在 $A$ 上无零点，则 $1/f$ 解析，从而 $|f|$ 的最小值也在边界（除非 $f$ 常数）。
- 工程味道：解析函数的“峰值”只能在定义域边缘——类似静电学中调和势的极值原理。

> [!example] 单位圆盘上的 $f(z)=z$
> $|f|$ 在内部 $<1$，在边界 $|z|=1$ 上达到 $1$。

> [!example] 用最大模估上界
> 若在 $|z|\le R$ 上 $|f|\le M$，则对 $|z_0|<R$ 有 $|f(z_0)|\le M$；更细的定量靠 Schwarz 引理等（后续共形映射）。

---
## 8. 与 Cauchy 定理的关系小结

| 工具 | 典型结论 |
|------|----------|
| Cauchy 定理 | 内部无奇点 $\Rightarrow\oint=0$ |
| CIF | $\oint f/(z-z_0)\,dz=2\pi i f(z_0)$ |
| 导数 CIF | $\oint f/(z-z_0)^{n+1}\,dz=2\pi i f^{(n)}(z_0)/n!$ |
| ML / Cauchy 估计 | 积分与导数的上界 |
| Liouville | 有界整函数 $\Rightarrow$ 常数；$\Rightarrow$ FTA |
| 均值 / 最大模 | 解析函数的刚性 |

计算围道积分时：先看能否化成 CIF 标准形（分子在围道内解析，分母是 $(z-z_0)^{k}$）。多奇点时需部分分式或留数定理（后续专题）。

---
## 9. 自检

1. 会陈述并应用 CIF 与导数 CIF 计算标准围道积分。
2. 理解解析 $\Rightarrow$ $C^\infty$（及后续幂级数）。
3. 会写 ML 估计与 Cauchy 估计；能用 Liouville 推 FTA。
4. 记住均值性质与最大模原理的结论（不必先啃完证明细节）。

> [!success]- 参考答案
> 1. $\oint f/(z-z_0)\,dz=2\pi i f(z_0)$（$z_0$ 在内）；高阶 $\oint f/(z-z_0)^{n+1}=2\pi i f^{(n)}(z_0)/n!$。
> 2. 导数 CIF 对一切 $n$ 成立 $\Rightarrow$ 解析函数无穷可微；进一步局部幂级数展开。
> 3. $|\int|\le ML$；$|f^{(n)}(z_0)|\le n!\,M/R^n$。有界整 $\Rightarrow$ 常数（Liouville）；若 $p$ 无根则 $1/p$ 有界整 $\Rightarrow$ 常数，得 FTA。
> 4. 圆均值：$f(z_0)$ 等于圆周平均。最大模：非常数解析 $|f|$ 内点取不到最大，最大在边界。

> [!example] 练习：套 CIF
> 计算 $\displaystyle\oint_{|z|=2}\dfrac{e^z}{z-1}\,dz$。

> [!success]- 练习参考答案
> $e^z$ 整，$z=1$ 在 $|z|<2$ 内：直接 CIF 得 $2\pi i\,e^{1}=2\pi i e$。

下一讲：调和函数——解析函数的实部 / 虚部满足 Laplace 方程。

## 参考

- Jeremy Orloff, *18.04 Topic 4: Cauchy's integral formula*, MIT OCW Spring 2018
- https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/
