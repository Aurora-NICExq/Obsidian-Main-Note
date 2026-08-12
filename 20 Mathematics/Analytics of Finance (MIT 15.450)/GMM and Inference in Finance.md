---
aliases:
  - GMM
  - 广义矩估计
  - GMM and Inference in Finance
  - HAC
  - 矩条件
tags: [math, analytics_finance]
up: "[[Analytics of Finance (MIT 15.450) MOC]]"
related:
  - "[[Financial Econometrics MLE and QMLE]]"
  - "[[Linear Regression]]"
  - "[[Return Predictability]]"
  - "[[Bootstrap Methods in Finance]]"
  - "[[Probability and Statistics (MIT 18.05) MOC]]"
  - "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
down:
  - "[[Bootstrap Methods in Finance]]"
---
# GMM 与金融中的推断

> [!summary] 核心结论
> **GMM** 用矩条件 $\mathbb{E}[g(X_t,\theta)]=0$ 估计参数：样本均值 $\bar g(\theta)\approx 0$，二次型最小化。OLS 是 GMM 的特例（正交条件）。金融时间序列常有异方差与自相关，标准误需 **HAC**（如 Newey–West）。资产定价中 Euler 方程 $\mathbb{E}[m_{t+1}R_{t+1}^e]=0$ 是典型矩条件（Cochrane 视角）。

> 底本：MIT 15.450 GMM 单元；CL&M / Cochrane 为参考。

> 关键词：moment conditions、GMM、OLS as GMM、HAC、Newey–West、overidentification

---

## 1. 矩条件与样本模拟

参数 $\theta\in\mathbb{R}^k$，矩函数 $g(x,\theta)\in\mathbb{R}^q$，$q\ge k$，真值满足
$$
\mathbb{E}\bigl[g(X_t,\theta_0)\bigr]=0.
$$
样本：
$$
\bar g_T(\theta)=\frac{1}{T}\sum_{t=1}^T g(X_t,\theta).
$$
GMM：选权重正定矩阵 $W$，
$$
\hat\theta=\arg\min_\theta\;\bar g_T(\theta)^\mathsf{T} W\,\bar g_T(\theta).
$$
恰识别 $q=k$ 时常等价于解 $\bar g_T(\hat\theta)=0$。

![[af-gmm.svg]]

---

## 2. OLS 作为 GMM

线性模型 $y_t=x_t^\mathsf{T}\beta+u_t$。若 $\mathbb{E}[x_t u_t]=0$（外生 / 预定回归元），则
$$
g_t(\beta)=x_t(y_t-x_t^\mathsf{T}\beta).
$$
$\bar g_T(\hat\beta)=0$ 即正规方程 $\sum x_t\hat u_t=0$ → **OLS**。  
见 [[Linear Regression]]。可预测性回归 $r_{t+1}=a+bx_t+u_{t+1}$ 正是这种矩——见 [[Return Predictability]]。

> [!example] 单变量正交
> $y=a+u$，$\mathbb{E}[u]=0$ → $\hat a=\bar y$。这是一维 GMM / 矩估计。

---

## 3. 资产定价矩（素描）

随机折扣因子 $m$：对超额收益 $R^e$，
$$
\mathbb{E}[m_{t+1} R_{t+1}^e]=0.
$$
线性因子模型常写成 $\mathbb{E}[R^e]=\beta\lambda$ 等，可用 GMM 估 $\beta,\lambda$ 并做过度识别检验。课内抓住：**定价 = 一组矩**，不必先写全似然。

---

## 4. 推断与 HAC 标准误

渐近：$\sqrt{T}(\hat\theta-\theta_0)\Rightarrow\mathcal{N}(0,V)$，$V$ 依赖 $G=\mathbb{E}[\partial g/\partial\theta^\mathsf{T}]$ 与长期方差
$$
S=\sum_{j=-\infty}^\infty\mathrm{Cov}\bigl(g_t(\theta_0),g_{t-j}(\theta_0)^\mathsf{T}\bigr).
$$
若 $g_t$ 有序列相关 / 条件异方差，$S\neq\mathrm{Var}(g_t)$。**HAC** 估计 $S$（Newey–West 等）再插入 $V$ 的公式。

> [!warning] 忽略 HAC 的后果
> 收益可预测性回归、重叠多期收益时，OLS 常规 SE 往往**严重偏小** → 虚假显著。务必 HAC 或合适 Bootstrap（见 [[Bootstrap Methods in Finance]]）。

---

## 5. 过度识别与权重

$q>k$：多余矩可检验模型（Hansen $J$ 检验）。两步 GMM：先用粗 $W$（如单位阵）得初估，再 $W=\hat S^{-1}$ 提高效率。课内知道“有效权重 ≈ 逆长期方差”即可。

---

## 6. 与 MLE / QMLE

| | MLE | GMM |
|--|-----|-----|
| 输入 | 完整密度 | 矩条件 |
| 得分 | $\mathbb{E}[\partial\ell/\partial\theta]=0$ 也是矩 | 可只用部分矩 |
| 误设 | QMLE 故事 | 矩对则一致 |

金融里因子模型、矩约束定价更常直接 GMM。

---

## 7. 实施清单（课内）

1. 写清 $g(X_t,\theta)$ 与识别（$q$ vs $k$）；
2. 恰识别先解 $\bar g=0$；过度识别选 $W$，报告 $J$；
3. SE 默认考虑 HAC（带宽与滞后说明）；
4. 重叠收益、持久回归元单独做稳健性（Bootstrap）；
5. 不要把“GMM 比 OLS 高级”当免检金牌——矩错则一切错。

> [!example] 预测回归的矩
> $g_t=(1,x_t)^\mathsf{T}(r_{t+1}-a-b x_t)$。样本均值零 ⇒ OLS。HAC 作用在这对得分上。见 [[Return Predictability]]。

Hansen $J$ 在过度识别时检验“所有矩是否同时成立”；拒绝意味着因子模型 / 定价核设定与数据冲突，不一定指出是哪一条矩在作怪。

---

## 8. 自检与参考答案

1. 陈述 GMM 优化目标。
2. 说明 OLS 对应哪条矩条件。
3. 为何金融回归常要 HAC SE。
4. 过度识别 $q>k$ 多提供了什么。
5. 下一主题：[[Bootstrap Methods in Finance]]。

> [!success]- 参考答案
> 1. 最小化 $\bar g(\theta)^\mathsf{T} W\bar g(\theta)$。
> 2. $\mathbb{E}[x u]=0$ → 正规方程。
> 3. 残差异方差 + 自相关（重叠收益）使朴素 SE 无效。
> 4. 可检验矩是否整体成立（$J$ 检验），并可能提高效率。
> 5. 用重抽样估抽样分布，尤其时间序列块方法。

> [!example] 练习：恰识别
> 矩 $\mathbb{E}[r_t-\mu]=0$，$T=4$，数据 $r=(0.01,0.02,-0.01,0.04)$。$\hat\mu$？

> [!success]- 练习参考答案
> $\hat\mu=\bar r=(0.01+0.02-0.01+0.04)/4=0.015$。

> [!tip] SE 工具箱
> HAC 与 [[Bootstrap Methods in Finance]] 可交叉核对。

## 参考

- Leonid Kogan, *15.450 Analytics of Finance*, MIT OCW Fall 2010（GMM）
- https://ocw.mit.edu/courses/15-450-analytics-of-finance-fall-2010/
- John Cochrane, *Asset Pricing*；CL&M, *The Econometrics of Financial Markets*（教材参考）
- [[Linear Regression]]、[[Hypothesis Testing]]
