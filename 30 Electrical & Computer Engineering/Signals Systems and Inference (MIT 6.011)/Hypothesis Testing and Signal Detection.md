---
aliases:
  - 假设检验与信号检测
  - Hypothesis Testing and Signal Detection
  - 信号检测
  - Neyman-Pearson
  - ROC
  - 似然比检验
tags: [ee, signals_systems_inference]
up: "[[Signals Systems and Inference (MIT 6.011) MOC]]"
related:
  - "[[Hypothesis Testing]]"
  - "[[Conditional Probability and Bayes Theorem]]"
  - "[[Bayesian Inference]]"
  - "[[Matched Filtering]]"
  - "[[MMSE and LMMSE Estimation]]"
down:
  - "[[Matched Filtering]]"
---
# 假设检验与信号检测

> [!summary] 核心结论
> 检测把观测 $Y$ 判给假设 $H_0$ 或 $H_1$（如噪声 alone vs 信号+噪声）。**Bayes / MAP** 最小化平均风险或错误概率，导致**似然比检验（LRT）**
> $$
> \Lambda(y)=\frac{p(y\mid H_1)}{p(y\mid H_0)}\ \gtrless\ \eta.
> $$
> **Neyman–Pearson**：在虚警率 $P_{\mathrm{FA}}=P(\text{判}H_1\mid H_0)\le\alpha$ 下最大化检测概率 $P_{\mathrm{D}}=P(\text{判}H_1\mid H_1)$——最优仍是 LRT，阈值 $\eta$ 由 $\alpha$ 标定。**ROC** 曲线刻画 $(P_{\mathrm{FA}},P_{\mathrm{D}})$ 权衡。统计课 NHST 见 [[Hypothesis Testing]]；本篇侧重通信 / 雷达式信号检测与似然比。

> 底本：MIT 6.011 OCW Spring 2018 — detection；Bayes 预备 [[Conditional Probability and Bayes Theorem]]。

---
## 1. 二元假设与两类错误

| | 真相 $H_0$ | 真相 $H_1$ |
|---|---|---|
| 判 $H_0$ | 正确 | 漏检（Type II） |
| 判 $H_1$ | 虚警（Type I） | 正确检测 |

通信：比特 0/1；雷达：$H_0$ 无目标，$H_1$ 有目标。代价可以不对称（虚警很贵或漏检很贵）⇒ Bayes 风险。

![[ssi-detection.svg]]

---
## 2. Bayes 与 MAP 检测

先验 $\pi_0=P(H_0)$，$\pi_1=1-\pi_0$。0-1 代价下最小化错误概率 ⇒ **MAP**：
$$
\text{选}\arg\max_i P(H_i\mid y)=\arg\max_i p(y\mid H_i)\pi_i.
$$
即 LRT 与阈值 $\eta=\pi_0/\pi_1$（再乘代价因子则改 $\eta$）。最大似然检测是 $\pi_0=\pi_1$ 的特例。

与估计不同：输出是**离散决策**，不是连续 $\hat X$。同一观测可先做充分统计量压缩再判决。

---
## 3. Neyman–Pearson 与似然比

雷达等场景先验难定，改为：约束 $P_{\mathrm{FA}}\le\alpha$，最大化 $P_{\mathrm{D}}$。**Neyman–Pearson 引理**：最优检验为似然比与阈值比较，阈值选得使虚警恰为 $\alpha$（随机化处理离散情形）。无需先验，但需能计算 $H_0$ 下统计量分布以定阈值。

> [!example] 高斯均值检测（完整数字）
> $H_0: Y\sim\mathcal{N}(0,1)$，$H_1: Y\sim\mathcal{N}(a,1)$，$a=2$。似然比
> $$
> \Lambda(y)=\exp\bigl(ay-a^2/2\bigr)\ \gtrless\ \eta
> $$
> ⇔ $y\gtrless \gamma$（$\gamma=\frac{a}{2}+\frac{1}{a}\ln\eta$）。取 NP：要 $P_{\mathrm{FA}}=\alpha=0.05$。$H_0$ 下 $Y\sim\mathcal{N}(0,1)$，
> $$
> P(Y>\gamma\mid H_0)=Q(\gamma)=0.05\Rightarrow\gamma\approx 1.645.
> $$
> 检测概率
> $$
> P_{\mathrm{D}}=P(Y>1.645\mid H_1)=Q(1.645-2)=Q(-0.355)=1-Q(0.355)\approx 0.639.
> $$
> 若 $a=3$，同 $\alpha$ 下 $\gamma=1.645$，$P_{\mathrm{D}}=Q(1.645-3)=Q(-1.355)\approx 0.912$。**信号幅度 ↑ ⇒ 同虚警下检测率 ↑**——ROC 上移。

---
## 4. ROC 曲线

横轴 $P_{\mathrm{FA}}$，纵轴 $P_{\mathrm{D}}$，扫阈值得到曲线。

- 理想：拐角到 $(0,1)$。
- 无信息：对角线 $P_{\mathrm{D}}=P_{\mathrm{FA}}$。
- AUC（曲线下面积）常作整体可分性摘要。

高斯均值漂移族的 ROC 由 SNR / 偏移 $a/\sigma$ 决定；匹配滤波（下一篇）正是在白噪声下把波形检测化为「最大 SNR 的一维高斯」问题。

