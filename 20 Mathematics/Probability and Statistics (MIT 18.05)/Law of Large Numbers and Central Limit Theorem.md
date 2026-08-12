---
aliases:
  - 大数定律与中心极限定理
  - Law of Large Numbers
  - Central Limit Theorem
  - LLN CLT
tags: [math, probability_statistics]
up: "[[Probability and Statistics (MIT 18.05) MOC]]"
related:
  - "[[Joint Distributions Covariance and Correlation]]"
  - "[[Continuous Random Variables]]"
  - "[[Maximum Likelihood Estimation]]"
  - "[[Confidence Intervals]]"
  - "[[Hypothesis Testing]]"
down:
  - "[[Maximum Likelihood Estimation]]"
---
# 大数定律与中心极限定理

> [!summary] 核心结论
> 大数定律（LLN）：独立同分布、期望存在时，样本均值 $\bar X_n$ 依概率收敛到 $\mu$。中心极限定理（CLT）：再加有限方差时，$\sqrt{n}(\bar X_n-\mu)/\sigma$ 的分布逼近标准正态。LLN 说明“平均会稳”；CLT 说明“稳的速度与形状”——正态近似是区间估计、$z$/$t$ 检验、大量工程近似的理论支柱。

> 底本：MIT 18.05（Orloff / Kamrin）LLN / CLT 单元。

> 关键词：WLLN、CLT、标准化均值、连续性校正、正态近似

---

## 1. 设定与记号

设 $X_1,\ldots,X_n$ i.i.d.，$\mathbb{E}X_i=\mu$，$\operatorname{Var}X_i=\sigma^2<\infty$（CLT 需要方差；弱大数定律通常只需一阶矩）。样本均值
$$
\bar X_n=\frac{1}{n}\sum_{i=1}^n X_i.
$$
由线性与独立（或不相关）：
$$
\mathbb{E}[\bar X_n]=\mu,\qquad
\operatorname{Var}(\bar X_n)=\frac{\sigma^2}{n}.
$$
标准差（标准误）$\sigma/\sqrt{n}$ 以 $1/\sqrt{n}$ 收缩——这是“多测几次更准”的定量版本。

---

## 2. 弱大数定律（WLLN）直觉

**陈述（弱形式）**：对任意 $\varepsilon>0$，
$$
P\bigl(|\bar X_n-\mu|>\varepsilon\bigr)\to 0\quad(n\to\infty).
$$
即 $\bar X_n\xrightarrow{P}\mu$（依概率收敛）。

### 2.1 用切比雪夫看为什么

若方差有限，Chebyshev 给出
$$
P\bigl(|\bar X_n-\mu|\ge\varepsilon\bigr)
\le\frac{\operatorname{Var}(\bar X_n)}{\varepsilon^2}
=\frac{\sigma^2}{n\varepsilon^2}\to 0.
$$
这不是最一般的证明路径，但工科上足够说明：**方差按 $1/n$ 下降 $\Rightarrow$ 均值集中到 $\mu$。**

### 2.2 图示：相对频率稳定

掷公平硬币，$X_i\in\{0,1\}$，$\mu=1/2$。路径 $\bar X_n$ 抖动，但 $n$ 增大后贴住 $1/2$。

![[ps-lln.svg]]

> [!tip] LLN 不说的事
> 它不给出有限 $n$ 的误差分布，也不保证“下一次”更接近——它约束的是**样本均值**的集中，不是单次试验。

> [!example] 手算版“模拟”：切比雪夫给出有限 $n$ 上界
> 公平硬币 $X_i\in\{0,1\}$，$\mu=1/2$，$\sigma^2=1/4$。取 $\varepsilon=0.05$，$n=400$。
> $$
> P\bigl(|\bar X_{400}-0.5|\ge 0.05\bigr)
> \le \frac{(1/4)/400}{0.05^2}=\frac{0.000625}{0.0025}=0.25.
> $$
> 切比雪夫只给**上界** $0.25$（往往偏松）。CLT 更尖：
> $$
> Z=\frac{\bar X-0.5}{(0.5)/\sqrt{400}}=\frac{\bar X-0.5}{0.025},
> $$
> $P(|\bar X-0.5|\ge 0.05)\approx 2(1-\Phi(2))\approx 0.0456$。同题：LLN 说“会集中”；CLT 说“大约 4.6% 机会偏离 ≥0.05”。

