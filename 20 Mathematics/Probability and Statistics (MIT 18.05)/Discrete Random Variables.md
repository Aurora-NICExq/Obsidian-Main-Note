---
aliases:
  - 离散随机变量
  - Discrete Random Variables
  - PMF
  - Binomial Distribution
  - Poisson Distribution
  - Reading 4 Discrete RVs
tags: [math, probability_statistics]
up: "[[Probability and Statistics (MIT 18.05) MOC]]"
related:
  - "[[Counting and Probability Basics]]"
  - "[[Conditional Probability and Bayes Theorem]]"
  - "[[Continuous Random Variables]]"
down:
  - "[[Continuous Random Variables]]"
---
# 离散随机变量

> [!summary] 核心结论
> 离散随机变量 $X$ 由 **PMF** $p_X(x)=P(X=x)$ 完全描述；CDF $F_X(x)=P(X\le x)$ 是其累积。期望 $E[X]=\sum x\,p(x)$ 是概率加权平均；方差量测偏离。Bernoulli / Binomial / Poisson / Geometric 是工科最常用的四件套；**期望线性** $E[X+Y]=E[X]+E[Y]$ 不要求独立——这是计数期望（指示变量）的杀手锏。

> 底本：MIT 18.05 Reading 4–5（Jeremy Orloff / Jennifer French Kamrin, Spring 2022）。

---
## 1. 随机变量与 PMF

随机变量是样本空间上的函数 $X:\Omega\to\mathbb{R}$。离散：取值可列（常为整数）。**概率质量函数（PMF）**：
$$
p_X(x)=P(X=x),\qquad p_X(x)\ge 0,\quad \sum_x p_X(x)=1.
$$
事件 $\{X\in A\}$ 的概率：$\displaystyle P(X\in A)=\sum_{x\in A}p_X(x)$。

> [!example] 掷公平骰子
> $p_X(k)=1/6$，$k=1,\ldots,6$。

---
## 2. CDF

累积分布函数
$$
F_X(x)=P(X\le x)=\sum_{t\le x}p_X(t).
$$
性质：$F$ 右连续、非降；$F(-\infty)=0$，$F(+\infty)=1$。离散时 $F$ 在支撑点处跳跃，跳跃高度恰为 $p_X(x)$：
$$
p_X(x)=F_X(x)-F_X(x^-).
$$

---
## 3. 期望与方差

### 3.1 期望

$$
E[X]=\sum_x x\,p_X(x)
$$
（绝对收敛时定义良好）。对函数 $g$：**律的无意识（LOTUS）**
$$
E[g(X)]=\sum_x g(x)\,p_X(x)
$$
——不必先求 $g(X)$ 的 PMF。

### 3.2 方差与标准差

$$
\operatorname{Var}(X)=E[(X-E[X])^2]=E[X^2]-(E[X])^2,
$$
$\mathrm{SD}(X)=\sqrt{\operatorname{Var}(X)}$。平移不变、平方缩放：
$$
\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X).
$$

### 3.3 期望的线性性

对任意（可积）$X,Y$——**不需独立**：
$$
E[X+Y]=E[X]+E[Y],\qquad E[cX]=cE[X].
$$
独立时还有 $E[XY]=E[X]E[Y]$，以及
$$
\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y).
$$

> [!tip] 指示变量
> 令 $I_A=1$ 当 $A$ 发生否则 $0$，则 $E[I_A]=P(A)$。复杂计数的期望常写成 $\sum E[I_j]=\sum P(A_j)$。

---
## 4. Bernoulli 与 Binomial

**Bernoulli($p$)**：一次成功/失败试验，$P(X=1)=p$，$P(X=0)=1-p$。
$$
E[X]=p,\qquad \operatorname{Var}(X)=p(1-p).
$$

**Binomial($n,p$)**：$n$ 次独立 Bernoulli 之和——$n$ 次试验中成功次数：
$$
p_X(k)=\binom{n}{k}p^k(1-p)^{n-k},\quad k=0,1,\ldots,n.
$$
$$
E[X]=np,\qquad \operatorname{Var}(X)=np(1-p).
$$
由线性性：若 $X=I_1+\cdots+I_n$ 独立同 Bernoulli，期望方差直接相加。

![[ps-binomial-pmf.svg]]

> [!example] 10 次独立投篮，命中率 $0.3$
> $X\sim\mathrm{Bin}(10,0.3)$，$P(X=3)=\binom{10}{3}(0.3)^3(0.7)^7$，$E[X]=3$。

> [!example] 端到端：二项概率 + 矩
> $X\sim\mathrm{Bin}(5,0.4)$。求 $P(X=2)$、$E[X]$、$\mathrm{Var}(X)$。
> $$
> P(X=2)=\binom{5}{2}(0.4)^2(0.6)^3=10\cdot 0.16\cdot 0.216=0.3456.
> $$
> $E[X]=5\cdot 0.4=2$，$\mathrm{Var}(X)=5\cdot 0.4\cdot 0.6=1.2$。
> 用定义验期望：$\sum_{k=0}^5 k\,p(k)$ 应得 2（可手算抽查 $k=2$ 项贡献 $2\cdot 0.3456$）。

