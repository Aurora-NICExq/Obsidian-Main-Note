---
aliases:
  - Taylor 与 Laurent 级数
  - Taylor Series
  - Laurent Series
  - Topic 7 Taylor and Laurent
tags: [math, complex_analysis]
up: "[[Complex Analysis (MIT 18.04) MOC]]"
related:
  - "[[Analytic Functions]]"
  - "[[Residue Theorem]]"
  - "[[Cauchy's Integral Formula]]"
down: []
---
# Taylor 与 Laurent 级数

> [!summary] 核心结论
> 解析函数在解析点邻域内等于其 Taylor 幂级数（半径由最近奇点决定）。有孤立奇点时，改在**圆环**上展开成 Laurent 级数；主部（负幂项）决定奇点类型：可去 / 极点 / 本性。留数 $\operatorname{Res}=b_{-1}$（常记 $b_1$）是下一讲围道积分的唯一贡献项。

> 底本：MIT 18.04 Topic 7（Jeremy Orloff）。

---
## 1. 几何级数：CIF 的展开引擎

有限几何和：
$$
\sum_{k=0}^{n}ar^{k}=a\frac{1-r^{n+1}}{1-r}\quad(r\neq 1).
$$
$|r|<1$ 时无限和收敛：
$$
\sum_{k=0}^{\infty}r^{k}=\frac{1}{1-r}.
$$

Cauchy 积分公式里的核 $\dfrac{1}{z-w}$ 可写成几何级数。固定中心 $z_0$，对 $|w-z_0|<|z-z_0|$：
$$
\frac{1}{z-w}=\frac{1}{z-z_0}\cdot\frac{1}{1-\dfrac{w-z_0}{z-z_0}}
=\sum_{n=0}^{\infty}\frac{(w-z_0)^{n}}{(z-z_0)^{n+1}}.
$$
对 $|w-z_0|>|z-z_0|$（外区）则展开成负幂——这正是 Laurent 主部的来源。

---
## 2. 幂级数的收敛半径

幂级数
$$
\sum_{n=0}^{\infty}a_n(z-z_0)^{n}
$$
存在半径 $R\in[0,\infty]$，使得：

| 区域 | 行为 |
|------|------|
| $\|z-z_0\|<R$ | 绝对收敛，和函数解析；可逐项求导 / 沿盘内曲线积分 |
| $\|z-z_0\|>R$ | 发散 |
| $\|z-z_0\|=R$ | 定理不说话（需逐点检查） |

$R=\infty$ $\Rightarrow$ 整函数；$R=0$ $\Rightarrow$ 仅在 $z_0$ 收敛，不代表开盘上的解析函数。

### 2.1 比值 / 根值检验（工科常用）

若 $L=\lim_{n\to\infty}\bigl|\dfrac{a_{n+1}}{a_n}\bigr|$ 存在，则 $R=1/L$（约定 $L=0\Rightarrow R=\infty$，$L=\infty\Rightarrow R=0$）。根值检验类似：$R=1/\limsup|a_n|^{1/n}$。

> [!example] $e^{z}=\sum z^{n}/n!$
> $\bigl|\dfrac{a_{n+1}}{a_n}\bigr|=1/(n+1)\to 0$，故 $R=\infty$。

> [!example] $\sum z^{n}$
> $R=1$，圆盘边界恰碰到奇点 $z=1$（解析延拓后）。

**经验法则**：以 $z_0$ 为心，收敛圆盘向外扩张，直到碰到**最近的奇点**——半径等于该距离。

---
## 3. Taylor 定理（由 CIF 推出）

设 $f$ 在区域 $A$ 解析，$z_0\in A$。则在任意落在 $A$ 内的圆盘 $|z-z_0|<R$ 上，
$$
f(z)=\sum_{n=0}^{\infty}a_n(z-z_0)^{n},\qquad
a_n=\frac{f^{(n)}(z_0)}{n!}=\frac{1}{2\pi i}\oint_{C}\frac{f(w)}{(w-z_0)^{n+1}}\,dw,
$$
其中 $C$ 是盘内绕 $z_0$ 的正向简单闭曲线。

