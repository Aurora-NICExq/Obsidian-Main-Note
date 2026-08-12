---
aliases:
  - 维纳滤波
  - Wiener Filtering
  - Wiener filter
  - 因果维纳滤波
  - noncausal Wiener
tags: [ee, signals_systems_inference]
up: "[[Signals Systems and Inference (MIT 6.011) MOC]]"
related:
  - "[[MMSE and LMMSE Estimation]]"
  - "[[Power Spectral Density]]"
  - "[[Wide-Sense Stationary Processes]]"
  - "[[Matched Filtering]]"
  - "[[Estimation and Kalman Filtering (NPTEL) MOC]]"
down:
  - "[[Hypothesis Testing and Signal Detection]]"
---
# 维纳滤波：过程上的 LMMSE

> [!summary] 核心结论
> 在 WSS 设定下，用观测过程 $Y$ 的线性时不变滤波估计信号 $X$（滤波 / 平滑 / 预测），使误差功率最小，即过程版 **LMMSE**。**非因果** Wiener 滤波器在频域为
> $$
> H_{\mathrm{nc}}(j\omega)=\frac{S_{xy}(\omega)}{S_y(\omega)}
> $$
> （或信号在观测中为加性模型时的等价形式）。**因果**约束要求 $h(t)=0$（$t<0$），需对 $S_y$ 做谱因式分解后再投影——公式更繁，但直觉是「只用过去与现在的 $Y$」。非因果给性能上界；实时系统用因果（或有限延迟平滑）。Kalman 滤波是状态空间、可非平稳推广。

> 底本：MIT 6.011 OCW Spring 2018 — Wiener filtering；代数内核见 [[MMSE and LMMSE Estimation]]，谱语言见 [[Power Spectral Density]]。

---
## 1. 问题分类

| 类型 | 要估的时刻 vs 观测 | 典型用途 |
|---|---|---|
| 滤波 | $\hat X(t)$ 用到 $Y(s),\ s\le t$ | 实时去噪 |
| 平滑 | 用到未来观测（延迟） | 离线精炼 |
| 预测 | 估 $X(t+\Delta)$，$\Delta>0$ | 预报 |

线性 + 时不变 + WSS ⇒ 最优估计器是卷积：$\hat X=h*Y$。设计 $h$ 或 $H(j\omega)$。

![[ssi-wiener.svg]]

---
## 2. 正交原理（过程版）

误差 $E(t)=X(t)-\hat X(t)$ 必须与所有允许使用的观测线性组合正交。非因果（可用全部时间的 $Y$）时，对一切 $\tau$，
$$
\mathbb{E}\bigl[E(t)\,Y^*(t-\tau)\bigr]=0
\quad\Leftrightarrow\quad
R_{xy}(\tau)=R_{\hat x y}(\tau)=(h*R_y)(\tau).
$$
取 FT：
$$
S_{xy}(\omega)=H(j\omega)S_y(\omega)
\quad\Rightarrow\quad
H_{\mathrm{nc}}(j\omega)=\frac{S_{xy}(\omega)}{S_y(\omega)}.
$$
加性模型 $Y=X+W$，$X\perp W$ 时 $S_{xy}=S_x$，$S_y=S_x+S_w$，故
$$
H_{\mathrm{nc}}=\frac{S_x}{S_x+S_w}.
$$
这是「信噪比高的频带增益接近 1，噪声主导频带增益压低」的精确说法。

> [!example] 平坦信号谱 + 有色噪声（非因果）
> 设 $S_x(\omega)=1$（$|\omega|\le 10$，否则 0 的带限理想化简化为在带内常数），带内 $S_w(\omega)=0.25$，带外观测无信号。带内
> $$
> H_{\mathrm{nc}}=\frac{1}{1+0.25}=0.8.
> $$
> 误差 PSD $S_e=S_x\lvert 1-H\rvert^2+S_w\lvert H\rvert^2$（标准公式）在带内 $=1\cdot(0.2)^2+0.25\cdot(0.8)^2=0.04+0.16=0.20$。相对输入信号功率 1，MSE 功率密度 0.2——与标量 LMMSE 方差公式 $\sigma_x^2\sigma_w^2/(\sigma_x^2+\sigma_w^2)$ 同构：$1\cdot 0.25/1.25=0.2$。

---
## 3. 因果 Wiener：直觉与谱分解

约束 $h(t)=0$ for $t<0$。正交原理只对 $\tau\ge 0$ 的「过去观测」成立，导致 **Wiener–Hopf 积分方程**，一般不能在频域简单相除。

标准路线（标量）：

1. 对 $S_y(\omega)$ **谱因式分解** $S_y=S_y^+ S_y^-$（$S_y^+$ 及其逆在右半平面解析 ↔ 因果最小相位因子）。
2. 把 $S_{xy}/S_y^-$ 拆成因果与反因果部分。
3. 因果部分除以 $S_y^+$ 得 $H_{\mathrm{c}}$。

直觉：先把观测「白化」成因果白噪声，再对白化过程做因果投影，最后映射回去。细节代数冗长；6.011 要的是：**因果性改变公式，且性能 ≤ 非因果**。

> [!warning] 直接把 $S_x/(S_x+S_w)$ 当实时滤波器？
> 该式一般是**非因果**的（冲激响应双边）。若 $S_x,S_w$ 有理且你截断 $t<0$ 部分，得到的是次优。真要因果最优，走谱分解或改用 Kalman（因果递推实现）。

