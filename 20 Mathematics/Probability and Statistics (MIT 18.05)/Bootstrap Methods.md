---
aliases:
  - Bootstrap
  - Bootstrap Methods
  - 自助法
  - percentile bootstrap
  - resampling
tags: [math, probability_statistics]
up: "[[Probability and Statistics (MIT 18.05) MOC]]"
related:
  - "[[Confidence Intervals]]"
  - "[[Hypothesis Testing]]"
  - "[[Law of Large Numbers and Central Limit Theorem]]"
  - "[[Maximum Likelihood Estimation]]"
down:
  - "[[Linear Regression]]"
---
# Bootstrap 方法

> [!summary] 核心结论
> Bootstrap 用**有放回重抽样**把“样本当作总体”，估计统计量 $\hat\theta$ 的抽样分布，从而得到标准误与置信区间——尤其当解析方差公式很难或不可用时。百分位 Bootstrap CI 取重抽样统计量的经验分位数；它依赖经验分布接近真分布（大样本 / 光滑泛函时更稳）。不能替代坏模型或有偏抽样设计，但对中位数、相关、复杂变换等是工科默认工具之一。

> 底本：MIT 18.05 Bootstrap / 重抽样思想。

---
## 1. 问题：抽样分布未知

估计量 $\hat\theta=T(X_1,\ldots,X_n)$。推断需要 $\hat\theta$ 的标准误或分位数，但：

- 公式只对均值、比例等简单情形干净；
- Delta 方法要导数与渐近；
- 小样本正态近似可能差。

**Bootstrap 想法（Efron）**：把观测样本的经验分布 $\hat F_n$ 当作“真实” $F$，从 $\hat F_n$ 再抽样来**模拟** $\hat\theta$ 的变异。

![[ps-bootstrap.svg]]

---
## 2. 算法：非参数 Bootstrap

数据 $x_1,\ldots,x_n$。重复 $b=1,\ldots,B$（如 $B=1000$–$10000$）：

1. 有放回抽取 $n$ 个下标，得 Bootstrap 样本 $x^{*b}_1,\ldots,x^{*b}_n$。
2. 计算 $\hat\theta^{*b}=T(x^{*b})$。

得到经验分布 $\{\hat\theta^{*b}\}$。估计：

- **标准误**：$\widehat{\mathrm{se}}=\mathrm{sd}(\hat\theta^{*})$（样本标准差）。
- **偏倚**：$\overline{\hat\theta^{*}}-\hat\theta$（有时用于偏倚校正）。

关键：对 i.i.d. 样本，经验分布 $\hat F_n$ 一致逼近 $F$（Glivenko–Cantelli），故对许多“足够光滑”的 $T$，Bootstrap 分布逼近真抽样分布。

有放回意味着 Bootstrap 样本中会有重复、也会漏掉约 $e^{-1}\approx 37\%$ 的原始点（大 $n$ 时）；这正是“把样本当总体再抽样”的变异来源，不是实现 bug。

---
## 3. 百分位 Bootstrap 置信区间

令 $\hat\theta^{*(\alpha)}$ 为 $\{\hat\theta^{*b}\}$ 的经验 $\alpha$ 分位数。百分位区间：
$$
\bigl[\hat\theta^{*( \alpha/2)},\;\hat\theta^{*(1-\alpha/2)}\bigr].
$$
例如 $95\%$ CI：取 $2.5\%$ 与 $97.5\%$ 分位。

**优点**：实现简单，无需公式标准误；自动反映偏态（区间可左右不对称）。
**局限**：

- 若 $\hat\theta$ 偏倚大或变换尺度差，覆盖可能偏离名义水平；
- 极端分位数需要较大 $B$；
- 对离散、边界参数（如 $p=0$）表现差。

对称正态近似区间 $\hat\theta\pm z_{\alpha/2}\widehat{\mathrm{se}}$（$\widehat{\mathrm{se}}$ 来自 Bootstrap）是百分位法的近亲；偏态明显时优先百分位或 BCa。

