---
aliases:
  - 蒙特卡洛衍生品定价
  - Monte Carlo Methods for Derivatives
  - MC pricing
  - 对偶变量
  - 控制变量
tags: [math, analytics_finance]
up: "[[Analytics of Finance (MIT 15.450) MOC]]"
related:
  - "[[Black-Scholes Model and Extensions]]"
  - "[[No Arbitrage and Risk Neutral Pricing]]"
  - "[[Ito Calculus for Finance]]"
  - "[[Interest Rate Models]]"
  - "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
down:
  - "[[Financial Econometrics MLE and QMLE]]"
---
# 衍生品定价中的蒙特卡洛方法

> [!summary] 核心结论
> 风险中性定价把价格写成 $\mathbb{E}^\mathbb{Q}[e^{-rT}g(S_T)]$（或路径依赖的折现收益）。**粗蒙特卡洛**模拟 $\mathbb{Q}$-路径、平均折现收益；误差 $\propto\sigma_{\hat V}/\sqrt{N}$。对偶变量、控制变量等减方差技巧用相同计算预算换更小标准误。MC 擅长高维 / 路径依赖；美式提前行权需额外（回归 / 对偶）技巧，本笔记以欧式与路径依赖为主。

> 底本：MIT 15.450 Monte Carlo 单元。

> 关键词：risk-neutral simulation、crude MC、antithetic、control variate

---

## 1. 从期望到模拟

GBM 风险中性：
$$
S_T=S_0\exp\Bigl((r-\tfrac12\sigma^2)T+\sigma\sqrt{T}\,Z\Bigr),\quad Z\sim\mathcal{N}(0,1).
$$
欧式看涨：
$$
\hat C_N=\frac{1}{N}\sum_{i=1}^N e^{-rT}(S_T^{(i)}-K)^+.
$$
由 LLN，$\hat C_N\to C$；由 CLT，
$$
\sqrt{N}(\hat C_N-C)\Rightarrow\mathcal{N}(0,\mathrm{Var}^\mathbb{Q}[e^{-rT}g(S_T)]).
$$
标准误 $\widehat{\mathrm{se}}=\hat\sigma/\sqrt{N}$。接 [[Law of Large Numbers and Central Limit Theorem]]。

![[af-monte-carlo.svg]]

---

## 2. 算法清单（欧式）

1. 在 $\mathbb{Q}$ 下抽取 $Z^{(i)}$（或离散化 SDE 多步）；
2. 得 $S_T^{(i)}$ 或整条路径；
3. 计算折现收益 $X^{(i)}$；
4. 平均；报告 $\hat C\pm 1.96\,\widehat{\mathrm{se}}$（近似 $95\%$ CI）。

路径依赖（亚式、障碍）：必须模拟整条路径；步长偏差（discretization bias）与统计误差要分开谈。

> [!warning] 物理测度模拟不能直接当无套利价
> 用历史 $\mu$ 模拟再折现，得到的是“真实世界期望收益”，不是复制价格。定价路径的漂移必须是 $r$（或 $r-q$）。

---

## 3. 粗 MC 的方差问题

深度虚值期权：多数路径收益为 0，少量很大 → $\mathrm{Var}(X)$ 大，需巨大 $N$。维数高时网格 / 树爆炸，MC 相对有竞争力，但仍要减方差或重要性抽样。

> [!example] 标准误缩放
> 若单次折现收益样本标准差 $\hat\sigma=20$（价格单位），$N=10^4$，则 $\widehat{\mathrm{se}}=20/100=0.2$。要 se$=0.02$ 需 $N=10^6$（粗 MC，$100\times$ 样本）。减方差把有效 $\sigma$ 变小，比盲目加 $N$ 更划算。

---

## 4. 对偶变量（antithetic）

若用 $Z$ 与 $-Z$ 成对模拟（GBM 下 $S_T(Z)$ 与 $S_T(-Z)$），取
$$
X^{\mathrm{anti}}=\tfrac12\bigl(X(Z)+X(-Z)\bigr).
$$
当 $X(Z)$ 与 $X(-Z)$ 负相关时，$\mathrm{Var}(X^{\mathrm{anti}})$ 小于独立两次平均的方差。对近似单调的收益（如看涨关于 $Z$）常常有效；实现简单。