> [!warning] 把 LLN 误读成“下一次更准”
> LLN 不保证第 $n+1$ 次试验更接近 $\mu$，也不消除赌徒谬误。它约束的是**平均值** $\bar X_n$，不是路径上的下一次结果。

---

## 3. 中心极限定理（CLT）

### 3.1 标准陈述

$X_i$ i.i.d.，$\mathbb{E}X_i=\mu$，$\operatorname{Var}X_i=\sigma^2\in(0,\infty)$。则
$$
Z_n=\frac{\bar X_n-\mu}{\sigma/\sqrt{n}}
=\frac{\sum_{i=1}^n X_i-n\mu}{\sigma\sqrt{n}}
$$
的分布函数收敛到 $\Phi$（标准正态 CDF）：
$$
P(Z_n\le z)\to\Phi(z)=\int_{-\infty}^{z}\frac{1}{\sqrt{2\pi}}e^{-t^2/2}\,dt.
$$
等价写法：$\bar X_n$ 近似 $\mathcal{N}(\mu,\sigma^2/n)$。

### 3.2 图示：偏态母体也能变正态

指数分布母体高度右偏；$\bar X_5$ 已开始对称化，$\bar X_{30}$ 已与正态密度重合得很好。

![[ps-clt.svg]]

> [!important] 记住标准化
> CLT 的“货币单位”是标准误 $\sigma/\sqrt{n}$。比较不同 $n$ 或不同 $\sigma$ 时，先标准化再谈“几个 $\sigma$”。

---

## 4. 何时近似够用？

经验规则（非定理）：

- **对称、轻尾**：$n\approx 20$–$30$ 常可用  
- **中等偏态**：$n$ 要更大  
- **Bernoulli / 二项**：常用规则 $np\ge 5$（或 $10$）且 $n(1-p)\ge 5$（或 $10$）  
- **重尾 / 极端离群**：均值本身可能不稳定；先检查模型假设

CLT 是**极限**结果：它保证大 $n$ 行为，不自动保证你的 $n=12$ 实验。

---

## 5. 二项 / 计数数据的正态近似与连续性校正

若 $S_n\sim\operatorname{Bin}(n,p)$，则 $S_n$ 是 $n$ 个 Bernoulli 之和，CLT 给出
$$
S_n\;\approx\;\mathcal{N}\bigl(np,\,np(1-p)\bigr).
$$
$S_n$ 取整数值，而正态连续。计算 $P(S_n\le k)$ 时，常用**连续性校正（continuity correction）**：
$$
P(S_n\le k)\approx P\bigl(Y\le k+0.5\bigr),\qquad
Y\sim\mathcal{N}(np,np(1-p)).
$$
类似地，$P(S_n\ge k)\approx P(Y\ge k-0.5)$。

> [!example] 粗算
> $n=100$，$p=0.5$，$P(S\le 40)$。均值 $50$，方差 $25$，标准差 $5$。
> 校正后 $z=(40.5-50)/5=-1.9$，查 $\Phi(-1.9)\approx 0.029$。

> [!example] 正态近似算均值区间概率（端到端）
> 灯泡寿命 i.i.d.，$\mu=1000$ h，$\sigma=100$ h。抽 $n=25$ 只，求 $P(980\le \bar X\le 1020)$。
> $$
> \mathrm{SE}=100/5=20,\qquad
> Z_{\mathrm{lo}}=\frac{980-1000}{20}=-1,\quad
> Z_{\mathrm{hi}}=\frac{1020-1000}{20}=1.
> $$
> $$
> P(-1\le Z\le 1)\approx \Phi(1)-\Phi(-1)=2\Phi(1)-1\approx 2\cdot 0.8413-1=0.6826.
> $$
> 即约 68%——与“$±1$ 个标准误”经验法则一致。若 $n=100$，SE$=10$，同样 $\pm 20$ 变成 $\pm 2$ SE，概率升至约 $95\%$。

校正在 $n$ 中等、对单个整数点概率敏感时更有用；$n$ 很大时 $\pm 0.5$ 相对标准误可忽略。

---

## 6. 为何 CLT 对统计至关重要

几乎所有“经典”入门推断都站在 CLT（或其精确正态/ $t$ 模型）上：

