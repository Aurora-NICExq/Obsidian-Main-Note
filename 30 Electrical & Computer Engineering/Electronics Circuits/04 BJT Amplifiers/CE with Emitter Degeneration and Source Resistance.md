---
title: "CE with Emitter Degeneration and Source Resistance"
aliases: ["射极退化", "Emitter Degeneration", "带射极电阻的共射级", "阻抗速查规则"]
tags: [electronic_circuits, ee, bjt, amplifier, feedback]
up: "[[Electronic Circuits I MOC]]"
down: ["[[Common-Base Stage and Emitter Follower]]"]
related: ["[[Common-Emitter Stage]]", "[[BJT Small-Signal Model]]", "[[BJT Biasing Schemes]]"]
---
# CE with Emitter Degeneration and Source Resistance

## 共射级（二）：射极退化、阻抗速查规则与源电阻

> [!summary] 核心结论
> $$A_v = -\frac{R_C}{R_E + 1/g_m}$$
> $R_E$ 是一个**局部负反馈**，用增益换来三样东西：更好的线性度、对 $g_m$（因而对温度和 $I_C$）不敏感的可预测增益、更高的输入阻抗。
> 当 $R_E \gg 1/g_m$ 时 $A_v\to -R_C/R_E$ —— 增益完全由电阻比决定，这是模拟设计里最想要的性质。

---
## 1. 为什么要加 $R_E$

共射级的增益 $g_mR_C$ 里，$g_m=I_C/V_T$ 依赖偏置电流和温度，且 $I_C$ 对 $v_{be}$ 是指数关系（大信号下严重失真）。射极电阻同时治这两个病。

![[ec-ce-with-emitter-degeneration-and-source-resistance-01.svg]]

---
## 2. 增益

用 T 模型最快：从射极看进去是 $1/g_m$，它与 $R_E$ 串联构成射极总阻抗。射极电流

$$
i_e = \frac{v_{in}}{R_E + 1/g_m}
$$

集电极电流 $i_c \approx i_e$，于是

$$
\boxed{\;A_v = -\frac{R_C}{R_E + 1/g_m} = -\frac{g_mR_C}{1+g_mR_E}\;}
$$

两个极限：

- $R_E = 0$：退化回 $-g_mR_C$。
- $R_E \gg 1/g_m$：$A_v \to -\dfrac{R_C}{R_E}$。

第二个极限是关键。$1/g_m = V_T/I_C = 26\,\Omega$（$I_C=1\,\mathrm{mA}$），所以只要 $R_E$ 取几百欧，增益就基本只由 $R_C/R_E$ 决定 —— **和器件参数、温度、偏置全都脱钩**。

> [!important] 这是负反馈的第一次登场
> 「用环路增益换精度」是模拟电路的核心思想。$R_E$ 把一部分输出（射极电流）反馈回输入（减小 $V_{BE}$），代价是增益降低 $(1+g_mR_E)$ 倍，收益是所有非理想因素也同样被压低 $(1+g_mR_E)$ 倍。这个因子就是环路增益。

---
## 3. 线性度的改善

大信号下，$V_{BE}$ 的变化只占输入变化的一部分：

$$
v_{be} = v_{in}\cdot\frac{1/g_m}{R_E + 1/g_m}
$$

$R_E$ 越大，落在非线性的 BE 结上的电压越少，落在线性电阻上的越多。所以失真被压低同样的 $(1+g_mR_E)$ 倍。

这也把「小信号成立」的门限从 $v_{in}\ll 26\,\mathrm{mV}$ 放宽到 $v_{in}\ll 26\,\mathrm{mV}\times(1+g_mR_E)$ —— 对处理较大信号的级来说很实在。

---
## 4. 两条阻抗速查规则

![[ec-ce-with-emitter-degeneration-and-source-resistance-02.svg]]

$$
\boxed{\;R_{B,\text{in}} = r_\pi + (\beta+1)R_E\;}\qquad
\boxed{\;R_{E,\text{in}} = \frac{1}{g_m} + \frac{R_B}{\beta+1}\;}
$$

一句话记：**阻抗从射极看向基极放大 $(\beta+1)$ 倍，从基极看向射极缩小 $(\beta+1)$ 倍。**

这两条能直接读出后面所有组态的阻抗，不需要每次重新列 KCL：

| 组态 | $R_{in}$ | 由哪条规则 |
|---|---|---|
| 共射（无 $R_E$） | $r_\pi$ | 规则一，$R_E=0$ |
| 共射 + $R_E$ | $r_\pi+(\beta+1)R_E$ | 规则一 |
| 射极跟随器 | $r_\pi+(\beta+1)(R_E\parallel R_L)$ | 规则一 |
| 共基级 | $1/g_m$ | 规则二，$R_B=0$ |

### 输出阻抗也被抬高

从集电极看进去，$R_E$ 的存在使输出电阻从 $r_o$ 涨到

$$
R_{out} = r_o\left[1 + g_m(R_E\parallel r_\pi)\right] + (R_E\parallel r_\pi)
$$

这个「$r_o$ 被 $(1+g_mR_E)$ 放大」的效应正是 **cascode** 的原理：把一个管子的射极接到另一个管子的集电极，等效于给下管加了一个极大的 $R_E$，于是输出电阻变成 $g_mr_o^2$ 量级。

---
## 5. 源电阻 $R_S$ 的影响

真实信号源有内阻。它与 $R_{in}$ 分压：

$$
A_{v,\text{overall}} = -\frac{R_C}{R_E + 1/g_m}\cdot\frac{R_{in}}{R_{in}+R_S}
$$

或者合成一个式子（用 T 模型，把 $R_S$ 折算到射极侧除以 $\beta+1$）：

$$
A_v = -\frac{R_C}{R_E + \dfrac{1}{g_m} + \dfrac{R_S}{\beta+1}}
$$

这里 $R_E$ 抬高 $R_{in}$ 的价值就显出来了：**它让这一级不那么怕高阻信号源**。

---
## 6. 直流退化 vs 交流退化

工程上常常两者都要，但用途不同：

- **直流退化**（$R_E$ 无旁路电容）：稳定工作点。见 [[BJT Biasing Schemes]]。
- **交流退化**（$R_E$ 也在交流路径上）：提高线性度和可预测性，代价是增益。

如果只想要前者，就并一个足够大的旁路电容 $C_E$，让 $R_E$ 在信号频段被短路。

如果两者都要一点，常用做法是把射极电阻拆成两段：$R_{E1}$（不旁路，提供交流退化）+ $R_{E2}$（旁路，只管直流）。

$$
A_v = -\frac{R_C}{R_{E1}+1/g_m}
$$

这是分立放大器里非常常见的结构。

---
## 7. 与其他笔记的关系

- 无退化的基准情形：[[Common-Emitter Stage]]。
- 速查规则的来源：[[BJT Small-Signal Model]]。
- $R_E$ 用于直流稳定：[[BJT Biasing Schemes]]。
- 下一讲的两种组态也靠这两条规则：[[Common-Base Stage and Emitter Follower]]。
