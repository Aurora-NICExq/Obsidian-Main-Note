---
aliases:
  - 置信区间
  - Confidence Intervals
  - CI
  - coverage probability
tags: [math, probability_statistics]
up: "[[Probability and Statistics (MIT 18.05) MOC]]"
related:
  - "[[Hypothesis Testing]]"
  - "[[Bootstrap Methods]]"
  - "[[Bayesian Inference]]"
  - "[[Law of Large Numbers and Central Limit Theorem]]"
down:
  - "[[Bootstrap Methods]]"
---
# 置信区间

> [!summary] 核心结论
> $(1-\alpha)$ 置信区间是**随机区间** $[L,U]$，其长期覆盖率满足 $P(L\le\theta\le U)=1-\alpha$（在模型正确时）。对**已算出的**数区间，不能说“$\theta$ 有 $95\%$ 概率落在里面”——频率派里 $\theta$ 不是随机的。正态均值：$\bar X\pm z_{\alpha/2}\sigma/\sqrt n$；$\sigma$ 未知换 $t$；比例用 $\hat p\pm z\sqrt{\hat p(1-\hat p)/n}$（大样本）。18.05 用三种视角理解同一对象：覆盖、与检验对偶、与贝叶斯可信区间对照。

> 底本：MIT 18.05 置信区间与频率派推断。

---
## 1. 覆盖率诠释（最重要）

固定未知参数 $\theta$。重复抽样，每次算一个区间 $C(\text{data})$。定义
$$
\text{coverage}=P_\theta\bigl(\theta\in C(\text{data})\bigr).
$$
名义水平 $95\%$ 的区间程序应使 coverage $\approx 0.95$（对所有或大多数 $\theta$）。

![[ps-confidence-interval.svg]]

> [!warning] 单次实现的语言陷阱
> 算出 $[2.1, 3.4]$ 后，$\theta$ 要么在里面要么不在——没有剩下的随机性。正确说法是：“该区间由 $95\%$ 覆盖率的程序生成。”错误说法：“$\theta$ 有 $95\%$ 概率在 $[2.1,3.4]$。”后者是**可信区间 / 后验**语言。

---
## 2. 正态均值、$\sigma$ 已知

$X_i\overset{\mathrm{iid}}{\sim}N(\mu,\sigma^2)$，$\sigma$ 已知。枢轴量
$$
Z=\frac{\bar X-\mu}{\sigma/\sqrt n}\sim N(0,1).
$$
故
$$
P\Bigl(-z_{\alpha/2}\le\frac{\bar X-\mu}{\sigma/\sqrt n}\le z_{\alpha/2}\Bigr)=1-\alpha,
$$
整理得
$$
\bar X\pm z_{\alpha/2}\frac{\sigma}{\sqrt n}.
$$
常见：$z_{0.025}=1.96$（约 $2$），$z_{0.005}=2.576$。

即使非正态，CLT 在中等 $n$ 上常给出可用的近似覆盖（方差有限时）。

> [!example] $z$ 区间端到端
> $n=36$，$\bar x=12.4$，$\sigma=3.0$ 已知，求 $\mu$ 的 $95\%$ CI。
> $$
> \mathrm{SE}=\frac{3}{6}=0.5,\qquad
> 12.4\pm 1.96\cdot 0.5=12.4\pm 0.98
> $$
> 得 $[11.42,\,13.38]$。解读：该区间由名义覆盖约 $95\%$ 的程序生成；**不要**说“$\mu$ 有 $95\%$ 概率落在 $[11.42,13.38]$”。

---
## 3. $t$ 区间（$\sigma$ 未知）

用 $S^2=\frac{1}{n-1}\sum(X_i-\bar X)^2$，
$$
T=\frac{\bar X-\mu}{S/\sqrt n}\sim t_{n-1}
\quad\text{（正态总体）}.
$$
置信区间：
$$
\bar X\pm t_{n-1,\,\alpha/2}\frac{S}{\sqrt n}.
$$
$t$ 临界值 $>z$ $\Rightarrow$ 区间更宽——为估计 $\sigma$ 付的代价。大 $n$ 时二者几乎相同。

