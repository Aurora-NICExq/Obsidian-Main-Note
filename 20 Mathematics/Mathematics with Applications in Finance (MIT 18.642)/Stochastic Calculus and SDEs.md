---
aliases:
  - 随机微积分与SDE
  - Stochastic Calculus and SDEs
  - Itô公式
  - geometric Brownian motion
tags: [math, math_finance]
up: "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
related:
  - "[[Black-Scholes and Risk Neutral Valuation]]"
  - "[[Probability and Stochastic Processes for Finance]]"
  - "[[Volatility Modeling]]"
  - "[[Analytics of Finance (MIT 15.450) MOC]]"
  - "[[Linear Algebra and Differential Equations]]"
down:
  - "[[Machine Learning in Finance]]"
---
# 随机微积分与 SDE

> [!summary] 核心结论
> 随机微分方程 $\mathrm{d}X=a(X,t)\mathrm{d}t+b(X,t)\mathrm{d}W$ 描述噪声驱动的动态。**Itô 公式**是链式法则的修正版：因 $(\mathrm{d}W)^2=\mathrm{d}t$，二阶项留下。乘积规则 $\mathrm{d}(XY)=X\mathrm{d}Y+Y\mathrm{d}X+\mathrm{d}X\mathrm{d}Y$。GBM 是 $a=\mu S$、$b=\sigma S$ 的特例，解为对数正态——BS 的动力引擎。

> 底本：MIT 18.642 随机微积分单元；布朗运动直觉见 [[Probability and Stochastic Processes for Finance]]；应用见 [[Black-Scholes and Risk Neutral Valuation]]。

> 关键词：Itô 积分、Itô 公式、乘积规则、GBM、二次变差

---

## 1. 为何普通微积分不够

布朗路径几乎处处不可微、无限长。积分 $\int H\,\mathrm{d}W$ 需 Itô（非预期被积函数）或 Stratonovich 等定义。金融默认 **Itô**：今天的持仓乘明天的增量，符合“不能预知 $\mathrm{d}W$”。

二次变差：$[W,W]_t=t$。形式规则：
$$
\mathrm{d}t\cdot\mathrm{d}t=0,\quad \mathrm{d}t\cdot\mathrm{d}W=0,\quad \mathrm{d}W\cdot\mathrm{d}W=\mathrm{d}t.
$$

![[mf-sde.svg]]

---

## 2. Itô 公式（一维）

$X$ 满足 $\mathrm{d}X=a\mathrm{d}t+b\mathrm{d}W$，$f(x,t)$ 足够光滑，则
$$
\begin{aligned}
\mathrm{d}f(X,t)&=f_t\mathrm{d}t+f_x\mathrm{d}X+\tfrac12 f_{xx}(\mathrm{d}X)^2\\
&=\bigl(f_t+a f_x+\tfrac12 b^2 f_{xx}\bigr)\mathrm{d}t+b f_x\,\mathrm{d}W.
\end{aligned}
$$
多了 $\tfrac12 b^2 f_{xx}\mathrm{d}t$——对数、指数变换时决定漂移修正。

> [!example] $f=\log S$（GBM）
> $\mathrm{d}S=\mu S\mathrm{d}t+\sigma S\mathrm{d}W$。$f_x=1/S$，$f_{xx}=-1/S^2$，$f_t=0$：
> $$
> \mathrm{d}\log S=\bigl(\mu-\tfrac12\sigma^2\bigr)\mathrm{d}t+\sigma\mathrm{d}W.
> $$
> 故 $\mathbb{E}[\log S_T]=\log S_0+(\mu-\tfrac12\sigma^2)T$，而 $\mathbb{E}[S_T]=S_0 e^{\mu T}$——两者不矛盾。

---

## 3. 乘积规则

$$
\mathrm{d}(XY)=X\mathrm{d}Y+Y\mathrm{d}X+\mathrm{d}X\,\mathrm{d}Y.
$$
若 $X,Y$ 皆有扩散项，交叉项 $\mathrm{d}X\mathrm{d}Y=b_X b_Y\mathrm{d}t$ 一般非零。应用：折现价格 $\tilde S=e^{-rt}S$，
$$
\mathrm{d}\tilde S=e^{-rt}(\mathrm{d}S-rS\mathrm{d}t)+\cdots
$$
在 $\mathbb{Q}$ 下漂移抵消 → 鞅（[[Black-Scholes and Risk Neutral Valuation]]）。

---

## 4. GBM 显式解

$$
\mathrm{d}S=\mu S\mathrm{d}t+\sigma S\mathrm{d}W\ \Rightarrow\
S_t=S_0\exp\Bigl(\bigl(\mu-\tfrac12\sigma^2\bigr)t+\sigma W_t\Bigr).
$$
验证：对指数函数用 Itô 即可。这是少数有漂亮闭式的非线性 SDE。

