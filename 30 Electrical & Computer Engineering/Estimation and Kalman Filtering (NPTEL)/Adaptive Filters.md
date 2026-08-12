---
aliases:
  - 自适应滤波器
  - Adaptive Filters
  - LMS
  - RLS 自适应
  - 最小均方算法
tags: [ee, estimation_kalman]
up: "[[Estimation and Kalman Filtering (NPTEL) MOC]]"
related:
  - "[[Least Squares and Optimal Filters]]"
  - "[[System Identification and Recursive Least Squares]]"
  - "[[Linear MMSE and Innovations]]"
  - "[[Signals Systems and Inference (MIT 6.011) MOC]]"
down:
  - "[[State Estimation Problem]]"
---
# 自适应滤波器

> [!summary] 核心结论
> 当统计未知或缓变时，用数据**在线调整**滤波器权重。**LMS** 以瞬时误差梯度下降逼近 Wiener 解，实现极简；**RLS** 递推最小化加权 LS，收敛快、算量与数值更敏感。自适应滤波是“未知环境中的 LMMSE / LS”，与系统辨识、噪声消除、回声抵消同一套块图。

> 底本：NPTEL 108105059 L16。

> 关键词：LMS、NLMS、RLS、步长、误调、跟踪

---

## 1. 问题设定

输入 $u[n]$（向量形式常取抽头延迟线 $u[n],\ldots,u[n-M+1]$），期望响应 $d[n]$，横向滤波器权重 $w[n]$，误差
$$
e[n]=d[n]-w[n]^\mathsf{T}u[n].
$$
目标：使 $w$ 跟踪使 $\mathbb{E}[e^2]$ 最小的 Wiener 解 $w^*=R^{-1}p$（$R=\mathbb{E}[uu^\mathsf{T}]$，$p=\mathbb{E}[ud]$）。

![[ekf-adaptive.svg]]

---

## 2. LMS 算法

用瞬时量代替期望：$R\approx u u^\mathsf{T}$，$p\approx u d$，得随机梯度：
$$
w[n+1]=w[n]+\mu\,e[n]\,u[n].
$$
**步长** $\mu>0$：太大发散，太小收敛慢、跟踪迟钝。粗规则：$\mu$ 小于 $2/\lambda_{\max}(R)$ 量级（实际用更保守值或 NLMS）。

**NLMS**：$\mu$ 换成 $\tilde\mu/(\varepsilon+\lVert u\rVert^2)$，对输入功率归一化，更稳。

> [!example] 标量单抽头
> $w$ 标量，$u[n]=1$（直流偏置估计），$d[n]=a+v[n]$。LMS：$w\leftarrow w+\mu(d-w)$。期望迭代 $w\to a$（噪声驱动下在 $a$ 附近抖动）。$\mu$ 大则方差大——**误调（misadjustment）** 与 $\mu$ 正相关。

---

## 3. RLS 直觉

递推最小化
$$
J_n(w)=\sum_{i=1}^n \lambda^{n-i}\bigl(d[i]-w^\mathsf{T}u[i]\bigr)^2
$$
（$\lambda\in(0,1]$ 遗忘因子）。用矩阵求逆引理更新 $P_n\approx(\sum\lambda^{n-i}uu^\mathsf{T})^{-1}$ 与 $w_n$。相对 LMS：收敛快、对特征值散布更不敏感；复杂度 $O(M^2)$，需注意数值正定性（可用平方根 / UD 形式）。

与 [[System Identification and Recursive Least Squares|辨识用 RLS]] 同一算法；此处强调**滤波 / 抵消**应用叙事。

---

## 4. 典型应用块图

| 应用 | $u$ | $d$ | 输出用法 |
|------|-----|------|----------|
| 系统辨识 | 激励 | 未知系统输出 | $w\approx$ 冲激响应 |
| 逆模型 / 均衡 | 接收 | 训练序列 | $w\approx$ 逆信道 |
| 噪声消除 | 噪声参考 | 含噪主通道 | $e$ 为清洁信号 |
| 预测 | 过去样本 | 当前样本 | 预测误差白化 |

---

## 5. 与 Kalman 的关系（一瞥）

