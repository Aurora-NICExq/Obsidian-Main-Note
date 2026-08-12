---
aliases:
  - 利率产品与模型
  - Interest Rates Products and Models
  - 久期
  - swap libor intuition
tags: [math, math_finance]
up: "[[Mathematics with Applications in Finance (MIT 18.642) MOC]]"
related:
  - "[[Financial Markets Bonds and One-Period Models]]"
  - "[[Regression and PCA in Finance]]"
  - "[[Black-Scholes and Risk Neutral Valuation]]"
  - "[[Linear Algebra for Finance]]"
  - "[[Analytics of Finance (MIT 15.450) MOC]]"
down:
  - "[[Time Series Analysis for Finance]]"
---
# 利率产品与模型

> [!summary] 核心结论
> 利率市场的骨架是**零息曲线**：$P(0,T)$ 给出任意确定性现金流的折现。附息债、远期、互换都是零息的线性组合（或由曲线隐含的远期利率拼装）。**久期**是价格对收益率的一阶敏感度，是利率风险的线性代数一阶项；凸性为二阶。LIBOR / SOFR / 互换的制度细节保持高层——抓住“曲线 → 定价 → 对冲”即可。

> 底本：MIT 18.642 利率单元；一期折现见 [[Financial Markets Bonds and One-Period Models]]；曲线 PCA 见 [[Regression and PCA in Finance]]。

> 关键词：零息、即期/远期、互换、修正久期、凸性

---

## 1. 曲线对象

| 对象 | 含义 |
|------|------|
| $P(0,T)$ | 零息债价格（$T$ 时刻付 1） |
| 即期 $y_T$ | $(1+y_T)^{-T}=P(0,T)$（按约定复利） |
| 瞬时远期 $f(0,T)$ | $-\partial_T\log P(0,T)$（连续） |
| 简单远期 $F(0;T,S)$ | 由 $P(0,T)/P(0,S)$ 锁定 |

无套利：同一现金流用曲线折现只能有一个今日价值（忽略摩擦）。构建曲线：用存款、期货、互换等工具自举（bootstrap）——课程强调逻辑，不抠报价惯例。

---

## 2. 附息债再访

现金流 $c_{t_i}$，价格
$$
P=\sum_i c_{t_i} P(0,t_i).
$$
若强行用单一 YTM $y$：
$$
P=\sum_i c_{t_i}(1+y)^{-t_i},
$$
则 $y$ 只是**方程的解**，不是每段真实折现率。曲线不平坦时，YTM 久期与关键曲线场景会分叉。

> [!example] 三年年付票息
> 零息：$P(0,1)=0.97$，$P(0,2)=0.93$，$P(0,3)=0.88$。面值 100、年票息 4：
> $$
> P=4\cdot0.97+4\cdot0.93+104\cdot0.88=4\cdot0.97+4\cdot0.93+91.52=3.88+3.72+91.52=99.12.
> $$

---

## 3. 互换直觉（高层）

普通利率互换：一方付固定 $K$，收浮动（历史上常与 LIBOR 挂钩；美元市场已迁向 SOFR 等 RFR）。在经典教材叙述下，合理定价的固定端接近**互换利率** $S$，使互换今日价值为零：
$$
S=\frac{1-P(0,T_n)}{\sum_i \delta_i P(0,T_i)}
$$
（支付频率决定 $\delta_i$）。直觉：固定腿 $=$ 浮动腿的现值；浮动腿（理想化）≈ $1-P(0,T_n)$ 的某种归一。

> [!warning] LIBOR 已退出主流定价锚
> 学公式时把 “floating index” 当抽象浮动腿即可。监管改革后折扣曲线与预测曲线可能分离（双曲线）——进阶细节见行业笔记 / [[Analytics of Finance (MIT 15.450) MOC]]，本课不展开。

---

## 4. 久期与凸性

对 YTM 口径（修正久期）：
$$
D_{\mathrm{mod}}=-\frac{1}{P}\frac{\mathrm{d}P}{\mathrm{d}y},\qquad
\frac{\Delta P}{P}\approx -D_{\mathrm{mod}}\Delta y+\frac12 C(\Delta y)^2.
$$
Macaulay 久期是现金流时间的现值加权平均；修正久期 $=D_{\mathrm{Mac}}/(1+y)$（按期约定）。

