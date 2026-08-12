---
aliases:
  - 金融时间序列
  - Time Series Analysis for Finance
  - ARMA ACF 收益
  - returns autocorrelation
tags: [math, math_finance]
up: "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
related:
  - "[[Probability and Stochastic Processes for Finance]]"
  - "[[Volatility Modeling]]"
  - "[[Regression and PCA in Finance]]"
  - "[[Law of Large Numbers and Central Limit Theorem]]"
  - "[[Hypothesis Testing]]"
  - "[[Analytics of Finance (MIT 15.450) MOC]]"
down:
  - "[[Portfolio Management]]"
---
# 金融时间序列分析

> [!summary] 核心结论
> 收益序列 $\{r_t\}$ 近似**弱相关**（高效市场粗糙版），但 $|r_t|$ 与 $r_t^2$ 常显**长记忆相关**——波动聚集。用 ACF/PACF 识别 AR/MA；ARMA 刻画条件均值，波动留给 ARCH/GARCH（[[Volatility Modeling]]）。平稳性是多数估计的前提；价格本身常近单位根，故分析收益而非原始价位。

> 底本：MIT 18.642 时间序列单元；概率底座 [[Probability and Stochastic Processes for Finance]]。

> 关键词：平稳、ACF、AR(1)、MA(1)、白噪声、波动聚集

---

## 1. 收益，不是价格

简单收益 $R_t=(P_t-P_{t-1})/P_{t-1}$，对数收益 $r_t=\log(P_t/P_{t-1})$。对数收益可加：
$$
\log(P_T/P_0)=\sum_{t=1}^T r_t.
$$
经验：日频 $r_t$ 的 ACF 在滞后 1 以外常接近 0；但 $r_t^2$ 的 ACF 显著为正。

![[mf-timeseries.svg]]

---

## 2. 弱平稳与 ACF

弱平稳：$\mathbb{E}[r_t]=\mu$ 常、$\mathrm{Cov}(r_t,r_{t+k})=\gamma(k)$ 只依赖滞后 $k$。自相关
$$
\rho(k)=\frac{\gamma(k)}{\gamma(0)}.
$$
样本 ACF $\hat\rho(k)$；在白噪声下 $\hat\rho(k)$ 约 $N(0,1/T)$，可用 $\pm 1.96/\sqrt{T}$ 粗检（[[Hypothesis Testing]] 口径）。

> [!example] 白噪声带
> $T=250$ 个交易日，$1.96/\sqrt{250}\approx 0.124$。若 $\hat\rho(1)=0.03$，通常不显著；若 $\hat\rho_{r^2}(1)=0.25$，则指向条件异方差。

---

## 3. AR 与 MA

**AR(1)**：
$$
r_t=\phi r_{t-1}+\varepsilon_t,\quad |\phi|<1\Rightarrow\text{平稳},\quad
\rho(k)=\phi^k.
$$
**MA(1)**：
$$
r_t=\varepsilon_t+\theta\varepsilon_{t-1},\quad
\rho(1)=\frac{\theta}{1+\theta^2},\ \rho(k)=0\ (k\ge 2).
$$
ARMA$(p,q)$ 混合二者。识别：ACF 截尾偏 MA，PACF 截尾偏 AR（经典 Box–Jenkins 口诀，实操需信息准则）。

> [!warning] 收益上 AR 系数接近 0 很常见
> 勉强化 ARMA 拟合日收益均值，样本内 $R^2$ 可观、样本外常崩——可预测性极度脆弱。更稳定的结构往往在波动或低频因子，而非日频条件均值。

---

## 4. 随机游走与价格

若 $r_t=\mu+\varepsilon_t$ 白噪声，则 $\log P_t$ 为带漂移随机游走（单位根）。差分（取收益）后平稳——这是“对价格做回归要小心伪回归”的根源。检验单位根（ADF 等）在课程里点到：先差分再建模是默认卫生习惯。

---

## 5. 与回归、波动的接口

