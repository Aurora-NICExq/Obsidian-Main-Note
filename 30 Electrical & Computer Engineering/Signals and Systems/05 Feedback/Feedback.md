---
title: "Feedback"
aliases:
  - "反馈"
  - "负反馈"
  - "环路增益"
  - "灵敏度"
  - "相位裕度"
tags: [signals_and_systems, ee, feedback, control]
up: "[[Signals and Systems MOC]]"
related:
  - "[[The Laplace Transform]]"
  - "[[Continuous-Time Second-Order Systems]]"
  - "[[Feedback Example - The Inverted Pendulum]]"
  - "[[System Interconnection and Basic Properties]]"
---
# Feedback

> [!summary] 核心结论
> $$\frac{Y}{X}=\frac{G}{1+GH},\qquad T=GH\ (\text{环路增益})$$
> $|T|\gg1$ 时闭环 $\to 1/H$ —— **系统特性由反馈网络决定，与那个不精确的 $G$ 无关**。灵敏度、失真、阻抗、带宽全都被同一个因子 $1/(1+T)$ 改善。
> 代价只有一个但很致命：**稳定性**。若某频率处环路相移到 $-180°$ 而 $|T|$ 仍 $>1$，负反馈变正反馈，系统起振。相位裕度、增益裕度、频率补偿全是为这件事发明的。

依据：奥本海姆 MIT OCW RES.6-007 [Lecture 25](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/lecture-25-feedback/)；教材 §11。

前置：[[The Laplace Transform]]、[[System Interconnection and Basic Properties]]。

---

## 1. 闭环公式

![[ss-feedback-01.svg]]

从图上直接读：$e=x-Hy$，$y=Ge$，消去 $e$：

$$
\boxed{\;\frac{Y}{X}=\frac{G}{1+GH}\;}
$$

- $G$ —— **前向通路增益**（那个大而不精确的东西：运放、功放、电机）
- $H$ —— **反馈网络**（那个小而精确的东西：电阻分压、传感器）
- $T=GH$ —— **环路增益**，整个理论的主角

---

## 2. $|T|\gg1$ 时的四条推论

### (1) 闭环只由反馈网络决定

$$
\frac{Y}{X}=\frac{G}{1+GH}\approx\frac{G}{GH}=\frac{1}{H}
$$

$G$ 的具体值**完全不出现**。运放开环增益从 $10^5$ 变到 $10^6$（批次、温度），闭环增益纹丝不动 —— 因为它只由两个电阻的比值决定。

这是整个模拟电子学最重要的一条工程原理：**用一个不精确但很大的增益，换一个精确的传递函数。**

### (2) 灵敏度

定义闭环增益 $A=G/(1+GH)$ 对 $G$ 的相对灵敏度：

$$
S=\frac{dA/A}{dG/G}=\frac{1}{1+T}
$$

$T=1000$ 时，$G$ 漂移 $10\%$ 只让闭环漂 $0.01\%$。

### (3) 失真与噪声

$G$ 内部产生的失真（在前向通路中点注入的干扰）被同样的 $1/(1+T)$ 压低。

> [!warning] 但是：输入端的噪声压不掉
> 反馈只能压低**环路内部**产生的干扰。信号源本身和第一级输入端的噪声与信号一起被放大，反馈无能为力。
> 所以低噪声设计的重点永远在第一级，反馈救不了。

### (4) 阻抗与带宽

- 串联反馈提高输入阻抗，并联反馈降低；取样电压降低输出阻抗，取样电流提高 —— 都是 $(1+T)$ 倍。
- 单极点 $G$ 的带宽被展宽 $(1+T)$ 倍，而增益降低同样倍数 $\Rightarrow$ **增益带宽积不变**。这是运放数据手册上 GBW 这个参数的由来。

---

## 3. 极点被移动了

闭环极点是 $1+G(s)H(s)=0$ 的根，一般**不等于**开环极点。

