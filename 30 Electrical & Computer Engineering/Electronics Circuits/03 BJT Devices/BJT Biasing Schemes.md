---
title: "BJT Biasing Schemes"
aliases: ["BJT 偏置", "分压偏置", "射极退化偏置", "自偏置", "PNP 偏置"]
tags: [electronic_circuits, ee, bjt, biasing]
up: "[[Electronic Circuits I MOC]]"
down: ["[[Common-Emitter Stage]]"]
related: ["[[BJT Small-Signal Model]]", "[[Caltech Analog Circuit Design-131N-Biasing Basics-Stable Operating Point and Self-Bias]]"]
---
# BJT Biasing Schemes

## BJT（五）：偏置电路 —— 让工作点不依赖 $\beta$

> [!summary] 核心结论
> 偏置的唯一目标：**把 $I_C$ 钉在一个不依赖 $\beta$、不随温度乱跑的值上**。
> 简单基极电阻偏置 $I_C=\beta\dfrac{V_{CC}-V_{BE}}{R_B}$ 直接正比于 $\beta$，实践中不可用。
> 工程标准解是**分压偏置 + 射极电阻**：$I_C\approx\dfrac{V_B-V_{BE}}{R_E}$，由外部电阻比决定，$\beta$ 只需「够大」。

---
## 1. 为什么偏置是个问题

$\beta$ 的离散性极大（同型号可以从 80 到 300），还随温度以约 $+0.5\%/^\circ\mathrm{C}$ 漂移。$V_{BE}$ 则以 $-2\,\mathrm{mV}/^\circ\mathrm{C}$ 漂移，而 $I_S$ 每升温 $5\,^\circ\mathrm{C}$ 翻倍。

任何让 $I_C$ 直接依赖 $\beta$ 或 $I_S$ 的电路，在产线上都会给出散得一塌糊涂的工作点。偏置电路的全部工作就是**用负反馈把这些不确定性压下去**。

---
## 2. 两种偏置的对比

![[ec-bjt-biasing-schemes-01.svg]]

### (a) 简单基极电阻偏置 —— 反面教材

$$
I_B = \frac{V_{CC}-V_{BE}}{R_B},\qquad
I_C = \beta I_B = \beta\,\frac{V_{CC}-V_{BE}}{R_B}
$$

$I_C$ **正比于 $\beta$**。$\beta$ 从 80 变到 300，$I_C$ 就变 3.75 倍 —— 工作点可能直接冲进饱和或掉到截止。这个电路只在教学里出现。

### (b) 分压偏置 + 射极电阻 —— 工程标准解

$$
V_B \approx V_{CC}\frac{R_2}{R_1+R_2},\qquad
I_C \approx I_E = \frac{V_B - V_{BE}}{R_E}
$$

$\beta$ 消失了。$I_C$ 只由 $V_{CC}$ 和三个电阻决定。

**负反馈机制**：

$$
I_C\uparrow \;\Rightarrow\; V_E = I_ER_E\uparrow \;\Rightarrow\; V_{BE}=V_B-V_E\downarrow \;\Rightarrow\; I_C\downarrow
$$

温度升高使 $V_{BE}$ 下降时，同样被这个环路吸收掉。

> [!important] 两条设计经验
> 1. **分压器要「硬」**：流过 $R_1R_2$ 的电流取 $I_B$ 的 $10$ 倍以上，否则基极电流会把 $V_B$ 拉偏，$\beta$ 又回来了。等价的严格条件是 $R_1\parallel R_2 \ll (\beta+1)R_E$。
> 2. **$V_E$ 要够大**：一般取 $V_E \gtrsim 0.5\sim1\,\mathrm{V}$。太小则 $V_{BE}$ 的温漂（$-2\,\mathrm{mV}/^\circ\mathrm{C}$）相对 $V_B-V_{BE}$ 占比过大，稳定性打折。
>
> 这两条互相拉扯：$V_E$ 越大越稳，但吃掉的电压裕量越多，输出摆幅越小。$3.3\,\mathrm{V}$ 以下的低压设计里这个矛盾很尖锐。

