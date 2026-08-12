---
aliases:
  - Black-Scholes
  - Black–Scholes 模型
  - BS PDE
  - Greeks
  - 布莱克-斯科尔斯
tags: [math, analytics_finance]
up: "[[Analytics of Finance (MIT 15.450) MOC]]"
related:
  - "[[Ito Calculus for Finance]]"
  - "[[No Arbitrage and Risk Neutral Pricing]]"
  - "[[Monte Carlo Methods for Derivatives]]"
  - "[[Black-Scholes and Risk Neutral Valuation]]"
  - "[[Volatility Modeling]]"
  - "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
down:
  - "[[Interest Rate Models]]"
---
# Black–Scholes 模型与扩展

> [!summary] 核心结论
> 在 GBM、常数 $r,\sigma$、无摩擦、可连续交易等假设下，欧式看涨有唯一无套利价；等价表述为 **BS PDE** 或 **风险中性期望** $\mathbb{E}^\mathbb{Q}[e^{-rT}(S_T-K)^+]$。Greeks 描述对参数的敏感度（$\Delta$ 对冲）。简单扩展：连续股息率 $q$、时变确定波动 $\sigma(t)$；随机波动 / 跳跃则超出经典闭式。

> 底本：MIT 15.450；对照 [[Black-Scholes and Risk Neutral Valuation]]。

> 关键词：BS PDE、risk-neutral expectation、delta hedge、Greeks、dividend yield

---

## 1. 模型假设（清单）

- $dS=\mu S\,dt+\sigma S\,dW$（$\sigma$ 常数）；
- 常数无风险利率 $r$；可连续交易、无交易成本、可卖空；
- 欧式行权，到期收益 $g(S_T)=(S_T-K)^+$（看涨）或 $(K-S_T)^+$（看跌）。

物理漂移 $\mu$ **不进入** 期权价格——被风险中性替换为 $r$。

---

## 2. 两条定价路

### 2.1 PDE

$C(S,t)$ 满足终值 $C(S,T)=(S-K)^+$ 与
$$
C_t+r S C_S+\tfrac12\sigma^2 S^2 C_{SS}=r C
$$
（推导见 [[Ito Calculus for Finance]]：$\Delta$-对冲 + 无套利）。

### 2.2 期望

在 $\mathbb{Q}$ 下 $dS=r S\,dt+\sigma S\,dW^\mathbb{Q}$，
$$
C(S,t)=e^{-r(T-t)}\mathbb{E}^\mathbb{Q}\bigl[(S_T-K)^+\bigm|S_t=S\bigr].
$$
对数正态积分得闭式（下节）。Monte Carlo 直接估这个期望——见 [[Monte Carlo Methods for Derivatives]]。

两条路数学等价（Feynman–Kac）。

---

## 3. 闭式公式（记结构，少背细节）

$$
\begin{aligned}
C&=S_t\Phi(d_1)-Ke^{-r\tau}\Phi(d_2),\\
d_1&=\frac{\ln(S_t/K)+(r+\sigma^2/2)\tau}{\sigma\sqrt{\tau}},\quad
d_2=d_1-\sigma\sqrt{\tau},\quad \tau=T-t.
\end{aligned}
$$
$\Phi$ 为标准正态 CDF。看跌由看跌–看涨平价：
$$
P=C-S_t+Ke^{-r\tau}
$$
（无股息时）。

> [!example] ATM 粗算直觉
> $S=K=100$，$r=0$，$\sigma=0.2$，$\tau=1$。  
> $d_1=\sigma/2=0.1$，$d_2=-0.1$，$\Phi(0.1)\approx 0.540$，$\Phi(-0.1)\approx 0.460$。  
> $C\approx 100\cdot 0.540-100\cdot 0.460=8.0$。  
> 经验口诀：短到期 ATM 约 $0.4\,S\sigma\sqrt{\tau}$（此处 $0.4\cdot 20=8$）量级正确。

---

## 4. Greeks 直觉

