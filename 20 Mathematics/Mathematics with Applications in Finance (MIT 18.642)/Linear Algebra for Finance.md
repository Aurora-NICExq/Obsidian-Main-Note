---
aliases:
  - 金融中的线性代数
  - Linear Algebra for Finance
  - 组合向量与线性定价
  - portfolio as vector
tags: [math, math_finance]
up: "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
related:
  - "[[Financial Markets Bonds and One-Period Models]]"
  - "[[Regression and PCA in Finance]]"
  - "[[Portfolio Management]]"
  - "[[Linear Algebra (MIT 18.06) MOC]]"
  - "[[Eigenvalues and Eigenvectors]]"
down:
  - "[[Probability and Stochastic Processes for Finance]]"
---
# 金融中的线性代数

> [!summary] 核心结论
> 把 $n$ 种资产的持仓写成向量 $\theta$，价格 $p$，收益/支付写成矩阵作用：$V=A\theta$。无套利定价是**正线性泛函**；因子模型与 PCA 是对收益协方差 $\Sigma$ 的谱分解。18.06 的投影、特征值、正交对角化在这里直接变成：复制、主成分因子、均值–方差二次型 $\theta^\top\Sigma\theta$。

> 底本：MIT 18.642 线性代数单元；底座 [[Linear Algebra (MIT 18.06) MOC]]；市场设定见 [[Financial Markets Bonds and One-Period Models]]。

> 关键词：持仓向量、支付矩阵、协方差二次型、投影、谱分解

---

## 1. 组合作向量

权重 $w\in\mathbb{R}^n$（常约束 $1^\top w=1$ 为全投资），或份额 $\theta$。单期简单收益向量 $R$，组合收益
$$
R_p=w^\top R,\qquad
\mathbb{E}[R_p]=w^\top\mu,\qquad
\mathrm{Var}(R_p)=w^\top\Sigma w.
$$
$\Sigma=\mathrm{Cov}(R)$ 对称半正定。几何：方差是 $\Sigma$-半范数的平方——[[Portfolio Management]] 的有效前沿即二次型水平集与超平面的切触。

> [!example] 两资产数字
> $\mu=(0.08,0.12)^\top$，$\sigma_1=0.15$，$\sigma_2=0.25$，$\rho=0.2$。则
> $$
> \Sigma=\begin{pmatrix}0.0225&0.0075\\0.0075&0.0625\end{pmatrix}
> $$
> （因 $\rho\sigma_1\sigma_2=0.2\cdot0.15\cdot0.25=0.0075$）。$w=(0.6,0.4)^\top$：
> $$
> \mathbb{E}[R_p]=0.6\cdot0.08+0.4\cdot0.12=0.096,\quad
> w^\top\Sigma w=0.6^2\cdot0.0225+2\cdot0.6\cdot0.4\cdot0.0075+0.4^2\cdot0.0625=0.0205.
> $$
> $\sigma_p=\sqrt{0.0205}\approx 0.143$。

---

## 2. 一期线性定价 = 线性方程

回顾支付矩阵 $A\in\mathbb{R}^{m\times n}$、价格 $p$。复制支付 $X$：解 $A\theta=X$。

- 有解 $\Leftrightarrow X\in\mathrm{Col}(A)$（完备方向）。
- 多解 $\Leftrightarrow$ 存在冗余资产（列相关）——价格须满足相容性 $p^\top\theta$ 对所有解相同，否则套利。
- 最小范数解：$\theta=A^{+}X$（伪逆），与 18.06 最小二乘同一套。

状态价格：$\psi$ 满足 $A^\top\psi=p$。这是 $n$ 个方程、$m$ 个未知数；无套利要求存在 $\psi\gg 0$。

---

## 3. 投影：回归与对冲的共同几何

观测收益 $y\in\mathbb{R}^T$，因子载荷矩阵 $X$（列=因子实现）。OLS
$$
\hat\beta=(X^\top X)^{-1}X^\top y,\qquad \hat y=Hy,\quad H=X(X^\top X)^{-1}X^\top
$$
把 $y$ 正交投影到 $\mathrm{Col}(X)$。金融解读：

- **因子模型**：$R=\alpha+B f+\varepsilon$，残差正交于因子（样本版）；
- **对冲**：用可交易工具列空间去逼近目标支付，残差 = 基差风险。

详见 [[Regression and PCA in Finance]] 与 [[Linear Regression]]。

---

## 4. 协方差与谱：PCA 预备

$\Sigma=Q\Lambda Q^\top$（正交对角化，$Q$ 列=特征向量）。主成分得分是 $Q^\top(R-\mu)$ 的坐标。前 $k$ 个大特征值解释“市场 / 斜率 / 曲率”等共同波动——收益率曲线 PCA 的线性代数内核。

