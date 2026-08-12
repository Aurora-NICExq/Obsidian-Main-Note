---
aliases:
  - 金融中的回归与PCA
  - Regression and PCA in Finance
  - 因子模型
  - yield curve PCA
tags: [math, math_finance]
up: "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
related:
  - "[[Linear Algebra for Finance]]"
  - "[[Probability and Stochastic Processes for Finance]]"
  - "[[Interest Rates Products and Models]]"
  - "[[Portfolio Management]]"
  - "[[Linear Regression]]"
  - "[[Hypothesis Testing]]"
  - "[[Joint Distributions Covariance and Correlation]]"
down:
  - "[[Interest Rates Products and Models]]"
---
# 金融中的回归与 PCA

> [!summary] 核心结论
> 资产收益的共同波动用**因子模型**压缩：$R=\alpha+Bf+\varepsilon$。回归估计载荷与检验 $\alpha$（[[Linear Regression]]、[[Hypothesis Testing]]）；**PCA** 对 $\Sigma$ 或收益矩阵做谱分解，得到数据驱动因子——收益率曲线上典型前三主成分对应水平 / 斜率 / 曲率。工具是线性代数，解释要警惕样本内过拟合与因子不稳定。

> 底本：MIT 18.642 统计 / PCA 单元；底座 [[Linear Regression]] 与 [[Linear Algebra for Finance]]。

> 关键词：因子载荷、特异风险、主成分、水平–斜率–曲率

---

## 1. 单因子与 CAPM 型回归

市场模型：
$$
R_{i,t}-r_f=\alpha_i+\beta_i(R_{m,t}-r_f)+\varepsilon_{i,t}.
$$
OLS 得 $\hat\beta_i,\hat\alpha_i$。$\beta$ 是系统风险；$\alpha$ 是否显著异于 0 用 $t$ 检验（注意异方差与重叠——金融残差很少理想 i.i.d.）。组合层面见 [[Portfolio Management]]。

> [!example] 迷你回归
> 超额收益（%）五期：市场 $x=(1,2,-1,0,3)$，股票 $y=(1.5,2.5,-0.5,0.2,4)$。
> $\bar x=1$，$\bar y=1.54$。
> $\sum(x-\bar x)(y-\bar y)=0.5\cdot(-0.04)+1\cdot0.96+(-2)\cdot(-2.04)+(-1)\cdot(-1.34)+2\cdot2.46$
> 更干净：直接用公式
> $$
> \hat\beta=\frac{\sum(x_i-\bar x)(y_i-\bar y)}{\sum(x_i-\bar x)^2}.
> $$
> $\sum(x-\bar x)^2=0+1+4+1+4=10$，
> $\sum(x-\bar x)(y-\bar y)=0\cdot(-0.04)+1\cdot0.96+(-2)(-2.04)+(-1)(-1.34)+2\cdot2.46=0.96+4.08+1.34+4.92=11.3$，
> $\hat\beta=1.13$，$\hat\alpha=\bar y-\hat\beta\bar x=0.41$。解读：样本内偏攻击、略正 $\alpha$（仅 5 点，勿当真）。

---

## 2. 多因子模型

$$
R_t=\alpha+B f_t+\varepsilon_t,\quad
\mathrm{Cov}(\varepsilon)=\Omega\ \text{（常设对角）}.
$$
$B$ 为载荷矩阵。协方差结构
$$
\Sigma=B\,\mathrm{Cov}(f)\,B^\top+\Omega
$$
把风险拆成**共同**与**特异**——组合分散化主要压 $\Omega$ 部分。经济因子（Fama–French 等）vs 统计因子（PCA）是建模选择，不是对错二元。

---

## 3. PCA 做法（收益）

数据矩阵中心化后样本协方差 $\hat\Sigma$。特征值 $\lambda_1\ge\lambda_2\ge\cdots$，方差解释比 $\lambda_k/\sum\lambda_j$。前 $k$ 个特征向量作因子方向；得分序列作因子实现。

选择 $k$：碎石图肘部、解释比例阈值、或交叉验证预测。金融里 $k$ 常很小（市场 + 少数风格）。

> [!warning] 主成分没有先天名字
> 第一 PC 常像“市场”，但是符号可翻、且随样本窗漂移。回测里把 PC 当成稳定可交易因子，容易过拟合。

---

