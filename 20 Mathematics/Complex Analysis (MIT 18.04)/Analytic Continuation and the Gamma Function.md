---
aliases:
  - 解析延拓与 Gamma 函数
  - Gamma Function
  - Analytic Continuation
  - Topic 13 Gamma
tags: [math, complex_analysis]
up: "[[Complex Analysis (MIT 18.04) MOC]]"
related:
  - "[[Laplace Transform]]"
  - "[[Argument Principle]]"
  - "[[Analytic Functions]]"
down: []
---
# 解析延拓与 Gamma 函数

> [!summary] 核心结论
> 连通区域上，解析延拓若存在则唯一。$\Gamma(z)=\int_0^\infty t^{z-1}e^{-t}\,dt$（$\operatorname{Re}z>0$）经 $\Gamma(z+1)=z\Gamma(z)$ 延拓到除 $0,-1,-2,\ldots$ 外的全平面；这些点是单极点，$\operatorname{Res}(\Gamma;-n)=(-1)^n/n!$。反射公式 $\Gamma(z)\Gamma(1-z)=\pi/\sin(\pi z)$ 给出 $\Gamma(1/2)=\sqrt{\pi}$。与 Laplace 的桥梁：$\mathcal{L}\{t^{z-1}\}=\Gamma(z)/s^z$。

> 底本：MIT 18.04 Topic 13（Jeremy Orloff）。工科向：延拓唯一性 + $\Gamma$ 作为阶乘与 Laplace 的共同推广。

---
## 1. 解析延拓与唯一性

设 $f$ 在区域 $A$ 上解析，$F$ 在更大区域 $B\supset A$（或与 $A$ 相交的连通区域）上解析，且在 $A\cap B$ 上 $F\equiv f$。则称 $F$ 是 $f$ 的**解析延拓**。

> [!abstract] 唯一性定理
> 若 $D$ 连通，$F,G$ 在 $D$ 上解析，且在某个有极限点落在 $D$ 内的集合上 $F=G$（例如在开子集或有聚点的点列上相等），则在整个 $D$ 上 $F\equiv G$。

> [!note]- 证明提纲（唯一性）
> $H=F-G$ 的零点集在连通域内有聚点 $\Rightarrow$ 由零点孤立性（非恒零则零点孤立）得 $H\equiv 0$。故延拓至多一个。

推论：从同一“种子”出发，在给定连通域上的解析延拓至多一个。课程里已多次暗用这一点——例如用幂级数在重叠圆盘上接力、或用函数方程把积分定义推到更大半平面。

> [!example] $\sum_{n=0}^\infty z^n=1/(1-z)$
> 左侧只在 $|z|<1$ 收敛；右侧在 $\mathbb{C}\setminus\{1\}$ 解析。后者是前者的延拓，且由唯一性，任何其它延拓必须与之重合。

> [!warning] 多值性不是“不唯一”
> $\log z$ 的不同分支是在**不同的割平面**（或 Riemann 曲面）上定义的单值解析函数；在同一连通、已选定支割的区域上，延拓仍然唯一。

---
## 2. Gamma 的积分定义

对 $\operatorname{Re}z>0$，
$$
\Gamma(z)=\int_0^\infty t^{z-1}e^{-t}\,dt.
$$

积分在该半平面绝对收敛，故 $\Gamma$ 在 $\{\operatorname{Re}z>0\}$ 上解析。

### 2.1 函数方程与阶乘

分部积分（边界项在 $\operatorname{Re}z>0$ 消失）得
$$
\Gamma(z+1)=z\Gamma(z).
$$

又 $\Gamma(1)=\int_0^\infty e^{-t}\,dt=1$，故对整数 $n\ge 0$，
$$
\Gamma(n+1)=n!.
$$
因此 $\Gamma$ 是阶乘到复变量的解析推广（差一个移位：$\Gamma(n+1)=n!$）。

> [!example] $\Gamma(2)=1$，$\Gamma(3)=2$，$\Gamma(4)=6$。

---
## 3. 向左半平面的延拓与极点

把函数方程改写为
$$
\Gamma(z)=\frac{\Gamma(z+1)}{z}.
$$
右侧在 $\operatorname{Re}z>-1$、$z\neq 0$ 有定义（因 $\Gamma(z+1)$ 在 $\operatorname{Re}(z+1)>0$ 已知）。迭代：
$$
\Gamma(z)=\frac{\Gamma(z+n+1)}{z(z+1)\cdots(z+n)},
$$
可把定义域推到 $\operatorname{Re}z>-n-1$ 挖去 $\{0,-1,\ldots,-n\}$。

取极限，$n\to\infty$，得到在
$$
\mathbb{C}\setminus\{0,-1,-2,\ldots\}
$$
上的亚纯延拓；在非正整数处为**单极点**。

![[ca-gamma-poles.svg]]

### 3.1 留数

在 $z=0$：$\Gamma(z)=\Gamma(z+1)/z$，而 $\Gamma(1)=1$，故
$$
\operatorname{Res}(\Gamma;0)=1=\frac{(-1)^0}{0!}.
$$

一般地，在 $z=-n$（$n=0,1,2,\ldots$），
$$
\operatorname{Res}(\Gamma;-n)=\frac{(-1)^n}{n!}.
$$

> [!tip] 推导骨架
> $$
> \Gamma(z)=\frac{\Gamma(z+n+1)}{z(z+1)\cdots(z+n)},
> $$
> 在 $z=-n$ 处分母有单因子 $(z+n)$，分子 $\Gamma(1)=1$，其余因子为 $(-n)(-n+1)\cdots(-1)=(-1)^n n!$，整理即得留数。