这既是反馈的威力所在（能把不稳定的极点拉进左半平面，见 [[Feedback Example - The Inverted Pendulum]]），也是它的危险所在（能把稳定的极点推到右半平面）。

**根轨迹**就是画出 $T$ 从 0 增大到 $\infty$ 时闭环极点在 $s$ 平面上走的路径。两条端点性质：

- $T\to0$：闭环极点 $\to$ **开环极点**
- $T\to\infty$：闭环极点 $\to$ **开环零点**（或跑向无穷远）

---

## 4. 稳定性：反馈唯一的代价

$1+T(s)=0$ 若有右半平面的根，闭环就不稳定。

直觉版本：环路里的每一级都带延迟（极点），相位不断滞后。当某个频率上总相移达到 $-180°$ 时，「负」反馈的减号被抵消，变成了正反馈。若此时环路增益仍 $\ge1$，扰动就会自我放大 —— 起振。

**奈奎斯特判据**给出严格版本：画出 $T(j\omega)$ 在复平面上的轨迹，看它绕 $-1$ 点的圈数。

工程上更常用两个裕度：

| 裕度 | 定义 | 经验值 |
| ---- | ---- | ---- |
| **相位裕度** PM | $\lvert T\rvert=1$ 处，相位距 $-180°$ 还差多少 | $\ge45°$（$60°$ 更稳） |
| **增益裕度** GM | 相位 $=-180°$ 处，$\lvert T\rvert$ 距 1 还差多少 | $\ge6\,\mathrm{dB}$ |

相位裕度与闭环阻尼直接挂钩：$\mathrm{PM}\approx60°$ 大致对应 $\zeta\approx0.6$，超调约 $10\%$（见 [[Continuous-Time Second-Order Systems]]）。

> [!important] 补偿：故意让它变慢
> 三个极点以上的环路几乎必然在某个频率转过 $-180°$。**频率补偿**的做法是人为加一个主极点，让 $|T|$ 在相位转过来之前就先掉到 1 以下。
> 通用运放内部那个几十 pF 的补偿电容干的就是这件事 —— 用带宽换无条件稳定。

---

## 5. 正反馈也有用

$|1+T|<1$ 的频段上信号被放大而非压制。刻意用它可以做：

- **振荡器**：让 $T=1$ 恰在某一个频率成立（巴克豪森条件），系统在该频率持续振荡。
- **迟滞比较器**（施密特触发器）：正反馈制造两个阈值，抗噪声抖动。
- **锁存与存储**：交叉耦合的正反馈是 SRAM 和触发器的基础。

所以「正反馈 = 坏」是误解。区别只在于：你是不是故意的。

---

## 6. 速查

| 项目 | 内容 |
| ---- | ---- |
| 闭环 | $\dfrac{G}{1+GH}$ |
| 环路增益 | $T=GH$ |
| $\lvert T\rvert\gg1$ | 闭环 $\to 1/H$ |
| 灵敏度 | $1/(1+T)$ |
| 阻抗、失真、带宽 | 都改善 $(1+T)$ 倍 |
| 增益带宽积 | 不变 |
| 闭环极点 | $1+GH=0$ 的根 |
| 不稳定条件 | 某频率 $\angle T=-180°$ 且 $\lvert T\rvert\ge1$ |
| 相位裕度 | $\ge45°\sim60°$ |

---

## 参见

- [[Signals and Systems MOC]]
- [[The Laplace Transform]]（极点与稳定性）
- [[Continuous-Time Second-Order Systems]]（相位裕度与阻尼的对应）
- [[Feedback Example - The Inverted Pendulum]]（反馈让不稳定系统变稳定）
- [[System Interconnection and Basic Properties]]（反馈是第三种互联方式）
- [OCW Lecture 25 notes (PDF)](https://ocw.mit.edu/courses/res-6-007-signals-and-systems-spring-2011/resources/mitres_6_007s11_lec25/)
