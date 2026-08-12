---
aliases:
  - 非线性滤波 EKF
  - EKF
  - UKF
  - 粒子滤波
  - Extended Kalman Filter
tags: [ee, estimation_kalman]
up: "[[Estimation and Kalman Filtering (NPTEL) MOC]]"
related:
  - "[[Kalman Filter Derivation]]"
  - "[[Kalman Filter Applications]]"
  - "[[State Estimation Problem]]"
  - "[[Signals Systems and Inference (MIT 6.011) MOC]]"
  - "[[Bayesian Inference]]"
down:
  - "[[System Identification and Recursive Least Squares]]"
---
# 非线性滤波：EKF 及其后

> [!summary] 核心结论
> 真实系统常是 $x_{k+1}=f(x_k,u_k)+w_k$，$y_k=h(x_k)+v_k$。**EKF** 在当前估计处线性化，借用 KF 公式，便宜但可能发散。**UKF** 用 sigma 点传播均值方差，免显式 Jacobian，对强非线性常更稳。**粒子滤波**用样本逼近整后验，非高斯多峰时有优势、算量大。本笔记以 NPTEL 线性主线为骨，辅读 16.322 / Siena SEF 的非线性部分。

> 关键词：Jacobian、线性化、sigma 点、重要性采样、发散

---

## 1. 非线性问题在哪里破功？

KF 的预测 / 更新依赖**线性**把高斯映成高斯。非线性 $f,h$ 使分布扭曲：均值不再简单 $f(\hat x)$，协方差不能只用 $FPF^\mathsf{T}$。必须近似。

![[ekf-nonlinear.svg]]

---

## 2. EKF：扩展卡尔曼滤波

在 $\hat x_{k\mid k}$ 处：
$$
F_k=\frac{\partial f}{\partial x}\Big|_{\hat x_{k\mid k}},\qquad
H_k=\frac{\partial h}{\partial x}\Big|_{\hat x_{k\mid k-1}}.
$$
**预测**：$\hat x^-=f(\hat x,u)$（用非线性 $f$），$P^-=F P F^\mathsf{T}+Q$。  
**更新**：$\nu=y-h(\hat x^-)$（用非线性 $h$），$K,P$ 用线性化 $H$ 套 KF。

> [!example] 标量非线性测量
> 状态随机游走 $x_k=x_{k-1}+w$，$q=0.1$。测量 $y=\arctan(x)+v$，$r=0.05$。  
> 设 $\hat x^-=1.0$，$P^-=0.2$，$y=0.70$。  
> $h(\hat x^-)=\arctan(1)\approx0.785$，$\nu=0.70-0.785=-0.085$。  
> $H=\partial\arctan/\partial x=1/(1+x^2)=0.5$。  
> $S=H^2 P^-+R=0.25\cdot 0.2+0.05=0.10$，$K=(P^- H)/S=0.1/0.10=1.0$。  
> $\hat x=1.0+1.0\cdot(-0.085)=0.915$，$P=(1-KH)P^-=(1-0.5)\cdot 0.2=0.1$。  
> 注意：$K=1$ 是状态对“线性化测量”的增益，不表示直接信 $y$ 的数值单位。

---

## 3. EKF 失效模式

> [!warning] EKF 发散
> - 线性化点远离真值（初值差、强非线性）→ $H$/$F$ 错误 → 更新往错方向拉。  
> - $P$ 过度自信（$Q$ 过小）→ 增益过小，无法纠正。  
> - 多峰后验（模糊数据关联）→ 单高斯代表不了。  
> 缓解：更好初值、增大 $Q$、二阶 EKF、改 UKF/粒子、多假设。
>
> 经验规则：若蒙特卡洛均方误差长期大于 $P$ 的迹，先别加复杂控制，先修滤波器一致性。

---

## 4. UKF：无迹卡尔曼滤波（Siena / 现代辅读）

选取 $2n+1$ 个 **sigma 点** 捕捉均值与协方差，经真实 $f$ / $h$ 传播，再用加权样本均值方差，最后仍用线性更新结构（或等价统计线性化）。

