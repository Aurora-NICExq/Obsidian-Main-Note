---
aliases:
  - 金融计量 MLE 与 QMLE
  - Financial Econometrics MLE
  - QMLE
  - 准最大似然
  - 收益似然
tags: [math, analytics_finance]
up: "[[Analytics of Finance (MIT 15.450) MOC]]"
related:
  - "[[Maximum Likelihood Estimation]]"
  - "[[GMM and Inference in Finance]]"
  - "[[Volatility Models GARCH]]"
  - "[[Probability and Statistics (MIT 18.05) MOC]]"
  - "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
down:
  - "[[GMM and Inference in Finance]]"
---
# 金融计量：MLE 与 QMLE

> [!summary] 核心结论
> 对收益模型写条件密度、最大化样本对数似然，得到 **MLE**。金融里常假设条件正态做方便的似然，即使真实条件分布有厚尾——此时估计量是 **QMLE（准最大似然）**：在合适条件下，对**条件均值 / 条件方差参数**仍可一致，但信息矩阵等式可能破坏，需稳健（三明治）标准误。基础 MLE 复习见 [[Maximum Likelihood Estimation]]。

> 底本：MIT 15.450 金融计量 / 似然单元；Tsay 类时序书为参考。

> 关键词：likelihood、QMLE、conditional normal、sandwich SE、misspecification

---

## 1. 收益的条件模型

日收益 $r_t$（或对数收益）。通用写法：
$$
r_t=\mu_t(\theta)+\varepsilon_t,\qquad
\varepsilon_t=\sigma_t(\theta)\,z_t,\quad
\mathbb{E}[z_t\mid\mathcal{F}_{t-1}]=0,\;
\mathrm{Var}(z_t\mid\mathcal{F}_{t-1})=1.
$$
$\mu_t$ 可为常数、AR；$ \sigma_t$ 可为常数或 GARCH（见 [[Volatility Models GARCH]]）。

若进一步假设 $z_t\mid\mathcal{F}_{t-1}\sim\mathcal{N}(0,1)$，则条件对数似然
$$
\ell_t(\theta)=-\tfrac12\log(2\pi)-\tfrac12\log\sigma_t^2(\theta)-\frac{(r_t-\mu_t(\theta))^2}{2\sigma_t^2(\theta)}.
$$
样本目标 $\sum_{t=1}^T\ell_t(\theta)$ 最大化 → $\hat\theta$。

---

## 2. 例：i.i.d. 正态收益

$\mu_t\equiv\mu$，$\sigma_t\equiv\sigma$。MLE：
$$
\hat\mu=\bar r,\qquad
\hat\sigma^2=\frac{1}{T}\sum_{t=1}^T(r_t-\bar r)^2.
$$
（与 [[Maximum Likelihood Estimation]] 中正态 MLE 相同。）

> [!example] 迷你数值
> 收益（%）：$1.2,-0.5,0.8,-1.0,0.5$。$T=5$，$\bar r=0.2$。  
> $\hat\sigma^2=\frac{1}{5}[(1)^2+(-0.7)^2+(0.6)^2+(-1.2)^2+(0.3)^2]=\frac{1+0.49+0.36+1.44+0.09}{5}=0.676$。  
> 年化波动粗算（若日频）：$\hat\sigma\sqrt{252}$（先把 $\%$ 与小数单位弄清）。

---

## 3. QMLE：错误分布下的稳健性

实务：$z_t$ 常有厚尾 / 偏度，正态似然**误设**。仍最大化正态条件似然 → **QMLE**。

经典结果（启发式陈述）：

- 若 $\mu_t(\theta)$、$\sigma_t^2(\theta)$ 的参数化正确，且矩条件足够，则 $\hat\theta$ 对均值/方差参数仍**一致**；
- 渐近方差一般不是“逆 Fisher”，而是**三明治**形式 $A^{-1}BA^{-1}$；应用稳健 SE / HAC（时序相关时）。

> [!warning] QMLE 不是万能
> 若条件方差方程本身错（例如忽略波动群集却当常数 $\sigma$），QMLE 不会神奇地修好模型。稳健的是“分布形状”误设，不是任意误设。

