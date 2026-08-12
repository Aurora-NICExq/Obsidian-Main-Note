---
title: "MOSFET Structure and Operation"
aliases: ["MOSFET 结构", "MOS 工作原理", "阈值电压", "沟道形成", "夹断"]
tags: [electronic_circuits, ee, mosfet]
up: "[[Electronic Circuits I MOC]]"
down: ["[[MOSFET Characteristics and Small-Signal Model]]"]
related: ["[[Bipolar Transistor Structure and Operation]]", "[[Caltech Analog Circuit Design-113N-MOSFET Subthreshold Behavior]]"]
---
# MOSFET Structure and Operation

## MOSFET（一）：结构、阈值电压与三个工作区

> [!summary] 核心结论
> MOS 是一个**电容控制的电阻**：栅极隔着氧化层在半导体表面感应出反型沟道，$V_{GS}$ 控制沟道里的电荷量，$V_{DS}$ 决定这些电荷怎么流。
> 三个区由两个不等式划分：$V_{GS}<V_{TH}$ 截止；$V_{DS}<V_{GS}-V_{TH}$ 三极管区（可变电阻）；$V_{DS}>V_{GS}-V_{TH}$ 饱和区（电流源，放大器用这个）。
> 与 BJT 最本质的差别：**栅极直流不吃电流**。

---
## 1. 结构

四个端子：栅（G）、源（S）、漏（D）、衬底（B）。

- 在 $p$ 型衬底上做两个重掺杂的 $n^+$ 区（源和漏）。
- 两者之间的表面覆一层极薄的氧化层（$\mathrm{SiO_2}$，现代工艺 $1\sim2\,\mathrm{nm}$）。
- 氧化层上是栅电极（早期是金属，现在是多晶硅或金属栅）。

**MOS = Metal–Oxide–Semiconductor**，这个三明治结构就是一个电容。

关键几何参数：沟道长度 $L$、沟道宽度 $W$。设计者能自由选的主要就是 $W/L$ 这个比值 —— 这是 MOS 相对 BJT 的一大自由度（BJT 只能调面积，不能独立调「长宽比」）。

> [!note] 源和漏在结构上是对称的
> 谁是源、谁是漏由电位决定：NMOS 里电位低的那个是源。这个对称性使 MOS 可以做成理想的双向开关（传输门），BJT 做不到。

---
## 2. 沟道是怎么形成的

![[ec-mosfet-structure-and-operation-01.svg]]

栅压从零开始升高，衬底表面依次经历三个阶段：

1. **多子耗尽**：正栅压把 $p$ 衬底表面的空穴推开，留下带负电的受主离子 —— 表面出现耗尽层，但还不导电。
2. **弱反型**：继续升高，表面开始吸引少量电子。此时已有微弱电流，且它是**指数**依赖于 $V_{GS}$ 的（亚阈值区，同样受 $60\,\mathrm{mV/dec}$ 铁律限制）。
3. **强反型**：$V_{GS}$ 超过阈值 $V_{TH}$ 后，表面电子浓度超过衬底空穴浓度，形成连续的 $n$ 型**反型沟道**，把源漏连通。

$V_{TH}$ 由氧化层厚度、衬底掺杂、栅材料功函数决定，工艺上可通过沟道注入精确调整。典型 $0.3\sim0.7\,\mathrm{V}$。

沟道电荷密度（单位面积）：

$$
Q_{ch} = C_{ox}(V_{GS}-V_{TH})
$$

其中 $C_{ox}=\varepsilon_{ox}/t_{ox}$。$V_{ov} \equiv V_{GS}-V_{TH}$ 称为**过驱电压**（overdrive），是 MOS 设计里最重要的自变量。

---
## 3. 三个工作区

### 截止区（$V_{GS} < V_{TH}$）

没有沟道，$I_D \approx 0$。严格说亚阈值电流仍然存在且指数依赖 $V_{GS}$，这在超低功耗设计和数字电路漏电分析里很重要（见 [[Caltech Analog Circuit Design-113N-MOSFET Subthreshold Behavior]]）。