> [!warning] 样本 $\hat\Sigma$ 在 $n$ 大、$T$ 不够时病态
> 特征值过度分散是高维组合的经典陷阱；需收缩、因子结构或正则。PCA 解释力高 ≠ 下一期仍稳定。

特征值直觉（18.06）：$\Sigma v=\lambda v$ 表示沿 $v$ 方向的方差为 $\lambda$。最大 $\lambda$ 方向 = 波动最大的组合方向（未做权重约束时）。

---

## 5. 久期作为线性敏感度

债券价格 $P(y)$ 对收益率 $y$ 的一阶：
$$
\mathrm{d}P\approx -D_{\mathrm{mod}}\,P\,\mathrm{d}y.
$$
组合久期是成分久期的**权重平均**（价值权重）——又是线性组合。凸性是二阶项，对应 Hessian / 二次型修正。高层产品语言见 [[Interest Rates Products and Models]]。

---

## 6. 现金与多余自由度

全投资约束 $1^\top w=1$ 把可行集变成仿射超平面；允许现金时增加一维。均值–方差优化在约束下对拉格朗日求导，得到线性方程组——再一次“金融问题 = 解 $Ax=b$”。

空头、杠杆：$\theta$ 可含负分量；线性代数照常，风险与保证金约束是额外不等式（本课点到为止）。

---

## 7. 与 18.06 的对照表

| 18.06 | 18.642 用法 |
|-------|-------------|
| 列空间 / 秩 | 可复制支付、市场完备性 |
| 正交投影 | 回归因子、最小二乘对冲 |
| $A^\top A$ / 正规方程 | OLS、协方差相关计算 |
| 特征值分解 | PCA 因子、风险模式 |
| 二次型 $x^\top Ax$ | 组合方差 $w^\top\Sigma w$ |
| 伪逆 | 欠定/过定复制 |

---

## 8. 条件数与数值

$\kappa(\Sigma)=\lambda_{\max}/\lambda_{\min}$。相关矩阵近奇异（资产几乎同质）时求逆不稳，最优权重抖。预处理：加对角线抖动 $\Sigma+\varepsilon I$、因子模型降秩、或约束优化避免显式逆。18.06 条件数直觉在这里直接变成“组合爆炸”。

> [!example] 两资产近共线
> $\rho=0.999$，$\sigma_1=\sigma_2=0.2$。最小特征值 $\propto(1-\rho)$ 极小；$\Sigma^{-1}$ 在差分成份上巨大——长一端短一端的“套利式”权重，对 $\rho$ 估偏极其敏感。

---

## 9. 从向量空间到现金流空间

把不同到期的零息 $\{P(0,T_j)\}$ 当基底，任意确定性现金流是坐标向量。附息债、摊还贷款都是该基底下的坐标——[[Interest Rates Products and Models]] 的线性结构。随机支付则要扩成情景空间 $\mathbb{R}^m$，回到支付矩阵。

---

## 10. 自检与参考答案

1. 写出 $w^\top\mu$ 与 $w^\top\Sigma w$；解释 $\Sigma\succeq 0$。
2. 复制方程 $A\theta=X$ 与列空间的关系。
3. 说明 OLS 投影 $H$ 在因子模型中的含义。
4. $\Sigma=Q\Lambda Q^\top$ 如何定义主成分。
5. 为何高维 $\hat\Sigma$ 的谱不可直接当真理。

> [!success]- 参考答案
> 1. 期望线性、方差二次型；协方差矩阵对称且对任意 $w$ 有 $w^\top\Sigma w=\mathrm{Var}(w^\top R)\ge 0$。
> 2. 有解 iff $X\in\mathrm{Col}(A)$；完备时任意 $X$ 可复制。
> 3. $\hat y$ 是用因子解释的部分；残差 $(I-H)y$ 是特异风险（样本正交于列空间）。
> 4. 列 $q_i$ 为载荷方向，$\lambda_i$ 为该方向方差；得分 $q_i^\top(R-\mu)$。
> 5. $T$ 有限时样本特征值有偏、不稳定；需结构或收缩。

> [!example] 练习：相关与组合方差
> 两资产 $\sigma=(0.2,0.2)$，$\rho=-0.5$，$w=(0.5,0.5)$。求 $\sigma_p$。

> [!success]- 练习参考答案
> $\mathrm{Var}=0.25\cdot0.04+0.25\cdot0.04+2\cdot0.5\cdot0.5\cdot(-0.5)\cdot0.04=0.02-0.01=0.01$，$\sigma_p=0.1$。负相关降低波动。

## 参考

- MIT 18.642 / 18.S096 linear algebra lectures（Kempthorne et al.）
- https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/
- 对照 [[Linear Algebra (MIT 18.06) MOC]]