> [!example] 中位数的区间
> 正态公式不直接给中位数 SE。对数据做 Bootstrap 中位数，取百分位即可——这是 Bootstrap 的典型“值得用”场景。

> [!example] 迷你手算：均值百分位区间（$B=5$ 示意）
> 数据 $x=(2,3,4,5,6)$，$\hat\theta=\bar x=4$。假设五次有放回重抽样得到均值：
> $$
> \bar x^{*}=\{3.2,\,4.0,\,4.6,\,3.8,\,4.4\}.
> $$
> 排序：$3.2,\,3.8,\,4.0,\,4.4,\,4.6$。
> 真实应用需 $B\ge 1000$；此处仅示意百分位读取：经验 $20\%$/$80\%$ 分位约取第 1 与第 5 个 → $[3.2,\,4.6]$（粗糙）。
> 对照解析：$s=\sqrt{2.5}\approx 1.58$，$t_{4,0.025}\approx 2.776$，
> $$
> 4\pm 2.776\cdot 1.58/\sqrt5\approx 4\pm 1.96\;\Rightarrow\;[2.04,\,5.96].
> $$
> $B$ 太小时 Bootstrap 分位极不稳定——这正是“$B$ 要大”的手感来源。

---
## 4. 其他常用变体（知晓即可）

- **Bootstrap-$t$**：对学生化统计量 $(\hat\theta^{*}-\hat\theta)/\widehat{\mathrm{se}}^{*}$ 取分位数，再映射回 $\theta$ 尺度；小样本覆盖往往优于纯百分位。
- **BCa**（bias-corrected and accelerated）：校正偏倚与偏度，百分位的升级版。
- **参数 Bootstrap**：先拟合参数模型再从模型抽样（而非有放回原数据）——模型对时更高效，错则同错。
- **残差 Bootstrap**（回归）：重抽样残差或配对 $(x_i,y_i)$——见回归笔记中的稳健 SE 思路。

经验规则：先试百分位；若 $\hat\theta^{*}$ 明显偏态或 $n$ 不大，再升到 Bootstrap-$t$ / BCa。18.05 重点掌握**百分位法 + 何时可信**即可。

计算上每次重算 $T$ 的代价 × $B$；均值 / 中位数便宜，复杂优化型统计量要控制 $B$ 或并行。

---
## 5. 何时帮助大？何时要小心？

**帮助大：**

- 统计量复杂：中位数、截断均值、相关系数、比值、分位数回归系数等；
- 想要非对称区间且不愿推导变换；
- 教学 / 探索：可视化 $\hat\theta^{*}$ 直方图即见偏态与多峰警告。

**小心 / 可能失败：**

- $n$ 很小（经验分布太糙）；
- 依赖极值的统计量（样本最大、某些风险度量）；
- 强依赖结构却当 i.i.d. 重抽样（时间序列需 block bootstrap；聚类需按簇重抽样）；
- 用 Bootstrap“证明”因果或弥补有偏样本——重抽样不能创造外部效度。

> [!warning] 与排列检验的区别
> 排列 / 随机化检验在**交换性空假设**下重排标签，直接控 Type I。Bootstrap 估的是**抽样分布形状**，主要用于 SE/CI；也可用“Bootstrap 世界里的检验”，但逻辑与排列不同。

---
## 6. 与解析 CI、$t$ 区间的关系

均值这种有干净公式的量：大样本下百分位 Bootstrap $\approx$ 正态 / $t$ 区间。一致性是健全性检查；若差很多，检查代码、偏态或 $n$。

对均值，有时仍偏好 $t$ 区间（精确度在正态模型下更高）。Bootstrap 的比较优势在**公式稀缺**处。与 [[Confidence Intervals]] 的覆盖诠释完全相同：评价的是程序的长期覆盖，不是单次区间的“概率含参”。

渐近理论（略）：在 i.i.d. 与 $T$ 的 Hadamard 可微等条件下，Bootstrap 分布与真抽样分布的距离以合适速率趋于 0；这解释了“大样本 + 光滑统计量”时百分位法为何可用，也解释了为何对 $\max_i X_i$ 一类不光滑 / 极值泛函会失效。

