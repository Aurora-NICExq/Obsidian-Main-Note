---
aliases:
  - 金融分析
  - Analytics of Finance
  - MIT 15.450
  - 金融定量分析
  - Kogan 15.450
tags: [math, analytics_finance, MOC]
up: "[[Mathematics MOC]]"
related:
  - "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
  - "[[Probability and Statistics (MIT 18.05) MOC]]"
  - "[[Economics MOC]]"
down:
  - "[[No Arbitrage and Risk Neutral Pricing]]"
  - "[[Ito Calculus for Finance]]"
  - "[[Black-Scholes Model and Extensions]]"
  - "[[Interest Rate Models]]"
  - "[[Dynamic Programming and Asset Allocation]]"
  - "[[Monte Carlo Methods for Derivatives]]"
  - "[[Financial Econometrics MLE and QMLE]]"
  - "[[GMM and Inference in Finance]]"
  - "[[Bootstrap Methods in Finance]]"
  - "[[Volatility Models GARCH]]"
  - "[[Return Predictability]]"
---
# Analytics of Finance (MIT 15.450) MOC

> 课程底本：[MIT 15.450 Analytics of Finance (Fall 2010)](https://ocw.mit.edu/courses/15-450-analytics-of-finance-fall-2010/)（Leonid Kogan，Sloan）。覆盖金融定量方法：无套利 / 风险中性定价、Itô 与衍生品、利率模型、动态规划与资产配置、Monte Carlo、以及 MLE/QMLE、GMM、Bootstrap、GARCH、收益可预测性等金融计量工具。讲义 / 作业 / 考试可离线下载。
>
> **与 [[Mathematics with Applications in Finance (MIT 18.642) MOC]] 的分工：** 18.642 偏量化数学总览（市场、线代、时序、组合、BS 入门）；本课加深**定价与推断的操作工具**（风险中性路径、蒙特卡洛减方差、GMM/HAC、block bootstrap、GARCH 估计、样本内外可预测性）。建议先扫 18.642 相关笔记，再读本夹加深。
>
> **课内常引教材（仅作参考书目，非原文转载）：** Kerry Back, *A Course in Derivative Securities*；Ruey S. Tsay, *Analysis of Financial Time Series*；John H. Cochrane, *Asset Pricing*；Campbell / Lo / MacKinlay (CL&M), *The Econometrics of Financial Markets*。

![[af-moc-roadmap.svg]]

## 01 定价骨架：无套利 → Itô → BS / 利率
- [[No Arbitrage and Risk Neutral Pricing]]：FTAP、风险中性测度、一期完备市场数值例
- [[Ito Calculus for Finance]]：GBM、Itô 公式、简单应用（对照 [[Stochastic Calculus and SDEs]]）
- [[Black-Scholes Model and Extensions]]：PDE vs $\mathbb{E}^\mathbb{Q}$、Greeks、股息 / 时变波动（对照 [[Black-Scholes and Risk Neutral Valuation]]）
- [[Interest Rate Models]]：短期利率直觉 Vasicek / CIR（对照 [[Interest Rates Products and Models]]）

## 02 决策与模拟
- [[Dynamic Programming and Asset Allocation]]：Bellman、Merton、短视 vs 对冲需求（对照 [[Portfolio Management]]）
- [[Monte Carlo Methods for Derivatives]]：风险中性路径、粗 MC 方差、对偶 / 控制变量

## 03 金融计量与推断
- [[Financial Econometrics MLE and QMLE]]：收益似然、QMLE 稳健性（接 [[Maximum Likelihood Estimation]]）
- [[GMM and Inference in Finance]]：矩条件、OLS as GMM、HAC SE
- [[Bootstrap Methods in Finance]]：块 Bootstrap 与时间序列警告（接 [[Bootstrap Methods]]）
- [[Volatility Models GARCH]]：GARCH(1,1)、持续性、估计直觉（对照 [[Volatility Modeling]]）
- [[Return Predictability]]：样本内 vs 样本外、数据挖掘警告（接 [[Linear Regression]]、[[Hypothesis Testing]]）

## 插图（预生成 SVG）

嵌入 `90 Assets/diagrams/analytics-finance/`（`af-….svg`）。重新生成：

```bash
cd "90 Assets/scripts/analytics_finance"
python3 generate_all.py
```

| 文件 | 用途 |
|------|------|
| `af-moc-roadmap.svg` | 本 MOC 路线 |
| `af-risk-neutral.svg` | 无套利 → 风险中性 |
| `af-monte-carlo.svg` | GBM 蒙特卡洛路径 |
| `af-dynamic-opt.svg` | 动态资产配置 |
| `af-gmm.svg` | GMM 估计素描 |
| `af-garch.svg` | GARCH 条件波动 |
