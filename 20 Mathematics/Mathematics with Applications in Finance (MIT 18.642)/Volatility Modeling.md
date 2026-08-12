---
aliases:
  - 波动率建模
  - Volatility Modeling
  - 历史波动与隐含波动
  - volatility clustering
tags: [math, math_finance]
up: "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
related:
  - "[[Time Series Analysis for Finance]]"
  - "[[Black-Scholes and Risk Neutral Valuation]]"
  - "[[Portfolio Management]]"
  - "[[Probability and Stochastic Processes for Finance]]"
  - "[[Hypothesis Testing]]"
down:
  - "[[Black-Scholes and Risk Neutral Valuation]]"
---
# 波动率建模

> [!summary] 核心结论
> **历史波动**由过去收益估计；**隐含波动**由期权市价反演 BS 公式。收益近似不可预测，但**波动聚集**：大波动后常跟大波动。GARCH 类给出 $\sigma_t^2$ 的递推；期权面则看到微笑/偏斜——说明常 $\sigma$ 的 BS 只是报价语言。风险管理与定价要用对“哪一个 $\sigma$”。

> 底本：MIT 18.642 波动单元；时间序列接口 [[Time Series Analysis for Finance]]；定价接口 [[Black-Scholes and Risk Neutral Valuation]]。

> 关键词：已实现波动、隐含波动、GARCH、聚集、微笑

---

## 1. 历史 / 已实现波动

窗口 $N$ 的样本标准差（常年化：日频 $\times\sqrt{252}$）：
$$
\hat\sigma=\sqrt{\frac{1}{N-1}\sum_{i=1}^N(r_i-\bar r)^2}.
$$
更精细：已实现方差 $\sum_{日内} r_{t,k}^2$。窗口短 → 噪；长 → 滞后。指数加权（RiskMetrics 直觉）给近期更高权重：
$$
\hat\sigma_t^2=\lambda\hat\sigma_{t-1}^2+(1-\lambda)r_{t-1}^2.
$$

> [!example] 年化
> 日收益标准差 $1\%$（$0.01$）。年化 $\approx 0.01\sqrt{252}\approx 15.9\%$。若误乘 $252$ 而非 $\sqrt{252}$，会得到荒谬的 $252\%$。

---

## 2. 隐含波动

看涨市价 $C^{\mathrm{mkt}}$，解 $C_{\mathrm{BS}}(S,K,T,r,\sigma_{\mathrm{imp}})=C^{\mathrm{mkt}}$ 得 $\sigma_{\mathrm{imp}}(K,T)$。同一 $T$ 下对 $K$ 作图 → **波动微笑 / 偏斜**。交易员用 $\sigma_{\mathrm{imp}}$ 当报价坐标，并不相信真是常 $\sigma$ GBM。

![[mf-volatility.svg]]

> [!warning] 历史 ≠ 隐含
> 二者信息集不同：隐含含风险溢价与需求压力。用历史 $\sigma$ 估期权“便宜贵”必须解释风险中性 vs 物理测度差异。

---

## 3. 波动聚集与 ARCH/GARCH

ARCH(1) 直觉：
$$
r_t=\sigma_t z_t,\quad \sigma_t^2=\omega+\alpha r_{t-1}^2.
$$
GARCH(1,1)：
$$
\sigma_t^2=\omega+\alpha r_{t-1}^2+\beta\sigma_{t-1}^2,\quad \omega>0,\ \alpha,\beta\ge 0,\ \alpha+\beta<1.
$$
无条件方差 $\omega/(1-\alpha-\beta)$。$\alpha+\beta$ 接近 1 → 高持久性。

> [!example] 稳态方差
> $\omega=0.00001$，$\alpha=0.08$，$\beta=0.90$。$\alpha+\beta=0.98$，
> $$
> \bar\sigma^2=0.00001/0.02=0.0005,\quad \bar\sigma\approx 0.0224\ \text{（日）}\approx 35.6\%\ \text{年化}.
> $$

---

## 4. 与组合风险

