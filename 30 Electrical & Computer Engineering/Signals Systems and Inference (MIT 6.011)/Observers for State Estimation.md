---
aliases:
  - 状态观测器
  - Observers for State Estimation
  - Luenberger observer
  - 龙伯格观测器
  - state observer
tags: [ee, signals_systems_inference]
up: "[[Signals Systems and Inference (MIT 6.011) MOC]]"
related:
  - "[[Stability Reachability and Observability]]"
  - "[[State Feedback and Observer-Based Control]]"
  - "[[MMSE and LMMSE Estimation]]"
  - "[[Estimation and Kalman Filtering (NPTEL) MOC]]"
down:
  - "[[State Feedback and Observer-Based Control]]"
---
# 状态观测器：用输出重建状态

> [!summary] 核心结论
> 全状态反馈需要 $x$，但常只能测 $y$。**Luenberger 观测器**复制植物模型并用输出误差校正：
> $$
> \dot{\hat x}=A\hat x+Bu+L\bigl(y-C\hat x-Du\bigr).
> $$
> 误差 $e=x-\hat x$ 满足 $\dot e=(A-LC)e$。若 $(A,C)$ **能观**，可选 $L$ 使 $A-LC$ 稳定（且足够快），则 $\hat x\to x$。离散同理：$e^+ =(A-LC)e$。确定性观测器是 Kalman 滤波在「无噪声模型完美」时的骨架；有噪声时最优 $L$ 由协方差权衡（见估计课）。

> 底本：MIT 6.011 OCW Spring 2018 — observers；前置 [[Stability Reachability and Observability]]。

---
## 1. 问题设定

植物：$\dot x=Ax+Bu$，$y=Cx+Du$（常取 $D=0$ 简化）。已知 $u(t)$、$y(t)$，要在线产生 $\hat x(t)\approx x(t)$。

开环「平行模型」$\dot{\hat x}=A\hat x+Bu$ 仅当 $A$ 稳定且 $\hat x(0)=x(0)$ 才可靠——初始误差不校正、模型误差会累积。必须用**测量残差** $y-\hat y$ 反馈。

![[ssi-observer.svg]]

---
## 2. Luenberger 观测器动力学

取 $\hat y=C\hat x+Du$，注入增益 $L$（$n\times p$）：
$$
\dot{\hat x}=A\hat x+Bu+L(y-\hat y)= (A-LC)\hat x+Bu+Ly-LDu.
$$
与植物相减（$D$ 一致时）：
$$
\dot e=\dot x-\dot{\hat x}=Ax+Bu-\bigl(A\hat x+Bu+L(y-\hat y)\bigr)=(A-LC)e.
$$
因此**误差完全由 $A-LC$ 决定**，与 $u$ 无关（模型匹配时）。设计目标：把 $A-LC$ 的极点放到左半平面（且通常比植物开环极点更快，使估计迅速跟上）。

---
## 3. 增益 $L$ 与能观性

配置 $A-LC$ 的特征值 ⇔ 配置 $(A^\top-C^\top L^\top)$ 的特征值，对偶于状态反馈中配置 $A-BK$。

- **能观** ⇒ 存在 $L$ 任意配置 $A-LC$ 的极点（单输出时类似 Ackermann / 标准型公式）。
- **不能观** ⇒ 不能观特征值对 $L$ 不变；若它们已不稳定，则**不存在**渐近观测器。

> [!warning] 观测器极点不是越快越好
> 极大 $L$ 使误差模态很快，但对测量噪声极度敏感（高增益放大噪声），并加剧对模型误差的脆弱性。工程上在「收敛速度」与「噪声灵敏度」间折中——随机情形下 Kalman 增益正是该折中的最优解。

---
## 4. 离散时间观测器

$$
\hat x[k+1]=A\hat x[k]+Bu[k]+L\bigl(y[k]-C\hat x[k]-Du[k]\bigr),
$$
$$
e[k+1]=(A-LC)e[k].
$$
要求 $A-LC$ 的特征值在单位圆内。预测–校正叙述：先用模型预测一步，再用残差校正——与 Kalman 滤波的时间更新 / 测量更新同构（噪声协方差进入 $L$ 的公式时即 Kalman）。

> [!example] 标量植物上的观测器
> $\dot x=-0.5\,x+u$，$y=x$（$A=-0.5,\ C=1,\ B=1$）。观测器：
> $$
> \dot{\hat x}=-0.5\,\hat x+u+L(y-\hat x)=( -0.5-L)\hat x+u+Ly.
> $$
> 误差极点 $\lambda=-0.5-L$。若希望误差时间常数约 $0.2$（$\lambda=-5$），取 $L=4.5$。则
> $$
> e(t)=e(0)\,e^{-5t}.
> $$
> 若 $e(0)=1$，在 $t=0.5$ 时 $e\approx e^{-2.5}\approx 0.082$。注意：$L=4.5$ 已把测量噪声以增益量级注入 $\dot{\hat x}$；若 $y=x+v$，$v$ 为传感器噪声，实际误差方程变为 $\dot e=(A-LC)e-Lv$。