---

## 4. 与 GARCH 估计的接口

GARCH(1,1) 的标准估计正是条件正态（或 $t$）MLE/QMLE：递推 $\sigma_t^2$，累加 $\ell_t$。厚尾时可用 Student-$t$ 似然，或坚持正态 QMLE + 稳健 SE。细节见 [[Volatility Models GARCH]]。

---

## 5. 诊断清单（课堂级）

1. 标准化残差 $\hat z_t=(r_t-\hat\mu_t)/\hat\sigma_t$：应近似白噪声、方差 1；
2. $\hat z_t^2$ 的 ACF：检查是否还留波动群集；
3. QQ 图：正态假设是否离谱；
4. 报告 QMLE + 稳健 SE，避免只报“逆 Hessian”。

接 [[Time Series Analysis for Finance]] 的 ACF 直觉。

---

## 6. 与 GMM 的关系

MLE 的得分方程 $\sum\partial\ell_t/\partial\theta=0$ 是一组**矩条件**；GMM 可把部分矩（正交性）单独使用，无需完整密度——见 [[GMM and Inference in Finance]]。误设密度时，GMM / QMLE 视角帮助理解“还在估什么”。

---

## 7. 信息矩阵与三明治（直觉）

正则 MLE：渐近方差 $\approx I(\theta)^{-1}$（Fisher 信息的逆）。QMLE / 异方差下：
$$
V=A^{-1} B A^{-1},
$$
$A$ 为 Hessian（或得分对参数的期望导数），$B$ 为得分的（长期）外积方差。若模型正确且信息矩阵等式成立，$A=-B$（符号约定下）→ 退回 $I^{-1}$。金融收益几乎总是怀疑等式失败 → **默认报稳健 SE**。

时序相关时，$B$ 换成 HAC 型长期方差（与 [[GMM and Inference in Finance]] 同一套语言）。

> [!tip] 与 18.05 的衔接
> [[Maximum Likelihood Estimation]] 强调正则模型下的 $I^{-1}$；本课默认你已会写似然，重点转向**误设与稳健推断**。

对数似然对 $\sigma_t^2$ 的权重意味着：高波动日对均值参数的信息更少（异方差 OLS 的直觉亲缘）——这也解释了为何方差建模与均值推断往往绑在一起。

---

## 8. 自检与参考答案

1. 写出条件正态对数似然的一项 $\ell_t$。
2. 说明 QMLE 相对 MLE 的典型稳健对象。
3. 为何金融里常用三明治 SE。
4. 标准化残差应大致满足什么。
5. 三明治方差相对 $I^{-1}$ 多了哪一层。
6. 下一主题：[[GMM and Inference in Finance]]。

> [!success]- 参考答案
> 1. $-\frac12\log(2\pi)-\frac12\log\sigma_t^2-(r_t-\mu_t)^2/(2\sigma_t^2)$。
> 2. 条件分布形状误设（如非正态）时，均值/方差参数仍可一致。
> 3. 信息矩阵等式可能失败；朴素 SE 低估/错估不确定性。
> 4. 近似均值 0、方差 1、无（或弱）自相关；平方项无残留 ARCH。
> 5. 用得分的外积（长期）方差 $B$ 夹在 $A^{-1}$ 两侧，而不是只报 $-H^{-1}$。
> 6. 用矩条件估计，不必写全似然。

> [!example] 练习：常数方差 MLE
> 数据 $r=(-1,0,1)$，估 $\hat\mu,\hat\sigma^2$（正态 i.i.d. MLE）。

> [!success]- 练习参考答案
> $\hat\mu=0$，$\hat\sigma^2=(1+0+1)/3=2/3$。

> [!tip] 下一工具
> 不想写密度时转 [[GMM and Inference in Finance]]。

## 参考

- Leonid Kogan, *15.450 Analytics of Finance*, MIT OCW Fall 2010（MLE / QMLE）
- https://ocw.mit.edu/courses/15-450-analytics-of-finance-fall-2010/
- Ruey S. Tsay, *Analysis of Financial Time Series*（教材参考）
- [[Maximum Likelihood Estimation]]（18.05）
