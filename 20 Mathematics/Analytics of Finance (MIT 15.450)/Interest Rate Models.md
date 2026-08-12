---
aliases:
  - 利率模型
  - Interest Rate Models
  - Vasicek
  - CIR
  - 短期利率
tags: [math, analytics_finance]
up: "[[Analytics of Finance (MIT 15.450) MOC]]"
related:
  - "[[Black-Scholes Model and Extensions]]"
  - "[[No Arbitrage and Risk Neutral Pricing]]"
  - "[[Interest Rates Products and Models]]"
  - "[[Monte Carlo Methods for Derivatives]]"
  - "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
down:
  - "[[Dynamic Programming and Asset Allocation]]"
---
# 利率模型

> [!summary] 核心结论
> 当利率随机时，债券与利率衍生品不能再用常数 $r$ 的 BS 公式一笔带过。**短期利率模型**把 $r_t$ 写成 SDE（Vasicek、CIR 等），在风险中性下折现因子 $D_t=\exp(-\int_0^t r_s ds)$，零息债 $P(t,T)=\mathbb{E}^\mathbb{Q}[D_T/D_t\mid\mathcal{F}_t]$。本笔记只建直觉与名字级方程，不做百科全书；产品侧细节见 [[Interest Rates Products and Models]]。

> 底本：MIT 15.450 利率模型单元。

> 关键词：short rate、Vasicek、CIR、zero-bond、affine models

---

## 1. 为何需要利率模型？

- 定价长债、互换、债券期权、利率上限时，$r$ 路径本身是风险因子；
- 股票 BS 把 $r$ 当常数，对短到期股票期权常够用，对利率书不够；
- 目标：在无套利下给出整条**收益率曲线**的动态，并与今日观测曲线校准。

---

## 2. 短期利率与零息债

短期利率 $r_t$：瞬时无风险借贷利率。货币市场账户
$$
B_t=\exp\Bigl(\int_0^t r_s\,ds\Bigr).
$$
到期 $T$ 支付 1 的零息债价格：
$$
P(t,T)=\mathbb{E}^\mathbb{Q}\Bigl[\exp\Bigl(-\int_t^T r_s\,ds\Bigr)\Bigm|\mathcal{F}_t\Bigr].
$$
收益率（连续复利）$R(t,T)=-\frac{1}{T-t}\log P(t,T)$。

---

## 3. Vasicek 模型（直觉）

$$
dr_t=\kappa(\theta-r_t)\,dt+\sigma\,dW_t^\mathbb{Q}.
$$

- $\kappa>0$：**均值回复** 到长期水平 $\theta$；
- $\sigma$：利率波动；高斯驱动 → $r_t$ 可为负（历史上曾被视为缺陷，低利率时代有时反而“像”）。

仿射结构：零息债常有闭式
$$
P(t,T)=\exp\bigl(A(\tau)-B(\tau)r_t\bigr),\quad\tau=T-t,
$$
$A,B$ 由 ODE 决定（课堂知道“仿射 ⇒ 可算”即可）。

> [!example] 均值回复时间尺度
> $\kappa=0.5$（年$^{-1}$）时，冲击半衰期约 $\ln 2/\kappa\approx 1.4$ 年。$\kappa$ 大 → 快回到 $\theta$，长债波动相对受抑。

---

## 4. CIR 模型（直觉）

Cox–Ingersoll–Ross：
$$
dr_t=\kappa(\theta-r_t)\,dt+\sigma\sqrt{r_t}\,dW_t^\mathbb{Q}.
$$

- 扩散项 $\propto\sqrt{r}$：利率近 0 时波动变小，在 Feller 条件 $2\kappa\theta\ge\sigma^2$ 下可保持 $r_t\ge 0$；
- 仍属仿射族，零息债有闭式（涉及非中心 $\chi^2$ 等）。

