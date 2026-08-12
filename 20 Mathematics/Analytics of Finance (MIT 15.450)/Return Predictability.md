---
aliases:
  - 收益可预测性
  - Return Predictability
  - 样本外预测
  - data mining
  - 预测回归
tags: [math, analytics_finance]
up: "[[Analytics of Finance (MIT 15.450) MOC]]"
related:
  - "[[Linear Regression]]"
  - "[[Hypothesis Testing]]"
  - "[[GMM and Inference in Finance]]"
  - "[[Bootstrap Methods in Finance]]"
  - "[[Volatility Models GARCH]]"
  - "[[Regression and PCA in Finance]]"
  - "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
  - "[[Probability and Statistics (MIT 18.05) MOC]]"
down: ""
---
# 收益可预测性

> [!summary] 核心结论
> 预测回归 $r_{t+1}=a+bx_t+u_{t+1}$ 在样本内常显得“显著”，但**样本外（OOS）**表现可能崩塌。重叠收益、持久预测变量、数据挖掘与多重试错会制造虚假可预测性。可靠结论需要：正确 SE（HAC / Bootstrap）、样本外验证、以及预登记式的假设纪律。接 [[Linear Regression]]、[[Hypothesis Testing]]。

> 底本：MIT 15.450 可预测性 / 推断单元；CL&M 为参考。

> 关键词：predictive regression、in-sample vs out-of-sample、$R^2$、data mining、persistent regressor

---

## 1. 预测回归

$x_t$：股息价格比、期限利差、过去收益等。
$$
r_{t+1}=a+b x_t+u_{t+1}.
$$
$H_0:b=0$（不可预测）。估计用 OLS；推断必须面对异方差、序列相关（尤其 $r$ 为多期重叠收益时）。

见 [[GMM and Inference in Finance]]：正交条件 $\mathbb{E}[x_t u_{t+1}]=0$。

---

## 2. 样本内 vs 样本外

| | 样本内（IS） | 样本外（OOS） |
|--|-------------|---------------|
| 做法 | 全样本估 $a,b$，看 $t$ / $R^2$ | 滚动 / 扩展窗：只用 $t$ 前信息估，再预测 $t+1$ |
| 风险 | 过拟合、数据挖掘 | 更接近真实交易可行信息集 |
| 常见现象 | IS $R^2$ 几个百分点且 $t$ 显著 | OOS $R^2$ 近 0 或为负 |

> [!example] 伪成功
> 全样本 $b$ 的 $t=2.5$，$R^2=0.04$。滚动 OOS 预测与历史均值比，OOS $R^2<0$ → IS 显著**不能**直接当可交易边界。

---

## 3. 统计陷阱清单

1. **重叠收益**：$r_{t\to t+h}$ 与 $r_{t+1\to t+h+1}$ 共享区间 → 残差强自相关，朴素 SE 太小。
2. **持久 $x_t$**（如估值比率近似单位根）：小样本偏倚，$t$ 分布扭曲。
3. **数据挖掘**：试 100 个 $x$，报告最显著的那个 → 名义 $5\%$ 检验名存实亡。
4. **前视偏差 / 存活偏差**：用了当时不可得的修订数据或退市股票。
5. **波动群集**：均值方程残差异方差；可与 GARCH 联立或用稳健 SE。

> [!warning] 数据挖掘不是“多做稳健性”的同义词
> 无约束地搜索预测变量再只报赢家，与诚实的多重检验校正、样本分割是两回事。Bootstrap 也不能自动洗白搜参过程。

---

## 4. 经济 vs 统计显著

即使 OOS 有微弱 $R^2$，计入交易成本、卖空限制、危机期流动性后，**经济价值**可能消失。可与 [[Dynamic Programming and Asset Allocation]] 联系：可预测的风险溢价会改变对冲需求，但前提是可预测性真实且可利用。

---

## 5. 与波动可预测性的对比

