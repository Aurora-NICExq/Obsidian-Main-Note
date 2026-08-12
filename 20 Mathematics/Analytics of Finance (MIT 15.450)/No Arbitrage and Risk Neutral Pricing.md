---
aliases:
  - 无套利与风险中性定价
  - No Arbitrage
  - Risk Neutral Pricing
  - FTAP
  - 风险中性测度
tags: [math, analytics_finance]
up: "[[Analytics of Finance (MIT 15.450) MOC]]"
related:
  - "[[Ito Calculus for Finance]]"
  - "[[Black-Scholes Model and Extensions]]"
  - "[[Black-Scholes and Risk Neutral Valuation]]"
  - "[[Financial Markets Bonds and One-Period Models]]"
  - "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
down:
  - "[[Ito Calculus for Finance]]"
---
# 无套利与风险中性定价

> [!summary] 核心结论
> 在合适市场下，**无套利** $\Leftrightarrow$ 存在与物理测度 $\mathbb{P}$ 等价的**风险中性测度** $\mathbb{Q}$，使折现资产价格成为 $\mathbb{Q}$-鞅；可复制索赔的价格等于折现收益在 $\mathbb{Q}$ 下的期望。一期完备市场里可用线性代数手算状态价格 / 风险中性概率——这是 Black–Scholes 与利率模型的离散原型。

> 底本：MIT 15.450（Kogan）无套利 / 风险中性单元；对照 [[Financial Markets Bonds and One-Period Models]]、[[Black-Scholes and Risk Neutral Valuation]]。

> 关键词：arbitrage、FTAP、risk-neutral measure、state prices、complete market

---

## 1. 无套利：定义与直觉

**套利**（arbitrage）：零或负的初始净投入，未来收益几乎必然非负，且以正概率严格为正（“免费午餐”）。

无套利市场中，线性定价法则成立：相同净收益的组合必须同价；否则可做多便宜、做空贵的一边对冲净收益为零并锁定正现金流。

![[af-risk-neutral.svg]]

---

## 2. 一期模型：资产、收益矩阵

时间 $t=0,1$。状态 $\omega\in\Omega=\{\omega_1,\ldots,\omega_m\}$，概率 $\mathbb{P}(\omega)>0$。

- 无风险债券：$B_0=1$，到期 $B_1=1+r$（或直接用折现因子）。
- 风险资产价格向量 $S_0\in\mathbb{R}^n$；到期收益矩阵 $A$（$m\times n$），行对应状态、列对应资产。

组合 $\theta\in\mathbb{R}^n$：成本 $S_0\cdot\theta$，到期收益 $A\theta$。

**完备**（complete）：任意状态或有收益向量 $x\in\mathbb{R}^m$ 均可被某 $\theta$ 复制，即 $A\theta=x$ 对一切 $x$ 有解 $\Leftrightarrow$ $A$ 行满秩（通常 $n\ge m$ 且秩为 $m$）。

---

## 3. 数值例：完备市场定价

> [!example] 一期两状态、两资产
> $r=0$（折现因子 1），债券价格恒为 1。股票：$S_0=100$，
> $$
> S_1(\omega_u)=110,\qquad S_1(\omega_d)=90.
> $$
> 欧式看涨 $K=100$：$C_1=(S_1-100)^+$，故 $C_u=10$，$C_d=0$。
>
> **复制**：持有 $\Delta$ 股、借入 $B$（以债券计）：
> $$
> 110\Delta+B=10,\qquad 90\Delta+B=0
> \;\Rightarrow\;
> \Delta=\tfrac12,\quad B=-45.
> $$
> 无套利价格：
> $$
> C_0=\Delta S_0+B=50-45=5.
> $$
>
> **风险中性概率**：解
> $$
> 100=q\cdot 110+(1-q)\cdot 90
> \;\Rightarrow\;
> q=\tfrac12.
> $$
> （因 $r=0$。）故
> $$
> C_0=\mathbb{E}^\mathbb{Q}[C_1]=q\cdot 10+(1-q)\cdot 0=5.
> $$
> 与复制一致。注意 $\mathbb{Q}$ 由**价格**定出，不必等于真实 $\mathbb{P}$（哪怕 $\mathbb{P}(\omega_u)=0.7$）。

> [!warning] 完备 vs 不完全
> 若只有股票、没有足够独立收益源，$A$ 不满秩，部分期权不可复制；可能存在多个 $\mathbb{Q}$（无套利区间），唯一价格不再自动成立。

---

## 4. FTAP（第一基本定理，课堂版）

在有限 $\Omega$、无摩擦一期（或多期树）设定下：