---

## 5. 控制变量（control variate）轻量版

找已知期望的 $Y$（如同一路径上的 BS 看涨解析价对应的折现收益，或 $S_T$ 本身）：
$$
X^{\mathrm{cv}}=X-\beta\bigl(Y-\mathbb{E}[Y]\bigr).
$$
最优 $\beta=\mathrm{Cov}(X,Y)/\mathrm{Var}(Y)$（样本估计）。$Y$ 与 $X$ 越相关，减方差越强。

> [!example] 用 $S_T$ 控制
> $\mathbb{E}^\mathbb{Q}[e^{-rT}S_T]=S_0$。对看涨，$X=e^{-rT}(S_T-K)^+$ 与 $Y=e^{-rT}S_T$ 正相关 → 控制后常降方差。更强控制：用同一 $Z$ 的 BS 闭式收益作 $Y$（已知 $\mathbb{E}[Y]=C_{\mathrm{BS}}$）。

---

## 6. 与树 / PDE 的分工

| 方法 | 擅长 |
|------|------|
| 二叉树 / PDE 网格 | 低维、美式（提前行权）较直接 |
| 粗 MC + 减方差 | 高维标的、路径依赖欧式 |
| 拟蒙特卡洛 / 多层 MC | 进一步降误差（课内知晓即可） |

利率模型：模拟 $r_t$，累加 $\int r$，估 $P(0,T)$ 或债券期权——见 [[Interest Rate Models]]。

---

## 7. 实现注意（偏见与方差）

- **随机误差**：$\propto 1/\sqrt{N}$，可用对偶 / 控制压低；
- **离散化偏见**：Euler 步长 $\Delta t$ 太大时，$S$ 路径分布偏离真 SDE；欧式 GBM 可一步精确抽样避开；
- **美式**：不能朴素“路径上提前行权最优”——需 Longstaff–Schwartz 等回归后向；本课点到为止；
- **种子与并行**：报告 $N$、减方差方法、CI。

> [!tip] 先解析后 MC
> 能用 BS 闭式的合约，先当控制变量或校验器；MC 代码若连 ATM 看涨都对不上闭式，先修模拟再谈奇异期权。

路径依赖例子：亚式看涨 $g=\bigl(\frac{1}{m}\sum_{j}S_{t_j}-K\bigr)^+$——必须存整条路径；方差通常仍大，控制变量可用同一路径的欧式 BS 收益。

---

## 8. 自检与参考答案

1. 写出欧式期权粗 MC 估计量。
2. 说明标准误如何随 $N$ 下降。
3. 对偶变量的基本做法。
4. 控制变量公式中 $\beta$ 的直觉。
5. 下一主题：[[Financial Econometrics MLE and QMLE]]。

> [!success]- 参考答案
> 1. $\hat C_N=N^{-1}\sum e^{-rT}g(S_T^{(i)})$，$S$ 在 $\mathbb{Q}$ 下模拟。
> 2. $\mathrm{se}\propto 1/\sqrt{N}$（方差有限时）。
> 3. 成对用 $Z$ 与 $-Z$，平均两个折现收益。
> 4. $\beta$ 把已知均值的相关噪声从 $X$ 中减掉；相关越强减得越多。
> 5. 从定价模拟转向收益数据的似然估计。

> [!example] 练习：需要多大 $N$？
> $\hat\sigma=15$，希望 $\widehat{\mathrm{se}}\le 0.05$。粗 MC 至少需要多少路径？

> [!success]- 练习参考答案
> $15/\sqrt{N}\le 0.05\Rightarrow\sqrt{N}\ge 300\Rightarrow N\ge 90000$。

> [!tip] 与 BS 笔记对照
> 闭式可用时先校验 MC；见 [[Black-Scholes Model and Extensions]]。

## 参考

- Leonid Kogan, *15.450 Analytics of Finance*, MIT OCW Fall 2010（Monte Carlo）
- https://ocw.mit.edu/courses/15-450-analytics-of-finance-fall-2010/