> [!warning] 欧拉离散有偏
> 模拟 $S_{t+\Delta}=S_t+a\Delta+b\sqrt{\Delta}Z$ 是欧拉格式；对 GBM 更好用对数欧拉（精确格式）。步长过大时欧拉可产生负价格（若扩散非 Lipschitz 处理不当）。

---

## 5. 其他常用 SDE（地图）

| 模型 | SDE 素描 | 用途 |
|------|----------|------|
| OU / Vasicek | $\mathrm{d}r=\kappa(\bar r-r)\mathrm{d}t+\sigma\mathrm{d}W$ | 均值回复利率 |
| CIR | 扩散 $\propto\sqrt{r}$ | 正利率 |
| Heston | $\mathrm{d}v=\ldots$，$v$ 为方差 | 随机波动 |
| 本地波动 | $\sigma(S,t)$ | 拟合微笑 |

深入数值与估计：[[Analytics of Finance (MIT 15.450) MOC]]、[[Volatility Modeling]]。

---

## 6. 与确定性 ODE 对照

ODE $\dot x=a(x)$：流由初值唯一决定。SDE：同初值、不同 $\omega$ 给出束路径；“解”常指强解（路径意义）或弱解（分布意义）。存在唯一性要 Lipschitz 等条件——工程上先保证系数别爆炸。

---

## 7. 数值直觉：欧拉–丸山

离散：$X_{n+1}=X_n+a(X_n,t_n)\Delta t+b(X_n,t_n)\sqrt{\Delta t}\,Z_n$，$Z_n\sim N(0,1)$ i.i.d.。弱误差（期望泛函）阶 $O(\Delta t)$，强误差（路径）阶 $O(\sqrt{\Delta t})$。蒙特卡洛定价：模拟许多终点 $S_T$，平均支付再折现——这是 BS 积分的数值版，也适用于无闭式支付。

> [!example] 一步矩检查
> GBM 欧拉：$S_{\Delta}=S_0+\mu S_0\Delta+\sigma S_0\sqrt{\Delta}Z$。$\mathbb{E}[S_{\Delta}]=S_0(1+\mu\Delta)$，与真期望 $S_0 e^{\mu\Delta}$ 差 $O(\Delta^2)$。对数欧拉用精确解抽样，一步无偏（对 GBM）。

路径依赖支付（亚式、障碍）更依赖模拟质量：减少方差可用对偶变量、控制变量（用 BS 闭式作控制）。

---

## 8. 多维与相关噪声

$\mathrm{d}W$ 成向量，$\mathrm{d}W\mathrm{d}W^\top=\rho\,\mathrm{d}t$（相关矩阵）。资产篮子、外汇三角、利率因子都需要 Cholesky 把独立噪声染成相关。PCA 可对瞬时协方差降维——与 [[Regression and PCA in Finance]] 同一谱思想。

Feynman–Kac：期望 $\mathbb{E}[f(X_T)]$ 在一定条件下等于 PDE 解——这是 BS PDE 与风险中性期望的桥梁（点到即可）。

---

## 9. 自检与参考答案

1. 写出一维 Itô 公式并标出额外项。
2. 推导 $\mathrm{d}\log S$ 在 GBM 下的漂移。
3. 陈述乘积规则并解释何时有 $\mathrm{d}t$ 交叉项。
4. 写出 GBM 显式解。
5. 为何金融用 Itô 解释“非预期策略”？

> [!success]- 参考答案
> 1. $\mathrm{d}f=(f_t+af_x+\tfrac12 b^2 f_{xx})\mathrm{d}t+bf_x\mathrm{d}W$；额外 $\tfrac12 b^2 f_{xx}\mathrm{d}t$。
> 2. $\mu-\tfrac12\sigma^2$。
> 3. $\mathrm{d}(XY)=X\mathrm{d}Y+Y\mathrm{d}X+\mathrm{d}X\mathrm{d}Y$；两扩散系数之积给出 $\mathrm{d}t$ 项。
> 4. $S_t=S_0\exp((\mu-\tfrac12\sigma^2)t+\sigma W_t)$。
> 5. 被积函数在增量发生前已决定，对应不能预知未来噪声的持仓。

> [!example] 练习：Ornstein–Uhlenbeck 均值
> $\mathrm{d}X=-\kappa X\mathrm{d}t+\sigma\mathrm{d}W$，$X_0=x$。求 $\mathbb{E}[X_t]$。

> [!success]- 练习参考答案
> 取期望消去扩散：$\frac{d}{dt}\mathbb{E}[X]=-\kappa\mathbb{E}[X]$，故 $\mathbb{E}[X_t]=x e^{-\kappa t}$。

## 参考

- MIT 18.642 stochastic calculus lectures；18.S096
- https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/