| Greek | 定义 | 直觉 |
|-------|------|------|
| $\Delta=C_S$ | $=\Phi(d_1)$（看涨） | 对冲比：卖 1 份看涨 ≈ 买 $\Delta$ 股 |
| $\Gamma=C_{SS}$ | $\Delta$ 对 $S$ 的凸性 | $S$ 大动时 $\Delta$ 漂移快，需再平衡 |
| $\mathcal{V}$（Vega） | $\partial C/\partial\sigma$ | 长期权通常正 Vega：隐含波动升则贵 |
| $\Theta$ | $\partial C/\partial t$ | 时间流逝；ATM 附近常为负 |
| $\rho$ | $\partial C/\partial r$ | 看涨通常随 $r$ 升而升 |

> [!warning] $\Delta$-对冲不是无风险到期末
> 连续再平衡 + 模型正确时局部无风险；离散对冲有残差；$\sigma$ 估错 → 对冲误差系统性放大。

---

## 5. 简单扩展

### 5.1 连续股息率 $q$

股票持有者损失“股息漏出”；风险中性漂移变为 $r-q$：
$$
C=e^{-q\tau}S\Phi(d_1)-Ke^{-r\tau}\Phi(d_2),
$$
$d_{1,2}$ 中 $r\to r-q$。外汇用外国利率类比 $q$。

### 5.2 时变确定波动 $\sigma(t)$

有效总方差 $\int_0^T\sigma(t)^2 dt$ 替换 $\sigma^2 T$；仍有类 BS 公式。若波动是**随机过程**（Heston 等），则需另一状态变量，PDE 升维，一般无简单 BS 闭式。

### 5.3 与隐含波动

市场价反推 $\sigma_{\mathrm{imp}}$；微笑 / 偏斜说明常数 $\sigma$ 假设被破坏——接 [[Volatility Modeling]]、[[Volatility Models GARCH]]（历史 / 条件波动另一条线）。

---

## 6. 数值小例：平价与 $\Delta$

> [!example] 平价检查
> $S=100$，$K=100$，$r=0.05$，$\tau=1$，$C=10.45$（设）。  
> $P=C-S+Ke^{-r\tau}=10.45-100+100/e^{0.05}\approx 10.45-100+95.12=5.57$。  
> 若市价看跌显著偏离，存在静态套利（合成关系）。

对冲：若 $\Delta\approx 0.60$，做市商卖 10 份看涨约买 $6$ 股标的做 $\Delta$-中性；$\Gamma>0$ 时标的大涨后需再买一点。

---

## 7. 自检与参考答案

1. 写出 BS PDE 与风险中性期望两种表述。
2. 说明为何价格不含 $\mu$。
3. 解释 $\Delta$ 与离散对冲风险。
4. 股息率 $q$ 如何改漂移。
5. 时变确定 $\sigma(t)$ 与随机波动的差别（一句话）。
6. 下一主题：[[Interest Rate Models]]。

> [!success]- 参考答案
> 1. PDE：$C_t+rSC_S+\tfrac12\sigma^2 S^2 C_{SS}=rC$；期望：$e^{-r\tau}\mathbb{E}^\mathbb{Q}[(S_T-K)^+|S_t]$。
> 2. 复制 / $\mathbb{Q}$ 把漂移钉在 $r$；$\mu$ 被 Girsanov 吸收进测度变换。
> 3. $\Delta=C_S$ 为瞬时对冲比；离散再平衡 + 模型误差留下残差 PnL。
> 4. $\mathbb{Q}$ 下 $dS=(r-q)S\,dt+\sigma S\,dW$；公式中出现 $e^{-q\tau}S$。
> 5. 确定 $\sigma(t)$ 仍可并进总方差；随机波动需额外状态，一般失去经典闭式。
> 6. 利率本身随机时，$r$ 常数假设放开 → 短期利率模型。

> [!example] 练习：看跌–看涨
> 无股息，$C=12$，$S=100$，$K=100$，$r=0$，$\tau$ 任意。求 $P$。

> [!success]- 练习参考答案
> $P=C-S+K=12-100+100=12$（$r=0$ 时 ATM 看涨看跌同价）。

## 参考

- Leonid Kogan, *15.450 Analytics of Finance*, MIT OCW Fall 2010（Black–Scholes）
- https://ocw.mit.edu/courses/15-450-analytics-of-finance-fall-2010/
- Kerry Back, *A Course in Derivative Securities*（教材参考）