> [!example] $n=9$，$\bar x=10$，$s=3$，$\alpha=0.05$
> $t_{8,0.025}\approx 2.306$，半宽 $2.306\cdot 3/3=2.306$，区间约 $[7.69,\,12.31]$。

---
## 4. 比例的大样本 CI

$\hat p=X/n$，$X\sim\mathrm{Bin}(n,p)$。正态近似：
$$
\hat p\pm z_{\alpha/2}\sqrt{\frac{\hat p(1-\hat p)}{n}}.
$$
当 $n\hat p$ 与 $n(1-\hat p)$ 都不太小时近似尚可。改进：

- **Wilson / Agresti–Coull** 等：在边界 $p\approx 0$ 或 $1$、小 $n$ 时覆盖更稳。
- 精确 Clopper–Pearson：基于二项尾概率，偏保守。

与检验对偶：空假设 $H_0:p=p_0$ 的 $z$ 检验常用 $\sqrt{p_0(1-p_0)/n}$；CI 常用 $\hat p$——二者临界不完全相同，但大样本下接近。

---
## 5. 18.05 的三种视角

### 5.1 覆盖（频率派定义）

区间是程序；评价标准是长期覆盖率。模拟：固定 $\theta$，重复生成数据、算区间，数“套住 $\theta$”的比例 $\to 1-\alpha$。

### 5.2 与假设检验对偶

对许多标准程序，
$$
\theta_0\in\text{CI}_{1-\alpha}\quad\Leftrightarrow\quad\text{水平 }\alpha\text{ 的双边检验不拒绝 }H_0:\theta=\theta_0.
$$
因此 CI 可看成“所有与数据相容的 $\theta_0$ 的集合”。检验给是/否；CI 给**精度与方向**。

> [!example] 对偶的数字演示
> 接 §2 的数据：$\bar x=12.4$，$\sigma=3$，$n=36$，$95\%$ CI $=[11.42,13.38]$。
>
> - 检验 $H_0:\mu=12.0$：$\theta_0=12.0\in\mathrm{CI}$ $\Rightarrow$ 水平 $0.05$ 的双边 $z$ 检验**不拒绝**。
>   验算：$z=(12.4-12.0)/0.5=0.8$，$|0.8|<1.96$，确实不拒绝；$p=2(1-\Phi(0.8))\approx 0.42$。
> - 检验 $H_0:\mu=11.0$：$11.0\notin\mathrm{CI}$ $\Rightarrow$ **拒绝**。
>   验算：$z=(12.4-11.0)/0.5=2.8>1.96$，$p\approx 0.005$。
>
> 一张 CI 等价于对所有 $\theta_0$ 同时做了一族双边检验。

---
### 5.3 与贝叶斯可信区间对照

可信区间来自后验：$P(\theta\in I\mid\text{data})=1-\alpha$。语句可直接概率化参数，但依赖先验。平坦先验 + 正态模型时，数值上常与 $z$/$t$ 区间重合——**数字像、哲学不同**。见 [[Bayesian Inference]]。

---
## 6. 宽度、样本量与设计

半宽大致
$$
\text{margin}\approx z_{\alpha/2}\frac{\sigma}{\sqrt n}
\quad\Rightarrow\quad
n\approx\Bigl(\frac{z_{\alpha/2}\sigma}{\text{margin}}\Bigr)^2.
$$
要更窄的区间：增大 $n$、减小噪声、或接受更低置信水平（一般不推荐为“好看”而降到 $80\%$）。

> [!warning] 多重比较与挑选
> 先看数据再只对“显著的”参数报 CI，或对多假设只报最小 $p$ 对应区间，会破坏名义覆盖。预注册或校正（Bonferroni 等）属于设计问题。

---
## 7. 单侧区间与差的区间

