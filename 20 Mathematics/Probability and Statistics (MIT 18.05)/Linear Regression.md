---
aliases:
  - 线性回归
  - Linear Regression
  - least squares
  - OLS
  - R-squared
tags: [math, probability_statistics]
up: "[[Probability and Statistics (MIT 18.05) MOC]]"
related:
  - "[[Joint Distributions Covariance and Correlation]]"
  - "[[Confidence Intervals]]"
  - "[[Hypothesis Testing]]"
  - "[[Bootstrap Methods]]"
  - "[[Linear Algebra (MIT 18.06) MOC]]"
down: []
---
# 线性回归

> [!summary] 核心结论
> 简单线性模型 $Y=\beta_0+\beta_1 x+\varepsilon$ 用**最小二乘**选 $\hat\beta_0,\hat\beta_1$ 使残差平方和最小；几何上是把响应向量投影到设计矩阵列空间（与 18.06 投影同一件事）。残差诊断模型是否离谱；$R^2$ 衡量“线性解释了多少变异”，高不代表因果。多元回归是同构：$Y=X\beta+\varepsilon$，$\hat\beta=(X^\top X)^{-1}X^\top Y$（满秩时）。

> 底本：MIT 18.05 回归单元；几何联系 [[Linear Algebra (MIT 18.06) MOC]]。

---
## 1. 简单线性模型

观测对 $(x_i,Y_i)$，$i=1,\ldots,n$。模型
$$
Y_i=\beta_0+\beta_1 x_i+\varepsilon_i,
$$
常设 $\varepsilon_i$ i.i.d.、$\mathbb{E}[\varepsilon_i]=0$、$\mathrm{Var}(\varepsilon_i)=\sigma^2$（推断时再加正态）。

- $\beta_1$：斜率——$x$ 增加 1 单位时，**平均** $Y$ 的变化（在模型内）。
- $\beta_0$：截距——$x=0$ 时的平均响应（外推时未必有实质意义）。

$x$ 可视为固定（设计）或随机；最小二乘点估计公式相同，随机 $x$ 下解释与条件期望 $\mathbb{E}[Y\mid x]$ 相连。

![[ps-regression.svg]]

---
## 2. 最小二乘

残差平方和
$$
\mathrm{RSS}(\beta_0,\beta_1)=\sum_{i=1}^n\bigl(Y_i-\beta_0-\beta_1 x_i\bigr)^2.
$$
对 $\beta_0,\beta_1$ 求导并令零，得正规方程，解为
$$
\hat\beta_1=\frac{\sum(x_i-\bar x)(Y_i-\bar Y)}{\sum(x_i-\bar x)^2},\qquad
\hat\beta_0=\bar Y-\hat\beta_1\bar x.
$$
拟合值 $\hat Y_i=\hat\beta_0+\hat\beta_1 x_i$，残差 $e_i=Y_i-\hat Y_i$。恒有 $\sum e_i=0$（含截距时）及残差与 $x$ 正交：$\sum e_i x_i=0$。

> [!example] 与相关
> 若令 $s_x,s_y$ 为样本标准差，$r$ 为样本相关，则
> $$
> \hat\beta_1=r\frac{s_y}{s_x}.
> $$
> 相关无量纲；斜率有单位。见 [[Joint Distributions Covariance and Correlation]]。

> [!example] 四行迷你数据：手算斜率与截距
> | $x$ | $y$ |
> |-----|-----|
> | 1 | 2 |
> | 2 | 3 |
> | 3 | 5 |
> | 4 | 6 |
>
> $\bar x=2.5$，$\bar y=4$。
> $$
> \begin{aligned}
> \sum(x_i-\bar x)(y_i-\bar y)
> &=(-1.5)(-2)+(-0.5)(-1)+(0.5)(1)+(1.5)(2)=3+0.5+0.5+3=7,\\
> \sum(x_i-\bar x)^2
> &=2.25+0.25+0.25+2.25=5.
> \end{aligned}
> $$
> $$
> \hat\beta_1=7/5=1.4,\qquad
> \hat\beta_0=4-1.4\cdot 2.5=0.5.
> $$
> 拟合直线 $\hat y=0.5+1.4x$。拟合值：$1.9,\,3.3,\,4.7,\,6.1$；残差：$0.1,\,-0.3,\,0.3,\,-0.1$（和为 0）。
> $$
> \mathrm{SSE}=0.01+0.09+0.09+0.01=0.2,\quad
> \mathrm{SST}=4+1+1+4=10,\quad
> R^2=1-0.2/10=0.98.
> $$

---
## 3. 残差与诊断

残差是模型没吃掉的部分。画图检查：

1. **残差 vs 拟合值**：应大致无结构、等宽；喇叭形 $\Rightarrow$ 异方差；弯曲 $\Rightarrow$ 非线性。
2. **QQ 图**：推断靠正态时看尾部。
3. **残差 vs 顺序 / 其他变量**：查独立与遗漏变量。

单个大残差或高杠杆点（$x$ 远离 $\bar x$）可强烈撬动 $\hat\beta_1$。工科实践：报告时说明是否剔除、是否用稳健回归。

---
## 4. $R^2$ 直觉

总平方和与回归平方和：
$$
\mathrm{SST}=\sum(Y_i-\bar Y)^2,\quad
\mathrm{SSR}=\sum(\hat Y_i-\bar Y)^2,\quad
\mathrm{SSE}=\sum e_i^2,
$$
（含截距的 OLS）有 $\mathrm{SST}=\mathrm{SSR}+\mathrm{SSE}$，定义
$$
R^2=1-\frac{\mathrm{SSE}}{\mathrm{SST}}=\frac{\mathrm{SSR}}{\mathrm{SST}}.
$$
简单回归中 $R^2=r^2$。