关键久期：对曲线关键点 $y(T_k)$ 的偏导，用于真实曲线风险。PCA 对冲 ≈ 匹配前几特征场景的敏感度（[[Regression and PCA in Finance]]）。

> [!example] 久期一阶
> $P=99.12$，$D_{\mathrm{mod}}=2.7$（年）。收益率 $+10\,\mathrm{bp}=0.001$：
> $$
> \Delta P\approx -2.7\cdot99.12\cdot0.001\approx -0.268.
> $$
> 大平行移动时需加凸性，否则低估价格上升、高估下跌（凸性为正时）。

---

## 5. 利率模型光谱（仅地图）

| 层次 | 例子 | 用途 |
|------|------|------|
| 静态曲线 | 自举 $P(0,T)$ | 线性产品定价 |
| 短率模型 | Vasicek / CIR | 教学、债券期权直觉 |
| 远期模型 | HJM / LMM | 一致曲线动态 |
| 市场模型 | Bachelier / Black on swap rate | 报价惯例 |

18.642 要你认得“无套利曲线动态必须满足漂移约束”，不必推导完整 HJM。股票 BS 的 $\sigma$ 在利率里变成整条曲线的波动结构。

---

## 6. 与债券组合管理

- **免疫**：久期匹配负债，一阶对平行移动不敏感；
- **杠铃 vs 子弹**：同久期不同凸性 / 曲线风险；
- **利差**：信用债 = 利率曲线 + 利差；利差久期单独计量。

线性代数视角：风险因子暴露向量 $g$，对冲组合 $\theta$ 使 $G\theta\approx 0$（[[Linear Algebra for Finance]]）。

---

## 7. 久期美元与 DV01

实务常报 **DV01**：收益率上升 1 bp 时价值变化的美元数。
$$
\mathrm{DV01}\approx D_{\mathrm{mod}}\cdot P\cdot 0.0001.
$$
组合 DV01 = 各腿代数和（空头为负）。对冲：使净 DV01≈0；更精细则多关键 DV01 或 PCA 因子 DV01。

> [!example] 数字
> $P=10^7$ 美元，$D_{\mathrm{mod}}=7$。平行 $+1\,\mathrm{bp}$：$\Delta P\approx -7\cdot10^7\cdot 10^{-4}=-7000$ 美元。若负债侧 DV01 相同，盈余对平行移动一阶免疫。

---

## 8. 名义、交割与日算（知晓即可）

互换报价依赖日算惯例（Actual/360 等）、支付频率、远期起始。学习模型时把 $\delta_i$ 当“年化分数权重”。真正写定价库再抠惯例；OCW 习题通常给简化 $\delta$。

---

## 9. 自检与参考答案

1. 用零息表示附息债价格。
2. 即期与远期如何从 $P(0,T)$ 读出（离散一年）。
3. 互换利率公式的结构直觉。
4. 修正久期的定义与一阶 P&L。
5. 为何单一 YTM 久期不足以管曲线风险。

> [!success]- 参考答案
> 1. $P=\sum c_{t_i}P(0,t_i)$。
> 2. $y_T$ 由 $P=(1+y_T)^{-T}$；一年远期 $F(0;T,T+1)=P(0,T)/P(0,T+1)-1$。
> 3. $S=(1-P(0,T_n))/\sum\delta_i P(0,T_i)$，使固定腿现值 = 浮动腿现值。
> 4. $D_{\mathrm{mod}}=-(1/P)\mathrm{d}P/\mathrm{d}y$；$\Delta P/P\approx -D_{\mathrm{mod}}\Delta y$。
> 5. 非平行移动（斜率/曲率）会留下关键风险；需关键久期或 PCA。

> [!example] 练习：远期
> $P(0,1)=0.96$，$P(0,2)=0.91$。求 $F(0;1,2)$。

> [!success]- 练习参考答案
> $F=0.96/0.91-1\approx 0.05495$（约 $5.5\%$）。

## 参考

- MIT 18.642 interest-rate lectures；18.S096 补充材料
- https://ocw.mit.edu/courses/18-642-topics-in-mathematics-with-applications-in-finance-fall-2024/
