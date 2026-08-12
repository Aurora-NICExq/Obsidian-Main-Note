---
aliases:
  - 金融市场与一期模型
  - Financial Markets Bonds and One-Period Models
  - 一期市场模型
  - 债券与折现
  - one-period model
tags: [math, math_finance]
up: "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
related:
  - "[[Linear Algebra for Finance]]"
  - "[[Interest Rates Products and Models]]"
  - "[[Black-Scholes and Risk Neutral Valuation]]"
  - "[[Analytics of Finance (MIT 15.450) MOC]]"
  - "[[Economics MOC]]"
down:
  - "[[Linear Algebra for Finance]]"
---
# 金融市场、债券与一期模型

> [!summary] 核心结论
> 金融数学的第一块积木是**折现**与**一期市场**：今天价格 $p$，明天随机支付 $X$（或在有限情景 $\omega$ 下的支付向量）。组合 $\theta$ 的成本 $p\cdot\theta$，支付 $A\theta$（$A$ 为支付矩阵）。**无套利**粗说：零成本不能几乎必然得正收益；存在正状态价格（或风险中性概率）时线性定价 $p=A^\top\psi$。债券是确定性支付的特例——利率把“时间价值”写成折现因子。

> 底本：MIT 18.642 / 前身 18.S096（Kempthorne–Strela–Xia）；线性结构接 [[Linear Algebra for Finance]]，概率接 [[Probability and Stochastic Processes for Finance]]。

> 关键词：折现、零息债、支付矩阵、套利、状态价格

---

## 1. 市场语言（极简）

| 对象 | 直觉 |
|------|------|
| 现货 / 股票 | 今天买，明天随机卖出或分红 |
| 债券 | 承诺未来固定（或按规则浮动）的现金流 |
| 衍生品 | 支付由其他资产价格“派生” |
| 利率 | 钱的时间价格；折现把未来现金流拉回 $t=0$ |

本课先用**一期、有限情景**把定价写成线性代数，再逐步接到连续时间 BS / SDE。制度与宏观背景可对照 [[Economics MOC]]；更偏估计/控制的量化路径见 [[Analytics of Finance (MIT 15.450) MOC]]。

---

## 2. 折现与债券算术

无风险一期利率 $r$（按期复利）：今天 1 元 $\mapsto$ 明天 $1+r$ 元。折现因子
$$
D=\frac{1}{1+r}.
$$
面值 1 的**零息债**（zero）：今天价格 $P=D$，明天支付 1。

多期零息（离散）：到期 $T$ 的价格常写 $P(0,T)=\prod_{k=1}^{T}(1+r_k)^{-1}$，或用即期利率 $y_T$：
$$
P(0,T)=(1+y_T)^{-T}.
$$
附息债 = 各期票息 + 本金的零息组合（剥离 / stripping 直觉）。

> [!example] 两期数字
> $r_1=r_2=5\%$。面值 100、票息 5（每年一次）的两年附息债：
> $$
> \mathrm{Price}=\frac{5}{1.05}+\frac{105}{1.05^2}\approx 4.762+95.238=100.
> $$
> 平价：票息率 = 收益率时价格≈面值（此例精确平价）。

> [!warning] $r$ 不是“收益率”的全部
> 即期、远期、到期收益率（YTM）是不同对象。把附息债的 YTM 当成每一期真实折现率，会在曲线不平坦时算错对冲与久期——见 [[Interest Rates Products and Models]]。

---

## 3. 一期有限情景模型

情景 $\omega\in\{\omega_1,\ldots,\omega_m\}$。有 $n$ 种可交易资产：

- 今天价格向量 $p\in\mathbb{R}^n$；
- 明天支付矩阵 $A\in\mathbb{R}^{m\times n}$，$A_{ij}=$ 情景 $i$ 下资产 $j$ 的支付。

组合 $\theta\in\mathbb{R}^n$（可空头）：

- 成本：$V_0=p^\top\theta$；
- 支付向量：$V_1=A\theta\in\mathbb{R}^m$。

![[mf-one-period.svg]]

现金账户可并入某列：支付恒为 $1+r$，价格为 1。

---

## 4. 套利直觉

**第一类套利（粗说）**：存在 $\theta$ 使
$$
p^\top\theta\le 0,\quad A\theta\ge 0,\quad\text{且至少一个严格}.
$$
（零/负成本，支付非负且有正可能。）无套利 $\Rightarrow$ 定价必须“线性且正”——存在状态价格向量 $\psi\in\mathbb{R}^m_{++}$（或风险中性概率 $q$ 与折现）使
$$
p=A^\top\psi
$$
（在适当归一下 $\psi_i=D\,q_i$）。完整 FTAP 叙述留给教材；本课抓住：**支付落在列空间时价格由线性泛函决定，正性排除套利**。

