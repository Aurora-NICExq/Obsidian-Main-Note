---
aliases:
  - 辐角原理
  - Argument Principle
  - Rouché
  - Nyquist criterion
  - Topic 11 Argument Principle
tags: [math, complex_analysis]
up: "[[Complex Analysis (MIT 18.04) MOC]]"
related:
  - "[[Laplace Transform]]"
  - "[[Residue Theorem]]"
  - "[[Cauchy's Integral Formula]]"
down: []
---
# 辐角原理

> [!summary] 核心结论
> 对数导数 $f'/f$ 的留数在零点为重数、在极点为负的阶数。因此
> $$
> \frac{1}{2\pi i}\oint_\gamma\frac{f'}{f}\,dz=N-P=\operatorname{Ind}(f\circ\gamma,0).
> $$
> Rouché 用“小扰动不改围道内零点数”推出代数基本定理。反馈回路的 Nyquist 判据是同一公式在 $KG$ 与点 $-1$ 上的工程表述：闭环稳定 $\Leftrightarrow$ $\operatorname{Ind}(KG\circ\gamma_{\mathrm{Im}},-1)=P_{G,\mathrm{RHP}}$。

> 底本：MIT 18.04 Topic 11（Jeremy Orloff）。工科向：零极点计数 → 稳定性。

---
## 1. 对数导数与零极点留数

设 $f$ 在区域上亚纯。在零点 $z_0$（阶 $m$）附近
$$
f(z)=(z-z_0)^m g(z),\qquad g(z_0)\neq 0,\ g\text{ 解析},
$$
则
$$
\frac{f'(z)}{f(z)}=\frac{m}{z-z_0}+\frac{g'(z)}{g(z)},
$$
故
$$
\operatorname{Res}\!\left(\frac{f'}{f};z_0\right)=m.
$$

在极点 $z_0$（阶 $p$）附近 $f(z)=(z-z_0)^{-p}h(z)$（$h(z_0)\neq 0$ 解析），同理
$$
\operatorname{Res}\!\left(\frac{f'}{f};z_0\right)=-p.
$$

> [!tip] 记忆
> $f'/f=(\log f)'$。绕零点一周，$\log f$ 的虚部（辐角）增加 $2\pi m$；绕极点一周则减少 $2\pi p$。

---
## 2. 辐角原理（Argument Principle）

设 $\gamma$ 为正向简单闭曲线，$f$ 在 $\gamma$ 上解析且非零，在内部亚纯。记

- $N$ = 内部零点总数（计重数）
- $P$ = 内部极点总数（计阶数）

则
$$
\frac{1}{2\pi i}\oint_\gamma\frac{f'(z)}{f(z)}\,dz=N-P.
$$

另一方面，把映射 $w=f(z)$ 看成把 $\gamma$ 送到曲线 $f\circ\gamma$。绕原点的**绕数**（winding number）满足
$$
\operatorname{Ind}(f\circ\gamma,0)=\frac{1}{2\pi i}\oint_{f\circ\gamma}\frac{dw}{w}
=\frac{1}{2\pi i}\oint_\gamma\frac{f'}{f}\,dz.
$$
因此
$$
N-P=\operatorname{Ind}(f\circ\gamma,0)=\frac{\Delta_\gamma\operatorname{arg} f}{2\pi}.
$$

> [!warning] $N-P$，不是 $N+P$
> 零点贡献**正**重数，极点贡献**负**阶数。漏掉极点或把符号弄反，绕数会对不上。另：$\gamma$ 上不能有零/极，否则 $f'/f$ 在路径上奇异。

![[ca-argument-principle.svg]]

> [!example] $f(z)=z^2(z-i)/(z+2)$，单位圆 $|z|=1$
> 内部：零点 $0$（二重）、$i$（单）；无极点（极点 $-2$ 在外）。
> $N-P=2+1-0=3$。像曲线绕 $0$ 三圈。

### 2.1 与留数定理的关系

辐角原理 = 对 $f'/f$ 用留数定理，并把各零/极留数加总。前提：$f$ 在 $\gamma$ 上无零无极（否则 $f'/f$ 在围道上有奇点）。

---
## 3. Rouché 定理

> [!abstract] Rouché
> 在简单闭曲线 $\gamma$ 上，$|g|<|f|$，且 $f,g$ 在 $\gamma$ 及内部解析。则 $f$ 与 $f+g$ 在内部有**相同个数**的零点（计重数）。

直觉：$f+g=f(1+g/f)$，而 $|g/f|<1$ 使 $1+g/f$ 的像不绕过 $0$，故
$$
\operatorname{Ind}((f+g)\circ\gamma,0)=\operatorname{Ind}(f\circ\gamma,0).
$$

> [!note]- 证明提纲（Rouché → FTA）
> 大圆上 $|a_{n-1}z^{n-1}+\cdots|<|z^n|$ $\Rightarrow$ $p$ 与 $z^n$ 同零点数 $n$。细节：把低次项当作 $g$，首项为 $f$。

> [!example] 代数基本定理（FTA）
> 多项式 $p(z)=z^n+a_{n-1}z^{n-1}+\cdots+a_0$。在大圆 $|z|=R$ 上取 $f=z^n$、$g=$ 低次项。$R$ 充分大时 $|g|<|f|$，故 $p$ 与 $z^n$ 同有 $n$ 个零点。

> [!example] $z^5+3z+1=0$ 在单位圆内的根数
> 取 $f=3z$、$g=z^5+1$。在 $|z|=1$ 上 $|g|\le 2<3=|f|$，故恰有 $1$ 个根在单位圆内（与 $3z$ 相同）。

---
## 4. 工科应用：反馈与 Nyquist

### 4.1 开环 / 闭环

单位负反馈：开环传递函数 $G(s)$，增益 $K$，闭环
$$
T(s)=\frac{KG(s)}{1+KG(s)}.
$$
闭环极点 = $1+KG$ 的零点。设开环 $G$ 在右半平面（RHP）有 $P_{G,\mathrm{RHP}}$ 个极点（计重数）。

稳定性（BIBO / 极点判据，工科常用）：闭环节所有极点在左半平面（LHP）$\Leftrightarrow$ $1+KG$ 在 RHP **无零点**。

### 4.2 Nyquist 围道

标准 Nyquist 围道 $\gamma_{\mathrm{Im}}$：沿虚轴 $-i\infty\to i\infty$，再以大半径半圆包住整个 RHP（若虚轴上有极点，用小半圆绕开）。该定向相对 RHP 为**顺时针**（与“正向简单闭曲线”差一个符号）。

对 $f=1+KG$：开环极点即 $1+KG$ 的极点（$K$ 常数），$P_{1+KG}=P_{G,\mathrm{RHP}}$。顺时针定向下绕数满足
$$
\operatorname{Ind}((1+KG)\circ\gamma_{\mathrm{Im}},0)=P_{G,\mathrm{RHP}}-N_{1+KG}.
$$
闭环稳定要求 $N_{1+KG}=0$。又 $1+KG$ 绕 $0$ 等价于 $KG$ 绕 $-1$，故

$$
\boxed{\operatorname{Ind}(KG\circ\gamma_{\mathrm{Im}},-1)=P_{G,\mathrm{RHP}}}
$$

为闭环稳定的充要条件（在所述假设下）。开环本身稳定（$P_{G,\mathrm{RHP}}=0$）时，Nyquist 图**不得**包围 $-1$。

> [!note] 定向
> 若改用包住 RHP 的**逆时针**数学围道，则稳定条件写成 $\operatorname{Ind}(KG\circ\gamma,-1)=-P_{G,\mathrm{RHP}}$。工科 Nyquist 图习惯与上行的 $+P$ 形式一致。

![[ca-nyquist.svg]]

> [!tip] 画图实务
> 通常只画 $KG(i\omega)$，$\omega:0\to+\infty$，再对实轴镜像得到 $\omega:-\infty\to 0$；大圆弧的像常坍缩到原点（严格相对阶 $\ge 1$ 时）。

### 4.3 与辐角原理的对应表

| 复分析 | 控制 |
|--------|------|
| $N-P=\operatorname{Ind}(f\circ\gamma,0)$ | 零极差 = 像曲线绕数 |
| $f=1+KG$，$0$ | 特征方程 |
| $f=KG$，$-1$ | 经典 Nyquist 临界点 |
| RHP 围道 | $\gamma_{\mathrm{Im}}$ |

---
## 5. 自检

1. 会算 $f'/f$ 在零/极处的留数；写出 $N-P=\operatorname{Ind}(f\circ\gamma,0)$。
2. 会用 Rouché 估根的位置；会用大圆 + Rouché 证 FTA。
3. 会把 Nyquist 写成：$\operatorname{Ind}(KG\circ\gamma_{\mathrm{Im}},-1)=P_{G,\mathrm{RHP}}$ 时闭环稳定。

> [!success]- 参考答案
> 1. 零点阶 $m$ $\Rightarrow\operatorname{Res}(f'/f)=m$；极点阶 $p$ $\Rightarrow -p$。积分得 $N-P=$ 像曲线绕 $0$ 的绕数。
> 2. 围道上 $|g|<|f|$ $\Rightarrow$ $f$ 与 $f+g$ 同零点数；FTA：大圆上低次项扰动不改 $z^n$ 的 $n$ 个零点。
> 3. 工科顺时针 Nyquist：$KG$ 绕 $-1$ 的圈数应等于开环 RHP 极点数；开环稳定则不得包围 $-1$。

> [!example] 练习：数零点
> $f(z)=z^2(z-i)/(z+2)$，在 $|z|=1$ 上用辐角原理求 $N-P$。

> [!success]- 练习参考答案
> 内部：零点 $0$（二重）、$i$（单）；极点 $-2$ 在外。$N-P=3-0=3$。

下一讲：[[Laplace Transform]]——把传递函数 $G(s)$ 与 Bromwich 反演接到同一套围道语言。

## 参考

- Jeremy Orloff, *18.04 Topic 11: Argument Principle*, MIT OCW Spring 2018
- https://ocw.mit.edu/courses/18-04-complex-variables-with-applications-spring-2018/
