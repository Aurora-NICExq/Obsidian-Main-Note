---
title: "MOSFET Characteristics and Small-Signal Model"
aliases: ["MOS 输出特性", "沟道长度调制", "MOS 小信号模型", "体效应", "gm 三种写法"]
tags: [electronic_circuits, ee, mosfet, small_signal]
up: "[[Electronic Circuits I MOC]]"
down: ["[[MOS Biasing and the Common-Source Stage]]"]
related: ["[[MOSFET Structure and Operation]]", "[[BJT Small-Signal Model]]", "[[Caltech Analog Circuit Design-120N-Amplifier Basics (2)-MOS Common-Source and Intrinsic Gain]]"]
---
# MOSFET Characteristics and Small-Signal Model

## MOSFET（二）：I–V 特性、沟道长度调制与小信号模型

> [!summary] 核心结论
> 饱和区：$I_D=\dfrac12\mu_nC_{ox}\dfrac{W}{L}V_{ov}^2(1+\lambda V_{DS})$，于是
> $$g_m = \mu_nC_{ox}\frac{W}{L}V_{ov} = \frac{2I_D}{V_{ov}} = \sqrt{2\mu_nC_{ox}\frac{W}{L}I_D},\qquad r_o=\frac{1}{\lambda I_D}$$
> 与 BJT 的关键差别：$g_m\propto\sqrt{I_D}$（不是 $\propto I_D$），本征增益 $g_mr_o=\dfrac{2}{\lambda V_{ov}}$ **依赖设计选择**而非工艺常数。

---
## 1. 输出特性族

![[ec-mosfet-characteristics-and-small-signal-model-01.svg]]

横轴 $V_{DS}$、纵轴 $I_D$，每条曲线一个固定 $V_{GS}$。

- **三极管区**：抛物线上升段。
  $$I_D=\mu_nC_{ox}\frac{W}{L}\left[V_{ov}V_{DS}-\frac{V_{DS}^2}{2}\right]$$
- **边界**：$V_{DS}=V_{ov}$，把各条曲线的顶点连起来，本身也是一条抛物线 $I_D = \frac{1}{2}\mu_nC_{ox}\frac{W}{L}V_{DS}^2$。
- **饱和区**：近水平，带一个小斜率。
  $$I_D=\frac{1}{2}\mu_nC_{ox}\frac{W}{L}V_{ov}^2(1+\lambda V_{DS})$$

注意与 BJT 输出特性族的一个视觉差别：BJT 各条曲线的间距按 $e^{V_{BE}/V_T}$ 指数拉开，MOS 按 $V_{ov}^2$ 平方拉开 —— 后者疏得多。这直观反映了 MOS 的跨导效率更低。

---
## 2. 沟道长度调制

$V_{DS}$ 增大 $\Rightarrow$ 夹断点向源端移动 $\Rightarrow$ 有效沟道长度 $L_{eff}$ 变短 $\Rightarrow$ $I_D\propto 1/L$ 略增。

用 $\lambda$（沟道长度调制系数，单位 $\mathrm{V^{-1}}$）唯象地描述：

$$
r_o = \left(\frac{\partial I_D}{\partial V_{DS}}\right)^{-1}_Q = \frac{1}{\lambda I_D}
$$

**$\lambda \propto 1/L$** —— 沟道越长，同样的 $\Delta L$ 占比越小，调制效应越弱，$r_o$ 越大。这是模拟设计里「需要高增益就用长管子」的原因（代价是面积和寄生电容）。

这与 BJT 的 Early 效应是完全同构的现象：$V_A \leftrightarrow 1/\lambda$。

---
## 3. 跨导的三种写法

![[ec-mosfet-characteristics-and-small-signal-model-02.svg]]

对饱和区方程求导：

$$
g_m=\frac{\partial I_D}{\partial V_{GS}} = \mu_nC_{ox}\frac{W}{L}V_{ov}
$$

配合 $I_D=\frac12\mu_nC_{ox}\frac{W}{L}V_{ov}^2$ 消元，得到三个等价形式：

$$
\boxed{\;g_m = \mu_nC_{ox}\frac{W}{L}V_{ov}
= \frac{2I_D}{V_{ov}}
= \sqrt{2\mu_nC_{ox}\frac{W}{L}I_D}\;}
$$

用哪个取决于你手上固定的是什么：

