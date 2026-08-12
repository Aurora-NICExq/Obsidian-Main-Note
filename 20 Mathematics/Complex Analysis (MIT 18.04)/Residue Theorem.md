---
aliases:
  - 留数定理
  - Residue Theorem
  - Residues
  - Topic 8 Residue Theorem
tags: [math, complex_analysis]
up: "[[Complex Analysis (MIT 18.04) MOC]]"
related:
  - "[[Taylor and Laurent Series]]"
  - "[[Definite Integrals Using Residues]]"
  - "[[Cauchy's Integral Formula]]"
down: []
---
# 留数定理

> [!summary] 核心结论
> 孤立奇点处 $\operatorname{Res}(f,z_0)=b_{-1}$（Laurent 的 $1/(z-z_0)$ 系数）。单极点有极限 / $p/q$ / $1/g'$ 等快速公式；高阶极点用 $g^{(m-1)}(z_0)/(m-1)!$。Cauchy 留数定理：正向简单闭曲线上的积分 $=2\pi i\sum$ 内部留数。有限个奇点时还可用**无穷远留数**一次算完。

> 底本：MIT 18.04 Topic 8（Jeremy Orloff）。

---
## 1. 术语回顾：零点、极点、亚纯

- **$m$ 阶零点**：$f(z)=(z-z_0)^{m}g(z)$，$g$ 解析且 $g(z_0)\neq 0$。
- **$m$ 阶极点**：Laurent 最高负幂为 $(z-z_0)^{-m}$；等价于 $(z-z_0)^{m}f$ 在 $z_0$ 解析非零。
- **全纯（holomorphic）**：区域上解析。
- **亚纯（meromorphic）**：除有限阶极点外解析（有理函数是典型）。

局部行为：$m$ 阶零点附近 $f\sim c(z-z_0)^{m}$；$m$ 阶极点附近 $f\sim c/(z-z_0)^{m}$。

商的阶数：若 $f$、$g$ 分别有阶 $m$、$n$ 的零点，则 $f/g$ 有“极点阶” $n-m$（负则变为零点）。

---
## 2. 留数定义

$f$ 在 $z_0$ 有孤立奇点，去心盘 $0<|z-z_0|<r$ 上
$$
f(z)=\sum_{n=1}^{\infty}\frac{b_n}{(z-z_0)^{n}}+\sum_{n=0}^{\infty}a_n(z-z_0)^{n}.
$$
定义
$$
\operatorname{Res}(f,z_0)=b_1
$$
（即 $1/(z-z_0)$ 的系数；有的书写作 $a_{-1}$）。

若 $C$ 是绕 $z_0$、足够小且不含其它奇点的正向简单闭曲线，则
$$
\oint_{C}f=2\pi i\operatorname{Res}(f,z_0).
$$

> [!warning] 圆环选错 = 留数算错
> 必须用**穿孔小盘**上的 Laurent，不能用大圆环（例如 $1<|z|<\infty$）上的另一套系数。

> [!example] $e^{1/z}=1+z^{-1}+\dfrac{1}{2}z^{-2}+\cdots$
> $\operatorname{Res}(e^{1/z},0)=1$。

> [!example] $\sin z/z=1-z^{2}/6+\cdots$
> 可去奇点，$\operatorname{Res}=0$。

---
## 3. 单极点留数公式

设 $z_0$ 为孤立奇点。下列等价判据与公式在工科计算中最常用。

### 3.1 极限公式

若
$$
\lim_{z\to z_0}(z-z_0)f(z)=L
$$
存在（有限），则 $z_0$ 至多为单极点（或可去），且 $\operatorname{Res}(f,z_0)=L$。

### 3.2 $f=p/q$ 型

