---
aliases:
  - 卡尔曼滤波性质与稳态
  - Kalman Filter Properties
  - Steady-State Kalman
  - 代数 Riccati
  - 稳态卡尔曼增益
tags: [ee, estimation_kalman]
up: "[[Estimation and Kalman Filtering (NPTEL) MOC]]"
related:
  - "[[Kalman Filter Derivation]]"
  - "[[Kalman Filter Applications]]"
  - "[[Least Squares and Optimal Filters]]"
  - "[[Signals Systems and Inference (MIT 6.011) MOC]]"
down:
  - "[[Kalman Filter Applications]]"
---
# 卡尔曼滤波性质与稳态

> [!summary] 核心结论
> 线性–高斯下 KF 是 MMSE 最优且递推充分；新息白化、正交性给出一致性检验把手。时间不变且可达 / 可观时，$P_k$ 与增益 $K_k$ 常收敛到**稳态**，由离散代数 Riccati 方程（DARE）决定——实现可预计算 $K_\infty$，等价于一组 LTI 滤波器，与因果 Wiener 相连。

> 底本：NPTEL 108105059 L20–L21。

> 关键词：最优性、新息白、DARE、稳态增益、可稳可检

---

## 1. 最优性声明（精确版）

在线性状态空间 + 所述二阶噪声假设下：

1. $\hat x_{k\mid k}$ 是基于 $y_{0:k}$ 的**线性** MMSE 估计；
2. 若再加高斯，则为条件均值（全 MMSE）；
3. $P_{k\mid k}$ 是对应误差协方差（模型正确时）。

模型错定（$F$/$H$/$Q$/$R$ 不符真实）时，公式仍跑，但“最优”相对错误世界——$P$ 可能乐观或悲观。

---

## 2. 新息性质与诊断

最优且模型匹配时，$\nu_k=y_k-H\hat x_{k\mid k-1}$ 满足：

- $\mathbb{E}[\nu_k]\approx 0$；
- $\mathbb{E}[\nu_k\nu_j^\mathsf{T}]=0$（$k\neq j$）；
- $\mathbb{E}[\nu_k\nu_k^\mathsf{T}]=S_k$。

归一化新息平方和可用于 $\chi^2$ 门限检测野值 / 模型破裂（与 [[Hypothesis Testing|假设检验]] 同族思想）。ACF 检新息是否白——实用辨识与调 $Q$/$R$ 的核心工具（[[Practical Identification and Instrumentation]]）。

---

## 3. 正交性再叙述

后验误差 $\tilde x_{k\mid k}=x_k-\hat x_{k\mid k}$ 与 $y_{0:k}$ 的线性张成正交。预测误差与 $y_{0:k-1}$ 正交。这保证无法再用线性滤波器从残差里榨出信息——除非非线性或模型增广。

---

## 4. 时间不变与稳态

设 $F,H,Q,R$ 常值。在合适条件（如 $[F,Q^{1/2}]$ 可稳、$[F,H]$ 可检）下，$P_{k\mid k-1}\to P_\infty$，增益 $K_k\to K_\infty$，且 $P_\infty$ 满足 **DARE**：
$$
P=FPF^\mathsf{T}+Q-FP H^\mathsf{T}(HPH^\mathsf{T}+R)^{-1}HPF^\mathsf{T}.
$$
（预测协方差形式；后验形式等价可转换。）

稳态滤波器：
$$
\hat x_{k\mid k}=(I-K_\infty H)F\hat x_{k-1\mid k-1}+K_\infty y_k
$$
（无控制时）——常系数线性系统，可频域分析带宽、噪声增益。

> [!example] 标量稳态
> $x_k=x_{k-1}+w$，$y=x+v$，$Q=q$，$R=r$。DARE 对 $p=P_\infty^-$：
> $$
> p=p+q-\frac{p^2}{p+r}\implies p=\frac{p^2}{p+r}+q.
> $$
> 整理得 $p^2-qp-qr=0$，正根
> $$
> p=\frac{q+\sqrt{q^2+4qr}}{2},\qquad
> K=\frac{p}{p+r}.
> $$
> 取 $q=1,r=4$：$p=(1+\sqrt{1+16})/2=(1+\sqrt{17})/2\approx 2.56$，$K\approx 2.56/6.56\approx 0.39$。  
> 与推导篇瞬态比较：第 1 步 $K\approx0.71$，第 2 步 $\approx0.49$，继续会趋向 $\approx0.39$。