**含义**：$Y$ 的样本变异中，被直线拟合解释的比例。
**不是**：因果证据、预测一定准、模型正确的证明。增加自变量会非降地抬高 $R^2$（多元时看调整 $R^2$ 或信息准则）。

---
## 5. 推断速览（正态误差）

在 $\varepsilon_i\sim N(0,\sigma^2)$ 下，$\hat\beta_1$ 正态，
$$
\frac{\hat\beta_1-\beta_1}{\widehat{\mathrm{se}}(\hat\beta_1)}\sim t_{n-2},
$$
可做 $H_0:\beta_1=0$ 的 $t$ 检验与斜率 CI——与 [[Hypothesis Testing]]、[[Confidence Intervals]] 同一套语言。$\widehat{\mathrm{se}}$ 含 $\hat\sigma=\sqrt{\mathrm{SSE}/(n-2)}$。

预测两类区间：

- **均值响应** $\mathbb{E}[Y\mid x_0]$ 的 CI：较窄；
- **新观测** $Y_{\mathrm{new}}$ 的预测区间：额外加一项 $\sigma^2$，更宽。

公式细节可查标准教材；概念上“估平均”vs“猜下一个点”不可混。

---
## 6. 多元回归（简述）

$$
Y_i=\beta_0+\beta_1 x_{i1}+\cdots+\beta_p x_{ip}+\varepsilon_i,
$$
矩阵形式 $Y=X\beta+\varepsilon$，$X$ 为 $n\times(p+1)$。OLS：
$$
\hat\beta=\arg\min_\beta\|Y-X\beta\|^2=(X^\top X)^{-1}X^\top Y
$$
（$X$ 满列秩）。$\hat Y=X\hat\beta=HY$，帽子矩阵 $H=X(X^\top X)^{-1}X^\top$ 是到列空间的正交投影——**线性代数主线**。

解释：$\beta_j$ 是**控制其他自变量后** $x_j$ 的偏效应。共线时 $X^\top X$ 病态，SE 膨胀。变量选择、交互项、分类变量编码属于后续课程；18.05 建立“投影 + 残差 + $R^2$”直觉即可。

> [!warning] 相关 ≠ 因果
> 观测数据回归估计的是条件关联（在模型假定下）。因果需要设计、工具变量或明确的反事实框架——超出本课范围，但必须在报告中克制措辞。

---
## 7. 拟合优度之外：模型用途

同一条 OLS 直线可服务于不同目标，措辞要分开：

| 目标 | 关注点 |
|---|---|
| 描述关联 | 斜率符号与大致大小、$R^2$、残差形态 |
| 预测 | 预测区间宽度、外推风险、新 $x$ 是否在训练范围 |
| 控制 / 调整 | 多元中偏系数；是否遗漏混杂（观测研究） |

外推：在 $x$ 远超样本范围处，$\hat Y$ 仍可算，但方差公式与线性假定都更脆。报告应标明 $x$ 的观测范围。

---
## 8. 与 Bootstrap 的结合

异方差或非正态时，解析 $t$ 区间可能不准。可对配对 $(x_i,y_i)$ 做 Bootstrap，或对残差重抽样后重构 $Y^{*}$，得到 $\hat\beta_1^{*}$ 的百分位区间——见 [[Bootstrap Methods]]。残差 Bootstrap 默认同方差；明显喇叭形残差时配对（病例）Bootstrap 更稳妥。

---
## 9. 自检与参考答案

1. 写出简单线性模型与 OLS 公式；解释 $\hat\beta_0,\hat\beta_1$。
2. 会算 / 读残差，知道基本诊断图在查什么。
3. 正确叙述 $R^2$，并说出它不意味着什么。
4. 知道斜率 $t$ 检验与“均值 CI vs 预测区间”的区别。
5. 能把多元 OLS 写成投影 $\hat Y=HY$，并警惕共线与因果话术。

> [!success]- 参考答案
> 1. $Y=\beta_0+\beta_1 x+\varepsilon$；$\hat\beta_1=\sum(x-\bar x)(y-\bar y)/\sum(x-\bar x)^2$，$\hat\beta_0=\bar y-\hat\beta_1\bar x$。
> 2. 残差 $e=y-\hat y$；残差–拟合图查非线性/异方差；QQ 查正态尾。
> 3. $R^2=$ 被直线解释的样本变异比例；**不是**因果、也不是“模型正确”。
> 4. $H_0:\beta_1=0$ 用 $t_{n-2}$。均值响应 CI 较窄；新观测预测区间额外加 $\sigma^2$。
> 5. $\hat Y=X(X^\top X)^{-1}X^\top Y=HY$；共线使 SE 膨胀；观测回归≠因果。

> [!example] 练习：用公式验算
> 数据 $(0,1),(1,3),(2,4)$。求 $\hat\beta_0,\hat\beta_1$ 与 $R^2$。

> [!success]- 练习参考答案
> $\bar x=1$，$\bar y=8/3$。$\sum(x-\bar x)(y-\bar y)=(-1)(-5/3)+(0)(1/3)+(1)(4/3)=3$，
> $\sum(x-\bar x)^2=2$，$\hat\beta_1=1.5$，$\hat\beta_0=8/3-1.5=7/6$。
> 拟合 $7/6,\,8/3,\,25/6$；残差 $-1/6,\,1/3,\,-1/6$；SSE$=1/6$，SST$=14/3$，
> $R^2=1-(1/6)/(14/3)=1-1/28=27/28$。

## 参考

- Jeremy Orloff & Jennifer French Kamrin, *18.05 Introduction to Probability and Statistics*, MIT OCW Spring 2022（regression）
- https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/