若 $p(z_0)\neq 0$，$q(z_0)=0$，$q'(z_0)\neq 0$，则 $f$ 在 $z_0$ 有单极点，且
$$
\operatorname{Res}\Bigl(\frac{p}{q},z_0\Bigr)=\frac{p(z_0)}{q'(z_0)}.
$$

### 3.3 $f=g/h$，$h$ 有单零点

更一般：$\operatorname{Res}(g/h,z_0)=g(z_0)/h'(z_0)$（$g(z_0)\neq 0$）。

特例：$1/g$ 在 $g$ 的单零点处
$$
\operatorname{Res}\Bigl(\frac{1}{g},z_0\Bigr)=\frac{1}{g'(z_0)}.
$$

### 3.4 乘以解析因子

若 $f$ 有单极点、$h$ 在 $z_0$ 解析，则
$$
\operatorname{Res}(hf,z_0)=h(z_0)\operatorname{Res}(f,z_0).
$$

> [!example] $\cot z=\cos z/\sin z$
> 在 $z=n\pi$：$\operatorname{Res}=\cos(n\pi)/\cos(n\pi)=1$。这是求和与部分分式的标准工具。

> [!example] $1/\sin z$ 在 $n\pi$
> $\operatorname{Res}=1/\cos(n\pi)=(-1)^{n}$。

> [!example] $f(z)=\dfrac{z^{2}+z+2}{(z-2)(z-3)(z-4)(z-5)}$
> 在 $z=2$：
> $$
> \operatorname{Res}=\frac{4+2+2}{(2-3)(2-4)(2-5)}=\frac{8}{(-1)(-2)(-3)}=-\frac{4}{3}.
> $$

---
## 4. 高阶极点

若 $f$ 有 $m$ 阶极点，令
$$
g(z)=(z-z_0)^{m}f(z)
$$
（在 $z_0$ 解析，$g(z_0)\neq 0$）。则
$$
\operatorname{Res}(f,z_0)=\frac{g^{(m-1)}(z_0)}{(m-1)!}.
$$
即：$g$ 的 Taylor 中 $(z-z_0)^{m-1}$ 项的系数。

$m=1$ 时退化为 $\operatorname{Res}=g(z_0)$，与极限公式一致。

> [!example] $f(z)=\dfrac{1}{(z^{2}+1)(z-2)^{2}}$ 在 $z=2$（二阶极点）
> $g(z)=1/(z^{2}+1)$，
> $$
> g'(z)=\frac{-2z}{(z^{2}+1)^{2}},\quad
> \operatorname{Res}(f,2)=g'(2)=\frac{-4}{25}.
> $$

> [!tip] 实务
> 二、三阶极点求导尚可；更高阶常改用部分分式、已知级数乘积，或把分子分母一起 Taylor。

> [!example] $\sinh z/z^{5}$ 在 $0$
> $\sinh z=z+z^{3}/3!+z^{5}/5!+\cdots$，故
> $$
> \frac{\sinh z}{z^{5}}=\frac{1}{z^{4}}+\frac{1}{3!z^{2}}+\frac{1}{5!}+\cdots,
> $$
> 无 $z^{-1}$ 项（偶函数），$\operatorname{Res}=0$。

---
## 5. Cauchy 留数定理

设 $f$ 在区域 $A$ 内除孤立奇点外解析，$C\subset A$ 为正向简单闭曲线，不经过奇点。则
$$
\oint_{C}f(z)\,dz=2\pi i\sum_{z_k\text{ 在 }C\text{ 内}}\operatorname{Res}(f,z_k).
$$

![[ca-residue-theorem.svg]]

> [!note]- 证明提纲（挖洞）
> 从 $C$ 向每个内部奇点挖小圆并加切割线，得无奇点闭围道 $\tilde C$。Cauchy $\Rightarrow\oint_{\tilde C}f=0$；切割线来回抵消，剩下 $\oint_C f=\sum\oint_{C_k}f=2\pi i\sum\operatorname{Res}$。

> [!example] $\displaystyle\oint_{|z|=2}\frac{5z-2}{z(z-1)}\,dz$
> 奇点 $0,1$ 都在圆内。
> $$
> \operatorname{Res}_{0}=2,\quad\operatorname{Res}_{1}=3
> \Rightarrow\text{积分}=2\pi i(2+3)=10\pi i.
> $$
> （Orloff 写 $10\pi i$ 的 $2\pi i\cdot 5$；上式一致。）

> [!example] $\displaystyle\oint_{|z|=1}z^{2}\sin(1/z)\,dz$
> $$
> z^{2}\sin\frac{1}{z}=z^{2}\Bigl(\frac{1}{z}-\frac{1}{6z^{3}}+\cdots\Bigr)=z-\frac{1}{6z}+\cdots,
> $$
> $\operatorname{Res}=-1/6$，积分 $=2\pi i(-1/6)=-\pi i/3$。

---
## 6. 无穷远留数

设 $f$ 在 $\mathbb{C}$ 上仅有有限个奇点。取足够大的正向圆周 $C_R$ 包围全部奇点，定义
$$
\operatorname{Res}(f,\infty):=-\frac{1}{2\pi i}\oint_{C_R}f(z)\,dz.
$$
于是
$$
\operatorname{Res}(f,\infty)=-\sum_{\text{有限奇点}}\operatorname{Res}(f,z_k),
$$
且
$$
\oint_{C_R}f=-2\pi i\operatorname{Res}(f,\infty).
$$

**计算定理**（换元 $w=1/z$）：
$$
\operatorname{Res}(f,\infty)=-\operatorname{Res}\Bigl(\frac{1}{w^{2}}f\bigl(\tfrac{1}{w}\bigr),\,0\Bigr).
$$

> [!example] 重算 $\displaystyle\oint_{|z|=2}\dfrac{5z-2}{z(z-1)}\,dz$
> $$
> \frac{1}{w^{2}}f(1/w)=\frac{5/w-2}{(1/w)(1/w-1)}=\frac{5-2w}{1-w},
> $$
> 在 $0$ 的留数经整理得 $\operatorname{Res}(f,\infty)=-5$，故积分 $= -2\pi i(-5)=10\pi i$。一次留数代替两个。

直觉：$-C_R$ 的“内部”是圆外（含 $\infty$）；要让留数定理在扩充平面上自洽，必须给 $\infty$ 一个留数。

---
## 7. 自检

1. 会写 / 认 Laurent 中的 $b_1$。
2. 单极点：极限、$\dfrac{p(z_0)}{q'(z_0)}$、$1/g'(z_0)$。
3. $m$ 阶极点：$\dfrac{g^{(m-1)}(z_0)}{(m-1)!}$。
4. 留数定理：$\oint=2\pi i\sum\operatorname{Res}$。
5. 无穷远：$-\operatorname{Res}\bigl(w^{-2}f(1/w),0\bigr)$。

> [!success]- 参考答案
> 1. $\operatorname{Res}=b_1=$ 去心盘 Laurent 中 $(z-z_0)^{-1}$ 的系数。
> 2. $\lim(z-z_0)f$；有理 $p/q$ 且 $q(z_0)=0\neq q'$ 用 $p(z_0)/q'(z_0)$；简单零点 $g(z_0)=0$ 时 $\operatorname{Res}(1/g)=1/g'(z_0)$。
> 3. $g=(z-z_0)^m f$ 在 $z_0$ 解析非零时，$\operatorname{Res}=\frac{g^{(m-1)}(z_0)}{(m-1)!}$。
> 4. 正向简单闭曲线内部孤立奇点留数之和乘 $2\pi i$。
> 5. $\operatorname{Res}(f,\infty)=-\operatorname{Res}(w^{-2}f(1/w),0)$；大圆积分 $=-2\pi i\operatorname{Res}(f,\infty)$。

> [!example] 练习：单极点留数
> 求 $\operatorname{Res}\!\left(\dfrac{e^z}{z^2+1},i\right)$，并写出 $\oint_{|z-i|=1}\dfrac{e^z}{z^2+1}\,dz$。

> [!success]- 练习参考答案
> $z^2+1=(z-i)(z+i)$，在 $i$ 为单极点：$\operatorname{Res}=e^i/(2i)$。圆 $|z-i|=1$ 只围 $i$（$-i$ 在外），积分 $=2\pi i\cdot e^i/(2i)=\pi e^i$。

下一讲：用留数算实轴上的定积分（半圆、钥匙孔、凹陷围道）。

## 参考

- Jeremy Orloff, *18.04 Topic 8: Residue theorem*, MIT OCW Spring 2018
- https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/
