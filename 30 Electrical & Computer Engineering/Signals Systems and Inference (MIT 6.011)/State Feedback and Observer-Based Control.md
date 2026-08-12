---
aliases:
  - 状态反馈与观测器控制
  - State Feedback and Observer-Based Control
  - 极点配置
  - pole placement
  - separation principle
  - 分离原理
tags: [ee, signals_systems_inference]
up: "[[Signals Systems and Inference (MIT 6.011) MOC]]"
related:
  - "[[Observers for State Estimation]]"
  - "[[Stability Reachability and Observability]]"
  - "[[Feedback]]"
  - "[[Feedback Example - The Inverted Pendulum]]"
down:
  - "[[MMSE and LMMSE Estimation]]"
---
# 状态反馈与基于观测器的控制

> [!summary] 核心结论
> 全状态反馈 $u=-Kx+r$（$r$ 为参考相关项）把闭环矩阵变成 $A-BK$。若 $(A,B)$ **能达**，可任意配置 $A-BK$ 的极点（SISO 极点配置）。若只能测 $y$，用观测器 $\hat x$ 代替 $x$：$u=-K\hat x+\cdots$。**分离原理**：闭环特征值 = 状态反馈极点（$A-BK$ 的谱）∪ 观测器极点（$A-LC$ 的谱）——可分开设计 $K$ 与 $L$。这是确定性 LTI 输出反馈综合的主干；与经典 [[Feedback]] 的回路整形互补。

> 底本：MIT 6.011 OCW Spring 2018 — state feedback / observer-based control。

---
## 1. 状态反馈与闭环

植物 $\dot x=Ax+Bu$。取
$$
u=-Kx+v,
$$
其中 $v$ 为外部命令（可再经预滤波 / 积分器处理参考跟踪）。闭环
$$
\dot x=(A-BK)x+Bv.
$$
特征值由 $A-BK$ 决定。直觉：把「开环模态」搬到期望阻尼与带宽。

![[ssi-feedback.svg]]

能达 ⇔ 存在 $K$ 实现任意单变量特征多项式（多输入时尚有额外自由度，可用特征结构配置或 LQR）。

> [!warning] 不能达子系统搬不动
> 若某模态不能达，其开环特征值在任意 $K$ 下保持不变。不稳定不能达 ⇒ **无法**用状态反馈镇定。先做秩 / PBH 检验（见 [[Stability Reachability and Observability]]）。

---
## 2. 极点配置直觉（SISO）

目标特征多项式 $\alpha_d(s)=s^n+\alpha_{n-1}s^{n-1}+\cdots+\alpha_0$。在可控标准型下，$K$ 的元素几乎直接等于系数差；一般坐标用 Ackermann 公式
$$
K=e_n^\top\,\mathcal{C}^{-1}\,\alpha_d(A)
$$
（$e_n^\top=(0,\ldots,0,1)$，$\mathcal{C}$ 能控矩阵）或数值 `place`。工程上更常：

- 选主导极点对（$\zeta,\omega_n$）满足超调 / 调节时间；
- 其余极点推远（注意执行器饱和与噪声）；
- 或解 LQR：权衡状态偏离与控制能量，自动给出稳定 $K$（能达 + 合理权 ⇒ 稳定）。

> [!example] 二阶极点配置数值
> $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$（双积分器），$B=\begin{pmatrix}0\\1\end{pmatrix}$。开环双极点在 $0$。期望 $\omega_n=2$，$\zeta=0.7$ ⇒
> $$
> s^2+2\zeta\omega_n s+\omega_n^2=s^2+2.8s+4.
> $$
> 取 $K=\begin{pmatrix}k_1&k_2\end{pmatrix}$：
> $$
> A-BK=\begin{pmatrix}0&1\\-k_1&-k_2\end{pmatrix}.
> $$
> 特征多项式 $s^2+k_2 s+k_1$。故 $k_1=4$，$k_2=2.8$。单位阶跃（令 $v$ 经静态增益使稳态跟踪）：调节时间约 $t_s\sim 4/(\zeta\omega_n)\approx 2.9\,\mathrm{s}$ 量级。$\mathcal{C}=[B\ AB]=I$ 满秩，配置合法。

---
## 3. 参考跟踪与稳态

纯 $u=-Kx$ 把状态赶到 $0$（调节问题）。跟踪常值参考 $y\to r$ 时，常用：

- **静态预补偿**：$v=N r$，选 $N$ 使直流增益为 1（若可行）；
- **积分增广**：把 $\int(y-r)$ 扩进状态，再对增广系统做状态反馈——抗常值扰动，类似经典 PI。

存在右半平面零点或执行器饱和时，极限性能受制，不能只靠「把极点推远」。

