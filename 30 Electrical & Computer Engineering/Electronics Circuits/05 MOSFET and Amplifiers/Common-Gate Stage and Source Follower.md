---
title: "Common-Gate Stage and Source Follower"
aliases: ["共栅级", "源极跟随器", "Common-Gate", "Source Follower", "六种组态汇总"]
tags: [electronic_circuits, ee, mosfet, amplifier]
up: "[[Electronic Circuits I MOC]]"
related: ["[[MOS Biasing and the Common-Source Stage]]", "[[Common-Base Stage and Emitter Follower]]", "[[Caltech Analog Circuit Design-124N-MOS Stages (2)-Source Follower Common-Gate and Cascode]]"]
---
# Common-Gate Stage and Source Follower

## MOSFET（四）：共栅级、源极跟随器与六种组态总表

> [!summary] 核心结论
> MOS 的三种组态与 BJT 一一对应，但有两处系统性差别：
> 1. **$R_{in}$ 在栅极永远是无穷大**（BJT 的基极只有 $r_\pi$）——所以 MOS 没有「$(\beta+1)$ 缩放」那套规则，只剩一条「源极看进去是 $1/g_m$」。
> 2. **体效应无处不在**：只要源极不接地，$g_{mb}$ 就登场，把源跟随器的增益和共栅级的输入阻抗都拉低。
>
> 至此单级放大器讲完，六种组态可以放进同一张表里对照。

---
## 1. 共栅级（CG）

![[ec-common-gate-stage-and-source-follower-01.svg]]

输入加在源极，栅极接固定偏压（交流地），输出取自漏极。

$$
A_v = +g_mR_D \quad(\text{同相}),\qquad
R_{in} = \frac{1}{g_m+g_{mb}},\qquad
R_{out} = R_D\parallel r_o
$$

$R_{in}$ 很低（$I_D=0.5\,\mathrm{mA}$、$V_{ov}=0.2\,\mathrm{V}$ 时 $1/g_m=200\,\Omega$），所以与共基级一样，共栅级适合做：

- **电流缓冲**：把电流从低阻节点搬到高阻节点，几乎无损。
- **宽带输入级**：$R_{in}$ 低意味着输入节点的 RC 时间常数小；同时栅极接固定电位，**输入到输出没有跨接电容**，因而没有密勒效应。这是共栅级带宽好的根本原因。
- **cascode 的上管**：这是它在 IC 里最主要的身份。

### cascode

共源级（下管）+ 共栅级（上管）叠在一起：

- 下管的漏极看到上管的 $1/g_m$（极低）$\Rightarrow$ 下管电压增益 $\approx 1$ $\Rightarrow$ **密勒效应被消灭**，带宽大幅改善。
- 从上管漏极看进去，输出电阻被抬到
  $$R_{out}\approx g_{m2}r_{o2}r_{o1}$$
  于是配上电流源负载可以得到 $(g_mr_o)^2$ 量级的增益。

**一个结构同时买到带宽和增益**，代价是多消耗一个 $V_{ov}$ 的电压裕量。低压工艺下这个代价越来越贵，这也是折叠式 cascode、增益自举等结构出现的原因。

---
## 2. 源极跟随器（SF）

输入加在栅极，输出取自源极。

$$
A_v = \frac{g_mR_S}{1+(g_m+g_{mb})R_S} = \frac{R_S}{R_S + \dfrac{1}{g_m+g_{mb}}}\cdot\frac{g_m}{g_m}
$$

化简后更常写成：

$$
\boxed{\;A_v=\frac{g_m}{g_m+g_{mb}+1/R_S}\;}
$$

$$
R_{in}=\infty\ (\text{直流}),\qquad
R_{out}=\frac{1}{g_m+g_{mb}}\parallel R_S
$$

### 源跟随器不如射极跟随器

即使 $R_S\to\infty$（用理想电流源做负载），增益也只能达到

$$
A_{v,max}=\frac{g_m}{g_m+g_{mb}}=\frac{1}{1+\eta}
$$

$\eta\approx0.2$ 时增益约 $0.83$ —— 而射极跟随器可以做到 $0.99$ 以上。

原因就是体效应：源极电位跟着输入摆动，$V_{SB}$ 随之变化，$V_{TH}$ 也跟着变，衬底像第二个栅极在「拖后腿」。