> [!warning] 物理测度 vs 定价测度
> 估计 $\kappa,\theta$ 用历史数据（$\mathbb{P}$）与用债券价格校准（$\mathbb{Q}$）不是同一回事；风险溢价把漂移改写。混用两套参数会错价。

---

## 5. 与无套利 / 曲线校准（素描）

单因子短期利率模型自由度有限：往往无法完美拟合今日整条曲线的每个点，同时保持简单动力学。实务有：

- 扩展 Vasicek / Hull–White：让 $\theta=\theta(t)$ 变成确定性函数以拟合曲线；
- 远期利率框架（HJM）、LIBOR 市场模型：直接对曲线或市场报价建模——超出本笔记深度。

15.450 重点：理解 **$P=\mathbb{E}^\mathbb{Q}[e^{-\int r}]$** 与均值回复 / 仿射闭式的存在性。

---

## 6. 久期直觉（桥接产品笔记）

修正久期度量债券价格对收益率的敏感度；短期利率模型给出 $P(t,T;r)$ 后，
$$
\frac{\partial P}{\partial r}=-B(\tau)P
$$
（仿射债）提供模型内久期。产品侧的 Macauley / 修正久期与曲线构建见 [[Interest Rates Products and Models]]——此处只强调：**利率模型给出的是状态变量敏感度，需与市场报价语言对齐**。

多因子短期利率（如两因子）可改善曲线形态与相关性，但校准与风险中性漂移设定显著更重——课内以单因子建立 $\mathbb{E}^\mathbb{Q}[e^{-\int r}]$ 心智模型即可。

---

## 7. 与股票 BS 的对比

| | 股票 BS | 短期利率 |
|--|---------|----------|
| 状态 | $S_t$ | $r_t$（或整条曲线） |
| 折现 | $e^{-r\tau}$（$r$ 常数） | 随机 $\exp(-\int r)$ |
| 典型闭式 | 对数正态看涨 | 仿射债 $e^{A-Br}$ |
| 波动 | $\sigma S$ | $\sigma$ 或 $\sigma\sqrt{r}$ |

利率衍生品 Monte Carlo：模拟 $r_t$ 路径，累加 $\int r$，平均折现收益——接 [[Monte Carlo Methods for Derivatives]]。

---

## 8. 自检与参考答案

1. 写出零息债的风险中性定价公式。
2. 对比 Vasicek 与 CIR 的扩散项与符号限制。
3. 解释均值回复参数 $\kappa$ 的含义。
4. 为何历史估计的漂移不能直接当定价漂移。
5. 下一主题：[[Dynamic Programming and Asset Allocation]]。

> [!success]- 参考答案
> 1. $P(t,T)=\mathbb{E}^\mathbb{Q}[\exp(-\int_t^T r_s ds)\mid\mathcal{F}_t]$。
> 2. Vasicek：常数 $\sigma$，可负；CIR：$\sigma\sqrt{r}$，Feller 条件下可非负。
> 3. $\kappa$ 越大，$r$ 越快拉回 $\theta$。
> 4. 债券价格隐含风险溢价；$\mathbb{P}$-漂移 $\neq\mathbb{Q}$-漂移。
> 5. 从定价工具转向投资者动态优化（Merton）。

> [!example] 练习：折现因子
> 若路径上 $r_t\equiv 0.04$（常数）共 2 年，求 $\exp(-\int_0^2 r)$。

> [!success]- 练习参考答案
> $\exp(-0.04\cdot 2)=\exp(-0.08)\approx 0.923$。随机利率时对该量取 $\mathbb{Q}$-期望即得 $P(0,2)$。

> [!tip] 产品侧
> 互换 / 久期语言见 [[Interest Rates Products and Models]]。

## 参考

- Leonid Kogan, *15.450 Analytics of Finance*, MIT OCW Fall 2010（interest rate models）
- https://ocw.mit.edu/courses/15-450-analytics-of-finance-fall-2010/
- 产品直觉对照：[[Interest Rates Products and Models]]