> [!note]- 证明提纲（Taylor）
> CIF 写 $f(z)=\frac{1}{2\pi i}\oint\frac{f(w)}{w-z}\,dw$；把 $\dfrac{1}{w-z}=\dfrac{1}{w-z_0}\cdot\dfrac{1}{1-\frac{z-z_0}{w-z_0}}$ 按几何级数展开，逐项积分得 $a_n=f^{(n)}(z_0)/n!$。

### 3.1 唯一性

同一圆盘上的幂级数展开唯一：系数由导数（或围道积分）完全确定。因此可用代数技巧（几何级数、已知展开的乘除）代替反复求导。

> [!example] $\operatorname{Log}(1+z)$ 在 $|z|<1$
> $$
> \frac{1}{1+z}=\sum_{n=0}^{\infty}(-1)^{n}z^{n}
> \Rightarrow
> \operatorname{Log}(1+z)=\sum_{n=1}^{\infty}(-1)^{n-1}\frac{z^{n}}{n}.
> $$
> 半径 $1$：最近奇点在 $z=-1$。

---
## 4. 零点孤立性

设 $f$ 在连通区域解析且不恒为零。若 $f(z_0)=0$，则存在阶 $m\ge 1$ 与解析且 $g(z_0)\neq 0$ 的 $g$，使
$$
f(z)=(z-z_0)^{m}g(z).
$$
于是存在去心邻域使 $f\neq 0$——**零点孤立**。

推论：

- 零点集合在区域内无聚点（除非 $f\equiv 0$）。
- 恒等式定理：两解析函数在有聚点的集合上相等 $\Rightarrow$ 处处相等。

---
## 5. Laurent 级数（圆环上的展开）

设 $f$ 在圆环
$$
r_1<|z-z_0|<r_2
$$
上解析。则
$$
f(z)=\sum_{n=1}^{\infty}\frac{b_n}{(z-z_0)^{n}}+\sum_{n=0}^{\infty}a_n(z-z_0)^{n},
$$
系数
$$
a_n=\frac{1}{2\pi i}\oint_{C}\frac{f(w)}{(w-z_0)^{n+1}}\,dw,\qquad
b_n=\frac{1}{2\pi i}\oint_{C}f(w)(w-z_0)^{n-1}\,dw,
$$
$C$ 为圆环内任一正向圆周 $|z-z_0|=\rho$（$r_1<\rho<r_2$）。

![[ca-laurent-annulus.svg]]

- **正则部（analytic part）**：$\sum a_n(z-z_0)^{n}$，在 $|z-z_0|<r_2$ 收敛。
- **主部（principal / singular part）**：$\sum b_n(z-z_0)^{-n}$，在 $|z-z_0|>r_1$ 收敛。
- 二者合起来在圆环上收敛到 $f$。

> [!tip] 工科计算
> 积分公式几乎从不直接用。常用：部分分式、已知 Taylor、几何级数、乘除已知展开。

> [!warning] 圆环选错 = 展开选错
> **不同圆环可以有不同 Laurent 展开**。谈“在 $z_0$ 的留数”必须用去心小盘 $0<|z-z_0|<r$ 上那一组 $b_1$；在大圆环上展开得到的 $1/(z-z_0)$ 系数一般**不是**该奇点的留数。

> [!example] $1/(z^{2}+1)$ 在 $0<|z-i|<2$
> $$
> \frac{1}{z^{2}+1}=\frac{1}{2i}\Bigl(\frac{1}{z-i}-\frac{1}{z+i}\Bigr).
> $$
> 对 $1/(z+i)$ 在 $z=i$ 处作几何级数；主部是 $\dfrac{1}{2i}\cdot\dfrac{1}{z-i}$。

---
## 6. 孤立奇点分类

$z_0$ 为**孤立奇点**：存在 $r>0$ 使 $f$ 在 $0<|z-z_0|<r$ 解析。该去心盘上的 Laurent 主部决定类型：

