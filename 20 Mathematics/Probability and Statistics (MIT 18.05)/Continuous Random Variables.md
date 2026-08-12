---
aliases:
  - 连续随机变量
  - Continuous Random Variables
  - PDF
  - Normal Distribution
  - Exponential Distribution
  - Reading 6 Continuous RVs
tags: [math, probability_statistics]
up: "[[Probability and Statistics (MIT 18.05) MOC]]"
related:
  - "[[Discrete Random Variables]]"
  - "[[Conditional Probability and Bayes Theorem]]"
  - "[[Joint Distributions Covariance and Correlation]]"
  - "[[Law of Large Numbers and Central Limit Theorem]]"
down:
  - "[[Joint Distributions Covariance and Correlation]]"
---
# 连续随机变量

> [!summary] 核心结论
> 连续随机变量用 **PDF** $f_X$ 描述：$P(a\le X\le b)=\int_a^b f_X(x)\,dx$，单点概率为 0。CDF 仍是 $F_X(x)=P(X\le x)$，且在连续型下 $F'=f$。期望 / 方差把求和换成积分。Uniform / Exponential / Normal / Gamma 构成标准画廊；分位数与标准化 $Z=(X-\mu)/\sigma$ 把任意正态问题化归标准正态表。

> 底本：MIT 18.05 Reading 6–7（Jeremy Orloff / Jennifer French Kamrin, Spring 2022）。

---
## 1. PDF 与概率

连续型：$X$ 有概率密度函数 $f_X$，满足
$$
f_X(x)\ge 0,\qquad \int_{-\infty}^{\infty}f_X(x)\,dx=1,
$$
且对任意区间（更一般 Borel 集）
$$
P(X\in A)=\int_A f_X(x)\,dx.
$$
特别地 $P(X=x)=0$，故 $P(a\le X\le b)=P(a<X<b)$。密度 $f_X(x)$ **不是**概率；$f_X(x)\Delta x$ 才近似落在 $[x,x+\Delta x]$ 的概率。

> [!warning] 密度可以大于 1
> PDF 不是概率。例如 $\mathrm{Unif}(0,0.1)$ 的密度是 $10$。$f(x)>1$ 完全合法，只要积分仍为 1。

> [!example] 端到端：由 PDF 算概率与期望
> 设 $f(x)=cx$ 在 $(0,2)$ 上，别处为 0。先归一化：
> $$
> \int_0^2 cx\,dx=c\cdot 2=1\Rightarrow c=1/2.
> $$
> $P(X>1)=\int_1^2 (x/2)\,dx=3/4$。
> $E[X]=\int_0^2 x\cdot(x/2)\,dx=\int_0^2 x^2/2\,dx=4/3$。
> $E[X^2]=\int_0^2 x^2\cdot(x/2)\,dx=2$，故 $\mathrm{Var}(X)=2-(4/3)^2=2/9$。

---
## 2. CDF 与微分关系

$$
F_X(x)=P(X\le x)=\int_{-\infty}^{x}f_X(t)\,dt.
$$
在 $f$ 的连续点：$F_X'(x)=f_X(x)$。区间概率：
$$
P(a<X\le b)=F_X(b)-F_X(a).
$$
CDF 仍非降、右连续，$F(-\infty)=0$，$F(+\infty)=1$；连续型下 $F$ 连续（无跳跃）。

> [!tip] 离散 vs 连续
> 离散：PMF 点质量，CDF 阶梯。连续：PDF 面积，CDF 光滑（或至少连续）。混合型（既有点质量又有密度）在 18.05 后期偶尔出现，用 Stieltjes 图像理解即可。

---
## 3. 期望与方差

$$
E[X]=\int_{-\infty}^{\infty} x\,f_X(x)\,dx,
$$
$$
E[g(X)]=\int_{-\infty}^{\infty} g(x)\,f_X(x)\,dx\quad(\text{LOTUS}),
$$
$$
\operatorname{Var}(X)=E[X^2]-(E[X])^2.
$$
线性性照旧：$E[aX+b]=aE[X]+b$，$\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$。独立时方差可加。

