---
aliases:
  - 动态规划与资产配置
  - Dynamic Programming
  - Merton Portfolio
  - 默顿组合
  - Bellman 方程
tags: [math, analytics_finance]
up: "[[Analytics of Finance (MIT 15.450) MOC]]"
related:
  - "[[Portfolio Management]]"
  - "[[Ito Calculus for Finance]]"
  - "[[Black-Scholes Model and Extensions]]"
  - "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
  - "[[No Arbitrage and Risk Neutral Pricing]]"
down:
  - "[[Monte Carlo Methods for Derivatives]]"
---
# 动态规划与资产配置

> [!summary] 核心结论
> 多期消费–投资问题用**动态规划（DP）**：价值函数满足 Bellman 方程，最优策略使当期效用与期望续值之和最大。Merton 问题在 i.i.d. 机会集下给出**短视（myopic）**需求；当投资机会随状态变量（随机 $r$、随机风险溢价等）变化时，出现额外的**对冲需求（hedging demand）**。对照静态均值–方差见 [[Portfolio Management]]。

> 底本：MIT 15.450 动态优化 / Merton 单元。

> 关键词：Bellman、value function、myopic demand、hedging demand、CRRA

---

## 1. 问题素描

投资者财富 $W_t$，可配置于无风险与风险资产（权重 $\pi_t$），并可消费 $c_t$。目标形如
$$
\max_{\pi,c}\;\mathbb{E}\Bigl[\int_0^T e^{-\delta t}U(c_t)\,dt+e^{-\delta T}U(W_T)\Bigr]
$$
（有限期；无限期类似）。约束：自融资预算（Itô 形式见 [[Ito Calculus for Finance]]）。

![[af-dynamic-opt.svg]]

---

## 2. Bellman 原理

价值函数 $J(t,W,\ldots)=$ 从状态 $(t,W,\ldots)$ 出发的最优期望目标。Bellman：
$$
J(t,W)=\max_{\pi,c}\Bigl\{U(c)\,\Delta t+\mathbb{E}\bigl[J(t+\Delta t,W+\Delta W)\bigr]+o(\Delta t)\Bigr\}.
$$
连续时间取极限得 HJB 方程（Hamilton–Jacobi–Bellman）：对控制最大化生成元 + 效用。要点不是背全 PDE，而是：

1. **向后归纳**思想；
2. 最优 $\pi^*$ 常由 $J$ 的导数（风险厌恶、财富敏感度）决定。

---

## 3. Merton：常系数、幂效用

经典设定：$dS/S=\mu\,dt+\sigma\,dW$，$r$ 常数；CRRA 效用 $U(c)=c^{1-\gamma}/(1-\gamma)$（$\gamma>0,\neq 1$）。

常投资机会下最优股票权重近似
$$
\pi^{*}=\frac{\mu-r}{\gamma\sigma^2}
$$
（Merton 分数）：风险溢价 /（相对风险厌恶 × 方差）。消费–财富比为常数（无限期时）。

> [!example] 数值
> $\mu-r=0.06$，$\sigma=0.20$，$\gamma=2$。  
> $\pi^{*}=0.06/(2\cdot 0.04)=0.06/0.08=0.75$。  
> $\gamma=4$ 则 $\pi^{*}=0.375$。风险厌恶加倍，风险仓位近似减半。

这与单期均值–方差最优在形式上同源（见 [[Portfolio Management]]），但来自多期效用最大化。

---

## 4. 短视需求 vs 对冲需求

将状态扩展为 $(W_t,X_t)$，$X$ 驱动投资机会（如随机风险溢价、随机 $r$）。最优 $\pi$ 分解直觉：

| 成分 | 含义 |
|------|------|
| **短视（myopic）** | 假装未来机会不变，只优化“这一瞬间”的均值–方差权衡 |
| **对冲（hedging）** | 当资产能对冲 $X$ 的不利变动时，额外持有 / 减持该资产 |