| 固定量 | 用哪个式子 | 结论 |
|---|---|---|
| $W/L$ 与 $V_{ov}$ | 第一式 | $g_m$ 线性于 $V_{ov}$ |
| $I_D$ 与 $V_{ov}$ | 第二式 | 小 $V_{ov}$ 给高 $g_m/I_D$ |
| $W/L$ 与 $I_D$ | 第三式 | $g_m\propto\sqrt{I_D}$ |

> [!important] $g_m/I_D$：MOS 设计的核心指标
> $$\frac{g_m}{I_D}=\frac{2}{V_{ov}}$$
> 「每一微安电流买到多少跨导」。$V_{ov}$ 越小效率越高，极限是弱反型区的 $g_m/I_D\to 1/(nV_T)\approx 25\sim 30\,\mathrm{V^{-1}}$ —— 恰好就是 BJT 的 $1/V_T$。
>
> 换句话说：**BJT 天生就工作在 MOS 拼命想接近的那个效率极限上**。代价是 MOS 可以自由选择用效率换速度，BJT 没得选。

---
## 4. 小信号模型

结构与 BJT 的混合 π 完全一样，**只是没有 $r_\pi$**（栅极直流开路）：

- $g_m v_{gs}$ 受控电流源，从 D 流向 S
- $r_o$ 与之并联
- G–S 之间直流开路（高频下是 $C_{gs}$）

$$
R_{in} = \infty\ (\text{直流}),\qquad R_{out}=r_o
$$

### 体效应（body effect）

当源极电位不等于衬底电位时，$V_{SB}>0$ 会使耗尽层加深，阈值电压升高：

$$
V_{TH} = V_{TH0} + \gamma\left(\sqrt{|2\phi_F| + V_{SB}} - \sqrt{|2\phi_F|}\right)
$$

小信号上表现为**第二个跨导** $g_{mb}=\eta g_m$（$\eta\approx0.1\sim0.3$），衬底像是第二个栅极：

$$
i_d = g_mv_{gs} + g_{mb}v_{bs} + \frac{v_{ds}}{r_o}
$$

体效应在源极不接地的场合（源跟随器、cascode 的上管、堆叠结构）会明显降低增益。在标准 CMOS 里 NMOS 的衬底通常统一接地，所以只要源极浮起来就一定有体效应；PMOS 可以做在独立 $n$ 阱里把体接到源，从而消除它。

---
## 5. 本征增益：与 BJT 的决定性差别

$$
g_m r_o = \frac{2I_D}{V_{ov}}\cdot\frac{1}{\lambda I_D} = \frac{2}{\lambda V_{ov}}
$$

$$
\boxed{\;g_mr_o = \frac{2}{\lambda V_{ov}}\;}
$$

$I_D$ 又一次被消掉了，但留下的不是工艺常数，而是**两个设计者可以选的量**：

- $\lambda \propto 1/L$：用长沟道管子 $\Rightarrow$ $\lambda\downarrow$ $\Rightarrow$ 增益$\uparrow$
- $V_{ov}$：降低过驱 $\Rightarrow$ 增益$\uparrow$（但速度和摆幅裕量变差）

典型数值：$\lambda=0.1\,\mathrm{V^{-1}}$、$V_{ov}=0.2\,\mathrm{V}$ $\Rightarrow$ $g_mr_o=100$。

对比 BJT 的 $V_A/V_T\approx 3800$ —— **MOS 的本征增益低一到两个数量级**。这就是为什么 MOS 模拟电路大量依赖 cascode、增益自举、多级放大来把增益堆上去，而 BJT 一级就够。

---
## 6. 短沟道效应

现代工艺（$L$ 在几十 nm）里平方律基本失效：

- **速度饱和**：$I_D$ 对 $V_{ov}$ 从平方退化到接近线性，于是 $g_m\to W C_{ox}v_{sat}$，几乎与 $V_{ov}$ 无关。
- **迁移率退化**：强垂直场使 $\mu$ 下降。
- **DIBL**：漏端电压影响势垒，$r_o$ 进一步恶化。

但**小信号方法本身完全不受影响** —— 无论 $I_D(V_{GS})$ 是平方、线性还是别的什么形状，$g_m$ 永远定义为工作点的偏导。这是小信号分析最强大的地方：它不要求你知道精确的大信号模型。

---
## 7. 与其他笔记的关系

- 器件结构与工作区：[[MOSFET Structure and Operation]]。
- 对照的 BJT 模型：[[BJT Small-Signal Model]]。
- 直接应用：[[MOS Biasing and the Common-Source Stage]]。
- 本征增益的 IC 设计视角：[[Caltech Analog Circuit Design-120N-Amplifier Basics (2)-MOS Common-Source and Intrinsic Gain]]。
