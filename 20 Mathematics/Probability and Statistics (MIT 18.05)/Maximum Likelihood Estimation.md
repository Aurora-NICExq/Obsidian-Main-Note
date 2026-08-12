---
aliases:
  - 最大似然估计
  - Maximum Likelihood Estimation
  - MLE
  - Likelihood
tags: [math, probability_statistics]
up: "[[Probability and Statistics (MIT 18.05) MOC]]"
related:
  - "[[Law of Large Numbers and Central Limit Theorem]]"
  - "[[Bayesian Inference]]"
  - "[[Confidence Intervals]]"
  - "[[Hypothesis Testing]]"
  - "[[Discrete Random Variables]]"
down:
  - "[[Bayesian Inference]]"
---
# 最大似然估计

> [!summary] 核心结论
> 似然 $L(\theta\mid\mathrm{data})$ 把“参数 $\theta$ 下看见这些数据有多合理”写成 $\theta$ 的函数。最大似然估计（MLE）取使似然最大的 $\hat\theta$。Bernoulli 得 $\hat p=\bar X$；正态均值（方差已知或未知）得 $\hat\mu=\bar X$。MLE 具有不变性：$g(\hat\theta)$ 是 $g(\theta)$ 的 MLE。大样本下 MLE 常近似正态，标准误由 Fisher 信息给出——这是从概率模型走向区间估计与检验的桥梁。

> 底本：MIT 18.05（Orloff / Kamrin）估计 / MLE 单元。

> 关键词：likelihood、MLE、log-likelihood、invariance、Fisher information（简介）

---

## 1. 从概率到似然：角色对调

参数模型：数据 $X$ 的 PMF/PDF 为 $f(x\mid\theta)$（离散写 $p$）。

- **概率视角**：$\theta$ 固定，把 $f(\,\cdot\mid\theta)$ 当 $x$ 的函数 → 描述随机性。  
- **似然视角**：数据 $x$ 已观察到，把
  $$
  L(\theta\mid x)=f(x\mid\theta)
  $$
  当 $\theta$ 的函数 → 比较哪个参数“更像”产生了这份数据。

$L$ 一般**不是** $\theta$ 上的概率密度（积分不必为 1）。比较的是相对高低，不是绝对概率。

独立样本 $x_1,\ldots,x_n$：
$$
L(\theta)=\prod_{i=1}^n f(x_i\mid\theta).
$$
数值上几乎总是改用对数似然
$$
\ell(\theta)=\log L(\theta)=\sum_{i=1}^n\log f(x_i\mid\theta),
$$
把乘积变求和，并改善浮点下溢。

---

## 2. MLE 定义

$$
\hat\theta_{\mathrm{MLE}}
=\arg\max_{\theta\in\Theta}L(\theta)
=\arg\max_{\theta\in\Theta}\ell(\theta).
$$

常见求法：

1. 对 $\ell$ 求导，解 $\ell'(\theta)=0$（得分方程）  
2. 检查二阶导 $\ell''<0$ 或边界行为，确认是最大  
3. 支撑依赖参数时（如 $\mathrm{Unif}(0,\theta)$），导数法可能失效，需直接分析 $L$

> [!warning] 支撑踩雷
> 均匀分布 $\mathrm{Unif}(0,\theta)$ 的 MLE 是 $X_{(n)}=\max_i X_i$，不是某个内部临界点。先看似然在参数空间上是否光滑。

---

## 3. 例：Bernoulli / 二项比例

$X_i\stackrel{\mathrm{iid}}{\sim}\mathrm{Bern}(p)$，$p\in(0,1)$。设 $k=\sum x_i$ 为成功次数，则
$$
L(p)=p^{k}(1-p)^{n-k},\qquad
\ell(p)=k\log p+(n-k)\log(1-p).
$$
$$
\ell'(p)=\frac{k}{p}-\frac{n-k}{1-p}=0
\quad\Rightarrow\quad
\hat p=\frac{k}{n}=\bar x.
$$
（端点 $p=0,1$ 仅在全 0/全 1 数据时需单独讨论。）

![[ps-mle-likelihood.svg]]

图中 $n=20$，$k=12$，峰值恰在 $12/20=0.6$。

> [!tip] 与矩估计
> 此例 MLE 与矩估计相同。一般模型二者可不同；MLE 通常有更好的大样本性质。

