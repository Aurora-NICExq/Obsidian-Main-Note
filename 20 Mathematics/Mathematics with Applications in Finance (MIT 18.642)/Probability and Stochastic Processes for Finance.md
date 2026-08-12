---
aliases:
  - 金融中的概率与随机过程
  - Probability and Stochastic Processes for Finance
  - 随机游走与布朗运动
  - martingale finance
tags: [math, math_finance]
up: "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
related:
  - "[[Linear Algebra for Finance]]"
  - "[[Time Series Analysis for Finance]]"
  - "[[Stochastic Calculus and SDEs]]"
  - "[[Black-Scholes and Risk Neutral Valuation]]"
  - "[[Probability and Statistics (MIT 18.05) MOC]]"
  - "[[Law of Large Numbers and Central Limit Theorem]]"
  - "[[Continuous Random Variables]]"
down:
  - "[[Regression and PCA in Finance]]"
---
# 金融中的概率与随机过程

> [!summary] 核心结论
> 价格与收益被建成随机过程：离散时间看**随机游走**与条件期望；连续极限给出**布朗运动**直觉。**鞅**是“公平游戏”——在风险中性测度下，折现资产价格是鞅，这是无套利定价的概率语言。本笔记保持轻量：接 18.05 的期望/方差/正态，为 [[Stochastic Calculus and SDEs]] 与 BS 铺路。

> 底本：MIT 18.642 概率与随机过程单元；底座 [[Probability and Statistics (MIT 18.05) MOC]]。

> 关键词：随机游走、布朗运动、滤过、鞅、独立增量

---

## 1. 从随机变量到过程

时刻 $t=0,1,\ldots,T$（或连续 $t\in[0,T]$），$X_t$ 为价格、对数价格或累积收益。路径 $\{X_t(\omega)\}$ 是样本轨道。信息流用滤过 $(\mathcal{F}_t)$ 表示“到 $t$ 为止可知”——交易策略 $\theta_t$ 须**非预期**（不能看未来）。

单期收益 $R_{t+1}=(S_{t+1}-S_t)/S_t$；对数收益 $r_{t+1}=\log(S_{t+1}/S_t)$ 更利于连加与正态近似（见 CLT：[[Law of Large Numbers and Central Limit Theorem]]）。

---

## 2. 随机游走

简单对称 RW：$X_{k}=X_0+\sum_{i=1}^k\xi_i$，$\xi_i=\pm 1$ i.i.d. 等概。则
$$
\mathbb{E}[X_{k+1}\mid\mathcal{F}_k]=X_k
$$
——已是鞅。金融常写
$$
S_{t+1}=S_t(1+\mu\Delta t+\sigma\sqrt{\Delta t}\,Z_{t+1}),\quad Z\sim N(0,1)\ \mathrm{i.i.d.}
$$
或乘性：对数价格做 RW。均值 $\mu$、波动 $\sigma$ 是漂移与扩散的离散影子。

> [!example] 十步随机游走
> $X_0=0$，$\xi=\pm 1$ 等概。$\mathbb{E}[X_{10}]=0$，$\mathrm{Var}(X_{10})=10$。约 $95\%$ 落在 $\pm 2\sqrt{10}\approx\pm 6.3$（正态近似）。股价对数在短窗常借用此尺度直觉，但真实收益有肥尾与波动聚集——见 [[Volatility Modeling]]。

---

## 3. 布朗运动直觉

标准布朗运动（维纳过程）$W_t$：

1. $W_0=0$；
2. 独立增量；$W_t-W_s\sim N(0,t-s)$；
3. 路径连续（几乎处处）。

缩放极限：随机游走步长 $\sqrt{\Delta t}$、步数 $t/\Delta t$，弱收敛到 $W_t$。带漂移：
$$
X_t=X_0+\mu t+\sigma W_t.
$$
几何布朗运动（GBM）$S_t=S_0\exp\bigl((\mu-\tfrac12\sigma^2)t+\sigma W_t\bigr)$ 是 BS 的经典假设——细节在 [[Stochastic Calculus and SDEs]]。

> [!warning] 连续路径 ≠ 现实无跳跃
> BM / GBM 是可算的理想化。新闻跳空、流动性断裂要用跳跃过程；本课先掌握连续核心。

---

## 4. 条件期望与鞅（轻触）

$M_t$ 为鞅：$\mathbb{E}[|M_t|]<\infty$ 且
$$
\mathbb{E}[M_{t}\mid\mathcal{F}_s]=M_s\quad(s\le t).
$$
直觉：已知现在，未来增量期望为零。

