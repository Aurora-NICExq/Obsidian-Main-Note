---
aliases:
  - GARCH
  - 波动率模型 GARCH
  - Volatility Models GARCH
  - GARCH(1,1)
  - 条件异方差
tags: [math, analytics_finance]
up: "[[Analytics of Finance (MIT 15.450) MOC]]"
related:
  - "[[Volatility Modeling]]"
  - "[[Financial Econometrics MLE and QMLE]]"
  - "[[Time Series Analysis for Finance]]"
  - "[[Bootstrap Methods in Finance]]"
  - "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
  - "[[Probability and Statistics (MIT 18.05) MOC]]"
down:
  - "[[Return Predictability]]"
---
# 波动率模型：GARCH

> [!summary] 核心结论
> 金融收益常近似不可预测，但**波动会群集**。GARCH(1,1) 用
> $\sigma_t^2=\omega+\alpha\varepsilon_{t-1}^2+\beta\sigma_{t-1}^2$
> 捕捉条件异方差；$\alpha+\beta$ 接近 1 表示高**持续性**。估计常用条件正态 MLE/QMLE。与隐含波动 / 历史波动概念对照 [[Volatility Modeling]]。

> 底本：MIT 15.450；Tsay 为时序参考。

> 关键词：ARCH/GARCH、persistence、volatility clustering、QMLE

---

## 1. 现象：波动群集

$r_t$ 的 ACF 往往很弱，但 $r_t^2$ 或 $|r_t|$ 的 ACF 显著且衰减慢 → 大波动后更可能继续大波动。常数方差的 i.i.d. 模型无法描述。

![[af-garch.svg]]

---

## 2. ARCH(1) → GARCH(1,1)

Engle ARCH(1)：
$$
\varepsilon_t=\sigma_t z_t,\quad
\sigma_t^2=\omega+\alpha\varepsilon_{t-1}^2.
$$
Bollerslev GARCH(1,1)：
$$
\sigma_t^2=\omega+\alpha\varepsilon_{t-1}^2+\beta\sigma_{t-1}^2,
$$
$\omega>0$，$\alpha,\beta\ge 0$，$\alpha+\beta<1$ 时存在弱平稳（无条件方差有限）。

无条件方差：
$$
\mathrm{Var}(\varepsilon_t)=\frac{\omega}{1-\alpha-\beta}
$$
（在 $|\alpha+\beta|<1$ 且矩存在时）。

> [!example] 持续性
> $\alpha=0.08$，$\beta=0.90$ → $\alpha+\beta=0.98$。冲击对 $\sigma_t^2$ 的影响半衰期约 $\ln 2/|\ln(\alpha+\beta)|\approx 34$ 期（日频则约一个多月量级）。$\alpha+\beta\to 1$ 接近 IGARCH，长记忆风险升高。

---

## 3. 完整收益方程

常见：
$$
r_t=\mu+\varepsilon_t,\qquad
\varepsilon_t=\sigma_t z_t,\quad z_t\sim\mathrm{i.i.d.}(0,1).
$$
$\mu$ 可扩展为 AR；均值方程与方差方程一起估。

---

## 4. 估计直觉（QMLE）

1. 设初值 $\sigma_1^2$（如样本方差）；
2. 递推 $\sigma_t^2(\theta)$；
3. 累加条件正态对数似然（见 [[Financial Econometrics MLE and QMLE]]）；
4. 数值最大化得 $(\hat\omega,\hat\alpha,\hat\beta,\hat\mu)$。

厚尾：改用 $t$ 分布似然，或正态 QMLE + 稳健 SE。

> [!warning] $\alpha+\beta\ge 1$ 的数值解
> 优化可能顶到边界或爆炸递推。检查约束、初值、样本（危机期持续性估得极高很常见，但外推要谨慎）。

---

## 5. 用途

- **风险**：次日 VaR / ES 用 $\hat\sigma_{T+1}$；
- **标准化残差** $\hat z_t$：供诊断与 Bootstrap；
- **期权 / 交易**：历史条件波动 vs 隐含波动——两条信息源，见 [[Volatility Modeling]]；
- **组合**：时变风险进入 Merton 短视权重 $\propto 1/\sigma_t^2$ 的启发版本。

---

## 6. 与 18.642 对照

| 15.450 | 18.642 |
|--------|--------|
| GARCH 方程 + 估计 | [[Volatility Modeling]] 历史 vs 隐含、群集现象 |
| QMLE / 诊断 | [[Time Series Analysis for Finance]] ACF |

---

## 7. 迷你数值递推

> [!example] 一步手算
> $\omega=0.00001$，$\alpha=0.1$，$\beta=0.8$，$\sigma_{t-1}^2=0.0004$，$\varepsilon_{t-1}=0.02$。  
> $\varepsilon_{t-1}^2=0.0004$。  
> $\sigma_t^2=0.00001+0.1\cdot 0.0004+0.8\cdot 0.0004=0.00001+0.00004+0.00032=0.00037$。  
> $\sigma_t\approx\sqrt{0.00037}\approx 0.0192$（约 $1.92\%$ 若收益为小数）。

---

## 8. 诊断与扩展（知晓）

- Ljung–Box 于 $\hat z_t$ 与 $\hat z_t^2$；
- 杠杆效应（坏消息推高波动）→ GJR / EGARCH（点名即可）；
- 多元：DCC 等（超出本笔记）；
- 预测：$\hat\sigma_{T+1}^2=\hat\omega+\hat\alpha\hat\varepsilon_T^2+\hat\beta\hat\sigma_T^2$，可多步迭代。

> [!tip] 与期权书的对话
> GARCH 给物理测度条件波动；定价常还需风险中性波动动态。不要把 $\hat\sigma_t$ 直接塞进 BS 当隐含波动的替代而不谈测度。

---

## 9. 自检与参考答案

1. 写出 GARCH(1,1) 方程与平稳条件（弱）。
2. 解释 $\alpha+\beta$ 的持续性含义。
3. 简述 QMLE 估计步骤。
4. 为何看 $r_t^2$ 的 ACF。
5. 如何做一步波动预测。
6. 下一主题：[[Return Predictability]]。

> [!success]- 参考答案
> 1. $\sigma_t^2=\omega+\alpha\varepsilon_{t-1}^2+\beta\sigma_{t-1}^2$；常要 $\alpha+\beta<1$。
> 2. 越接近 1，波动冲击衰减越慢。
> 3. 递推 $\sigma_t^2$，最大化条件似然。
> 4. 检测波动群集 / ARCH 效应。
> 5. $\hat\sigma_{T+1}^2=\hat\omega+\hat\alpha\hat\varepsilon_T^2+\hat\beta\hat\sigma_T^2$。
> 6. 讨论均值是否可预测及样本内外陷阱。

> [!example] 练习：无条件方差
> $\omega=0.00002$，$\alpha=0.05$，$\beta=0.90$。求无条件 $\mathrm{Var}(\varepsilon)$。

> [!success]- 练习参考答案
> $\omega/(1-\alpha-\beta)=0.00002/(1-0.95)=0.00002/0.05=0.0004$，故无条件 $\sigma=0.02$。

## 参考

- Leonid Kogan, *15.450 Analytics of Finance*, MIT OCW Fall 2010（GARCH）
- https://ocw.mit.edu/courses/15-450-analytics-of-finance-fall-2010/
- Ruey S. Tsay, *Analysis of Financial Time Series*（教材参考）
