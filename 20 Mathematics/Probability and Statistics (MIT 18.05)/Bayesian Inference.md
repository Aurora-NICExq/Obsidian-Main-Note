---
aliases:
  - 贝叶斯推断
  - Bayesian Inference
  - Bayes update
  - Prior Posterior
tags: [math, probability_statistics]
up: "[[Probability and Statistics (MIT 18.05) MOC]]"
related:
  - "[[Maximum Likelihood Estimation]]"
  - "[[Conditional Probability and Bayes Theorem]]"
  - "[[Confidence Intervals]]"
  - "[[Hypothesis Testing]]"
  - "[[Law of Large Numbers and Central Limit Theorem]]"
down:
  - "[[Hypothesis Testing]]"
---
# 贝叶斯推断

> [!summary] 核心结论
> 贝叶斯把未知参数 $\theta$ 当作随机变量：先验 $\pi(\theta)$ × 似然 $f(\mathrm{data}\mid\theta)$ → 后验 $\pi(\theta\mid\mathrm{data})$。离散时用表格/树更新；连续共轭如 Beta–Binomial 把更新变成“伪计数加减”。后验可用于点估计、可信区间与后验预测。可信区间陈述“参数落在区间的后验概率”；频率派置信区间陈述“程序的长期覆盖率”——措辞对象不同，不可混用。

> 底本：MIT 18.05（Orloff / Kamrin）贝叶斯单元。

> 关键词：prior / likelihood / posterior、共轭、Beta–Binomial、predictive、credible interval

---

## 1. 贝叶斯更新公式

参数 $\theta$，数据 $x$。

**密度形式（连续参数）**
$$
\pi(\theta\mid x)
=\frac{f(x\mid\theta)\,\pi(\theta)}{m(x)},
\qquad
m(x)=\int f(x\mid\theta)\,\pi(\theta)\,d\theta.
$$

**离散参数**（有限假设 $H_i$）
$$
P(H_i\mid x)
=\frac{P(x\mid H_i)P(H_i)}{\sum_j P(x\mid H_j)P(H_j)}.
$$

口头链：
$$
\text{posterior}\;\propto\;\text{likelihood}\times\text{prior}.
$$
$m(x)$（或分母求和）是归一化常数，又叫边缘似然 / evidence。

与事件版贝叶斯定理同一代数；此处“事件”是参数取值或模型假设。

---

## 2. 三件套的含义

| 对象 | 含义 | 谁提供 |
|------|------|--------|
| 先验 $\pi(\theta)$ | 见数据前对 $\theta$ 的信念 | 主观 / 历史 / 约定无信息 |
| 似然 $f(x\mid\theta)$ | 模型：数据如何由 $\theta$ 生成 | 与 MLE 相同的采样模型 |
| 后验 $\pi(\theta\mid x)$ | 见数据后的更新信念 | 推断的主要输出 |

似然在 MLE 里被对 $\theta$ 最大化；在贝叶斯里被当作权重，与先验相乘后再归一化。

> [!tip] 同一似然，两种用法
> [[Maximum Likelihood Estimation|MLE]]：找峰。贝叶斯：把整条似然曲线与先验合成整条后验。

---

## 3. 离散更新：表格法

设假设 $H_1,\ldots,H_m$，先验 $p_i=P(H_i)$，观测到数据 $D$。

1. 写似然 $L_i=P(D\mid H_i)$  
2. 未归一化后验质量 $u_i=L_i p_i$  
3. 归一化 $P(H_i\mid D)=u_i/\sum_j u_j$

可序贯进行：今天的后验 = 明天的先验（在似然正确、条件独立新数据时）。

> [!example] 两假说
> 疾病先验 $0.01$，灵敏度 $0.99$，假阳性率 $0.05$。阳性后验
> $$
> \frac{0.99\times 0.01}{0.99\times 0.01+0.05\times 0.99}\approx 0.167.
> $$
> 稀有事件 + 非零假阳性 → 后验远小于“感觉上的 99%”。

> [!example] 三假说离散表（端到端）
> 三种硬币，先验各 $1/3$：$H_F$（公平，$P(+)=1/2$）、$H_B$（偏向，$P(+)=0.8$）、$H_T$（双正面，$P(+)=1$）。观测三次正面。
>
> | 假设 | 先验 | 似然 | 未归一化 $u$ | 后验 |
> |------|------|------|--------------|------|
> | $H_F$ | $1/3$ | $0.125$ | $0.04167$ | $0.076$ |
> | $H_B$ | $1/3$ | $0.512$ | $0.1707$ | $0.313$ |
> | $H_T$ | $1/3$ | $1$ | $0.3333$ | $0.611$ |
>
> 分母 $\sum u\approx 0.5457$。数据把质量从公平推向双正面；若再抛一次反面，$H_T$ 的似然变 0，后验立刻清零——表格更新可序贯进行。