> [!example] 两资产两情景
> 无风险：$p_0=1$，支付两情景皆 $1.1$（故 $r=10\%$）。风险资产：$p_1=10$，支付 $(12,\,9)^\top$。
> 支付矩阵（列=资产）
> $$
> A=\begin{pmatrix}1.1&12\\1.1&9\end{pmatrix}.
> $$
> 求状态价格：解 $A^\top\psi=p$。先对风险中性：令 $q$ 使
> $$
> 10=\frac{1}{1.1}\bigl(q\cdot 12+(1-q)\cdot 9\bigr)\Rightarrow 11=12q+9-9q\Rightarrow q=\tfrac{2}{3}.
> $$
> 则 $\psi=\frac{1}{1.1}(\tfrac{2}{3},\tfrac{1}{3})^\top$。任意衍生品支付 $X$ 的无套利价为 $\psi^\top X$。

---

## 5. 复制与完备

若 $A$ 列满秩且 $n=m$（或列空间 $=\mathbb{R}^m$），市场**完备**：任意支付可复制，价格唯一。$n<m$ 时不完备：无套利给出价格区间，需效用或外加测度选择——连续时间不完全市场同构这一问题。

复制：给定目标支付 $X$，解 $A\theta=X$；成本 $p^\top\theta$。这与 [[Linear Algebra for Finance]] 的“解线性方程组 / 投影”是同一几何。

---

## 6. 从债券到“确定性行”

若某资产在所有情景支付相同常数 $c$，则它像折现后的现金：$p=D\,c$。国债曲线提供一整族这样的确定性支付（不同到期）。风险资产的超额收益相对这条曲线度量。

远期利率：约定未来借款利率，使远期合约今日价值为零——由零息比定义：
$$
F(0;T,T+1)=\frac{P(0,T)}{P(0,T+1)}-1
$$
（离散一年期）。直觉：锁定未来一期融资成本。

---

## 7. 与后文的接口

| 后文 | 从本笔记带走什么 |
|------|------------------|
| [[Linear Algebra for Finance]] | $p,A,\theta$ 的向量/矩阵语言 |
| [[Interest Rates Products and Models]] | 零息、互换、久期 |
| [[Black-Scholes and Risk Neutral Valuation]] | 风险中性 $q$ → 连续极限下的 $\mathbb{Q}$ |
| [[Portfolio Management]] | 收益是支付减成本再归一 |

一期模型故意粗糙：真实市场连续交易、有摩擦、有跳跃。它的价值是把“价格 = 折现期望（在适当测度下）”钉死，避免一上来陷入 PDE。

---

## 8. 自检与参考答案

1. 写出折现因子 $D$ 与两年平价附息债价格公式（常数 $r$）。
2. 解释支付矩阵 $A$、组合成本与支付。
3. 用两情景例子说明风险中性概率如何给股票定价。
4. 完备 vs 不完备：列空间与价格唯一性。
5. 无套利与“存在正状态价格”的直觉联系。

> [!success]- 参考答案
> 1. $D=1/(1+r)$；票息 $C$、面值 $F$：$C/(1+r)+ (C+F)/(1+r)^2$。
> 2. $A_{ij}=$ 情景 $i$ 资产 $j$ 支付；$V_0=p^\top\theta$，$V_1=A\theta$。
> 3. $p=D\,\mathbb{E}^{\mathbb{Q}}[X]$；例中 $q=2/3$ 使股票超额收益在 $\mathbb{Q}$ 下均值为 0。
> 4. 列空间 $=\mathbb{R}^m$ ⇒ 可复制 ⇒ 无套利价唯一；否则仅区间。
> 5. 正线性定价泛函 $\Leftrightarrow$ 无（第一类）套利；$\psi$ 或 $(D,q)$ 即该泛函的坐标。

> [!example] 练习：衍生品定价
> 上节两情景市场中，看涨支付 $X=(\max(12-10,0),\max(9-10,0))^\top=(2,0)^\top$。求无套利价。

> [!success]- 练习参考答案
> $C=\psi^\top X=\frac{1}{1.1}\cdot\frac{2}{3}\cdot 2=\frac{4}{3.3}=\frac{40}{33}\approx 1.212$。
> 或 $C=D(q\cdot 2+(1-q)\cdot 0)$。

## 参考

- Peter Kempthorne, Vasily Strela, Jake Xia, *18.642 Topics in Mathematics with Applications in Finance*, MIT OCW Fall 2024（及 18.S096 Fall 2013）
- https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/