> [!example] Bernoulli MLE 端到端
> 观测 $x=(1,0,1,1,0,1,1,1,0,1)$，故 $n=10$，$k=7$。
> $$
> L(p)=p^7(1-p)^3,\qquad
> \ell(p)=7\log p+3\log(1-p).
> $$
> $$
> \ell'(p)=\frac{7}{p}-\frac{3}{1-p}=0
> \quad\Rightarrow\quad 7(1-p)=3p
> \quad\Rightarrow\quad \hat p=0.7.
> $$
> $\ell''(p)=-7/p^2-3/(1-p)^2<0$，确为最大。不变性：$\widehat{p(1-p)}=0.7\cdot 0.3=0.21$。
> 大样本 SE：$I(p)=1/(p(1-p))$（Bernoulli），$\widehat{\mathrm{SE}}\approx\sqrt{0.21/10}\approx 0.145$，
> 近似 $95\%$ CI：$0.7\pm 1.96\cdot 0.145\approx[0.42,\,0.98]$。

---

## 4. 例：正态均值

$X_i\stackrel{\mathrm{iid}}{\sim}\mathcal{N}(\mu,\sigma^2)$。

### 4.1 $\sigma^2$ 已知，估 $\mu$

$$
\ell(\mu)=-\frac{n}{2}\log(2\pi\sigma^2)-\frac{1}{2\sigma^2}\sum_{i=1}^n(x_i-\mu)^2.
$$
最大化 $\ell$ $\Leftrightarrow$ 最小化平方和，故
$$
\hat\mu=\bar x.
$$

### 4.2 $\sigma^2$ 也未知

对 $(\mu,\sigma^2)$ 联合最大化，得
$$
\hat\mu=\bar x,\qquad
\hat\sigma^2=\frac{1}{n}\sum_{i=1}^n(x_i-\bar x)^2.
$$
注意分母是 $n$ 不是 $n-1$：$n-1$ 版本是无偏样本方差，**不是** MLE。小样本无偏与大样本效率是不同设计目标。

> [!example] 正态 $(\mu,\sigma^2)$ 联合 MLE
> 数据 $x=(2,3,5,6,4)$，$n=5$，$\bar x=4$。
> $$
> \hat\mu=4,\qquad
> \hat\sigma^2=\frac{1}{5}\bigl[(2-4)^2+(3-4)^2+(5-4)^2+(6-4)^2+(4-4)^2\bigr]
> =\frac{4+1+1+4+0}{5}=2.
> $$
> 无偏样本方差 $s^2=\frac{10}{4}=2.5\neq\hat\sigma^2$。似然在 $(\hat\mu,\hat\sigma^2)=(4,2)$ 处最大。

> [!warning] 不要把无偏 $s^2$ 当成 MLE
> 考试/推导问 MLE 时分母必须是 $n$。用 $s^2$ 做 $t$ 区间是另一套频率派设计，不是“MLE 写错了”。

---

## 5. 计算套路（工科清单）

1. 写出联合 PMF/PDF（独立则乘积）  
2. 丢掉与 $\theta$ 无关的常数因子（可选，不影响 $\arg\max$）  
3. 取对数 $\ell(\theta)$  
4. $\partial\ell/\partial\theta=0$ 求解；多参数则梯度为零  
5. 用二阶导 / Hessian / 边界比较确认最大  
6. 若参数有约束（如 $p\in[0,1]$），检查约束激活情形

多参数时也可能无闭式解 → 数值优化（牛顿法、BFGS）；18.05 以可手算例子为主。

---

## 6. 不变性（invariance）

若 $\hat\theta$ 是 $\theta$ 的 MLE，且 $g$ 是函数，则 $g(\hat\theta)$ 是 $g(\theta)$ 的 MLE。

> [!example]
> Bernoulli：$\widehat{p(1-p)}=\hat p(1-\hat p)$。  
> 正态：$\widehat{\sigma}=\sqrt{\hat\sigma^2}$（取正根）。

注意：若 $g$ 不可逆，$g(\theta)$ 的“似然”需用像诱导；课堂层面记住**先估 $\theta$ 再代入 $g$** 即可。

不变性使“先估自然参数再变换”合法，避免为每个感兴趣的函数重推一遍似然。

---

## 7. 大样本性质（与统计单元的接口）

在正则条件下（支撑不随 $\theta$ 变、可微可积等），当 $n\to\infty$：

