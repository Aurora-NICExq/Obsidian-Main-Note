---
aliases: [概率论, 数理统计, Probability and Statistics, MIT 18.05, 概率论及数理统计]
tags: [math, probability_statistics, MOC]
up: "[[Mathematics MOC]]"
related:
  - "[[Complex Analysis (MIT 18.04) MOC]]"
  - "[[Linear Algebra (MIT 18.06) MOC]]"
  - "[[Signals Systems and Inference (MIT 6.011) MOC]]"
  - "[[Estimation and Kalman Filtering (NPTEL) MOC]]"
  - "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
  - "[[Analytics of Finance (MIT 15.450) MOC]]"
down:
  - "[[Counting and Probability Basics]]"
  - "[[Conditional Probability and Bayes Theorem]]"
  - "[[Discrete Random Variables]]"
  - "[[Continuous Random Variables]]"
  - "[[Joint Distributions Covariance and Correlation]]"
  - "[[Law of Large Numbers and Central Limit Theorem]]"
  - "[[Maximum Likelihood Estimation]]"
  - "[[Bayesian Inference]]"
  - "[[Hypothesis Testing]]"
  - "[[Confidence Intervals]]"
  - "[[Bootstrap Methods]]"
  - "[[Linear Regression]]"
---
# Probability and Statistics (MIT 18.05) MOC

> 课程底本：[MIT 18.05 Introduction to Probability and Statistics (Spring 2022)](https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/)（Jeremy Orloff / Jennifer French Kamrin）。概率公理 → 随机变量与极限定理 → 频率派 / 贝叶斯推断 → 区间、Bootstrap 与回归。讲义 / 作业 / 考试可离线下载。

![[ps-moc-roadmap.svg]]

## 01 概率基础
- [[Counting and Probability Basics]]：计数、样本空间、公理、等可能、容斥
- [[Conditional Probability and Bayes Theorem]]：条件概率、独立性、Bayes、基础比率

## 02 随机变量与极限
- [[Discrete Random Variables]]：PMF、期望方差、Bernoulli / Binomial / Poisson / Geometric
- [[Continuous Random Variables]]：PDF、分位数、Uniform / Exp / Normal、标准化
- [[Joint Distributions Covariance and Correlation]]：联合 / 边际 / 条件、Cov、Corr、$\mathrm{Var}(X+Y)$
- [[Law of Large Numbers and Central Limit Theorem]]：WLLN、CLT、连续修正、对统计的意义

## 03 推断
- [[Maximum Likelihood Estimation]]：似然、MLE、不变性
- [[Bayesian Inference]]：先验 / 后验、Beta–Binomial、可信区间
- [[Hypothesis Testing]]：NHST、$p$ 值、$z$/$t$/$\chi^2$、与贝叶斯对照

## 04 区间与回归
- [[Confidence Intervals]]：覆盖率、$z$/$t$/比例区间、三种视角
- [[Bootstrap Methods]]：重抽样、百分位 CI、适用边界
- [[Linear Regression]]：OLS、残差、$R^2$、多元投影视角

## 插图（预生成 SVG）

嵌入 `90 Assets/diagrams/probability-and-statistics/`（文件名形如 `ps-….svg`）。重新生成：

```bash
cd "90 Assets/scripts/probability_and_statistics"
.venv/bin/python generate_all.py
```