---

## 4. Beta–Binomial 共轭

### 4.1 Beta 先验

$\theta\in(0,1)$ 为成功概率，先验
$$
\pi(\theta)=\mathrm{Beta}(\alpha,\beta)
\propto\theta^{\alpha-1}(1-\theta)^{\beta-1}.
$$
$\alpha,\beta>0$ 可理解为“先验伪计数”：$\alpha-1$ 次成功、$\beta-1$ 次失败的权重（对 $\alpha,\beta\ge 1$ 的直觉尤其好用）。

### 4.2 二项 / Bernoulli 数据

观测 $n$ 次独立试验，成功 $k$ 次。似然 $\propto\theta^{k}(1-\theta)^{n-k}$。后验仍是 Beta：
$$
\theta\mid\mathrm{data}\;\sim\;
\mathrm{Beta}(\alpha+k,\,\beta+n-k).
$$

**更新规则**：成功加到 $\alpha$，失败加到 $\beta$。

![[ps-bayes-update.svg]]

图示：先验 $\mathrm{Beta}(2,2)$（较平），经 $7$ 成 $3$ 败后得 $\mathrm{Beta}(9,5)$，质量移向较大 $\theta$。

### 4.3 后验摘要

- 后验均值：$\dfrac{\alpha+k}{\alpha+\beta+n}$（先验与 MLE $\hat\theta=k/n$ 的加权平均）  
- 后验众数（$\alpha,\beta>1$）：$\dfrac{\alpha+k-1}{\alpha+\beta+n-2}$  
- 大 $n$ 时后验集中在 $\hat\theta$ 附近，先验影响淡出（与 CLT/一致性叙事一致）

> [!example] 均匀先验
> $\mathrm{Beta}(1,1)$ 即 $\mathrm{Unif}(0,1)$。后验 $\mathrm{Beta}(1+k,1+n-k)$，后验均值 $(k+1)/(n+2)$（Laplace 修正），避免 $\hat p=0$ 或 $1$ 的僵硬。

> [!example] Beta–Binomial 完整数字
> 先验 $\theta\sim\mathrm{Beta}(2,2)$（均值 $0.5$）。观测 $n=10$ 次，成功 $k=7$。
> 后验 $\mathrm{Beta}(2+7,\,2+3)=\mathrm{Beta}(9,5)$。
>
> - 后验均值：$\dfrac{9}{9+5}=\dfrac{9}{14}\approx 0.643$（介于先验均值 $0.5$ 与 MLE $0.7$ 之间）。
> - 后验众数：$\dfrac{9-1}{9+5-2}=\dfrac{8}{12}\approx 0.667$。
> - 等尾 $95\%$ 可信区间的正态近似：后验方差 $=\dfrac{9\cdot 5}{14^2\cdot 15}\approx 0.0153$，SD $\approx 0.124$，
>   $$
>   0.643\pm 1.96\cdot 0.124\;\Rightarrow\;[0.40,\,0.89].
>   $$
>   （精确分位可用软件；此处展示手算路径。）
>
> 下一拍成功的后验预测概率 $=$ 后验均值 $\approx 0.643$，不是硬插 $\hat\theta=0.7$。

---

## 5. 共轭家族（地图）

| 似然 | 共轭先验 | 后验更新直觉 |
|------|----------|--------------|
| Bernoulli / Binomial | Beta | 成功/失败计数相加 |
| Poisson | Gamma | 事件计数与暴露时间更新 |
| 正态均值（$\sigma$ 已知） | 正态 | 精度（$1/\sigma^2$）加权平均 |
| 指数族一般 | 共轭先验 | 充分统计量加法更新 |

共轭的工程价值：闭式后验、易序贯更新、易做灵敏度分析（改 $\alpha,\beta$ 看后验动多少）。

---

## 6. 后验预测（posterior predictive）

新观测 $\tilde x$ 在已有数据 $x$ 下的预测分布：
$$
p(\tilde x\mid x)
=\int f(\tilde x\mid\theta)\,\pi(\theta\mid x)\,d\theta.
$$
先按后验抽 $\theta$，再按模型抽 $\tilde x$——自动计入**参数不确定性**。

Beta–Binomial 下，下一次成功概率的后验预测均值就是后验均值 $(\alpha+k)/(\alpha+\beta+n)$。这比只插 $\hat\theta_{\mathrm{MLE}}$ 再当“已知”更诚实。