**消除办法**：把衬底接到源极。标准 CMOS 里 NMOS 共用 $p$ 衬底做不到，但 PMOS 可以放进独立 $n$ 阱 —— 所以需要高精度跟随器时常用 PMOS。

### 另外两个缺点

- **电平移位**：输出比输入低一个 $V_{GS}=V_{TH}+V_{ov}$，通常 $0.5\sim1\,\mathrm{V}$，比 BJT 的 $0.7\,\mathrm{V}$ 更大且更不确定（$V_{TH}$ 有工艺离散）。
- **非线性**：输出摆动时 $V_{SB}$ 变化 $\Rightarrow$ $V_{TH}$ 变化 $\Rightarrow$ 增益随信号电平变化。

正因为这些，现代 CMOS 模拟设计里源跟随器用得**远不如** BJT 里的射随器普遍，常被运放 + 反馈组成的缓冲器取代。

---
## 3. 六种组态总表

| | CE | CB | EF | CS | CG | SF |
|---|---|---|---|---|---|---|
| 输入端 | 基极 | 射极 | 基极 | 栅极 | 源极 | 栅极 |
| 输出端 | 集电极 | 集电极 | 射极 | 漏极 | 漏极 | 源极 |
| $A_v$ | $-g_mR_C$ | $+g_mR_C$ | $\lesssim 1$ | $-g_mR_D$ | $+g_mR_D$ | $<1$（体效应压低） |
| 相位 | 反相 | 同相 | 同相 | 反相 | 同相 | 同相 |
| $R_{in}$ | $r_\pi$ | $1/g_m$ | $r_\pi+(\beta{+}1)R_E$ | $\infty$ | $\dfrac{1}{g_m+g_{mb}}$ | $\infty$ |
| $R_{out}$ | $R_C\parallel r_o$ | $R_C\parallel r_o$ | $\dfrac{1}{g_m}+\dfrac{R_S}{\beta+1}$ | $R_D\parallel r_o$ | $R_D\parallel r_o$ | $\dfrac{1}{g_m+g_{mb}}$ |
| 本征增益 | $V_A/V_T\approx 3800$ | 同左 | — | $\dfrac{2}{\lambda V_{ov}}\approx 100$ | 同左 | — |
| 主要用途 | 通用增益级 | 匹配 / cascode | 缓冲 / 输出级 | 通用增益级 | 匹配 / cascode | 缓冲（受限） |

**读表的两条线索**：

1. **输入端决定 $R_{in}$**：栅极 $\infty$、基极中等、源/射极最低。
2. **输出端决定 $R_{out}$**：漏/集电极高、源/射极低。

组态名（「共什么」）指的是那个交流接地的端子，它既不是输入也不是输出。

---
## 4. 怎么选组态

| 需求 | 选择 |
|---|---|
| 要电压增益 | CE / CS |
| 信号源阻抗很高 | 前面加 EF/SF，或直接用 CS（栅极不吃电流） |
| 负载阻抗很低 | 后面加 EF/SF |
| 要 $50\,\Omega$ 输入匹配 | CB / CG，调偏置电流即可 |
| 要带宽 | cascode（CS + CG），消除密勒效应 |
| 要高增益 | cascode + 电流源负载 |
| 要可预测的增益 | 加退化电阻，或二极管接法负载 |

---
## 5. 这门课到此为止，以及后面是什么

单级放大器讲完了。真实的运放还需要：

- **差分对**：抑制共模和电源噪声，是所有运放的输入级。
- **电流镜**：IC 里的标准偏置方式，也做有源负载。
- **频率响应**：密勒定理、极点零点、增益带宽积。
- **反馈**：四种反馈拓扑、环路增益、稳定性与补偿。
- **输出级**：A/B 类、交越失真、效率。

这些是 Electronic Circuits II 的内容。已有的相关笔记见 [[Caltech Analog Circuit Design-127N-Differential Amplifiers (1)-Large Signal and Current Steering]] 及其后续。

---
## 6. 与其他笔记的关系

- 同构的 BJT 版本：[[Common-Base Stage and Emitter Follower]]。
- 前一讲：[[MOS Biasing and the Common-Source Stage]]。
- Caltech 版：[[Caltech Analog Circuit Design-124N-MOS Stages (2)-Source Follower Common-Gate and Cascode]]。
