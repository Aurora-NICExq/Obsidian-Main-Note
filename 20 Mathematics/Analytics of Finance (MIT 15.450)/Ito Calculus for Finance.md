---
aliases:
  - Itô 微积分
  - Ito Calculus for Finance
  - 伊藤公式
  - Geometric Brownian Motion
  - GBM
tags: [math, analytics_finance]
up: "[[Analytics of Finance (MIT 15.450) MOC]]"
related:
  - "[[No Arbitrage and Risk Neutral Pricing]]"
  - "[[Black-Scholes Model and Extensions]]"
  - "[[Stochastic Calculus and SDEs]]"
  - "[[Probability and Stochastic Processes for Finance]]"
  - "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
down:
  - "[[Black-Scholes Model and Extensions]]"
---
# 金融中的 Itô 微积分

> [!summary] 核心结论
> 几何布朗运动（GBM）$dS=\mu S\,dt+\sigma S\,dW$ 是连续时间股价的基准模型。Itô 公式给出 $f(S,t)$ 的微分：除普通链式法则外，多出 $\tfrac12 f_{SS}(dS)^2$ 项，且 $(dW)^2=dt$。由此可推出折现股价在风险中性下的漂移、以及 Black–Scholes PDE 的随机来源。本笔记给陈述 + 简单应用；更广的随机过程背景见 [[Stochastic Calculus and SDEs]]。

> 底本：MIT 15.450 Itô / 随机微积分单元。

> 关键词：Wiener process、Itô formula、GBM、quadratic variation

---

## 1. 布朗运动速写

标准维纳过程 $W_t$：

- $W_0=0$；独立增量；$W_t-W_s\sim\mathcal{N}(0,t-s)$；
- 路径几乎必然连续，但几乎必然不可微；
- 二次变差 $\langle W\rangle_t=t$（离散和 $\sum(\Delta W)^2\to t$）。

启发式乘法表（Itô）：
$$
(dt)^2=0,\quad dt\,dW=0,\quad (dW)^2=dt.
$$

对照 [[Probability and Stochastic Processes for Finance]] 中的随机游走极限直觉。

---

## 2. Itô 过程与 Itô 公式

一般 Itô 过程：
$$
dX_t=a(X_t,t)\,dt+b(X_t,t)\,dW_t.
$$

对 $C^{2,1}$ 函数 $f(x,t)$，**Itô 公式**：
$$
\begin{aligned}
df(X_t,t)
&=f_t\,dt+f_x\,dX+\tfrac12 f_{xx}(dX)^2\\
&=\Bigl(f_t+a f_x+\tfrac12 b^2 f_{xx}\Bigr)dt+b f_x\,dW.
\end{aligned}
$$
多出的 $\tfrac12 b^2 f_{xx}\,dt$ 正是普通微积分没有的项。

> [!warning] 勿用“普通链式法则”对 $W_t^2$
> 若误用 $d(W^2)=2W\,dW$，会丢掉 $dt$。正确：$d(W_t^2)=2W_t\,dW_t+dt$。

---

## 3. 几何布朗运动（GBM）

$$
dS_t=\mu S_t\,dt+\sigma S_t\,dW_t,\qquad \sigma>0\text{ 常数}.
$$

对 $f=\log S$（$f_S=1/S$，$f_{SS}=-1/S^2$）：
$$
\begin{aligned}
d\log S
&=\frac{1}{S}dS+\tfrac12\Bigl(-\frac{1}{S^2}\Bigr)(\sigma S\,dW)^2+\cdots\\
&=\Bigl(\mu-\tfrac12\sigma^2\Bigr)dt+\sigma\,dW.
\end{aligned}
$$
积分得显式解：
$$
S_t=S_0\exp\Bigl(\bigl(\mu-\tfrac12\sigma^2\bigr)t+\sigma W_t\Bigr).
$$
故 $\log S_t$ 正态，$S_t$ 对数正态。$\mathbb{E}[S_t]=S_0 e^{\mu t}$（漂移是 $\mu$ 不是 $\mu-\sigma^2/2$）。

> [!example] 数值：对数均值
> $S_0=100$，$\mu=0.08$，$\sigma=0.20$，$t=1$。  
> $\mathbb{E}[\log(S_1/S_0)]=\mu-\sigma^2/2=0.08-0.02=0.06$。  
> 中位数 $S_1$：$100 e^{0.06}\approx 106.2$；均值 $\mathbb{E}[S_1]=100 e^{0.08}\approx 108.3$。  
> 偏态：均值 > 中位数——期权定价时勿混淆。