| 类型 | 主部特征 | 典型例子 |
|------|----------|----------|
| **可去（removable）** | 主部全零（无负幂） | $\sin z/z$ 在 $0$ |
| **$m$ 阶极点（pole）** | 最高负幂为 $(z-z_0)^{-m}$，$b_m\neq 0$ | $1/z^{m}$；$m=1$ 称单极点 |
| **本性（essential）** | 无穷多项负幂 | $e^{1/z}$ 在 $0$ |

等价判据（工科常用）：

- 可去 $\Leftrightarrow$ $\lim_{z\to z_0}f(z)$ 有限（定义该值后解析）。
- $m$ 阶极点 $\Leftrightarrow$ $(z-z_0)^{m}f(z)$ 在 $z_0$ 解析且非零。
- 本性：Picard 大定理——任意邻域内 $f$ 取遍 $\mathbb{C}$ 几乎所有值无穷多次（18.04 了解即可）。

> [!example] $e^{1/z}=\sum_{n=0}^{\infty}z^{-n}/n!$
> 主部无穷长 $\Rightarrow$ 本性奇点；下一讲留数是 $b_1=1$（即 $1/z$ 的系数）。

非孤立奇点例子：$\operatorname{Log} z$ 在 $0$（需要支割线）；$1/\sin(1/z)$ 在 $0$（附近有聚点奇点 $1/(n\pi)$）。

---
## 7. 留数预告：$\operatorname{Res}=b_{1}$

在孤立奇点 $z_0$ 的去心盘 Laurent 展开中，把主部写成
$$
\cdots+\frac{b_{2}}{(z-z_0)^{2}}+\frac{b_{1}}{z-z_0}+\text{正则部},
$$
定义
$$
\operatorname{Res}(f,z_0):=b_{1}.
$$
（Orloff 记法常把负幂系数写作 $b_n$，留数即 $b_1$。）

为何重要：对绕 $z_0$ 的小正向简单闭曲线 $C$，
$$
\oint_{C}f(z)\,dz=2\pi i\,b_{1},
$$
因为 $\oint(z-z_0)^{n}\,dz$ 仅当 $n=-1$ 时非零。这是**留数定理**的单奇点情形——下一讲推广到多个孤立奇点。

> [!example] $e^{1/z^{2}}=1+z^{-2}+\dfrac{1}{2}z^{-4}+\cdots$
> 无 $z^{-1}$ 项 $\Rightarrow$ $\operatorname{Res}(e^{1/z^{2}},0)=0$。

---
## 8. 自检

1. 会用比值检验估半径；记住“半径 = 到最近奇点的距离”。
2. Taylor：CIF + 几何级数；系数唯一。
3. 零点孤立；恒等式定理。
4. Laurent 在圆环；主部分类可去 / 极点 / 本性。
5. $\operatorname{Res}=b_1$；小圆积分 $=2\pi i\operatorname{Res}$。

> [!success]- 参考答案
> 1. $R=1/\limsup|a_n|^{1/n}$（或比值）；几何上 $R=$ 中心到最近奇点的距离。
> 2. 盘内解析 $\Rightarrow$ 幂级数；$a_n=f^{(n)}(z_0)/n!$；同一盘上展开唯一。
> 3. 非恒零解析函数的零点孤立；两解析函数在有聚点集上相等 $\Rightarrow$ 处处相等。
> 4. 圆环 $r_1<|z-z_0|<r_2$；主部有限长 $\Rightarrow$ 极点，全零 $\Rightarrow$ 可去，无穷长 $\Rightarrow$ 本性。
> 5. 去心盘 Laurent 的 $b_1$；$\oint=2\pi i b_1$。

> [!example] 练习：留数与奇点类型
> $f(z)=e^{1/z}/z$。在 $0$ 处属于哪类奇点？$\operatorname{Res}(f,0)=?$

> [!success]- 练习参考答案
> $e^{1/z}=\sum z^{-n}/n!$，故 $e^{1/z}/z=\sum z^{-n-1}/n!$，负幂无穷多 $\Rightarrow$ 本性。$z^{-1}$ 项来自 $n=0$：$1/z$，故 $\operatorname{Res}=1$。

## 参考

- Jeremy Orloff, *18.04 Topic 7: Taylor and Laurent series*, MIT OCW Spring 2018
- https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/