**风险中性叙事（一期已见）**：存在等价测度 $\mathbb{Q}\sim\mathbb{P}$，使折现价格 $\tilde S_t=S_t/B_t$ 为 $\mathbb{Q}$-鞅，则
$$
S_0=\mathbb{E}^{\mathbb{Q}}[\tilde S_T]\cdot B_0\text{ 等形式}.
$$
物理测度 $\mathbb{P}$ 下股票有风险溢价，故 $\tilde S$ 一般**不是** $\mathbb{P}$-鞅。定价用 $\mathbb{Q}$，风险评估常仍看 $\mathbb{P}$——不要混。

---

## 5. 正态、对数正态与厚尾

若 $\log S_T\sim N(m,s^2)$，则 $S_T$ 对数正态：
$$
\mathbb{E}[S_T]=e^{m+s^2/2},\quad
\mathbb{E}[(S_T-K)^+]
$$
可写成 BS 式积分（Black–Scholes 公式来源）。经验：日收益峰度常 $>3$，正态只是一阶工作假设；稳健做法用 $t$ 分布、混合分布或已实现波动——课程要求先会正态计算（[[Continuous Random Variables]]）。

> [!example] 对数正态期望
> $\log S\sim N(\log 100-0.5\cdot0.2^2,\ 0.2^2)$（一年、$\mu=0$ 的风险中性漂移简化）。则 $\mathbb{E}[S]=100$。若误把 $\mathbb{E}[S]=e^{\mathbb{E}[\log S]}$ 会得到 $100\cdot e^{-0.02}\approx 98$——漏了 Itô / 对数正态修正项 $\tfrac12\sigma^2$。

---

## 6. 与时间序列的分工

| 本笔记 | [[Time Series Analysis for Finance]] |
|--------|--------------------------------------|
| 概率结构、鞅、BM | ACF、ARMA、平稳、预测 |
| 测度变换直觉 | 样本相关与检验 |
| 为 SDE 服务 | 为计量与交易信号服务 |

随机过程提供**模型**；时间序列提供**在数据上识别与诊断**的工具。

---

## 7. 停时与可选抽样（直觉）

若 $M$ 为鞅，$\tau$ 有界停时，则 $\mathbb{E}[M_\tau]=\mathbb{E}[M_0]$（可选抽样，条件从略）。含义：没有免费的“看到好价再卖”策略——在无套利/鞅测度下，停止规则不创造超额期望。这与技术分析里“等突破再买必赚”的幻想相反（忽略风险溢价与测度）。

> [!example] 赌徒停手
> 对称随机游走是鞅；任何有界停时退出，期望仍在起点。有限资本或非对称回报会破坏“公平”，但那是换问题，不是推翻鞅定理。

---

## 8. 相关布朗运动

两资产 $\mathrm{d}W^1,\mathrm{d}W^2$ 相关 $\rho$：$\mathrm{d}W^1\mathrm{d}W^2=\rho\mathrm{d}t$。组合瞬时方差
$$
\sigma_p^2=w_1^2\sigma_1^2+w_2^2\sigma_2^2+2w_1w_2\rho\sigma_1\sigma_2
$$
与单期公式同构，只是瞬时版本——接 [[Portfolio Management]]。

---

## 9. 自检与参考答案

1. 写出简单随机游走并验证鞅性质（对称情形）。
2. 陈述布朗运动三条性质；解释 $\mathrm{Var}(W_t)=t$。
3. 区分 $\mathbb{P}$ 与 $\mathbb{Q}$ 下折现价格是否为鞅。
4. 为何 $\mathbb{E}[e^{\sigma W_t}]=e^{\sigma^2 t/2}$。
5. 对数收益 vs 简单收益：何时近似相等。

> [!success]- 参考答案
> 1. $X_{k+1}=X_k+\xi_{k+1}$，$\mathbb{E}[\xi]=0\Rightarrow\mathbb{E}[X_{k+1}\mid\mathcal{F}_k]=X_k$。
> 2. $W_0=0$；独立正态增量；连续路径。增量方差 $=t-s$，故 $\mathrm{Var}(W_t)=t$。
> 3. 无套利下存在 $\mathbb{Q}$ 使折现价格为 $\mathbb{Q}$-鞅；$\mathbb{P}$ 下通常有漂移溢价。
> 4. 矩母函数：$\mathbb{E}[e^{uZ}]=e^{u^2/2}$，$Z\sim N(0,1)$，取 $u=\sigma\sqrt{t}$。
> 5. 小收益时 $R\approx r$；多期连乘用对数更干净。

> [!example] 练习：两期二项
> $S_0=100$，每期 $\times u=1.1$ 或 $\times d=0.9$，无风险 $r=0$ / 期（$D=1$）。求风险中性 $q$。

> [!success]- 练习参考答案
> $100=q\cdot110+(1-q)\cdot90\Rightarrow 100=90+20q\Rightarrow q=1/2$。
> （$r=0$ 时期望收益在 $\mathbb{Q}$ 下也为 0。）

## 参考

- MIT 18.642 / 18.S096 probability & stochastic processes lectures
- https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/
- [[Probability and Statistics (MIT 18.05) MOC]]