对非负连续 $X$ 常用层公式：
$$
E[X]=\int_0^{\infty}P(X>t)\,dt.
$$

---
## 4. 分布画廊

### 4.1 Uniform$(a,b)$

$$
f_X(x)=\frac{1}{b-a}\mathbf{1}_{[a,b]}(x),\qquad
E[X]=\frac{a+b}{2},\quad
\operatorname{Var}(X)=\frac{(b-a)^2}{12}.
$$
“在区间上完全无知”的默认连续模型；也是逆变换抽样的原料（若 $U\sim\mathrm{Unif}(0,1)$，$F^{-1}(U)$ 有 CDF $F$）。

### 4.2 Exponential$(\lambda)$

$$
f_X(x)=\lambda e^{-\lambda x}\mathbf{1}_{x\ge 0},\qquad
F_X(x)=1-e^{-\lambda x}\ (x\ge 0).
$$
$$
E[X]=\frac{1}{\lambda},\qquad \operatorname{Var}(X)=\frac{1}{\lambda^2}.
$$
无记忆：$P(X>s+t\mid X>s)=P(X>t)$——连续版 Geometric。常模到达间隔、元件寿命（无老化假定下）。

> [!example] 指数寿命数值
> $\lambda=0.01$（单位：1/小时），$E[X]=100$ h。$P(X>120)=e^{-0.01\cdot 120}=e^{-1.2}\approx 0.301$。
> 无记忆：已用 50 h 后，再活 120 h 的概率仍是 $e^{-1.2}$，不是“更耐用”。

### 4.3 Normal$(\mu,\sigma^2)$

$$
f_X(x)=\frac{1}{\sqrt{2\pi}\,\sigma}\exp\!\left(-\frac{(x-\mu)^2}{2\sigma^2}\right).
$$
$$
E[X]=\mu,\qquad \operatorname{Var}(X)=\sigma^2.
$$
记 $X\sim\mathcal{N}(\mu,\sigma^2)$。钟形、关于 $\mu$ 对称；$\sigma$ 控制宽度。

![[ps-normal-pdf.svg]]

### 4.4 Gamma（简介）

形状 $\alpha>0$、速率 $\lambda>0$（或尺度 $\theta=1/\lambda$）：
$$
f_X(x)=\frac{\lambda^\alpha}{\Gamma(\alpha)}x^{\alpha-1}e^{-\lambda x}\mathbf{1}_{x>0}.
$$
$E[X]=\alpha/\lambda$，$\operatorname{Var}(X)=\alpha/\lambda^2$。$\alpha=1$ 退化为 Exponential$(\lambda)$；$n$ 个 i.i.d. $\mathrm{Exp}(\lambda)$ 之和为 $\mathrm{Gamma}(n,\lambda)$（Erlang）。卡方 $\chi^2_k$ 是 Gamma 的特例。

---
## 5. 分位数

对连续严格增的 $F$，**$p$-分位数** $q_p$ 满足 $F(q_p)=p$，即
$$
q_p=F^{-1}(p),\qquad P(X\le q_p)=p.
$$
中位数 $=q_{0.5}$；四分位距等描述散布时可少受尾部影响。标准正态分位数常记 $z_p$（如 $z_{0.975}\approx 1.96$）。

---
## 6. 标准化与正态计算

若 $X\sim\mathcal{N}(\mu,\sigma^2)$，则
$$
Z=\frac{X-\mu}{\sigma}\sim\mathcal{N}(0,1).
$$
任意区间概率化归标准正态 CDF $\Phi$：
$$
P(a\le X\le b)=\Phi\!\left(\frac{b-\mu}{\sigma}\right)-\Phi\!\left(\frac{a-\mu}{\sigma}\right).
$$
$\Phi(-z)=1-\Phi(z)$。经验法则：约 68% / 95% / 99.7% 质量落在 $\mu\pm\sigma,\ \mu\pm 2\sigma,\ \mu\pm 3\sigma$。

