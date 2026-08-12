---
aliases:
  - 卡尔曼滤波推导
  - Kalman Filter Derivation
  - KF 预测更新
  - 卡尔曼增益
tags: [ee, estimation_kalman]
up: "[[Estimation and Kalman Filtering (NPTEL) MOC]]"
related:
  - "[[State Estimation Problem]]"
  - "[[Kalman Filter Properties and Steady State]]"
  - "[[Linear MMSE and Innovations]]"
  - "[[Bayesian Inference]]"
  - "[[Signals Systems and Inference (MIT 6.011) MOC]]"
down:
  - "[[Kalman Filter Properties and Steady State]]"
---
# 卡尔曼滤波推导

> [!summary] 核心结论
> 线性–高斯（或线性 + 二阶）模型下，Kalman filter 在**预测**与**更新**两步之间循环：用动力学推 $\hat x^-$、$P^-$；用新息 $\nu=y-H\hat x^-$ 与增益 $K=P^-H^\mathsf{T}(HP^-H^\mathsf{T}+R)^{-1}$ 修正得 $\hat x$、$P$。正交原理保证线性 MMSE；高斯时即贝叶斯后验均值 / 协方差。标量数值走查应能手算一遍。

> 底本：NPTEL 108105059 L18–L19。

> 关键词：预测、更新、Kalman 增益、新息、Joseph 形式

---

## 1. 模型回顾

$$
x_{k}=F_{k-1}x_{k-1}+w_{k-1},\qquad
y_k=H_k x_k+v_k,
$$
（略写控制项；$w,v$ 零均值、协方差 $Q_{k-1},R_k$，白且互不相关。）已知 $\hat x_{k-1\mid k-1}$、$P_{k-1\mid k-1}$。

![[ekf-kf-cycle.svg]]

---

## 2. 预测（时间更新）

$$
\begin{aligned}
\hat x_{k\mid k-1}&=F_{k-1}\hat x_{k-1\mid k-1},\\
P_{k\mid k-1}&=F_{k-1}P_{k-1\mid k-1}F_{k-1}^\mathsf{T}+Q_{k-1}.
\end{aligned}
$$
均值按标称动力学走；协方差先按 $F$ 传播，再加过程噪声 $Q$。

---

## 3. 更新（测量更新）

新息与新息协方差：
$$
\nu_k=y_k-H_k\hat x_{k\mid k-1},\qquad
S_k=H_k P_{k\mid k-1}H_k^\mathsf{T}+R_k.
$$

![[ekf-innovation.svg]]

Kalman 增益与后验：
$$
\begin{aligned}
K_k&=P_{k\mid k-1}H_k^\mathsf{T}S_k^{-1},\\
\hat x_{k\mid k}&=\hat x_{k\mid k-1}+K_k\nu_k,\\
P_{k\mid k}&=(I-K_k H_k)P_{k\mid k-1}.
\end{aligned}
$$

![[ekf-gaussian-update.svg]]

推导素描：在 $\hat x=\hat x^-+K(y-H\hat x^-)$ 类中选 $K$ 使 $P=\mathbb{E}[\tilde x\tilde x^\mathsf{T}]$ 最小 → 对 $K$ 求导得上式（正交：后验误差 ⊥ 新息）。

---

## 4. 标量完整数值例

> [!example] 一维随机游走 + 标量测量
> 模型：$x_k=x_{k-1}+w_{k-1}$，$y_k=x_k+v_k$，$Q=1$，$R=4$。  
> 初值：$\hat x_{0\mid 0}=0$，$P_{0\mid 0}=9$。观测到 $y_1=5$。
>
> **预测**（$k=1$）：
> $$
> \hat x_{1\mid 0}=0,\qquad P_{1\mid 0}=9+1=10.
> $$
> **增益与更新**：
> $$
> K_1=\frac{10}{10+4}=\frac{10}{14}\approx 0.714,\qquad
> \nu_1=5-0=5,
> $$
> $$
> \hat x_{1\mid 1}=0+0.714\cdot 5\approx 3.57,\qquad
> P_{1\mid 1}=(1-0.714)\cdot 10\approx 2.86.
> $$
> 解释：先验很不确定（$P^-=10$），测量噪声方差 4，故较信测量，估计从 0 拉向 5，停在 $\approx 3.57$；后验方差大幅下降。
>
> 再设 $y_2=4$。预测：$P_{2\mid 0}=2.86+1=3.86$，$\hat x_{2\mid 0}\approx 3.57$。  
> $K_2=3.86/(3.86+4)\approx 0.491$，$\nu_2=4-3.57=0.43$，  
> $\hat x_{2\mid 2}\approx 3.57+0.491\cdot 0.43\approx 3.78$，$P_{2\mid 2}\approx(1-0.491)\cdot 3.86\approx 1.96$。  
> 增益下降：已较确信，新测量修正变小。