> [!warning] $p$ 值语言 vs 检测语言
> 统计 NHST 的 $p$ 值与「在固定 $\alpha$ 下的 NP 检验」相关但叙事不同；雷达 / 通信更常直接谈 $P_{\mathrm{FA}},P_{\mathrm{D}}$ 与阈值。不要把 $P_{\mathrm{D}}$ 叫成「$p$ 值」。详见 [[Hypothesis Testing]] 的误读清单。

---
## 5. 充分统计量与白高斯中的信号

模型 $Y(t)=s_i(t)+W(t)$，$W$ 白高斯。最优检测可化为有限维充分统计（相关器输出 / 匹配滤波采样）。多假设（星座）⇒ 最大相关 / 最小距离译码。彩色噪声：先白化再匹配——与 Wiener 白化思想相连。

离散：向量 $y=s_i+w$，$w\sim\mathcal{N}(0,\Sigma)$。LRT 常成二次型；$\Sigma=\sigma^2 I$ 时退化为最近邻。

---
## 6. 与估计的分工

| | 估计（MSE） | 检测（0-1 / NP） |
|---|---|---|
| 输出 | $\hat X$ 连续 | 假设编号 |
| 最优结构 | 条件均值 / LMMSE | 似然比 ≷ 阈值 |
| 典型后续 | Wiener / Kalman | 匹配滤波 + 阈值 |

复合假设（信号振幅未知等）导致 UMP / GLRT 等扩展；6.011 先掌握简单假设 LRT。

---
## 7. 从波形到标量：为何匹配滤波出现

连续时间 $y(t)=s(t)+w(t)$（$H_1$）vs $y(t)=w(t)$（$H_0$），$w$ 白高斯。对数似然比化为相关统计量 $\int y(t)s(t)\,dt$（及能量项）。这正是匹配滤波在符号末采样的输出——**检测最优前端**把无穷维观测压成一维，再阈值判决。彩色噪声先白化，再对白化信号匹配。细节与 SNR 公式见 [[Matched Filtering]]。

贝叶斯风险若对两类错误加权不同，只改变阈值 $\eta$，不改变「先算似然比」的结构——稳健的工程习惯是：实现充分统计量，阈值由代价 / 虚警指标单独标定。

---
## 8. 自检与参考答案

1. 画出虚警 / 漏检与 $P_{\mathrm{FA}},P_{\mathrm{D}}$。
2. MAP 如何导致似然比检验？
3. Neyman–Pearson 优化什么？最优形式？
4. ROC 上「更好」的检测器如何表现？
5. 例题中 $a$ 增大时为何 $P_{\mathrm{D}}$ 升？

> [!success]- 参考答案
> 1. $P_{\mathrm{FA}}=P(\text{判}H_1\mid H_0)$；$P_{\mathrm{D}}=P(\text{判}H_1\mid H_1)$；漏检 $1-P_{\mathrm{D}}$。
> 2. 比较 $p(y\mid H_i)\pi_i$ ⇔ $\Lambda(y)\gtrless\pi_0/\pi_1$。
> 3. 固定 $P_{\mathrm{FA}}\le\alpha$ 最大化 $P_{\mathrm{D}}$；最优为 LRT。
> 4. 同样 $P_{\mathrm{FA}}$ 下更高 $P_{\mathrm{D}}$（曲线更靠左上）。
> 5. 两假设分布距离增大，在同一阈值（同虚警）下 $H_1$ 质量更多落入拒绝域。

---
## 附录补充：多假设与最小距离

等先验、等能量、AWGN 下，$M$ 元信号检测退化为选择与接收向量最近的星座点（或最大相关）。错误概率由最近邻距离与噪声方差决定。这把几何（Voronoi）与 LRT 统一：似然 $\propto\exp(-\lVert y-s_i\rVert^2/(2\sigma^2))$。非等能量时多出偏置项 $\lVert s_i\rVert^2$。与 [[Matched Filtering]] 的联系：相关器组实现最大相关。

---
## 9. 阈值标定实务

NP 检验需要 $H_0$ 下统计量的尾部分布。解析可得（高斯）时用 $Q$ 函数；否则：

- 蒙特卡洛估虚警率 vs 阈值曲线，再反查 $\alpha$；
- 渐近大偏差 / CLT 近似（谨慎）；
- 恒虚警（CFAR）：用周围单元估噪声功率再归一化阈值。

代价敏感的 Bayes 阈值随先验漂移——若先验不确定，ROC 上选工作点往往比死守单一 $\eta$ 更透明。把检测器输出的软值（似然比）留给下游融合，而不是过早硬判决，是系统级好习惯。

> [!example] 改变 $\alpha$ 的权衡
> 承接前文 $a=2$ 高斯例：$\alpha=0.01$ ⇒ $\gamma\approx 2.326$，$P_{\mathrm{D}}=Q(2.326-2)=Q(0.326)\approx 0.372$（相对 $\alpha=0.05$ 时的 $0.639$ 明显下降）。压虚警 ⇒ 抬漏检，ROC 上只是换工作点，并不自动「更好」。

## 参考

- Verghese & Oppenheim, *Signals, Systems and Inference*, MIT 6.011 OCW Spring 2018
- https://ocw.mit.edu/courses/6-011-signals-systems-and-inference-spring-2018/
- [[Hypothesis Testing]]、[[Matched Filtering]]、[[Conditional Probability and Bayes Theorem]]
