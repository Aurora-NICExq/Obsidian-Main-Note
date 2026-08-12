---
aliases:
  - Black-Scholes与风险中性定价
  - Black-Scholes and Risk Neutral Valuation
  - 风险中性定价
  - delta hedging
tags: [math, math_finance]
up: "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
related:
  - "[[Volatility Modeling]]"
  - "[[Stochastic Calculus and SDEs]]"
  - "[[Financial Markets Bonds and One-Period Models]]"
  - "[[Probability and Stochastic Processes for Finance]]"
  - "[[Analytics of Finance (MIT 15.450) MOC]]"
down:
  - "[[Stochastic Calculus and SDEs]]"
---
# Black–Scholes 与风险中性定价

> [!summary] 核心结论
> 在 GBM + 无摩擦连续对冲假定下，欧式看涨有唯一无套利价——**Black–Scholes 公式**。推导主线不是猜 PDE，而是：**风险中性测度**下折现资产为鞅，故 $C=e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T-K)^+]$；等价地，Delta 对冲消去随机项得 PDE。$\Delta=\partial C/\partial S$ 是复制组合中的股票份数。

> 底本：MIT 18.642 衍生品 / BS 单元；一期原型见 [[Financial Markets Bonds and One-Period Models]]；Itô 细节见 [[Stochastic Calculus and SDEs]]。

> 关键词：风险中性、GBM、BS 公式、Delta、复制

---

## 1. 模型假设（经典）

$$
\mathrm{d}S_t=\mu S_t\,\mathrm{d}t+\sigma S_t\,\mathrm{d}W_t^{\mathbb{P}},
$$
常数 $r,\sigma$，可连续交易、无成本、可卖空，债券 $\mathrm{d}B=rB\,\mathrm{d}t$。欧式看涨支付 $(S_T-K)^+$。

![[mf-black-scholes.svg]]

现实违背：跳跃、随机波动、离散对冲——故有微笑（[[Volatility Modeling]]）。BS 仍是基准语言。

---

## 2. 风险中性定价

存在 $\mathbb{Q}\sim\mathbb{P}$，使
$$
\mathrm{d}S_t=r S_t\,\mathrm{d}t+\sigma S_t\,\mathrm{d}W_t^{\mathbb{Q}}.
$$
（漂移 $\mu\to r$；波动不变——Girsanov。）则
$$
C_0=e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T-K)^+].
$$
在 $\mathbb{Q}$ 下 $\log S_T\sim N\bigl(\log S_0+(r-\tfrac12\sigma^2)T,\ \sigma^2 T\bigr)$，积分得闭式。

> [!example] 数字直觉（平值粗算）
> $S=K=100$，$r=0$，$T=1$，$\sigma=0.2$。$d_1=\tfrac12\sigma\sqrt{T}=0.1$，$d_2=-0.1$。
> $$
> C=S\Phi(d_1)-K\Phi(d_2)=100\bigl(\Phi(0.1)-\Phi(-0.1)\bigr)=100\bigl(2\Phi(0.1)-1\bigr).
> $$
> $\Phi(0.1)\approx 0.5398$，故 $C\approx 7.97$。量级：约 $0.4\,S\sigma\sqrt{T}=8$（ATM 经验法则）。

---

## 3. BS 公式

$$
\begin{aligned}
C&=S_0\Phi(d_1)-Ke^{-rT}\Phi(d_2),\\
d_1&=\frac{\log(S_0/K)+(r+\tfrac12\sigma^2)T}{\sigma\sqrt{T}},\quad
d_2=d_1-\sigma\sqrt{T}.
\end{aligned}
$$
看跌由看跌–看涨平价：$P=C-S_0+Ke^{-rT}$（无股息）。有连续股息 $q$ 时 $S\to Se^{-qT}$ 等替换。

---

## 4. Delta 对冲素描