组合方差 $w^\top\Sigma_t w$ 中 $\Sigma_t$ 可随时间变：DCC 等多元 GARCH、或因子 + 随机波动。压力情景：相关升至 1 时分散化失效（[[Portfolio Management]]）。VaR/ES 对 $\sigma_t$ 高度敏感——模型风险本身要管。

---

## 5. 检验与诊断

- $r_t$ 的 ACF 弱、$r_t^2$ 的 ACF 强（[[Time Series Analysis for Finance]]）；
- ARCH-LM 检验（[[Hypothesis Testing]] 框架）；
- 标准化残差 $r_t/\hat\sigma_t$ 应近白噪声、峰度下降；
- 样本外：似然或 QLIKE 损失比较波动预测。

---

## 6. 连接 BS

BS 要一个 $\sigma$ 输入。实践：

| 用途 | 常用 $\sigma$ |
|------|----------------|
| 报价 | 隐含曲面 |
| 对冲 | 局部/随机波动或隐含 |
| 风险（P 测度） | 历史 / GARCH 预测 |

同一数字出现在不同测度与目标中，含义不同——写报告时标明。

---

## 7. 杠杆效应与非对称

股价下跌时波动常升更猛（杠杆效应）。TGARCH / EGARCH / GJR 让负残差对 $\sigma_t^2$ 的系数更大。权益指数偏斜的期权隐含波动（低执行价更高 $\sigma_{\mathrm{imp}}$）与此物理现象及相关风险溢价交织——定价要用 $\mathbb{Q}$ 动态，风险用 $\mathbb{P}$ 动态。

> [!example] 符号约定
> 某 GJR 项 $\alpha r_{t-1}^2+\gamma r_{t-1}^2\mathbf{1}_{\{r_{t-1}<0\}}$。若 $\gamma>0$，则下跌额外抬升方差。估得 $\alpha=0.05$，$\gamma=0.08$ 表示坏消息冲击约 $0.13$ vs 好消息 $0.05$。

多资产时还要管**相关的动态**：危机中 $\rho$ 上升，组合 $\sigma$ 的坏于各腿 GARCH 单独暗示的水平。最简压力：把相关矩阵往 1 推一截再重算 $w^\top\Sigma w$。

---

## 8. 波动风险溢价（一句话）

平均而言隐含波动常高于事后已实现波动——期权买方支付溢价。故“卖波动”策略有正的平均收益，但也有崩盘式左尾。18.642 点到现象即可；仓位与尾部对冲是风险管理课的主题。

期限结构：短端隐含对跳与需求更敏感，长端更平滑。交易日历效应（到期日、FOMC）会在曲面留下脊线——识别后再谈是否可交易。

报价常用 Delta 网格上的 $\sigma_{\mathrm{imp}}$ 而非行权价网格，便于跨即期比较；转换细节留给交易实务。

---

## 9. 自检与参考答案

1. 历史波动年化如何从日频来？
2. 隐含波动如何定义？
3. 写出 GARCH(1,1) 并给出平稳条件与无条件方差。
4. 波动聚集在 ACF 上的表现。
5. 为何微笑否定常 $\sigma$ GBM？

> [!success]- 参考答案
> 1. $\hat\sigma_{\mathrm{day}}\sqrt{252}$（交易日约定）。
> 2. 使 BS 价格 = 市价的 $\sigma$。
> 3. $\sigma_t^2=\omega+\alpha r_{t-1}^2+\beta\sigma_{t-1}^2$；$\alpha+\beta<1$；$\omega/(1-\alpha-\beta)$。
> 4. $r_t$ 相关弱；$r_t^2$ 或 $|r_t|$ 相关强且衰减慢。
> 5. 若常 $\sigma$，所有 $K$ 隐含波动应相同；微笑/偏斜显示矛盾。

> [!example] 练习：EWM
> $\lambda=0.94$，$\hat\sigma_{t-1}^2=0.0004$，$r_{t-1}^2=0.0009$。更新 $\hat\sigma_t^2$。

> [!success]- 练习参考答案
> $0.94\cdot0.0004+0.06\cdot0.0009=0.000376+0.000054=0.00043$。

## 参考

- MIT 18.642 volatility lectures；18.S096
- https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/