---

## 5. 向量形式要点

$S_k$ 维数 = 测量维 $m$；求逆在 $m\times m$ 上，故传感器不多时 KF 便宜。$K$ 为 $n\times m$：$P^-H^\mathsf{T}$ 把状态不确定度映到测量空间，再按 $S^{-1}$ 加权。

多传感器可堆叠 $H,R$ 一次更新，或序贯更新（$R$ 块对角时等价）。

---

## 6. 协方差更新的数值形式

简式 $P\leftarrow(I-KH)P^-$ 在有限精度下可能丢失对称正定。**Joseph 形式**（可选记忆）：
$$
P\leftarrow(I-KH)P^-(I-KH)^\mathsf{T}+KRK^\mathsf{T}
$$
理论上与最优 $K$ 等价，数值上更保正定。方根滤波器 / UD 分解是进一步工程化。

> [!warning] 实现陷阱
> - $R$ 奇异或近奇异 → $S$ 病态；检查传感器是否冗余未建模相关。  
> - 漏加 $Q$ → $P$ 塌缩、$K\to 0$，滤波器“睡着”。  
> - 用错离散化（连续 $Q_c$ 未积到离散 $Q$）→ 整条不确定度时间尺度错误。

---

## 7. 与贝叶斯一步更新

线性高斯：预测是先验 $\mathcal{N}(\hat x^-,P^-)$；似然 $\mathcal{N}(y;Hx,R)$；后验恰为 $\mathcal{N}(\hat x,P)$。KF 是 [[Bayesian Inference|贝叶斯更新]] 的闭环实现，不必每次算归一化积分。

---

## 8. 信息滤波器一瞥

对 $P^{-1}$（信息矩阵）与 $P^{-1}\hat x$ 递推，在 $R$ 大、$Q$ 导致 $P^-$ 大或无测量步时有时更稳；与标准 KF 代数等价。了解存在即可。

---

## 9. 控制输入与缺测

有已知 $u_{k-1}$ 时预测改为 $\hat x^-=F\hat x+Gu$。某步无测量：跳过更新，只预测并输出 $\hat x^-$、$P^-$。多速率融合由此自然出现（[[Kalman Filter Applications]]）。

> [!example] 改变 $Q$ 的对比（接 §4）
> 同 §4 设定但 $Q=4$，$P_0=9$，$y_1=5$。  
> $P^-=13$，$K=13/(13+4)=13/17\approx0.765$，  
> $\hat x\approx 3.82$，$P\approx 3.06$。  
> 相对 $Q=1$ 时的 $\hat x\approx 3.57$：更大过程噪声 → 更不信预测、更跟测量。

---

## 10. 自检与参考答案

1. 默写预测与更新五式（含 $K,S$）。
2. 重做标量例：若 $R=1$ 而非 4，$K_1$ 与 $\hat x_{1\mid 1}$ 如何变？
3. 新息 $\nu$ 在最优滤波器下应近似有何二阶性质？
4. 为何 Joseph 形式值得在嵌入式实现里考虑？
5. $P_{k\mid k}=(I-KH)P^-$ 在 $K$ 非最优时是否仍正确？
6. 无测量的一步应如何处理 $P$？

> [!success]- 参考答案
> 1. 见 §2–§3。
> 2. $K_1=10/(10+1)=10/11\approx0.909$，$\hat x\approx 4.55$——更信测量，更靠近 $y=5$，$P$ 更小。
> 3. 零均值、白（互不相关）、协方差为 $S_k$（一致性时）。
> 4. 简式在有限精度下可能非对称 / 负特征值；Joseph 二次型结构更稳。
> 5. 简式对任意 $K$ 一般**不**给出真误差协方差；Joseph 对任意 $K$ 仍给出正确 $P$（线性模型下），故次优增益分析常用 Joseph。
> 6. 只做预测：$P\leftarrow FPF^\mathsf{T}+Q$，不减“测量信息”。

## 参考

- NPTEL 108105059 L18–L19
- Kalman (1960), A New Approach to Linear Filtering and Prediction Problems
- Simon，《Optimal State Estimation》
