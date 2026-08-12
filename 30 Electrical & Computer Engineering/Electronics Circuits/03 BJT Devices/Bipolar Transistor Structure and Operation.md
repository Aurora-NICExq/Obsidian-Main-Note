---
title: "Bipolar Transistor Structure and Operation"
aliases: ["双极型晶体管", "BJT 结构", "npn 工作原理", "beta"]
tags: [electronic_circuits, ee, bjt]
up: "[[Electronic Circuits I MOC]]"
down: ["[[BJT Output Characteristics and the Early Effect]]"]
related: ["[[PN Junction Forward Bias and the Diode Equation]]", "[[Caltech Analog Circuit Design-106N-BJT Basics and Current Transport]]"]
---
# Bipolar Transistor Structure and Operation

## BJT（一）：结构、载流子输运与 $I_C=I_Se^{V_{BE}/V_T}$

> [!summary] 核心结论
> npn 就是把两个 pn 结背靠背做在一起，关键在于**基区薄到电子来不及复合就被集电结抽走**。
> 于是一个很小的基极电流控制一个大得多的集电极电流：$\beta=I_C/I_B$ 可达上百。
> 但真正重要的不是「电流放大」，而是 $I_C = I_S e^{V_{BE}/V_T}$ —— **BJT 本质是一个电压控制的电流源**（跨导器件），这才是它能做放大器的原因。

---
## 1. 结构

![[ec-bipolar-transistor-structure-and-operation-01.svg]]

三个区，掺杂浓度差别巨大：

| 区 | 掺杂 | 目的 |
|---|---|---|
| 发射极 E | $n^{+}$（最重） | 尽可能多地向基区注入电子 |
| 基区 B | $p$（最轻、最薄） | 薄到电子几乎不复合就穿过去 |
| 集电极 C | $n$（中等、面积大） | 收集电子，并承受较高电压与功耗 |

**结构不对称是本质的**。把 E 和 C 对调（反向有源区）虽然也能工作，但 $\beta$ 掉到个位数——因为 C 的掺杂和几何都不是为「注入」设计的。

---
## 2. 正向有源区的工作过程

条件：**BE 结正偏、BC 结反偏**。

1. BE 结正偏 $\Rightarrow$ 大量电子从 $n^+$ 发射极注入 $p$ 基区（这就是上一讲的少子注入）。
2. 基区很薄（远小于扩散长度）$\Rightarrow$ 电子几乎不与空穴复合就扩散到了基区另一端。
3. BC 结反偏，其耗尽区里有很强的电场，方向恰好把到达的电子「吸」进集电极。

于是绝大部分注入的电子成了 $I_C$，只有很小一部分在基区复合、或者反向注入回发射极，成了 $I_B$。

$$
\beta = \frac{I_C}{I_B}
$$

$\beta$ 的大小主要由「基区宽度 / 扩散长度」和「发射极与基区的掺杂比」决定。典型值 $50\sim 200$，但**离散性极大**（同一批次可以差 3 倍），且随温度和 $I_C$ 变化。

> [!warning] 永远不要让电路性能依赖 $\beta$ 的具体值
> 这是 [[BJT Biasing Schemes]] 那一讲的核心动机。好的偏置电路让 $I_C$ 只依赖外部电阻比，$\beta$ 只需要「足够大」即可。

三个端电流的关系：

$$
I_E = I_C + I_B = I_C\left(1 + \frac{1}{\beta}\right) = \frac{\beta+1}{\beta}I_C
$$

常用 $\alpha = \dfrac{I_C}{I_E} = \dfrac{\beta}{\beta+1}\approx 0.99$。

---
## 3. 核心方程

![[ec-bipolar-transistor-structure-and-operation-02.svg]]

基区边界的电子浓度由 BE 结的边界条件定律给出（$\propto e^{V_{BE}/V_T}$），基区里浓度近似线性下降，梯度即扩散流：

$$
\boxed{\;I_C = I_S\,e^{V_{BE}/V_T}\;}
$$

其中 $I_S \propto \dfrac{A_E n_i^2}{N_B W_B}$：面积越大、基区越薄越轻掺杂，$I_S$ 越大。

三点关键观察：

**(1) $I_C$ 与 $V_{CE}$ 无关。**
一阶近似下，集电极电压只负责「把电子吸走」，吸多快不影响有多少电子送过来。所以输出特性是水平的 —— 一个理想电流源。（二阶效应见 [[BJT Output Characteristics and the Early Effect]]。）

**(2) 这是一个跨导器件。**
输入是电压 $V_{BE}$，输出是电流 $I_C$。所以 BJT 的核心参数是**跨导**：

$$
g_m = \frac{\partial I_C}{\partial V_{BE}} = \frac{I_S e^{V_{BE}/V_T}}{V_T} = \frac{I_C}{V_T}
$$

$$
\boxed{\;g_m = \frac{I_C}{V_T}\;}
$$

这条式子有个惊人的性质：**$g_m$ 只由偏置电流决定，与器件尺寸、工艺、掺杂统统无关**。$1\,\mathrm{mA}$ 的 BJT，无论是分立件还是片上小管子，$g_m$ 都是 $1/26\,\Omega^{-1}\approx 38\,\mathrm{mS}$。MOS 完全没有这个性质，这是 BJT 在精密模拟电路里长盛不衰的原因。

**(3) 60 mV/decade 再次出现。**
$I_C$ 变 10 倍，$V_{BE}$ 只变 $60\,\mathrm{mV}$。所以「$V_{BE}\approx0.7\,\mathrm{V}$」在 $\mu\mathrm{A}$ 到 $\mathrm{mA}$ 的范围内都够用。

---
## 4. pnp

把所有掺杂类型、电流方向、电压极性反过来即可：

$$
I_C = I_S e^{|V_{BE}|/V_T},\qquad \text{条件：} V_{EB}>0,\ V_{BC} \text{（对 pnp 而言）反偏}
$$

电流从 $V_{CC}$ 流入发射极、由集电极流出。所有小信号结论与 npn 完全同构，只是极性翻转。

---
## 5. 与其他笔记的关系

- 少子注入与边界条件：[[PN Junction Forward Bias and the Diode Equation]]。
- 下一讲加上 $V_{CE}$ 的二阶依赖：[[BJT Output Characteristics and the Early Effect]]。
- 电流输运的更细物理：[[Caltech Analog Circuit Design-106N-BJT Basics and Current Transport]]。