1. **一致性**：$\hat\theta\xrightarrow{P}\theta$（与 [[Law of Large Numbers and Central Limit Theorem|LLN]] 精神一致）  
2. **渐近正态**：
   $$
   \sqrt{n}\,(\hat\theta-\theta)
   \;\Rightarrow\;
   \mathcal{N}\bigl(0,\,1/I(\theta)\bigr),
   $$
   其中 $I(\theta)$ 为 Fisher 信息（单观测），
   $$
   I(\theta)=\mathbb{E}_\theta\Bigl[\bigl(\partial_\theta\log f(X\mid\theta)\bigr)^2\Bigr]
   =-\mathbb{E}_\theta[\partial_{\theta\theta}\log f(X\mid\theta)].
   $$
3. **近似标准误**：$\operatorname{SE}(\hat\theta)\approx 1/\sqrt{nI(\hat\theta)}$（或用观测信息 $-\ell''(\hat\theta)$）

由此立刻得到近似置信区间
$$
\hat\theta\pm z_{\alpha/2}\,\widehat{\operatorname{SE}},
$$
以及 Wald 型检验。这正是课程后半 **CI / NHST** 对“估计量波动”的默认语言。

> [!warning] 正则条件
> 均匀分布上端点等非正则例子：MLE 收敛更快或渐近分布非正态。套用 $z$ 区间前先确认模型类型。

---

## 8. MLE vs 贝叶斯（预告）

| | MLE（频率派点估计） | 贝叶斯 |
|--|---------------------|--------|
| 随机对象 | 数据；$\theta$ 固定未知 | $\theta$ 有先验 |
| 输出 | 一个 $\hat\theta$（及 SE） | 后验分布 |
| 小样本 | 可能不稳定 / 贴边界 | 先验可正则化 |
| 大样本 | 与后验众数等常接近 | 先验影响减弱 |

详见 [[Bayesian Inference]]。两者都从同一似然函数出发，差在是否把 $\theta$ 随机化并乘先验。

---

## 9. 常见模型速查

| 模型 | MLE |
|------|-----|
| $\mathrm{Bern}(p)$ | $\hat p=\bar x$ |
| $\mathrm{Pois}(\lambda)$ | $\hat\lambda=\bar x$ |
| $\mathcal{N}(\mu,\sigma^2)$，$\sigma$ 已知 | $\hat\mu=\bar x$ |
| $\mathcal{N}(\mu,\sigma^2)$ 皆未知 | $\hat\mu=\bar x$，$\hat\sigma^2=n^{-1}\sum(x_i-\bar x)^2$ |
| $\mathrm{Exp}(\lambda)$（率参数） | $\hat\lambda=1/\bar x$ |
| $\mathrm{Unif}(0,\theta)$ | $\hat\theta=X_{(n)}$ |

---

## 10. 自检与参考答案

1. 会写似然与对数似然；用求导（或边界分析）求 MLE。  
2. 记住 Bernoulli $\hat p=\bar x$、正态 $\hat\mu=\bar x$ 与 $\hat\sigma^2$（分母 $n$）。  
3. 会用不变性：$g(\hat\theta)$ 是 $g(\theta)$ 的 MLE。  
4. 知道大样本 SE $\approx 1/\sqrt{nI(\hat\theta)}$，并连接 CI / 检验语言。

> [!success]- 参考答案
> 1. $L=\prod f(x_i\mid\theta)$，$\ell=\sum\log f$；解 $\ell'=0$ 并确认最大；支撑依赖参数时看边界。
> 2. $\hat p=k/n$；$\hat\mu=\bar x$；$\hat\sigma^2=n^{-1}\sum(x_i-\bar x)^2$。
> 3. 先求 $\hat\theta$，再 $g(\hat\theta)$ 即为 $g(\theta)$ 的 MLE。
> 4. 渐近 $\hat\theta\approx\mathcal{N}(\theta,1/(nI(\theta)))$，故 CI $\hat\theta\pm z\widehat{\mathrm{SE}}$。

> [!example] 练习：Poisson MLE
> 观测计数 $3,1,4,2,5$。求 $\hat\lambda$，并用 $I(\lambda)=1/\lambda$ 写近似 $95\%$ CI。

> [!success]- 练习参考答案
> $\hat\lambda=\bar x=3$。$\widehat{\mathrm{SE}}\approx\sqrt{3/5}\approx 0.775$，
> CI $\approx 3\pm 1.96\cdot 0.775\approx[1.48,\,4.52]$。

## 参考

- Jeremy Orloff & Jennifer French Kamrin, *18.05 Introduction to Probability and Statistics*, MIT OCW Spring 2022（MLE / estimation）
- https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/