---
## 4. 反射公式与特殊值

Euler 反射公式：
$$
\Gamma(z)\Gamma(1-z)=\frac{\pi}{\sin(\pi z)},
$$
在使两边有意义处成立（可通过延拓唯一性推到更大区域）。

令 $z=1/2$：
$$
\Gamma\!\left(\tfrac12\right)^2=\frac{\pi}{\sin(\pi/2)}=\pi
\implies
\Gamma\!\left(\tfrac12\right)=\sqrt{\pi}
$$
（取正值，与积分定义一致）。

> [!example] 高斯积分
> $\int_{-\infty}^\infty e^{-x^2}\,dx=\sqrt{\pi}$ 与 $\Gamma(1/2)=\sqrt{\pi}$ 是同一家族的计算；令 $t=x^2$ 可从 $\Gamma(1/2)$ 的积分定义推出。

反射公式也说明：$\Gamma$ 在正实轴上无零点（否则左侧在某正点为零，右侧一般非零），实际 $\Gamma$ 在有限平面**无零点**。

### 4.1 递推算几个值

由 $\Gamma(1/2)=\sqrt{\pi}$ 与 $\Gamma(z+1)=z\Gamma(z)$：
$$
\Gamma\!\left(\tfrac32\right)=\tfrac12\Gamma\!\left(\tfrac12\right)=\tfrac12\sqrt{\pi},\qquad
\Gamma\!\left(\tfrac52\right)=\tfrac32\cdot\tfrac12\sqrt{\pi}=\tfrac34\sqrt{\pi}.
$$
向负方向（避开极点）同理：$\Gamma(-1/2)=\Gamma(1/2)/(-1/2)=-2\sqrt{\pi}$。

---
## 5. 与 Laplace 变换的联系

对 $\operatorname{Re}z>0$、$\operatorname{Re}s>0$，
$$
\mathcal{L}\{t^{z-1}\}(s)=\int_0^\infty e^{-st}t^{z-1}\,dt.
$$
令 $u=st$（$t=u/s$，$dt=du/s$；主支 $\operatorname{Re}s>0$），
$$
\mathcal{L}\{t^{z-1}\}=\frac{1}{s^z}\int_0^\infty u^{z-1}e^{-u}\,du=\frac{\Gamma(z)}{s^z}.
$$

特别地，$z=n+1$ 正整数时回到 $\mathcal{L}\{t^n\}=n!/s^{n+1}$。这把 [[Laplace Transform]] 表中的幂次行与 $\Gamma$ 统一起来；对非整数 $z$，同一公式在选定 $s^z$ 的分支后仍成立。

> [!example] $\mathcal{L}\{t^{-1/2}\}=\Gamma(1/2)/s^{1/2}=\sqrt{\pi/s}$（$\operatorname{Re}s>0$）。

> [!example] 与 Topic 12 表对照
> $\mathcal{L}\{t\}=\Gamma(2)/s^2=1/s^2$；$\mathcal{L}\{t^2\}=\Gamma(3)/s^3=2/s^3$。

唯一性再次出场：两边在 $\operatorname{Re}z>0$、$\operatorname{Re}s>0$ 由积分相等；对固定 $s$，关于 $z$ 的解析延拓使公式在挖掉极点后继续可用（右侧 $\Gamma(z)$ 提供延拓）。

---
## 6. 自检

1. 能陈述连通域上解析延拓的唯一性，并举幂级数 / 有理延拓例子。
2. 会写 $\Gamma$ 的积分定义、$\Gamma(z+1)=z\Gamma(z)$、$\Gamma(n+1)=n!$。
3. 会说明极点在 $0,-1,-2,\ldots$，并记留数 $(-1)^n/n!$；会用反射得 $\Gamma(1/2)=\sqrt{\pi}$。
4. 会写 $\mathcal{L}\{t^{z-1}\}=\Gamma(z)/s^z$，与 Topic 12 对接。

> [!success]- 参考答案
> 1. 连通域上两解析函数在有聚点集上相等 $\Rightarrow$ 处处相等；$\sum z^n$ 延拓为 $1/(1-z)$（挖掉 $1$）。
> 2. $\Gamma(z)=\int_0^\infty t^{z-1}e^{-t}\,dt$（$\operatorname{Re}z>0$）；递推 $\Gamma(z+1)=z\Gamma(z)$；正整数 $\Gamma(n+1)=n!$。
> 3. 用递推向左延拓，极点在非正整数；$\operatorname{Res}(\Gamma;-n)=(-1)^n/n!$；反射 $\Rightarrow\Gamma(1/2)=\sqrt{\pi}$。
> 4. $\operatorname{Re}z>0$、$\operatorname{Re}s>0$ 时 $\mathcal{L}\{t^{z-1}\}=\Gamma(z)/s^z$（选定 $s^z$ 分支）。

> [!example] 练习：递推与反射
> 由 $\Gamma(1/2)=\sqrt{\pi}$ 求 $\Gamma(3/2)$ 与 $\Gamma(-1/2)$。

> [!success]- 练习参考答案
> $\Gamma(3/2)=\tfrac12\Gamma(1/2)=\sqrt{\pi}/2$；$\Gamma(1/2)=(-1/2)\Gamma(-1/2)\Rightarrow\Gamma(-1/2)=-2\sqrt{\pi}$。

## 参考

- Jeremy Orloff, *18.04 Topic 13: Analytic continuation and the Gamma function*, MIT OCW Spring 2018
- https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/
