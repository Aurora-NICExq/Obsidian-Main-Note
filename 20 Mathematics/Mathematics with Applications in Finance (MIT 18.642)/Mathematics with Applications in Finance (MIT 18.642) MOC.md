---
aliases:
  - 金融数学
  - MIT 18.642
  - 18.S096
  - Mathematics with Applications in Finance
  - Topics in Mathematics with Applications in Finance
tags: [math, math_finance, MOC]
up: "[[Mathematics MOC]]"
related:
  - "[[Probability and Statistics (MIT 18.05) MOC]]"
  - "[[Linear Algebra (MIT 18.06) MOC]]"
  - "[[Analytics of Finance (MIT 15.450) MOC]]"
  - "[[Economics MOC]]"
down:
  - "[[Financial Markets Bonds and One-Period Models]]"
  - "[[Linear Algebra for Finance]]"
  - "[[Probability and Stochastic Processes for Finance]]"
  - "[[Regression and PCA in Finance]]"
  - "[[Interest Rates Products and Models]]"
  - "[[Time Series Analysis for Finance]]"
  - "[[Portfolio Management]]"
  - "[[Volatility Modeling]]"
  - "[[Black-Scholes and Risk Neutral Valuation]]"
  - "[[Stochastic Calculus and SDEs]]"
  - "[[Machine Learning in Finance]]"
---
# Mathematics with Applications in Finance (MIT 18.642) MOC

> 课程底本：[MIT 18.642 Topics in Mathematics with Applications in Finance (Fall 2024)](https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/)（Peter Kempthorne / Vasily Strela / Jake Xia）。先修：微分方程、[[Probability and Statistics (MIT 18.05) MOC|概率 (18.05)]]、[[Linear Algebra (MIT 18.06) MOC|线性代数 (18.06)]]。本课是 **18.S096**（Fall 2013）的更新版；旧站仍有大量讲义与录像可离线对照。目标：把线性代数、概率、随机过程与数值方法接到金融业常见模型（定价、利率、组合、波动、BS / SDE、轻量 ML）。

![[mf-moc-roadmap.svg]]

## 01 市场与线性结构
- [[Financial Markets Bonds and One-Period Models]]：折现、债券、一期支付矩阵与无套利直觉
- [[Linear Algebra for Finance]]：组合作向量、线性定价、为 PCA 铺垫

## 02 概率、回归与因子
- [[Probability and Stochastic Processes for Finance]]：随机游走、布朗运动直觉、鞅轻触
- [[Regression and PCA in Finance]]：因子模型、收益率曲线 PCA
- [[Interest Rates Products and Models]]：债券/互换直觉、久期（高层）

## 03 时间序列与组合
- [[Time Series Analysis for Finance]]：AR/MA/ACF 与收益序列
- [[Portfolio Management]]：均值–方差、有效前沿、CAPM 素描

## 04 波动、定价与随机微积分
- [[Volatility Modeling]]：历史 vs 隐含、波动聚集
- [[Black-Scholes and Risk Neutral Valuation]]：风险中性、看涨公式直觉、Delta 对冲素描
- [[Stochastic Calculus and SDEs]]：Itô 积/商法则、GBM

## 05 机器学习（概览）
- [[Machine Learning in Finance]]：监督预测的陷阱（过拟合、非平稳）——对应课程 ML 讲座的轻量笔记

## 与姐妹课
- 数学底座：[[Probability and Statistics (MIT 18.05) MOC]]、[[Linear Algebra (MIT 18.06) MOC]]
- 金融分析深化（随机控制 / 估计视角）：[[Analytics of Finance (MIT 15.450) MOC]]
- 制度与宏观语境：[[Economics MOC]]

## 插图（预生成 SVG）

嵌入 `90 Assets/diagrams/math-finance/`（`mf-….svg`）。重新生成：

```bash
cd "90 Assets/scripts/math_finance"
.venv/bin/python generate_all.py
```