1. **无套利** $\Leftrightarrow$ 存在等价鞅测度 $\mathbb{Q}\sim\mathbb{P}$，使折现价格为 $\mathbb{Q}$-鞅。
2. **完备** + 无套利 $\Leftrightarrow$ $\mathbb{Q}$ **唯一**，且任一可达索赔有唯一无套利价 $=\mathbb{E}^\mathbb{Q}[\text{折现收益}]$。

连续时间 Black–Scholes 是同一逻辑：改写漂移为 $r$，在 $\mathbb{Q}$ 下取期望（见 [[Black-Scholes Model and Extensions]]）。

---

## 5. 状态价格与 Arrow–Debreu

状态价格 $\psi(\omega)>0$：在状态 $\omega$ 支付 1、其余支付 0 的证券在 $t=0$ 的价格。则
$$
\text{任意收益 }x\text{ 的价格}=\sum_{\omega}\psi(\omega)\,x(\omega).
$$
归一化 $q(\omega)=\psi(\omega)/\sum\psi$ 即风险中性概率（折现已并入 $\psi$ 时需小心约定）。完备市场下 $\psi$ 由资产价格唯一解出。

与线性代数视角：定价是收益空间上的正线性泛函——见 [[Linear Algebra for Finance]]。

---

## 6. 多期树与动态复制（素描）

二叉树每步局部重复一期计算：后向归纳得期权节点值；$\Delta$ 随节点变化 → **动态对冲**。连续极限 + GBM → Black–Scholes PDE / 风险中性期望。

关键实践口诀：

- 定价用 $\mathbb{Q}$（或复制），风险管理 / 情景分析常回到 $\mathbb{P}$；
- 错误地把历史频率当风险中性概率会系统性错价。

---

## 7. 与 18.642 / 本课后续

| 主题 | 笔记 |
|------|------|
| 一期市场、债券贴现 | [[Financial Markets Bonds and One-Period Models]] |
| BS 公式与对冲 | [[Black-Scholes and Risk Neutral Valuation]]、[[Black-Scholes Model and Extensions]] |
| Itô 工具 | [[Ito Calculus for Finance]]、[[Stochastic Calculus and SDEs]] |
| 模拟定价 | [[Monte Carlo Methods for Derivatives]] |

---

## 8. 自检与参考答案

1. 陈述无套利与存在 $\mathbb{Q}$ 的对应（FTAP 课堂版）。
2. 在 $r=0$、$S\in\{90,110\}$、$S_0=100$ 下重算 ATM 看涨价格。
3. 解释为何 $\mathbb{Q}$ 一般 $\neq\mathbb{P}$，但定价仍用 $\mathbb{Q}$。
4. 说明不完全市场为何可能只有价格区间。
5. 下一主题：[[Ito Calculus for Finance]]。

> [!success]- 参考答案
> 1. 无套利 $\Leftrightarrow$ 存在 $\mathbb{Q}\sim\mathbb{P}$ 使折现价为鞅；完备时 $\mathbb{Q}$ 唯一且价格 $=\mathbb{E}^\mathbb{Q}[\text{折现收益}]$。
> 2. $q=1/2$，$C_0=\tfrac12\cdot 10=5$；或 $\Delta=1/2$、$B=-45$，$C_0=5$。
> 3. $\mathbb{Q}$ 由相对价格（风险的市场价格）确定；真实概率影响“觉得贵不贵”，不直接进无套利复制价。
> 4. 不可复制索赔可被多个 $\mathbb{Q}$ 给出不同期望 → 无唯一无套利价，只有套利界。
> 5. 连续时间用 Itô / GBM 把树极限写成 SDE，再接 BS。

> [!example] 练习：$r=5\%$
> 同上 $S_0=100$、$S_u=110$、$S_d=90$，看涨 $K=100$。求风险中性 $q$ 与 $C_0$（一期）。

> [!success]- 练习参考答案
> $100=q\cdot 110/(1.05)+(1-q)\cdot 90/(1.05)$
> $\Rightarrow 105=110q+90(1-q)=90+20q\Rightarrow q=0.75$。
> $C_0=\bigl[0.75\cdot 10+0.25\cdot 0\bigr]/1.05=7.5/1.05\approx 7.143$。

## 参考

- Leonid Kogan, *15.450 Analytics of Finance*, MIT OCW Fall 2010（no-arbitrage / RN pricing）
- https://ocw.mit.edu/courses/15-450-analytics-of-finance-fall-2010/
- Kerry Back, *A Course in Derivative Securities*（教材参考）