| | 均值 | 波动 |
|--|------|------|
| 可预测性 | 弱、争议大 | 强（群集），GARCH 有用 |
| 典型 $R^2$ | 往往很小 | $r_t^2$ 方程可观 |
| 实务 | 谨慎 | 风险预算 / VaR 常规工具 |

见 [[Volatility Models GARCH]]、[[Volatility Modeling]]。

---

## 6. 最低实践标准

1. 预声明假设与变量，或报告多重试错范围；
2. HAC 或块 Bootstrap SE（[[Bootstrap Methods in Finance]]）；
3. 报告 OOS 指标（OOS $R^2$、VS 历史均值的 MSE）；
4. 子样本 / 危机期稳定性；
5. 与 [[Regression and PCA in Finance]] 的因子叙事交叉验证，避免单变量讲故事。

---

## 7. 迷你数值：IS $R^2$ 直觉

> [!example] 相关与 $R^2$
> 单变量回归 $R^2=\mathrm{Corr}(r_{t+1},x_t)^2$。若样本相关 $0.15$，则 $R^2=0.0225$。  
> 日频几乎不可用；月频 / 年频上“两个百分点 $R^2$”有时被文献讨论，但仍需 OOS 与正确 SE。

---

## 8. 滚动 OOS 的操作素描

1. 选估计窗（固定滚动或扩展窗）；
2. 在窗内估 $\hat a_t,\hat b_t$，预测 $\hat r_{t+1}=\hat a_t+\hat b_t x_t$；
3. 与基准（历史均值）比 MSE，定义
   $$
   R^2_{\mathrm{OOS}}=1-\frac{\sum(r_{t+1}-\hat r_{t+1})^2}{\sum(r_{t+1}-\bar r_t)^2}.
   $$
4. $R^2_{\mathrm{OOS}}<0$ 表示连“预测均值”都不如。

> [!warning] 窗长也是可挖的参数
> 只报告对某窗长最好的 OOS 结果，同样是数据挖掘。应预设规则或报告敏感性。

与 [[Hypothesis Testing]] 的联系：名义 $p$ 值只在单一预声明检验下好解释；搜遍预测变量后再谈“显著”，需要多重检验或假发现率纪律。

---

## 9. 自检与参考答案

1. 写出预测回归并陈述 $H_0$。
2. 对比 IS 与 OOS 的核心差别。
3. 列出至少三个虚假可预测性来源。
4. 为何波动可预测性强于均值。
5. $R^2_{\mathrm{OOS}}<0$ 意味着什么。
6. 回到 MOC：[[Analytics of Finance (MIT 15.450) MOC]]。

> [!success]- 参考答案
> 1. $r_{t+1}=a+bx_t+u_{t+1}$；$H_0:b=0$。
> 2. IS 用未来信息沾染的全样本拟合；OOS 只用过去信息做预测评估。
> 3. 重叠 SE 错误、持久回归元偏倚、数据挖掘、前视偏差等。
> 4. 平方收益有强自相关；均值接近鞅。
> 5. 预测 MSE 差于历史均值基准，统计 / 交易上都很可疑。
> 6. 本课收束：定价工具 + 计量纪律。

> [!example] 练习：SE 故事
> 用月度重叠的年度收益对 $x_t$ 回归，OLS 软件默认 SE 给出 $t=3$。最优先怀疑什么？

> [!success]- 练习参考答案
> 残差因重叠而强自相关，默认 SE 低估 → 先换 HAC / 合适 Bootstrap，再谈是否真显著。

## 参考

- Leonid Kogan, *15.450 Analytics of Finance*, MIT OCW Fall 2010（return predictability）
- https://ocw.mit.edu/courses/15-450-analytics-of-finance-fall-2010/
- CL&M, *The Econometrics of Financial Markets*（教材参考）
- [[Linear Regression]]、[[Hypothesis Testing]]、[[Bootstrap Methods]]