有时只要上界或下界（安全阈值、污染上限）：
$$
(-\infty,\;\bar X+z_{\alpha}\sigma/\sqrt n]
\quad\text{或}\quad
[\bar X-z_{\alpha}\sigma/\sqrt n,\;+\infty).
$$
与单侧检验对偶。两均值差（$\sigma$ 已知或大样本）常用
$$
(\bar X-\bar Y)\pm z_{\alpha/2}\sqrt{\frac{\sigma_X^2}{n}+\frac{\sigma_Y^2}{m}}
$$
（独立样本）；配对则对差分做单样本区间。

> [!example] 读报告时的检查清单
> 区间是均值还是预测？置信水平？用的是 $z$ 还是 $t$？比例是否靠近 $0/1$？若只给“$95\%$ CI = …”而不给方法，覆盖承诺可能虚标。

---
## 8. 与 Bootstrap 的衔接

解析公式依赖正态 / 大样本或已知枢轴。统计量复杂（中位数、相关系数、回归函数）时，可用重抽样构造百分位或 $t$-bootstrap 区间——见 [[Bootstrap Methods]]。频率派覆盖目标不变，只是临界值由经验分布代替查表。

---
## 9. 自检与参考答案

1. 用覆盖率正确解释 CI；避免对单次区间说“$\theta$ 有 $95\%$ 概率…”。
2. 会写正态均值的 $z$ 与 $t$ 区间；会写比例的大样本区间并知道局限。
3. 说清 CI $\leftrightarrow$ 双边检验的对偶。
4. 能对比频率派 CI 与贝叶斯可信区间的语言差异。
5. 会用半宽公式粗估所需 $n$；知道单侧与两样本差的基本形式。

> [!success]- 参考答案
> 1. CI 是随机程序：重复抽样时约 $1-\alpha$ 比例覆盖真 $\theta$。对已算出的数区间，$\theta$ 要么在内要么不在，不能赋“95% 概率”。
> 2. $\sigma$ 已知：$\bar x\pm z_{\alpha/2}\sigma/\sqrt n$；未知：换 $t_{n-1,\alpha/2}$ 与 $s$。比例：$\hat p\pm z\sqrt{\hat p(1-\hat p)/n}$，需 $n\hat p,n(1-\hat p)$ 不太小。
> 3. $\theta_0\in\mathrm{CI}_{1-\alpha}$ $\Leftrightarrow$ 水平 $\alpha$ 双边检验不拒绝 $H_0:\theta=\theta_0$。
> 4. 可信区间：$P(\theta\in I\mid\mathrm{data})=1-\alpha$（参数随机化）。CI：程序覆盖率。数字可接近，语句对象不同。
> 5. $n\approx(z_{\alpha/2}\sigma/\mathrm{margin})^2$。单侧用 $z_\alpha$ 只保一侧；两独立样本差用 SE $\sqrt{\sigma_X^2/n+\sigma_Y^2/m}$。

> [!example] 练习：比例 CI 与对偶
> $n=80$，成功 $28$，$\hat p=0.35$。写 $95\%$ 大样本 CI；并判断水平 $0.05$ 的双边检验是否拒绝 $H_0:p=0.5$。

> [!success]- 练习参考答案
> $$
> \mathrm{SE}=\sqrt{0.35\cdot 0.65/80}\approx\sqrt{0.002844}\approx 0.0533,
> $$
> $0.35\pm 1.96\cdot 0.0533\approx 0.35\pm 0.104$，CI $\approx[0.246,\,0.454]$。
> 因 $0.5\notin\mathrm{CI}$，对偶 $\Rightarrow$ 拒绝 $H_0:p=0.5$。验算：$z=(0.35-0.5)/\sqrt{0.5\cdot 0.5/80}=-0.15/0.0559\approx -2.68$，拒绝。

## 参考

- Jeremy Orloff & Jennifer French Kamrin, *18.05 Introduction to Probability and Statistics*, MIT OCW Spring 2022（confidence intervals）
- https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/