> [!warning] Geometric 的两种约定
> 有的教材让 $X$ 从 0 起算（失败次数），有的从 1 起算（试验次数）。$E[X]$ 差 1；套公式前先看支撑。

---
## 5. Poisson

**Poisson($\lambda$)**：单位时间（或空间）内稀有事件计数的标准模型：
$$
p_X(k)=e^{-\lambda}\frac{\lambda^k}{k!},\quad k=0,1,2,\ldots.
$$
$$
E[X]=\operatorname{Var}(X)=\lambda.
$$

**Poisson 极限**：若 $n\to\infty$、$p\to 0$ 且 $np\to\lambda$，则 $\mathrm{Bin}(n,p)$ 的 PMF 点点趋于 $\mathrm{Poisson}(\lambda)$。经验法则：$n$ 大、$p$ 小、$np$ 中等时可用 Poisson 近似二项。

独立 Poisson 之和仍为 Poisson，参数相加（在独立假定下）。

> [!example] Poisson 近似二项
> $n=100$，$p=0.03$，$\lambda=np=3$。$P(X=0)$：
> 精确二项 $(0.97)^{100}\approx 0.0476$；Poisson $e^{-3}\approx 0.0498$。相对误差约 5%，工程估算常用。

---
## 6. Geometric

有两种常见约定（读题时先确认从 0 还是从 1 起算）：

**直到首次成功的试验次数** $X\sim\mathrm{Geom}(p)$（支撑 $1,2,\ldots$）：
$$
p_X(k)=(1-p)^{k-1}p,\qquad E[X]=\frac{1}{p},\qquad \operatorname{Var}(X)=\frac{1-p}{p^2}.
$$

**首次成功前失败次数** $Y=X-1$（支撑 $0,1,2,\ldots$）：$E[Y]=(1-p)/p$。

无记忆性：$P(X>m+n\mid X>m)=P(X>n)$——已失败 $m$ 次不改变“还要再等多久”的分布。

---
## 7. 联合分布与边缘（速览）

离散对 $(X,Y)$ 由联合 PMF $p_{X,Y}(x,y)=P(X=x,Y=y)$ 描述。边缘：
$$
p_X(x)=\sum_y p_{X,Y}(x,y).
$$
独立 $\Leftrightarrow$ $p_{X,Y}(x,y)=p_X(x)p_Y(y)$ 对所有 $x,y$。条件 PMF：
$$
p_{X\mid Y}(x\mid y)=\frac{p_{X,Y}(x,y)}{p_Y(y)}.
$$
这与上一讲 Bayes / 全概率在“事件语言”上同构。

---
## 8. 分布速查表

| 分布 | PMF 要点 | $E$ | $\mathrm{Var}$ |
|------|----------|-----|----------------|
| $\mathrm{Bern}(p)$ | $p^x(1-p)^{1-x}$ | $p$ | $p(1-p)$ |
| $\mathrm{Bin}(n,p)$ | $\binom{n}{k}p^k(1-p)^{n-k}$ | $np$ | $np(1-p)$ |
| $\mathrm{Pois}(\lambda)$ | $e^{-\lambda}\lambda^k/k!$ | $\lambda$ | $\lambda$ |
| $\mathrm{Geom}(p)$（到首次成功） | $(1-p)^{k-1}p$ | $1/p$ | $(1-p)/p^2$ |

---
## 9. 自检与参考答案

1. 会写 / 归一化 PMF；会从 PMF 画 CDF（阶梯）。
2. 会算 $E[X]$、$E[g(X)]$、$\operatorname{Var}(X)$；熟练用 $E[X^2]-(E[X])^2$。
3. 记住 Bernoulli→Binomial 的构造，以及 Poisson / Geometric 的参数与矩。
4. **期望线性不需独立**；会用指示变量算计数期望。

> [!success]- 参考答案
> 1. $p(x)\ge 0$ 且求和为 1；CDF 在支撑点跳跃高度 $=p(x)$。
> 2. $E[X]=\sum xp(x)$；LOTUS 算 $E[g(X)]$；$\mathrm{Var}=E[X^2]-(E[X])^2$。
> 3. Bern→Bin 是独立和；Pois：$E=\mathrm{Var}=\lambda$；Geom（到首次成功）$E=1/p$。
> 4. $E[\sum I_j]=\sum P(A_j)$，即使 $I_j$ 相关。

> [!example] 练习：指示变量
> 掷 2 枚公平骰子。令 $X=$“出现 6 的骰子数”（0/1/2）。用指示变量求 $E[X]$，并与直接分布对照。

> [!success]- 练习参考答案
> $I_1,I_2$ 为各骰是否为 6，$E[I_j]=1/6$，$E[X]=1/3$。
> 直接：$P(X=0)=(5/6)^2$，$P(X=1)=2\cdot(1/6)(5/6)$，$P(X=2)=(1/6)^2$，
> $E[X]=0\cdot\ldots+1\cdot\frac{10}{36}+2\cdot\frac{1}{36}=\frac{12}{36}=\frac{1}{3}$。

## 参考

- Jeremy Orloff & Jennifer French Kamrin, *18.05 Introduction to Probability and Statistics*, Reading 4–5 (Discrete Random Variables), MIT OCW Spring 2022
- 课程主页：https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/