---

## 4. 简单应用：自融资与乘积法则

两过程 $X,Y$ 的 Itô 乘积法则：
$$
d(XY)=X\,dY+Y\,dX+dX\,dY.
$$
（多出的交叉项 $dX\,dY$ 来自二次协变差。）

自融资组合价值 $V=\phi S+\psi B$（$B$ 为货币市场账户）满足
$$
dV=\phi\,dS+\psi\,dB
$$
（无额外注入资金）。这是推导复制 / BS PDE 的预算约束。

---

## 5. 风险中性下的 GBM

无套利下存在 $\mathbb{Q}$，使折现 $e^{-rt}S_t$ 为 $\mathbb{Q}$-鞅，等价于
$$
dS_t=r S_t\,dt+\sigma S_t\,dW_t^\mathbb{Q}.
$$
（Girsanov：把物理漂移 $\mu$ 改为 $r$。）衍生品价格
$$
V_0=\mathbb{E}^\mathbb{Q}\bigl[e^{-rT}g(S_T)\bigr]
$$
——接 [[No Arbitrage and Risk Neutral Pricing]] 与 [[Monte Carlo Methods for Derivatives]]。

---

## 6. 从 Itô 到 Black–Scholes PDE（预告）

令 $C=C(S,t)$ 为看涨价格。Itô：
$$
dC=\Bigl(C_t+\mu S C_S+\tfrac12\sigma^2 S^2 C_{SS}\Bigr)dt+\sigma S C_S\,dW.
$$
用 $\Delta=C_S$ 对冲，消去 $dW$ 项；无套利迫使组合赚无风险利率 → PDE
$$
C_t+r S C_S+\tfrac12\sigma^2 S^2 C_{SS}=rC.
$$
细节见 [[Black-Scholes Model and Extensions]]。

---

## 7. 与 18.642 对照

| 15.450 侧重 | 18.642 对照 |
|-------------|-------------|
| 公式 + 定价应用 | [[Stochastic Calculus and SDEs]] 更广的 SDE 直觉 |
| GBM → RN 期望 | [[Black-Scholes and Risk Neutral Valuation]] |
| 模拟路径 | 本课 [[Monte Carlo Methods for Derivatives]] |

概率基础：[[Probability and Statistics (MIT 18.05) MOC]]、[[Continuous Random Variables]]（对数正态）。

---

## 8. 自检与参考答案

1. 写出 GBM 与 $S_t$ 显式解。
2. 陈述 Itô 公式并指出多出的二次变差项。
3. 计算 $d(W_t^2)$。
4. 说明风险中性下 $\mu$ 换成什么。
5. 下一主题：[[Black-Scholes Model and Extensions]]。

> [!success]- 参考答案
> 1. $dS=\mu S\,dt+\sigma S\,dW$；$S_t=S_0\exp((\mu-\sigma^2/2)t+\sigma W_t)$。
> 2. $df=f_t dt+f_x dX+\tfrac12 f_{xx}(dX)^2$；$(dW)^2=dt$ 贡献二次项。
> 3. $d(W^2)=2W\,dW+dt$。
> 4. 换成无风险利率 $r$（股票的 $\mathbb{Q}$-漂移）。
> 5. 用 Itô + 对冲推出 BS PDE，或直接 $\mathbb{E}^\mathbb{Q}$ 定价。

> [!example] 练习：对 $f=S^2$ 用 Itô
> GBM 下求 $d(S_t^2)$ 的漂移系数（$dt$ 项前的因子）。

> [!success]- 练习参考答案
> $f_S=2S$，$f_{SS}=2$。  
> $d(S^2)=2S\,dS+\tfrac12\cdot 2\cdot(\sigma S\,dW)^2=2S(\mu S dt+\sigma S dW)+\sigma^2 S^2 dt$  
> $=(2\mu+\sigma^2)S^2\,dt+2\sigma S^2\,dW$。漂移因子 $(2\mu+\sigma^2)S^2$。

## 参考

- Leonid Kogan, *15.450 Analytics of Finance*, MIT OCW Fall 2010（Itô calculus）
- https://ocw.mit.edu/courses/15-450-analytics-of-finance-fall-2010/