---
## 5. 降维观测器（直觉）

若 $y$ 已直接给出部分状态（例如 $C=[I\ 0]$ 分块），只需估计互补子状态，可得**降维（reduced-order）观测器**，阶次低于 $n$。6.011 强调全阶 Luenberger 结构与误差动力学；降维是实现层面的优化。关键仍是：能观性（或能检测性）保证可把误差极点放稳。

**能检测（detectability）**：不能观模态本身已渐近稳定——则仍可设计渐近观测器（不能观方向靠自身衰减）。比能观弱，常作为「存在稳定观测器」的充要条件。

---
## 6. 与估计理论的接口

| 设定 | 增益来源 |
|---|---|
| 确定性、模型精确 | 极点配置选 $L$（Luenberger） |
| 过程 / 测量噪声、已知协方差 | Kalman 滤波（时变或稳态 $L$） |
| 仅二阶统计、线性约束 | LMMSE / Wiener（输入–输出形式） |

确定性观测器回答「结构与可配置性」；[[MMSE and LMMSE Estimation]] 与 [[Wiener Filtering]] 回答「统计最优」；[[Estimation and Kalman Filtering (NPTEL) MOC]] 把状态空间 + 噪声推到递归最优估计。

---
## 7. 实现检查清单

1. 验证 $(A,C)$ 能观或至少能检测。
2. 选误差极点（比闭环控制极点略快是常见启发式，非定理）。
3. 算 $L$（Ackermann、place、LQR 对偶等）。
4. 仿真：初始误差衰减、噪声敏感性、模型失配。
5. 与状态反馈组合时用分离原理（下一篇）。

---
## 8. 模型误差与「观测器–控制器」互动

真实植物若是 $A+\Delta A$，观测器仍用名义 $A$，则误差方程不再是干净的 $(A-LC)e$，而会耦合真实 $x$ 与 $\hat x$。高增益 $L$ 可能放大这种失配。实务上：在预期参数摄动下做蒙特卡洛 / 最坏情形仿真；或改用包含积分作用、LMI 鲁棒观测器、或直接上 Kalman + 过程噪声「覆盖」未建模动态。分离原理保证的是**名义模型**上的极点集合，不是任意摄动下的鲁棒裕度。

---
## 9. 自检与参考答案

1. 写出连续 Luenberger 方程与误差动力学。
2. 为何需要 $(A,C)$ 能观（或能检测）？
3. 高增益 $L$ 的主要代价是什么？
4. 离散观测器误差如何演化？稳定条件？
5. Luenberger 与 Kalman 的概念关系？

> [!success]- 参考答案
> 1. $\dot{\hat x}=A\hat x+Bu+L(y-C\hat x-Du)$；$\dot e=(A-LC)e$。
> 2. 能观 ⇒ 可任意配置 $A-LC$ 极点；能检测 ⇒ 至少可稳定误差。不能观且不稳定 ⇒ 无法渐近估计。
> 3. 放大测量噪声、对模型误差更敏感、执行时增益过大。
> 4. $e^+=(A-LC)e$；需 $\lvert\lambda(A-LC)\rvert<1$。
> 5. Kalman 是噪声模型下的最优（时变）观测器；无噪声极限 / 结构上与 Luenberger 同类。

---
## 附录补充：连续与离散极点对应

若连续误差极点希望在 $-\alpha$（实），采样周期 $T_s$ 下离散极点约 $e^{-\alpha T_s}$。例：$\alpha=5$，$T_s=0.02$ ⇒ $e^{-0.1}\approx 0.90$。设计时可在 DT 直接 place，或先 CT 再离散化观测器方程。务必保证采样够快相对误差带宽，否则离散化失真、噪声折叠进基带。

---
## 10. 多输出与方向性

$y\in\mathbb{R}^p$，$L$ 为 $n\times p$。多传感器提供更多方向约束，能观性矩阵行数增加，PBH 更容易满秩。若两传感器噪声相关或共线（$C$ 行近似平行），有效信息仍接近单通道——设计 $L$ 时应结合噪声协方差（Kalman）或相对标定。输出加权（先把 $y$ 乘白化矩阵）可改善数值。

> [!example] 不能观时的失败模式
> $A=\mathrm{diag}(-1,2)$，$C=[1\ 0]$：稳定模态能观，不稳定模态不能观。任意 $L=[l_1;l_2]$，$A-LC$ 仍保留特征值 $2$（PBH）。观测器误差中沿第二基向的分量 $\sim e^{2t}$ 发散——再快的 $l_1$ 也救不了。必须改测点或改模型。

分离设计时，把观测器带宽设为控制带宽的 $2$–$5$ 倍是教科书启发式；最终仍以噪声谱与执行器限制为准绳，而不是固定倍数神话。

## 参考

- Verghese & Oppenheim, *Signals, Systems and Inference*, MIT 6.011 OCW Spring 2018
- https://ocw.mit.edu/courses/6-011-signals-systems-and-inference-spring-2018/
- [[Stability Reachability and Observability]]、[[State Feedback and Observer-Based Control]]