---

## 5. 与 Wiener 滤波器

稳态 KF 实现的从 $y$ 到 $\hat x$（或到 $\hat y$）的 LTI 映射，即该状态空间模型下的因果 Wiener 解。时变 / 有限时间必须用完整递推 $P_k$；只有长期运行且模型时不变才宜锁死 $K_\infty$。

---

## 6. 稳定性直觉

- **滤波器误差动力学**由 $(I-KH)F$ 等闭环矩阵决定；可检 + 可稳 ⇒ 稳态滤波误差渐稳。
- $Q=0$ 且模型完美时，$P$ 可趋于 0（确定性观测器极限）；但真实总有模型错，$Q=0$ 危险（增益熄灭）。

> [!warning] 过早使用稳态增益
> 开机初值 $P_0$ 很大时，前几步应用时变 $K_k$ 快速吸入信息；直接用 $K_\infty$ 会在瞬态低估增益、收敛变慢。嵌入式可：前 $N$ 步时变，之后切稳态。

---

## 7. 对偶性（一句话）

KF 与 LQR 控制在数学上对偶：Riccati 方程一对；把 $(F,H,Q,R)$ 与控制里 $(F,B,Q_{\mathrm{cost}},R_{\mathrm{cost}})$ 对照。16.322 把估计与随机控制放在一起讲，即此。

---

## 8. 带宽与噪声增益直觉

稳态下把 $\hat x$ 对 $y$ 的传递看作 LTI：增大 $Q/R$ 比通常加宽“信任测量”的带宽，跟踪更快、测量噪声透传更多；减小则更平滑、滞后更大。这与调 PID 截止频率的工程感觉同构，但有最优性与 $P_\infty$ 解释。

多维时看 $P_\infty$ 对角线：某状态若测量信息弱，稳态方差由 $Q$ 与弱可观性共同决定，不能指望“多跑一会儿就准”。

---

## 9. 时变增益的价值

即使存在 $K_\infty$，在下列情况保留时变 $K_k$ 更好：

- 开机 / 重捕获，$P_0$ 大；
- 间歇测量（有时无 $y$，只预测）；
- $R_k$ 随信噪比变化（雷达距离、视觉光照）。

无测量步：跳过更新，$P$ 仅按 $FPF^\mathsf{T}+Q$ 涨——这是“只靠模型漂”的不确定度诚实增长。

---

## 10. 自检与参考答案

1. 模型匹配时新息应满足哪三条二阶性质？
2. 写出标量随机游走的稳态 $p$ 与 $K$（用 $q,r$）。
3. 可稳 / 可检条件为何出现在稳态收敛定理里？
4. 稳态 KF 与 Wiener 的关系？
5. $Q\to 0$ 时稳态增益如何变？风险是什么？
6. 为何间歇测量时不宜锁死 $K_\infty$ 还假装每步都更新？

> [!success]- 参考答案
> 1. 零均值；时空白；协方差等于 $S_k$。
> 2. $p=(q+\sqrt{q^2+4qr})/2$，$K=p/(p+r)$。
> 3. 保证 Riccati 迭代收敛到唯一正定解且滤波误差稳定。
> 4. 同一 LMMSE 问题的两种实现；稳态 KF = 该模型的因果 Wiener。
> 5. $K$ 变小，更信模型；若模型有未建模误差，估计会偏且难被测量纠正。
> 6. 无测量时应只预测并增大 $P$；仍用固定更新会引入虚假信息、破坏一致性。

## 参考

- NPTEL 108105059 L20–L21
- Anderson & Moore，《Optimal Filtering》
- MIT 16.322：Riccati 与估计–控制对偶