| 任务 | CLT 角色 |
|------|----------|
| 点估计精度 | $\bar X$ 的 SE $\approx s/\sqrt{n}$ |
| 置信区间 | $\bar X\pm z_{\alpha/2}\,\sigma/\sqrt{n}$（$\sigma$ 未知则用 $t$） |
| $z$ 检验 | 原假设下统计量近似标准正态 |
| 比例推断 | $\hat p$ 近似正态，SE $\sqrt{\hat p(1-\hat p)/n}$ |
| 蒙特卡洛 | 模拟均值的误差条同样用 $\sigma/\sqrt{n}$ |

MLE 渐近正态、Delta 方法、大量工程测量的不确定度合成，深层都依赖“许多独立扰动之和近似正态”。

> [!warning] 相关与非同分布
> 经典课堂 CLT 假设 i.i.d.。强相关时间序列、异方差、重尾无穷方差时，朴素 $\sigma/\sqrt{n}$ 区间会骗人。先问清抽样模型。

---

## 7. LLN 与 CLT 的分工

| | LLN | CLT |
|--|-----|-----|
| 问题 | $\bar X_n$ 去哪？ | 以多快、呈什么形状靠近？ |
| 极限对象 | $\bar X_n\to\mu$ | $\sqrt{n}(\bar X_n-\mu)$ 的分布 |
| 尺度 | 原始尺度 | 放大 $\sqrt{n}$ 后的波动 |
| 典型用途 | 频率稳定、估计一致性直觉 | 区间、检验、正态近似 |

一句话：**LLN 给一致性直觉，CLT 给推断的误差条。**

---

## 8. 标准化与“经验法则”

若 $Z\approx\mathcal{N}(0,1)$：

- $P(|Z|\le 1)\approx 68\%$  
- $P(|Z|\le 2)\approx 95\%$  
- $P(|Z|\le 3)\approx 99.7\%$

对 $\bar X_n$，把区间写成 $\mu\pm k\,\sigma/\sqrt{n}$。这是沟通测量精度时最常用的工科语言。

---

## 9. 与课程前后单元

- **前**：单变量期望/方差、独立和的方差 → $\operatorname{Var}(\bar X_n)=\sigma^2/n$。  
- **后**：[[Maximum Likelihood Estimation]] 的大样本标准误；[[Confidence Intervals]] 与 [[Hypothesis Testing]] 的正态参照；Bootstrap 在解析 SE 困难时用重抽样近似同一思想。

---

## 10. 自检与参考答案

1. 用 Chebyshev / 方差 $1/n$ 解释 WLLN：$\bar X_n\xrightarrow{P}\mu$。  
2. 会写 CLT 标准化形式，并用 $\mathcal{N}(\mu,\sigma^2/n)$ 近似 $\bar X_n$。  
3. 会对二项做正态近似，并在需要时加连续性校正 $\pm 0.5$。  
4. 能说明 CLT 如何支撑 CI、$z$ 检验与比例推断的误差语言。

> [!success]- 参考答案
> 1. $\mathrm{Var}(\bar X)=\sigma^2/n\to 0$，切比雪夫 $\Rightarrow P(|\bar X-\mu|\ge\varepsilon)\to 0$。
> 2. $Z_n=(\bar X_n-\mu)/(\sigma/\sqrt n)\Rightarrow N(0,1)$，故 $\bar X_n\approx\mathcal{N}(\mu,\sigma^2/n)$。
> 3. $S\approx\mathcal{N}(np,np(1-p))$；$P(S\le k)\approx P(Y\le k+0.5)$。
> 4. SE $=\sigma/\sqrt n$ 进入 CI 半宽与 $z$ 统计量；比例用 $\sqrt{\hat p(1-\hat p)/n}$。

> [!example] 练习：比例的 CLT
> $n=200$，$p=0.4$。用正态近似（带连续性校正）估计 $P(S\ge 90)$。

> [!success]- 练习参考答案
> 均值 $80$，方差 $200\cdot 0.4\cdot 0.6=48$，SD$\approx 6.928$。
> $P(S\ge 90)\approx P(Y\ge 89.5)$，$z=(89.5-80)/6.928\approx 1.37$，$1-\Phi(1.37)\approx 0.085$。

## 参考

- Jeremy Orloff & Jennifer French Kamrin, *18.05 Introduction to Probability and Statistics*, MIT OCW Spring 2022（LLN / CLT）
- https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/
