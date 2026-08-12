---
aliases:
  - 金融中的 Bootstrap
  - Bootstrap Methods in Finance
  - 块自助法
  - block bootstrap
  - 时间序列 bootstrap
tags: [math, analytics_finance]
up: "[[Analytics of Finance (MIT 15.450) MOC]]"
related:
  - "[[Bootstrap Methods]]"
  - "[[GMM and Inference in Finance]]"
  - "[[Return Predictability]]"
  - "[[Volatility Models GARCH]]"
  - "[[Probability and Statistics (MIT 18.05) MOC]]"
  - "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
down:
  - "[[Volatility Models GARCH]]"
---
# 金融中的 Bootstrap 方法

> [!summary] 核心结论
> Bootstrap 用重抽样估计统计量的抽样分布（SE、CI、$p$ 值近似）。i.i.d. 数据可用经典有放回重抽；**收益时间序列有依赖与异方差**，对观测直接 i.i.d. 重抽会破坏依赖结构 → 需 **块 Bootstrap（block bootstrap）** 或残差 / 模型 Bootstrap。基础算法见 [[Bootstrap Methods]]；本笔记强调金融场景的陷阱。

> 底本：MIT 15.450 Lecture（Bootstrap）；接 18.05。

> 关键词：resampling、block bootstrap、stationary bootstrap、dependence、overlapping returns

---

## 1. 为何金融里特别需要？

- 估计量复杂：夏普比率、GMM 参数、可预测性斜率、风险价值；
- 渐近 SE 依赖 HAC 带宽等选择；
- 小样本、$t$ 分布近似差。

Bootstrap 提供计算型替代，但**假设要匹配数据依赖**。

---

## 2. 回顾：i.i.d. 百分位法

数据 $x_1,\ldots,x_n$，统计量 $\hat\theta$。有放回抽 Bootstrap 样本 → $\hat\theta^{*b}$；百分位 CI 取经验分位。详见 [[Bootstrap Methods]]。

> [!example] 夏普比率（i.i.d. 假设下）
> $\widehat{\mathrm{SR}}=\bar r/\hat\sigma$。对收益向量有放回重抽整段时期的日收益，重算 SR，得 SE / CI。若收益实际有波动群集，该 CI **偏乐观或扭曲**——应改块方法。

---

## 3. 块 Bootstrap：保留局部依赖

**思想**：一次重抽长度为 $\ell$ 的**连续块**，再拼接成长度约 $T$ 的伪序列，从而近似保留短程自相关。

常见变体：

| 方法 | 要点 |
|------|------|
| 移动块（moving block） | 固定块长 $\ell$，块起点随机 |
| 圆形块 | 把序列首尾相接，避免端点浪费 |
| 平稳 Bootstrap | 块长随机（几何），渐近平稳 |

块长 $\ell$ 的选择是调参：太短破坏依赖；太长有效独立块太少，方差估不准。

> [!warning] 绝对不要对强依赖序列假装 i.i.d. 重抽
> 典型翻车：重叠的多期收益 $R_{t\to t+h}$、GARCH 标准化之前的原始 $r_t$、带滞后回归元的可预测性回归。结果：Bootstrap SE 过小、CI 过窄、虚假显著——与忽略 HAC 同类错误。

---

## 4. 残差 / 模型 Bootstrap

若有模型 $r_t=\mu_t(\hat\theta)+\hat\sigma_t z_t$：

1. 得标准化残差 $\hat z_t$；
2. 对 $\hat z$ 重抽样（若近似 i.i.d.）或块重抽样；
3. 用估计的 $\mu_t,\sigma_t$ 递归生成伪收益；
4. 在伪样本上重估 $\tilde\theta^{*}$。

对 GARCH，模型 Bootstrap 常比直接对 $r_t$ 块重抽更自然——接 [[Volatility Models GARCH]]。

---

## 5. 与 HAC、GMM 的分工

| 工具 | 角色 |
|------|------|
| HAC SE | 解析 / 半参数长期方差，快 |
| Block Bootstrap | 少推公式、可反映非对称与有限样本 |
| 二者交叉验证 | SE 差一个数量级 → 查代码或块长 / 带宽 |

GMM 的 $J$ 统计量、可预测性 $t$ 统计量都可 Bootstrap 校準——见 [[GMM and Inference in Finance]]、[[Return Predictability]]。

---

## 6. 实践清单

1. 先画 ACF / ACF of squares，判断依赖类型；
2. 有依赖 → 块或模型 Bootstrap，并报告块长规则；
3. $B$ 足够大（分位 CI 至少数百～数千）；
4. 固定种子；对重叠收益明确构造单位；
5. 不把 Bootstrap 当“数据挖矿免罪卡”——多重试错仍膨胀 Type I。

---

## 7. 与百分位 CI / 检验的金融用法

- **CI**：对 $\hat\theta^{*}$ 取分位，报告夏普、$\hat b$、GARCH $\hat\alpha+\hat\beta$ 等的区间；
- **检验**：看 $H_0$ 下重抽样的 $t^{*}$ 是否覆盖观测 $t$（需小心如何施加 $H_0$）；
- **对比 HAC**：若 Newey–West 与块 Bootstrap SE 同阶，信心增加；差一个数量级则查重叠构造或块长。

> [!example] 块长经验量级
> 日频、关注约月度依赖时，试 $\ell\approx 10$–$20$ 并做敏感性；没有唯一正确 $\ell$。课内强调**敏感性报告**，不背单一公式。

对照 [[Bootstrap Methods]] 的 i.i.d. 理论；金融默认先问“依赖是否被重抽样保留”。

课内（15.450）Bootstrap 讲次强调的是：**重抽样方案必须与估计量的依赖结构匹配**，而不是把 18.05 的有放回算法原样套到收益率序列上。

---

## 8. 自检与参考答案

1. 何时可用经典 i.i.d. Bootstrap。
2. 块 Bootstrap 要解决什么问题。
3. 举一个金融里 i.i.d. 重抽危险的例子。
4. 模型 Bootstrap 的基本步骤。
5. 块长选择应报告什么。
6. 下一主题：[[Volatility Models GARCH]]。

> [!success]- 参考答案
> 1. 近似 i.i.d. 观测（或已充分预白 / 标准化残差近似白）。
> 2. 在重抽样中保留短程时间依赖。
> 3. 重叠多期收益、GARCH 收益、滞后预测回归。
> 4. 估模型 → 抽残差 → 生成伪数据 → 重估统计量。
> 5. 所用规则 / 试过的 $\ell$ 及 SE 对 $\ell$ 的敏感性。
> 6. 条件波动建模与持续性。

> [!example] 练习：概念
> 日收益 ACF 接近 0，但平方 ACF 显著。对原始 $r_t$ 做 i.i.d. Bootstrap 估均值 SE 是否大致可接受？估 $\mathrm{Var}(r_t)$ 的 CI 呢？

> [!success]- 练习参考答案
> 均值：在弱依赖下往往还凑合（均值的长期方差仍可能受异方差影响，HAC/块更稳）。方差 / 波动相关统计量：平方依赖重要，i.i.d. 重抽危险，应用块或 GARCH 残差 Bootstrap。

> [!tip] 与 18.05 分工
> [[Bootstrap Methods]] 学算法；本笔记学**何时不能 i.i.d. 重抽**。

## 参考

- Leonid Kogan, *15.450 Analytics of Finance*, MIT OCW Fall 2010（Bootstrap）
- https://ocw.mit.edu/courses/15-450-analytics-of-finance-fall-2010/
- [[Bootstrap Methods]]（18.05）