相对 EKF：

- 无需解析 Jacobian（黑盒 $f,h$ 也可）；
- 对近似高斯的非线性，精度常达二阶量级；
- 参数（$\alpha,\beta,\kappa$）需按文献惯例设置；算量约几个 EKF。

UKF 不是“免建模”：错误的 $f,h$ 或过小的 $Q$ 同样会一致性失败。

---

## 5. 粒子滤波（极简）

用粒子 $\{x^{(i)},w^{(i)}\}$ 表示后验。预测：按 $f$ 传播粒子；更新：按似然 $p(y\mid x^{(i)})$ 重加权；必要时重采样。

擅长多峰、非高斯；维数高时粒子数爆炸。数据关联、SLAM 前端等常用。

---

## 6. 与贝叶斯滤波统一视角

一般递归贝叶斯滤波：预测用 Chapman–Kolmogorov，更新用 Bayes。KF/EKF/UKF/粒子是对这二步的不同近似。[[Bayesian Inference]] 的“先验 × 似然”在动态里变成每步重复。

连续时间非线性还有 Stratonovich / Itô 滤波方程（16.322 深度）；离散实现仍回到上述近似族。

---

## 7. 何时选谁（工程口诀）

| 情境 | 倾向 |
|------|------|
| 弱非线性、好初值、需极简 | EKF |
| 中等非线性、Jacobian 难写 | UKF |
| 多峰 / 强非高斯 | 粒子 / 多假设 |
| 可精确线性化或小角度 | 考虑 MEKF 等结构技巧 |

---

## 8. 姿态与流形提示

姿态（四元数 / SO(3)）上硬套欧拉角 EKF 易万向节死锁与协方差奇异。常见做法：误差状态 EKF（MEKF）——标称轨迹用非线性积分，KF 只估小误差再注入。这属于 16.322 / 导航课延伸，但解释了“为何无人机固件不直接把四元数当普通欧氏状态”。

---

## 9. 调试非线性滤波器

1. 先在弱噪声、好初值仿真看是否跟上；  
2. 对比 EKF 与数值差分 Jacobian 是否一致；  
3. 监控新息与 $P$：误差出带且 $P$ 很小 → 典型发散前兆；  
4. 临时加大 $Q$ 看是否“救得回来”；  
5. 仍失败则升 UKF 或改参数化 / 多模型。

> [!warning] 只盯点估计曲线
> 轨迹“看起来顺”但无一致性检验，可能在积累不可见偏差。非线性下更要看新息与蒙特卡洛误差相对 $\sqrt{P}$。

---

## 10. 自检与参考答案

1. EKF 哪一步用非线性 $f/h$，哪一步用 Jacobian？
2. 上例中若 $\hat x^-$ 错到 $3$（真值近 1），定性会发生什么？
3. UKF 相对 EKF 的两个主要卖点？
4. 粒子滤波最怕什么维数问题？
5. “发散”在 EKF 里通常指什么现象？
6. 为何姿态估计常用误差状态而非直接欧拉角？

> [!success]- 参考答案
> 1. 均值预测 / 新息用 $f,h$；传播 $P$ 与算 $K$ 用 $F,H$。
> 2. $H=1/(1+9)=0.1$ 过小，线性化差，新息与增益都失真，更新可能拉错并伴随错误的小 $P$。
> 3. 免解析 Jacobian；对非线性均值/方差传播通常更准。
> 4. 状态维升高，有效覆盖后验所需粒子数剧增（维数灾难）。
> 5. 估计误差变大甚至发散，而 $P$ 仍可能过小（过度自信），滤波器“自信地错”。
> 6. 欧拉奇异 / 约束流形；误差状态在切空间上更近线性，协方差定义干净。

## 参考

- MIT OCW 16.322：非线性估计讲次
- Siena / 各类 SEF 讲义：EKF·UKF 对比章节（辅读）
- Julier & Uhlmann，UKF 原始文献；Särkkä，《Bayesian Filtering and Smoothing》