> [!example] $X\sim\mathcal{N}(100,15^2)$，$P(X>130)$
> $$
> P\!\left(Z>\frac{130-100}{15}\right)=P(Z>2)=1-\Phi(2)\approx 0.0228.
> $$

> [!example] 求 $c$ 使 $P(X\le c)=0.95$
> $c=\mu+\sigma\,z_{0.95}\approx 100+15\cdot 1.645=124.675$。

---
## 7. 变换与联合密度（速览）

若 $Y=g(X)$ 且 $g$ 光滑严格单调，则
$$
f_Y(y)=f_X(x)\left|\frac{dx}{dy}\right|=f_X\!\bigl(g^{-1}(y)\bigr)\big|(g^{-1})'(y)\big|.
$$
联合连续 $(X,Y)$ 有 $f_{X,Y}$；边缘 $f_X(x)=\int f_{X,Y}(x,y)\,dy$；独立 $\Leftrightarrow$ 联合密度因式分解。条件密度
$$
f_{X\mid Y}(x\mid y)=\frac{f_{X,Y}(x,y)}{f_Y(y)}
$$
把 Bayes 更新推进到连续参数——统计推断的语言由此展开。

---
## 8. 分布速查表

| 分布 | 密度要点 | $E$ | $\mathrm{Var}$ |
|------|----------|-----|----------------|
| $\mathrm{Unif}(a,b)$ | $1/(b-a)$ on $[a,b]$ | $(a+b)/2$ | $(b-a)^2/12$ |
| $\mathrm{Exp}(\lambda)$ | $\lambda e^{-\lambda x}$，$x\ge 0$ | $1/\lambda$ | $1/\lambda^2$ |
| $\mathcal{N}(\mu,\sigma^2)$ | 高斯核 | $\mu$ | $\sigma^2$ |
| $\mathrm{Gamma}(\alpha,\lambda)$ | $\propto x^{\alpha-1}e^{-\lambda x}$ | $\alpha/\lambda$ | $\alpha/\lambda^2$ |

---
## 9. 自检与参考答案

1. 用积分从 PDF 算概率与 CDF；分清“密度值”与“概率”。
2. 会算连续型期望 / 方差；记住 Unif / Exp / Normal 的矩。
3. 会标准化并用 $\Phi$ / 分位数解正态概率与分位点问题。
4. 知道 Exponential 无记忆、Gamma 与 Exp 的关系；为后续估计与假设检验备好语言。

> [!success]- 参考答案
> 1. $P(a\le X\le b)=\int_a^b f$；$f$ 本身不是概率；单点概率为 0。
> 2. $E[X]=\int xf$；$\mathrm{Var}=E[X^2]-(E[X])^2$。Unif/Exp/Normal 矩见表。
> 3. $Z=(X-\mu)/\sigma$；$P(X\le c)=\Phi((c-\mu)/\sigma)$；$q_p=\mu+\sigma z_p$。
> 4. Exp 无记忆；$n$ 个 i.i.d. Exp 之和为 Gamma（Erlang）。

> [!example] 练习：均匀分布
> $X\sim\mathrm{Unif}(2,8)$。求 $P(3\le X\le 5)$ 与 $P(|X-5|<1)$。

> [!success]- 练习参考答案
> 密度 $1/6$。$P(3\le X\le 5)=2/6=1/3$。
> $|X-5|<1\Leftrightarrow X\in(4,6)$，长度 2，概率 $2/6=1/3$。

## 参考

- Jeremy Orloff & Jennifer French Kamrin, *18.05 Introduction to Probability and Statistics*, Reading 6–7 (Continuous Random Variables), MIT OCW Spring 2022
- 课程主页：https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/