---
## 4. 有限冲激响应与离散 Wiener

DT 上同样：$H(e^{j\Omega})=S_{xy}/S_y$（非因果）。FIR 长度 $M$ 的因果近似 ⇒ 解有限 Toeplitz 法方程（Yule–Walker 型）——与 [[MMSE and LMMSE Estimation]] 向量公式同一回事。LMS / RLS 自适应滤波可视为未知统计时的在线近似。

---
## 5. 与匹配滤波、Kalman 的边界

- **匹配滤波**（[[Matched Filtering]]）：已知确定性信号波形 + 白噪声，最大化瞬时 SNR / 支撑检测——不是去估随机 WSS 信号的全程波形。可视为特定准则下的相关器。
- **Kalman**：状态空间、可处理瞬态与非平稳、自然因果；稳态 Kalman 增益对应某 Wiener 问题。见 [[Estimation and Kalman Filtering (NPTEL) MOC]]。
- **Wiener**：直接在相关 / PSD 域给 LTI 最优；适合平稳长期稳态。

---
## 6. 误差功率

非因果加性独立噪声情形，误差谱
$$
S_e=\frac{S_x S_w}{S_x+S_w},
$$
总 MSE $=\frac{1}{2\pi}\int S_e\,d\omega$。SNR 处处 ∞ ⇒ $S_e\to 0$；噪声压倒 ⇒ $H\to 0$，MSE → 信号功率（放弃估计）。

---
## 7. 设计清单

1. 确认 WSS + 二阶统计（或可估 $R$/$S$）。
2. 明确因果 / 非因果 / 允许延迟。
3. 非因果：算 $H=S_{xy}/S_y$；检查 $S_y>0$。
4. 因果：谱分解或状态空间 Kalman。
5. 用误差谱 / 仿真验证；注意模型失配。

---
## 8. 平滑（固定延迟）直觉

若允许延迟 $\Delta>0$，用到 $Y(t+\Delta)$ 估 $X(t)$，性能介于因果滤波与非因果之间：$\Delta$ 越大，越接近 $H_{\mathrm{nc}}$。实现上可把非因果 $h(t)$ 截断到 $[-\Delta,\infty)$ 再整体右移 $\Delta$ 成因果。录音去噪、图像（多维类比）常用「准非因果」；控制回路里延迟必须进稳定裕度账本。

---
## 9. 自检与参考答案

1. 写出非因果 Wiener 频域公式（一般与加性独立情形）。
2. 正交原理在过程滤波里如何表述？
3. 为何因果问题不能直接 $S_{xy}/S_y$？
4. 滤波 / 平滑 / 预测如何区分？
5. Wiener 与 Kalman 各适合什么设定？

> [!success]- 参考答案
> 1. $H=S_{xy}/S_y$；加性独立时 $H=S_x/(S_x+S_w)$。
> 2. 误差与所有允许的观测线性组合不相关；非因果 ⇒ 对一切 lag 的 $Y$ 正交。
> 3. 因果约束使 Wiener–Hopf 只在半轴成立，需谱分解，不能全局相除。
> 4. 滤波用到当前为止；平滑用未来；预测估未来信号。
> 5. Wiener：平稳、LTI、相关/PSD 已知；Kalman：状态空间、递归、可非平稳。

---
## 附录补充：多变量与对角化

向量 WSS 过程：$S_y(\omega)$ 为矩阵 PSD，$H_{\mathrm{nc}}(\omega)=S_{xy}(\omega)S_y(\omega)^{-1}$（在 $S_y\succ 0$ 频点）。传感器融合、多通道去噪用此式。若通道已被白化且互不相关，矩阵公式块对角化为多个标量 Wiener。数值上注意 $S_y$ 在某些频点接近奇异（强共线传感器）时需正则化——与 LMMSE 中 $R_Y^{-1}$ 病态同一问题。

---
## 10. 与确定性滤波的对照表

| | 经典频率整形 [[Filtering]] | Wiener |
|---|---|---|
| 输入模型 | 最坏 / 通带指标 | WSS 二阶统计 |
| 目标 | 通带平坦、阻带衰减 | 最小误差功率 |
| 典型输出 | 切比雪夫 / 巴特沃斯等 | $S_{xy}/S_y$ 或因果谱分解型 |
| 噪声 | 常当干扰指标 | 进入 $S_w$ 显式 |

当 $S_x$ 带限、$S_w$ 近似白时，非因果 Wiener 在信号通带接近全通、带外接近 0，外观像理想低通——但过渡带由 SNR 谱形状软决定，而非砖墙指标。

> [!example] 信噪比谱决定增益
> $S_x=4$，$S_w=1$ 的频带：$H=4/5=0.8$；另一频带 $S_x=0.25$，$S_w=1$：$H=0.2$。同一滤波器在不同频带「敢不敢信观测」不同——这是 Wiener 相对固定模拟滤波器的本质差异。

## 参考

- Verghese & Oppenheim, *Signals, Systems and Inference*, MIT 6.011 OCW Spring 2018
- https://ocw.mit.edu/courses/6-011-signals-systems-and-inference-spring-2018/
- [[MMSE and LMMSE Estimation]]、[[Power Spectral Density]]、[[Matched Filtering]]