---
## 7. 小例子：均值（对照公式）

数据 $x=(2,3,4,5,6)$，$\hat\theta=\bar x=4$。有放回抽 $n=5$，重复 $B$ 次得 $\{\bar x^{*b}\}$。百分位 $95\%$ CI 取 $2.5\%$/$97.5\%$ 分位。解析 $t$ 区间用 $s/\sqrt5$ 与 $t_{4,0.025}$。二者在此应接近；若你的实现差很远，多半是抽样容量写错（误用小于 $n$）或分位索引 off-by-one。

> [!example] 相关的百分位区间
> 对配对 $(x_i,y_i)$ 有放回重抽整行，每次算 $r^{*}$。经验分位给出 $r$ 的区间——无需 Fisher $z$ 变换公式（变换仍可改善覆盖，但是可选项）。

亦可做粗略假设检验：若百分位 CI 不含 $\theta_0$，则与水平约 $\alpha$ 的双边检验拒绝 $H_0:\theta=\theta_0$ 同向（覆盖对偶的 Bootstrap 版）；精确 Type I 控制仍以排列检验更干净。

百分位区间对参数变换**不总是**等变：若关心 $g(\theta)$，应对 $g(\hat\theta^{*})$ 直接取分位，而不是先对 $\hat\theta^{*}$ 取分位再变换端点（非线性 $g$ 时二者不同）。

---
## 8. 实践要点

1. $B$ 至少数百；报分位数区间时 $B\ge 1000$ 更稳妥。
2. 每次重抽样容量仍为 $n$（有放回）。
3. 固定种子便于复现。
4. 画 $\hat\theta^{*}$ 直方图：严重偏态考虑对数尺度或 BCa。
5. 报告时写明：非参数百分位 Bootstrap、$B$、统计量定义。
6. 依赖数据（时间、聚类）不要假装 i.i.d. 重抽观测。

---
## 9. 自检与参考答案

1. 能陈述 Bootstrap 用经验分布代替 $F$ 的核心思想。
2. 会写有放回重抽样算法并算百分位 CI。
3. 知道它擅长复杂统计量 / 非对称区间，以及小 $n$、依赖数据、极值统计量的风险。
4. 能区分百分位 Bootstrap 与解析 $z$/$t$ CI、与排列检验。
5. 下一主题：[[Linear Regression]]——回归系数同样可用残差或配对 Bootstrap 估 SE。

> [!success]- 参考答案
> 1. 把样本经验分布当总体，有放回重抽模拟 $\hat\theta$ 的抽样分布。
> 2. 每次抽 $n$ 个有放回 → 算 $\hat\theta^{*}$；百分位 CI 取 $\alpha/2$ 与 $1-\alpha/2$ 经验分位。
> 3. 擅长中位数/相关等；小 $n$、极值、$\mathrm{i.i.d.}$ 假设破坏时危险。
> 4. Bootstrap 估 SE/CI（覆盖诠释同频率派）；排列检验在交换性 $H_0$ 下直接控 Type I。
> 5. 回归可用配对 $(x_i,y_i)$ 或残差重抽样得系数的 Bootstrap SE/CI。

> [!example] 练习：标准误
> 同上，五次 $\bar x^{*}$ 为 $3.2,4.0,4.6,3.8,4.4$。估计 Bootstrap SE（用样本标准差）。

> [!success]- 练习参考答案
> 均值 $\overline{\bar x^{*}}=4.0$。平方偏差和 $=0.8+0+0.36+0.04+0.16=1.36$，
> $\widehat{\mathrm{se}}=\sqrt{1.36/4}=\sqrt{0.34}\approx 0.58$（分母 $B-1$）。
> 解析 SE $s/\sqrt n\approx 1.58/2.236\approx 0.71$；示意级 $B$ 下二者不必接近。

## 参考

- Jeremy Orloff & Jennifer French Kamrin, *18.05 Introduction to Probability and Statistics*, MIT OCW Spring 2022（bootstrap）
- https://ocw.mit.edu/courses/18-05-introduction-to-probability-and-statistics-spring-2022/