例：利率下降时债券涨；长期投资者怕再投资利率走低 → 可能**超配**长期债以对冲（状态变量对冲）。

> [!warning] 机会集 i.i.d. 时对冲项消失
> 若超额收益与波动不随时间变、无状态变量，只剩短视需求。实证“可预测收益 / 时变波动”会重新打开对冲通道——接 [[Return Predictability]]、[[Volatility Models GARCH]]。

---

## 5. 与定价课的边界

- **定价（RN）**：给出现金流的市场价值（无套利）。
- **组合优化（DP）**：在预算与偏好下选择持仓；用的是**物理测度**下的期望效用（或稳健偏好等）。

同一资产可同时出现在定价模型与优化模型中，但目标函数不同，勿把 $\mathbb{Q}$-期望直接当效用。

---

## 6. 离散 DP 迷你例

> [!example] 两期、对数效用（示意）
> 财富 $W_0=1$。每期可全投无风险（因子 $1.05$）或全投风险（以 $1/2$ 得 $1.2$ 或 $0.9$）。对数效用 $U=\log W$，只关心终期 $W_2$，无中间消费。
>
> 后向：在 $t=1$，若选风险，
> $\mathbb{E}[\log W_2]=\tfrac12\log(1.2 W_1)+\tfrac12\log(0.9 W_1)=\log W_1+\tfrac12\log(1.08)$；  
> 若选无风险：$\log(1.05 W_1)$。  
> 比较 $\tfrac12\log 1.08\approx 0.0385$ vs $\log 1.05\approx 0.0488$ → **此参数下选无风险更优**。  
> $t=0$ 同样比较。要点：后向比较续值，而不是只看单期均值。

（真实 Merton 允许连续权重 $\pi\in\mathbb{R}$，上例只演示 DP 方向。）

---

## 7. 与均值–方差的关系

单期均值–方差最优权重形如 $(\mu-r)/(\lambda\sigma^2)$，与 Merton 分数同构（$\lambda$ 扮演风险厌恶）。差别在于：

- MV 是单期 / 二次效用近似；
- Merton DP 在多期、中间消费、状态变量下系统导出对冲项；
- 约束（不允许卖空、负债）时需数值 DP，闭式消失。

静态有效前沿图见 [[Portfolio Management]] 的 `mf-portfolio` 思路；本课强调**动态**与状态依赖。

---

## 8. 自检与参考答案

1. 用一句话陈述 Bellman 原理。
2. 写出常系数 Merton 权重公式并解释 $\gamma$。
3. 区分短视需求与对冲需求。
4. 说明定价测度与效用优化为何不是同一运算。
5. 下一主题：[[Monte Carlo Methods for Derivatives]]。

> [!success]- 参考答案
> 1. 最优值 = 当期最优效用 + 期望后续最优价值（向后归纳）。
> 2. $\pi^*=(\mu-r)/(\gamma\sigma^2)$；$\gamma$ 相对风险厌恶，越大仓位越小。
> 3. 短视：瞬时均值–方差；对冲：对冲状态变量（机会集）风险的额外持仓。
> 4. 定价用 $\mathbb{Q}$ 期望折现收益；组合用 $\mathbb{P}$ 下期望效用最大化。
> 5. 用模拟估计 $\mathbb{E}^\mathbb{Q}[\text{payoff}]$ 等，转数值方法。

> [!example] 练习：Merton 权重
> $\mu=0.10$，$r=0.02$，$\sigma=0.25$，$\gamma=3$。求 $\pi^*$。

> [!success]- 练习参考答案
> $\pi^*=0.08/(3\cdot 0.0625)=0.08/0.1875\approx 0.427$。

## 参考

- Leonid Kogan, *15.450 Analytics of Finance*, MIT OCW Fall 2010（DP / Merton）
- https://ocw.mit.edu/courses/15-450-analytics-of-finance-fall-2010/
- John Cochrane, *Asset Pricing*（教材参考，组合 / 定价联系）