把权重当状态、随机游走过程噪声，可写 KF 估 $w$——某种意义下 RLS 是特定 $Q,R,\lambda$ 选择下的 KF。工程上 LMS/RLS 专用实现更轻；状态估计任务仍用标准 KF（[[Kalman Filter Derivation]]）。

代价面形状：二次 $J(w)$ 的 Hessian 即 $R$；LMS 沿随机梯度走，RLS 近似牛顿方向。条件数大时牛顿（RLS）优势最明显。

---

## 6. 收敛与跟踪权衡

- **平稳**：小 $\mu$ / $\lambda\to 1$ → 低误调、慢收敛。
- **时变**：需足够大 $\mu$ 或 $\lambda<1$ 以跟踪；必然抬高稳态抖动。

输入相关矩阵条件数差时，LMS 沿小特征值方向极慢——预白化或 RLS 可缓解。

---

## 7. 代价面与误调

Wiener 最优均方误差为 $J_{\min}$。自适应收敛后，权重在 $w^*$ 附近抖动，实际 $J(\infty)=J_{\min}(1+\mathcal{M})$，**误调** $\mathcal{M}$ 对 LMS 约与 $\mu\,\mathrm{tr}(R)$ 同阶。工程含义：要更低稳态误差就减小 $\mu$，并接受更长收敛；要快跟踪就容忍更大抖动。

RLS（$\lambda=1$）在平稳下误调可极低，但对时变仍需 $\lambda<1$，同样引入跟踪噪声。

---

## 8. 实现备忘

- 用 `float` 时 LMS 几乎无忧；RLS 的 $P$ 应用对称化或平方根形式防负特征值。
- 延迟线长度 $M$：太短欠建模，太长增条件数与算量。
- 有训练序列时用“学习–冻结–判决引导”切换（均衡器经典流程）。

> [!example] LMS 两抽头手算半步
> $w=[0,0]^\mathsf{T}$，$u=[1,0.5]^\mathsf{T}$，$d=1$，$\mu=0.2$。  
> $e=1-0=1$，$w\leftarrow [0,0]+0.2\cdot 1\cdot[1,0.5]=[0.2,0.1]$。  
> 下一步若 $u$ 再来，继续沿瞬时梯度爬——可见权重如何被数据“推”向相关方向。

---

## 9. 陷阱

> [!warning] 步长过大
> $\mu$ 超稳定界 → 权重爆炸。实现上对 $\mu$ 与 $\|u\|$ 做饱和 / 使用 NLMS。

> [!warning] 期望信号与输入相干不足
> 噪声消除里若参考通道与主通道噪声不相关，自适应“没事可学”，可能误伤信号。参考质量决定上限。

> [!warning] 信号泄漏进参考
> 若参考含有用信号分量，抵消器会把信号当“噪声”减掉 → 失真。声学回声消除里要用双端检测等逻辑。

---

## 10. 自检与参考答案

1. 写出 LMS 更新式；解释 $\mu$ 的两个极端。
2. NLMS 相对 LMS 的主要好处？
3. RLS 中遗忘因子 $\lambda$ 的作用？
4. 噪声消除块图里，为何常取误差 $e$ 为有用输出？
5. LMS 对 $R$ 特征值散布敏感的表现是什么？
6. 误调 $\mathcal{M}$ 与 $\mu$ 的定性关系？

> [!success]- 参考答案
> 1. $w\leftarrow w+\mu e u$；$\mu$ 过大发散，过小收敛/跟踪慢。
> 2. 按瞬时功率归一化，步长更稳、输入电平变化时少调参。
> 3. $\lambda<1$ 降低旧数据权重，使算法能跟踪时变；$\lambda=1$ 等价无限记忆 LS。
> 4. 滤波器估计的是噪声通路；主通道减估计噪声后残差近似为信号。
> 5. 小特征值方向收敛极慢，表现为部分抽头长期不到 Wiener 解。
> 6. $\mu$ 越大，稳态抖动越大，误调通常越高。

## 参考

- NPTEL 108105059 L16
- Haykin，《Adaptive Filter Theory》
- Widrow & Stearns，《Adaptive Signal Processing》