**代价**：$R_E$ 在交流下也存在，会把增益从 $g_mR_C$ 退化到 $R_C/(R_E+1/g_m)$。标准做法是并一个**旁路电容** $C_E$，让 $R_E$ 只在直流起作用、交流被短路掉。详见 [[CE with Emitter Degeneration and Source Resistance]]。

---
## 3. 自偏置与 PNP

![[ec-bjt-biasing-schemes-02.svg]]

### 自偏置（集电极反馈）

$R_B$ 从**集电极**而非 $V_{CC}$ 接到基极：

$$
V_{CE} = V_{BE} + I_B R_B
$$

由于 $V_{CE} > V_{BE}$ 恒成立，**晶体管永远不会进饱和** —— 这是这个拓扑最漂亮的性质。

反馈机制：$I_C\uparrow \Rightarrow V_C\downarrow \Rightarrow I_B\downarrow \Rightarrow I_C\downarrow$。

$I_C$ 的表达式：

$$
I_C \approx \frac{V_{CC}-V_{BE}}{R_C + R_B/\beta}
$$

当 $R_B/\beta \ll R_C$ 时 $\beta$ 的影响被压住。稳定性不如分压偏置，但零件少（两个电阻），且天然免疫饱和，在单管小信号级里很常用。

### PNP 偏置

结构与 npn 完全同构，只是上下翻转：电流从 $V_{CC}$ 流入发射极、由集电极流向地。所有方程形式不变，只是极性取反。

PNP 常用于：需要输出接近地电位的场合、以及和 npn 配对做互补输出级。

---
## 4. 偏置设计检查清单

拿到一个偏置电路，按这四条过一遍：

1. **$I_C$ 对 $\beta$ 敏感吗？** 把 $\beta$ 变成 3 倍，$I_C$ 变多少？
2. **$I_C$ 对温度敏感吗？** $V_{BE}$ 漂 $-2\,\mathrm{mV}/^\circ\mathrm{C}$ 时 $I_C$ 变多少？
3. **$V_{CE}$ 够不够？** 留给输出摆幅的空间是多少？会不会在信号峰值时进饱和？
4. **直流通路与交流通路分清了吗？** 耦合电容、旁路电容有没有让两者互相干扰？

---
## 5. 一个完整设计例子

要求：$V_{CC}=10\,\mathrm{V}$，$I_C=1\,\mathrm{mA}$，$\beta\ge 100$。

1. 取 $V_E = 1\,\mathrm{V}$ $\Rightarrow$ $R_E = 1\,\mathrm{V}/1\,\mathrm{mA} = 1\,\mathrm{k\Omega}$。
2. $V_B = V_E + V_{BE} = 1.7\,\mathrm{V}$。
3. 分压器电流取 $I_B$ 的 10 倍：$I_B = 1\,\mathrm{mA}/100 = 10\,\mathrm{\mu A}$，故分压电流取 $100\,\mathrm{\mu A}$。
   $$R_2 = \frac{1.7}{100\,\mathrm{\mu A}} = 17\,\mathrm{k\Omega},\qquad R_1 = \frac{10-1.7}{100\,\mathrm{\mu A}} = 83\,\mathrm{k\Omega}$$
4. 取 $V_{CE}=4\,\mathrm{V}$ 留摆幅 $\Rightarrow$ $V_{R_C} = 10-1-4 = 5\,\mathrm{V}$，$R_C = 5\,\mathrm{k\Omega}$。
5. 验算增益：$|A_v| = V_{R_C}/V_T = 5/0.026 \approx 192$（$R_E$ 已被旁路）。

---
## 6. 与其他笔记的关系

- 用到的小信号参数：[[BJT Small-Signal Model]]。
- 偏置好了才能谈增益：[[Common-Emitter Stage]]。
- $R_E$ 不旁路时会发生什么：[[CE with Emitter Degeneration and Source Resistance]]。
- 更偏 IC 的自偏置与基准：[[Caltech Analog Circuit Design-131N-Biasing Basics-Stable Operating Point and Self-Bias]]。