$C=C(S,t)$。Itô：
$$
\mathrm{d}C=\bigl(C_t+\mu S C_S+\tfrac12\sigma^2 S^2 C_{SS}\bigr)\mathrm{d}t+\sigma S C_S\,\mathrm{d}W.
$$
组合 $\Pi=C-\Delta S$，取 $\Delta=C_S$ 消去 $\mathrm{d}W$。无套利 ⇒ $\mathrm{d}\Pi=r\Pi\,\mathrm{d}t$，整理得 BS PDE：
$$
C_t+rSC_S+\tfrac12\sigma^2 S^2 C_{SS}=rC.
$$
终端 $C(S,T)=(S-K)^+$。

> [!warning] 离散对冲有误差
> 真实只能隔一段时间再平衡；误差随 $\sigma$、凸性 $|Gamma|$、重平衡间隔增大。Gamma 风险与跳跃无法由单 Delta 消除。

---

## 5. Greeks（极简）

| Greek | 定义 | 直觉 |
|-------|------|------|
| $\Delta$ | $C_S=\Phi(d_1)$（无股息看涨） | 对冲比率 |
| $\Gamma$ | $C_{SS}$ | Delta 对 $S$ 的敏感；凸性 |
| Vega | $C_\sigma$ | 对波动敏感（微笑交易核心） |
| $\Theta$ | $C_t$ | 时间衰减 |

作市：常卖出 Vega、管理 Gamma；方向用 Delta 对冲掉。

---

## 6. 与一期模型的连续极限

二项树：$u,d$ 与风险中性 $q$，步数 $n\to\infty$、适当缩放 → BS。一期笔记中的 $\psi$、$q$ 是同一 FTAP 的有限维版。完备市场：一个布朗运动、一个风险资产 ⇒ 期权可复制。

---

## 7. 公式中的概率解读

$\Phi(d_2)$：风险中性下 $S_T>K$ 的概率。$\Phi(d_1)$：股票测度（share measure）下同一事件概率，也等于 Delta。因而
$$
C=S_0\,\mathbb{Q}^S(S_T>K)-Ke^{-rT}\,\mathbb{Q}(S_T>K).
$$
这把公式读成“资产或无”与“现金或无”两种数字期权的组合——与一期状态权证思想一脉相承。

> [!example] 深度实值
> $S\gg K$，$d_1,d_2\to+\infty$，$\Phi\to 1$，$C\approx S-Ke^{-rT}$（远期价格意义下的内在价值）。深度虚值则 $C\to 0$，但 Vega 结构不同——短到期虚值对波动极敏感。

---

## 8. 有股息与外汇类比

连续股息率 $q$：把漂移改为 $r-q$，公式中 $S\to S e^{-qT}$ 出现在第一项。外汇：外币利率扮演 $q$。期货期权：Black-76 用 $F=S e^{(r-q)T}$ 改写。认清“一个对数正态标的 + 折现期望”即可在品种间平移。

---

## 9. 自检与参考答案

1. 写出 $\mathbb{Q}$ 下的 GBM 与定价公式 $C=e^{-rT}\mathbb{E}^{\mathbb{Q}}[\cdots]$。
2. 默写 $d_1,d_2$ 与看涨公式。
3. 说明为何 $\Delta=C_S$ 能消去风险。
4. 陈述看跌–看涨平价。
5. 指出两条 BS 假设在现实中的破裂方式。

> [!success]- 参考答案
> 1. $\mathrm{d}S=rS\mathrm{d}t+\sigma S\mathrm{d}W^{\mathbb{Q}}$；$C=e^{-rT}\mathbb{E}^{\mathbb{Q}}[(S_T-K)^+]$。
> 2. 见 §3。
> 3. $\mathrm{d}C$ 与 $\mathrm{d}S$ 的扩散项同为 $\sigma S C_S\mathrm{d}W$；空头 $\Delta=C_S$ 股股票抵消。
> 4. $C-P=S_0-Ke^{-rT}$（无股息）。
> 5. 常 $\sigma$（微笑）；连续对冲（离散/跳跃）；无成本等。

> [!example] 练习：平价
> $S=100$，$K=100$，$r=0$，$T=1$，$C=8$。求 $P$。

> [!success]- 练习参考答案
> $P=C-S+K=8$（因 $r=0$，$Ke^{-rT}=K$）。ATM 且 $r=0$ 时 $C=P$。

## 参考

- MIT 18.642 Black–Scholes lectures；18.S096
- https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/