- 均值方程：$r_t=x_t^\top\beta+\varepsilon_t$（因子、日历效应）→ [[Regression and PCA in Finance]]；
- 若 $\varepsilon_t=\sigma_t z_t$，$\sigma_t$ 随时间变 → GARCH 族 [[Volatility Modeling]]；
- 长程依赖 / 已实现波动：更高频课题，可转到 [[Analytics of Finance (MIT 15.450) MOC]]。

CLT 视角：长期累积收益近似正态的条件更苛刻（依赖与异方差）；见 [[Law of Large Numbers and Central Limit Theorem]]。

---

## 6. 诊断清单

1. 画 $r_t$、$r_t^2$ 的 ACF；
2. Ljung–Box 检验残差白噪声；
3. ARCH 效应检验（残差平方）；
4. 样本外：滚动一步预测 vs 朴素均值；
5. 制度切换：危机窗单独看，勿与平静期混估。

---

## 7. PACF 与信息准则（速记）

偏自相关 PACF$(k)$：去掉中间滞后影响后 $r_t$ 与 $r_{t-k}$ 的相关。AR$(p)$ 的 PACF 在 $k>p$ 后截尾；MA$(q)$ 的 ACF 截尾——口诀对换。实操中截尾很少干净，改用 AIC / BIC：
$$
\mathrm{AIC}=-2\log L+2k,\qquad \mathrm{BIC}=-2\log L+k\log T.
$$
BIC 对阶数惩罚更重，金融短样本里往往更稳妥。选定阶数后仍必须看样本外。

> [!example] AR vs 白噪声
> 估得 $\hat\phi=0.05$，$T=500$。渐近 $\mathrm{se}\approx\sqrt{(1-\phi^2)/T}\approx 0.045$，故 $\hat\phi$ 约 1 个标准误——统计上勉强，经济上日频可预测性几乎为零。报告时应同时给经济度量（年化夏普贡献），而非只报 $p$ 值。

长记忆备选：ARFIMA 等对收益均值通常过重；对已实现波动的长记忆更常见——点到即可，细节留给波动专题。

---

## 8. 季节与日历

收益可含星期效应、月份效应、期权到期日效应。用虚拟变量回归进均值方程，或在波动方程加日历项。发现显著季节后要问：成本吃掉后是否仍在？样本外是否消失？许多“日历异象”是多重检验产物。

微观结构噪声（超高频）会使超短滞后 ACF 呈现负相关伪影——日频以上建模通常先聚合再估。

与 [[Machine Learning in Finance]] 的衔接：ARMA 特征可进监督模型，但协议仍须前向验证，不能因“古典”就免检过拟合。

（作业建议：先对一只指数画 $r_t$ 与 $r_t^2$ 的 ACF，再决定要不要上 ARMA。）

---

## 9. 自检与参考答案

1. 为何对价格取对数差分再建模？
2. 写出 AR(1) 平稳条件与 $\rho(k)$。
3. MA(1) 的 ACF 形态。
4. 收益 ACF≈0 但平方 ACF>0 意味什么？
5. 给出一条样本外检验的朴素基准。

> [!success]- 参考答案
> 1. 价格近单位根；收益更接近平稳，可加性好。
> 2. $|\phi|<1$；$\rho(k)=\phi^k$。
> 3. $\rho(1)\neq 0$，更高阶为 0（理论）。
> 4. 条件均值难预测，但波动聚集——应用 GARCH 类。
> 5. 预测明日收益 = 历史均值；比复杂 ARMA 的 MSPE。

> [!example] 练习：AR(1) 方差
> $r_t=0.2 r_{t-1}+\varepsilon_t$，$\mathrm{Var}(\varepsilon)=0.01$。求 $\mathrm{Var}(r_t)$。

> [!success]- 练习参考答案
> $\gamma_0=\phi^2\gamma_0+\sigma_\varepsilon^2\Rightarrow\gamma_0=0.01/(1-0.04)=0.01/0.96\approx 0.01042$。

## 参考

- MIT 18.642 time series lectures；18.S096
- https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/
