---
aliases:
  - 投资组合管理
  - Portfolio Management
  - 均值方差
  - efficient frontier CAPM
tags: [math, math_finance]
up: "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
related:
  - "[[Linear Algebra for Finance]]"
  - "[[Regression and PCA in Finance]]"
  - "[[Volatility Modeling]]"
  - "[[Probability and Stochastic Processes for Finance]]"
  - "[[Economics MOC]]"
  - "[[Analytics of Finance (MIT 15.450) MOC]]"
down:
  - "[[Volatility Modeling]]"
---
# 投资组合管理

> [!summary] 核心结论
> Markowitz **均值–方差**：在给定预期收益下最小化 $w^\top\Sigma w$（或对偶）。可行集边界的上半支为**有效前沿**；引入无风险资产后得到资本市场线，风险资产相对供给引出 **CAPM** 素描：$\mathbb{E}[R_i]-r_f=\beta_i(\mathbb{E}[R_m]-r_f)$。数学是二次型优化；实践瓶颈是 $\mu,\Sigma$ 的估计误差。

> 底本：MIT 18.642 组合理论单元；线性代数见 [[Linear Algebra for Finance]]。

> 关键词：有效前沿、切点组合、$\beta$、分散化、估计误差

---

## 1. 问题设定

$n$ 风险资产，期望 $\mu$，协方差 $\Sigma\succ 0$。权重 $w$，常 $1^\top w=1$。
$$
\min_w\ \tfrac12 w^\top\Sigma w\quad\mathrm{s.t.}\quad w^\top\mu=m,\ 1^\top w=1.
$$
拉格朗日 ⇒ $w$ 为 $\mu,1$ 的线性组合（两基金分离在无约束空头允许时成立）。

![[mf-portfolio.svg]]

---

## 2. 有效前沿几何

$(\sigma_p,\mu_p)$ 平面：最小方差边界是双曲线型曲线；有效前沿取均值以上半。两资产时可用解析式：
$$
\sigma_p^2=w^2\sigma_1^2+(1-w)^2\sigma_2^2+2w(1-w)\rho\sigma_1\sigma_2.
$$
$\rho$ 越小，曲线越向左弯——**分散化**的数学来源。

> [!example] 两资产有效集点
> $\mu_1=0.06$，$\mu_2=0.12$，$\sigma_1=\sigma_2=0.2$，$\rho=0$。等权 $w=0.5$：
> $$
> \mu_p=0.09,\quad \sigma_p=\sqrt{0.5\cdot0.04}=0.1\sqrt{2}\approx 0.141.
> $$
> 低于任一单资产波动，均值居中。

---

## 3. 无风险资产与切点

无风险 $r_f$：可贷可借时，最优为持有**切点组合** $w_T$ 与现金的组合，前沿变成直线（资本市场线 CML）：
$$
\mathbb{E}[R_p]=r_f+\frac{\mathbb{E}[R_T]-r_f}{\sigma_T}\sigma_p.
$$
切点最大化夏普比 $(\mu-r_f\mathbf{1})^\top\Sigma^{-1}$ 相关方向：
$$
w_T\propto\Sigma^{-1}(\mu-r_f\mathbf{1}).
$$

> [!warning] $\mu$ 估不准时切点会疯
> $\Sigma^{-1}$ 放大误差；样本最优组合往往极端权重。实践：收缩期望、风险平价、约束优化、或因子风险模型——见估计讨论于 [[Regression and PCA in Finance]]。

---

## 4. CAPM 素描

若人人均值–方差且同质预期，市场组合 $m$ 即切点。对任意资产 $i$：
$$
\mathbb{E}[R_i]-r_f=\beta_i\bigl(\mathbb{E}[R_m]-r_f\bigr),\quad
\beta_i=\frac{\mathrm{Cov}(R_i,R_m)}{\mathrm{Var}(R_m)}.
$$
回归检验即市场模型（[[Regression and PCA in Finance]]）。经验 CAPM 粗糙：多因子、异常收益、杠杆约束都会破坏严格推导假设——课程要的是推导骨架，不是信仰声明。制度与风险偏好语境可对照 [[Economics MOC]]。

---

## 5. 分散化数量级

特异风险在等权、$n$ 资产近似不相关时按 $1/n$ 下降；系统风险留下。故“只买一只股票”的方差远大于市场。相关矩阵若全面升高（危机），分散化失效——波动与相关同时恶化，见 [[Volatility Modeling]]。

---

## 6. 约束与实务层（点到）

| 主题 | 一句话 |
|------|--------|
| 禁止空头 | 二次规划，有效集变“折线” |
| 交易成本 | 最优换手被压低 |
| 负债驱动 | 相对 surplus 优化，非绝对方差 |
| 风险预算 | 对边际风险贡献设限 |

更动态的再平衡 / 随机控制视角：[[Analytics of Finance (MIT 15.450) MOC]]。

---

## 7. 绩效度量（与优化目标对齐）

| 度量 | 公式直觉 | 注意 |
|------|----------|------|
| 超额收益 | $\bar R-r_f$ | 未罚风险 |
| 夏普 | $(\bar R-r_f)/\sigma$ | 假设近似 i.i.d.；杠杆可抬高 |
| 信息比 | 主动收益 / 跟踪误差 | 相对基准 |
| 最大回撤 | 峰到谷跌幅 | 路径依赖，样本敏感 |

优化若只盯方差，可能忽略偏度/尾部；危机中相关升高使事后夏普远差于样本内。报告应分平静期与压力期。

> [!example] 夏普粗算
> 年化超额 $6\%$，年化波动 $12\%$ → 夏普 $0.5$。若月频算夏普再 $\times\sqrt{12}$，需收益近似不相关；波动聚集时年化规则只是近似。

---

## 8. 从 $\beta$ 到主动风险

CAPM 下只有系统风险被定价；主动组合的残差方差 $\omega^2$ 应被分散或换取确凿 $\alpha$。基本定律粗糙版：信息比 $\approx \mathrm{IC}\cdot\sqrt{\mathrm{广度}}$（在理想化假定下）。它提醒：微弱 IC 需要大量独立押注——与 [[Machine Learning in Finance]] 的低信噪叙事一致。

---

## 9. 自检与参考答案

1. 写出均值–方差原问题。
2. 解释有效前沿与两基金分离（允许空头）。
3. 切点组合与夏普比的关系。
4. 写出 CAPM 期望收益公式与 $\beta$ 定义。
5. 为何样本 MV 优化危险？

> [!success]- 参考答案
> 1. $\min w^\top\Sigma w$ s.t. $w^\top\mu=m$，$1^\top w=1$（或等价形式）。
> 2. 上半最小方差边界；任意有效组合 = 两前沿基金的组合。
> 3. $w_T$ 最大化 $(\mu_p-r_f)/\sigma_p$；CML 与之相切。
> 4. $\mathbb{E}[R_i]-r_f=\beta_i(\mathbb{E}[R_m]-r_f)$，$\beta=\mathrm{Cov}/\mathrm{Var}_m$。
> 5. $\mu,\Sigma$ 估计误差经 $\Sigma^{-1}$ 放大，权重不稳定。

> [!example] 练习：$\beta$
> $\sigma_i=0.3$，$\sigma_m=0.2$，$\rho_{im}=0.5$。求 $\beta_i$。

> [!success]- 练习参考答案
> $\beta=\rho\sigma_i\sigma_m/\sigma_m^2=\rho\sigma_i/\sigma_m=0.5\cdot0.3/0.2=0.75$。

## 参考

- MIT 18.642 portfolio lectures；Markowitz / CAPM 标准推导
- https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/