### 三极管区 / 线性区（$V_{DS} < V_{ov}$）

沟道从源到漏都存在。小 $V_{DS}$ 时沟道厚度近似均匀，器件表现得像一个**受栅压控制的电阻**：

$$
R_{on} \approx \frac{1}{\mu_nC_{ox}\dfrac{W}{L}V_{ov}}
$$

这是所有 MOS 开关（传输门、功率 MOS、模拟开关）的工作区。

完整方程：

$$
I_D = \mu_nC_{ox}\frac{W}{L}\left[V_{ov}V_{DS} - \frac{V_{DS}^2}{2}\right]
$$

$V_{DS}$ 增大时沟道在漏端变薄（因为该处的 $V_{GD}=V_{GS}-V_{DS}$ 变小），所以 $I_D$ 的增长逐渐变慢 —— 那个 $-V_{DS}^2/2$ 项就是这个效应。

### 饱和区（$V_{DS} > V_{ov}$）

$V_{DS}$ 大到使漏端的 $V_{GD} = V_{GS}-V_{DS} < V_{TH}$ 时，漏端的沟道**夹断**（pinch-off）。

夹断后再增大 $V_{DS}$，夹断点只是稍微往源端移动，沟道两端的电压差基本锁死在 $V_{ov}$ —— 于是电流不再增长：

$$
I_D = \frac{1}{2}\mu_nC_{ox}\frac{W}{L}V_{ov}^2
$$

**这是放大器工作的区域**：$I_D$ 由 $V_{GS}$ 控制，几乎与 $V_{DS}$ 无关 —— 一个压控电流源。

> [!important] 夹断不等于断路
> 学生最常见的困惑。夹断点处沟道电荷趋于零，但电场极强，载流子以饱和速度被扫过去。电流是连续的（必须连续，KCL 要求），只是不再随 $V_{DS}$ 增长。类比：水管出口收窄到临界后，再加压也不会流得更多。

---
## 4. 与 BJT 的结构性对比

| | BJT | MOSFET |
|---|---|---|
| 控制方式 | 电流（$I_B$）+ 电压（$V_{BE}$） | 纯电压（$V_{GS}$） |
| 输入直流电流 | $I_C/\beta$，不为零 | **零**（氧化层绝缘） |
| 控制律 | 指数 $e^{V_{BE}/V_T}$ | 平方律 $V_{ov}^2$（长沟道） |
| 可设计的几何 | 面积 | $W$ 与 $L$ **独立** |
| 端子对称性 | E/C 不对称 | S/D 对称，可做双向开关 |
| 本征增益 | $V_A/V_T$，与偏置无关 | $2/(\lambda V_{ov})$，可设计 |
| 集成密度 | 低 | 高 |

「栅极不吃电流」这一条决定了 MOS 成为大规模集成的基础：无论驱动多少级，直流功耗都只在开关瞬间发生。

---
## 5. PMOS

在 $n$ 阱里做 $p^+$ 源漏，所有极性反转：$V_{GS}$ 为负、$V_{TH}$ 为负、电流从源流向漏。空穴迁移率约为电子的 $1/3$，所以同样驱动能力的 PMOS 要做到 NMOS 宽度的 $2\sim3$ 倍。

NMOS + PMOS 互补配对就是 **CMOS**，也是现代几乎全部数字与大部分模拟电路的基础。

---
## 6. 与其他笔记的关系

- 对照的 BJT 版本：[[Bipolar Transistor Structure and Operation]]。
- 下一讲给出完整 I–V 与小信号模型：[[MOSFET Characteristics and Small-Signal Model]]。
- 速度饱和的物理：[[Carrier Drift and Diffusion]]。
- 亚阈值区：[[Caltech Analog Circuit Design-113N-MOSFET Subthreshold Behavior]]。