---

## 7. 可信区间 vs 频率派置信区间

### 7.1 可信区间（credible interval）

由后验给出，例如 95% 等尾区间 $[\theta_L,\theta_U]$ 满足
$$
P(\theta_L\le\theta\le\theta_U\mid\mathrm{data})=0.95.
$$
陈述对象是**参数**（在先验+模型下）。

最高后验密度（HPD）区间是另一选择：在给定概率质量下长度最短。

### 7.2 置信区间（confidence interval）

频率派程序：重复抽样时，区间覆盖真参数的长期比例为 $95\%$。对**单次**实现的区间，不能说“$\theta$ 落在其中的概率是 95%”（$\theta$ 被当作固定常数）。

| | 可信区间 | 置信区间 |
|--|----------|----------|
| 概率落在 | 参数（后验） | 随机区间（频率） |
| 依赖 | 先验 + 似然 | 抽样分布 + 枢轴/近似 |
| 小样本 | 先验影响可见 | 常靠正态/$t$/Bootstrap |
| 大样本 | 二者数值常接近 | 常由 MLE±SE 给出 |

> [!warning] 措辞纪律
> 写报告时分清：贝叶斯可说“后验概率 95% 落在…”；频率派应说“按此程序长期约 95% 覆盖”。混用是概念错误，不是口味问题。

> [!warning] 可信区间 ≠ 置信区间（即使数字接近）
> 平坦先验 + 正态似然时，$95\%$ 可信区间的端点常与 $z$/$t$ 置信区间几乎相同。这**不**意味着两种陈述可互换：一个给参数后验概率，一个给程序覆盖率。换一个信息先验，可信区间会动，而同一份数据的频率派 CI 不变。

---

## 8. 与 MLE / NHST 的对照

- **点估计**：后验均值 / 众数 vs $\hat\theta_{\mathrm{MLE}}$；平坦先验下众数常等于 MLE。  
- **区间**：可信区间 vs 置信区间（上一节）。  
- **检验**：后验概率 $P(H_0\mid\mathrm{data})$ 或贝叶斯因子 vs $p$ 值。$p$ 值不是“$H_0$ 为真的概率”。  
- **正则化**：先验相当于把估计从极端数据拉开（如 $(k+1)/(n+2)$）。

---

## 9. 实践清单

1. 写清参数与采样模型（似然）  
2. 显式选择先验，并做灵敏度检查（$\alpha,\beta$ 加减）  
3. 能共轭则闭式；否则数值积分 / MCMC（课程外）  
4. 报告后验图或分位数，不只给一个点  
5. 需要预测时用后验预测，而不是“插入 $\hat\theta$ 假装已知”

---

## 10. 自检与参考答案

1. 会写 posterior $\propto$ likelihood × prior，并完成离散表格更新。  
2. 会用 Beta–Binomial：$(\alpha,\beta)\to(\alpha+k,\beta+n-k)$，算后验均值。  
3. 能解释后验预测为何计入参数不确定。  
4. 能对比可信区间（参数后验概率）与置信区间（程序覆盖率）。

> [!success]- 参考答案
> 1. 未归一化质量 $=$ 似然 × 先验，再除以总和（或积分）得后验。离散：先验列 × 似然列 → 归一化。
> 2. 成功加到 $\alpha$，失败加到 $\beta$；后验均值 $(\alpha+k)/(\alpha+\beta+n)$。
> 3. $p(\tilde x\mid x)=\int f(\tilde x\mid\theta)\pi(\theta\mid x)\,d\theta$ 对参数后验平均，而不是把 $\hat\theta$ 当已知常数。
> 4. 可信：$P(\theta\in I\mid\mathrm{data})=1-\alpha$。置信：重复抽样时区间覆盖真 $\theta$ 的比例。对象不同。

> [!example] 练习：换先验看灵敏度
> 同上数据 $k=7$，$n=10$。若先验改为 $\mathrm{Beta}(1,1)$ 与 $\mathrm{Beta}(10,10)$，后验均值各是多少？

> [!success]- 练习参考答案
> $\mathrm{Beta}(1,1)$：$(\alpha',\beta')=(8,4)$，均值 $8/12\approx 0.667$。
> $\mathrm{Beta}(10,10)$：$(17,13)$，均值 $17/30\approx 0.567$（强先验把估计往 $0.5$ 拉）。
> 同一数据，先验强度不同 → 后验不同；报告时应做这种灵敏度检查。

## 参考

- Jeremy Orloff & Jennifer French Kamrin, *18.05 Introduction to Probability and Statistics*, MIT OCW Spring 2022（Bayesian inference）
- https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/