---
## 4. 观测器基控制器与分离原理

实现：$u=-K\hat x+v$，其中 $\hat x$ 来自 Luenberger 观测器。增广状态 $(x,e)$ 或 $(x,\hat x)$ 的闭环矩阵在适当坐标下呈块三角，特征值集合为
$$
\sigma(A-BK)\ \cup\ \sigma(A-LC).
$$
因此：

1. 先当 $x$ 可测，设计 $K$ 满足控制规格；
2. 再单独设计 $L$ 使估计误差够快、够稳；
3. 合成时闭环极点自动是两堆的并——**分离**。

> [!warning] 分离 ≠ 时域响应完全解耦
> 极点集合可分开设计，但零点、暂态耦合、噪声到控制的通道仍纠缠。观测器太慢 ⇒ 控制「看到」滞后状态；太快 ⇒ 噪声打进执行器。分离给结构性保证，不替代整体仿真与鲁棒性检查。

经典输出反馈（传递函数补偿器）与「观测器 + 状态反馈」在 LTI 下可互译：补偿器阶次往往等于植物阶次（全阶观测器情形）。

---
## 5. 与经典反馈的对照

| 视角 | 工具 | 强项 |
|---|---|---|
| 频率域回路整形 | $L(j\omega)$、增益/相位裕度 | 噪声、未建模动态、SISO 直觉 |
| 状态空间 | $K,L$、极点、LQR | MIMO、时域规格、估计一体 |

倒立摆等不稳定对象：状态反馈（或高阶补偿）提供镇定；见 [[Feedback Example - The Inverted Pendulum]]。6.011 强调状态空间综合骨架；经典 Bode 工具仍在 [[Feedback]]。

---
## 6. 离散时间摘要

$u[k]=-Kx[k]+v[k]$ ⇒ $A-BK$ 的特征值须在单位圆内。观测器基同样分离。数字控制还须考虑采样、计算时延（可扩状态或 Smith 类补偿）——本课点到为止。

---
## 7. 设计流程（工科清单）

1. 建模 / 线性化 → $(A,B,C,D)$。
2. 检验能达、能观（或能稳、能检测）。
3. 定控制极点或 LQR 权 → $K$。
4. 定观测器极点或 Kalman → $L$。
5. 加参考 / 积分结构；仿真噪声与饱和。
6. 必要时回到频率域检查灵敏度与裕度。

---
## 8. LQR 一瞥（与极点配置并列）

二次代价 $\int(x^\top Qx+u^\top Ru)\,dt$（或 DT 求和）在能稳与标准条件下给出唯一最优 $u=-K_{\mathrm{lqr}}x$，$K_{\mathrm{lqr}}$ 由代数 Riccati 解出。不必手挑极点，但 $Q,R$ 仍体现规格：加大 $Q$ 相对 $R$ ⇒ 更「拼命」控状态、控制能量更大、闭环通常更快。多输入时 LQR 自动用掉额外自由度。与经典回路整形对照：LQR 保证名义稳定与一定增益裕度直觉，但对未建模高频动态仍需滚降与鲁棒检查。

---
## 9. 自检与参考答案

1. 状态反馈如何改变闭环矩阵？前提是什么？
2. 叙述分离原理（极点集合）。
3. 为何观测器极点常选得比控制极点快，但又不能过快？
4. 不能达时极点配置会怎样？
5. 跟踪常值参考的两种常用手法？

> [!success]- 参考答案
> 1. $A\mapsto A-BK$；需要 $(A,B)$ 能达（或至少能稳）才能把不稳定模态搬走。
> 2. 观测器基状态反馈闭环谱 $=\sigma(A-BK)\cup\sigma(A-LC)$，可分设 $K,L$。
> 3. 更快使 $\hat x$ 跟上，控制更接近全状态反馈；过快放大噪声、激执行器。
> 4. 不能达特征值对 $K$ 不变；若不稳定则无法镇定。
> 5. 静态预增益 $N$；或积分增广再反馈。

---
## 附录补充：执行器饱和与 windup

状态反馈假设 $u=-Kx$ 可任意大。饱和时等效增益下降，极点「往回走」，不稳定植物可能再次失控。积分增广时饱和还会引起 **integrator windup**：误差持续积分、退出饱和后大超调。对策：反计算饱和、条件积分、或在 LQR 权里加重 $R$ 以减小名义 $|u|$。仿真必须加饱和模型，否则「完美极点」只是纸面结果。

## 参考

- Verghese & Oppenheim, *Signals, Systems and Inference*, MIT 6.011 OCW Spring 2018
- https://ocw.mit.edu/courses/6-011-signals-systems-and-inference-spring-2018/
- [[Observers for State Estimation]]、[[Feedback]]