## 4. 收益率曲线 PCA

对到期网格上的收益率变化 $\Delta y(t,\tau_j)$（或水平）做 PCA，经典经验图景：

| PC | 绰号 | 形状直觉 |
|----|------|----------|
| 1 | Level 水平 | 各期限同向平移 |
| 2 | Slope 斜率 | 短长端反向 |
| 3 | Curvature 曲率 | 中间相对两端 |

前三成分常解释日变化 $90\%$+ 的方差（视市场与窗口）。对冲：用 2–3 个关键债券匹配前几 PC 的久期暴露，比“只匹配单一久期”更稳。接 [[Interest Rates Products and Models]]。

---

## 5. 回归诊断在金融中的重点

- **残差相关**：时间上的 ARCH 效应 → 波动模型；
- **$\beta$ 时变**：滚动回归或状态空间（进阶见 15.450）；
- **重叠与 HAC**：用周/月频率或 Newey–West 类标准误；
- **$R^2$ 高**：债券曲线拟合可以很高；股票横截面单因子 $R^2$ 往往一般——高不自动等于可交易 edge。

相关与协方差复习：[[Joint Distributions Covariance and Correlation]]。

---

## 6. 从 PCA 到降维交易 / 风险

风险系统：用前 $k$ 个因子 + 对角特异方差快速算组合方差。统计套利：残差均值回复假设——**强假设**，需严格样本外与成本。18.642 强调数学结构；实盘约束留给从业讲座与 [[Analytics of Finance (MIT 15.450) MOC]]。

---

## 7. 截面回归与时间序列回归

金融里两种“回归”常被混称：

- **时间序列**：固定资产 $i$，对 $t$ 回归得 $\beta_i$（市场模型）；
- **截面**：固定 $t$，对资产 $i$ 回归风格暴露，或 Fama–MacBeth：先截面估溢价再对时间平均。

标准误在截面相关、时间相关时都要调整。课程先练熟 OLS 几何与 PCA，再碰 FM 程序。

> [!example] 因子解释力
> 三因子模型截面 $R^2$ 高，不代表能预测下一期收益；它多半说明**共同风险**被吸收。可交易的是 $\alpha$ 或错误定价，不是高 $R^2$ 本身。

---

## 8. 特征值碎石图怎么读

横轴成分序号，纵轴 $\lambda_k$ 或解释比例。陡降后变平的“肘”是候选 $k$。金融收益常：第 1 巨大，2–3 中等，其后缓慢。曲线 PCA 类似但更集中。若前 20 个几乎等大，可能噪声主导——降维无神奇。

滚动窗口重估 PCA：载荷角度漂移大时，勿把旧因子当稳定可交易信号。

---

## 9. 自检与参考答案

1. 写出单因子市场模型并解释 $\alpha,\beta$。
2. 多因子下 $\Sigma=B\mathrm{Cov}(f)B^\top+\Omega$ 的含义。
3. PCA 的输入、输出与方差解释比。
4. 收益率曲线前三 PC 的典型解释。
5. 列出两条金融回归的特殊陷阱。

> [!success]- 参考答案
> 1. $R_i-r_f=\alpha_i+\beta_i(R_m-r_f)+\varepsilon$；$\beta$ 系统敏感度，$\alpha$ 截距（定价误差候选）。
> 2. 共同因子贡献低秩相关；$\Omega$ 为特异（常对角）风险。
> 3. 对 $\hat\Sigma$ 特征分解；特征向量=载荷方向；$\lambda_k/\sum\lambda$ 解释比。
> 4. 水平、斜率、曲率。
> 5. 异方差/波动聚集；$\beta$ 时变；样本 PC 不稳定；$R^2$ 误读为可预测性。

> [!example] 练习：两资产 PCA 直觉
> $\Sigma=\begin{pmatrix}1&0.8\\0.8&1\end{pmatrix}$。最大特征值方向近似 $(1,1)$，最小近似 $(1,-1)$。解释。

> [!success]- 练习参考答案
> 高相关 ⇒ 同向运动解释大部分方差（市场因子）；反向组合方差小（近似对冲）。特征值：$1.8$ 与 $0.2$，解释比 $90\%$ / $10\%$。

## 参考

- MIT 18.642 regression / PCA lectures；18.S096 相关录像
- https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/
- [[Linear Regression]]、[[Hypothesis Testing]]
