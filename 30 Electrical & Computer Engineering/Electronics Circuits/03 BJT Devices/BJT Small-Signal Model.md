---
title: "BJT Small-Signal Model"
aliases: ["BJT 小信号模型", "混合π模型", "T 模型", "gm rpi ro"]
tags: [electronic_circuits, ee, bjt, small_signal]
up: "[[Electronic Circuits I MOC]]"
down: ["[[BJT Biasing Schemes]]"]
related: ["[[BJT Operating Regions and Large-Signal Model]]", "[[Diode Models and Small-Signal Resistance]]", "[[Caltech Analog Circuit Design-115N-Small-Signal Model and gm-ro Intuition]]"]
---
# BJT Small-Signal Model

## BJT（四）：混合 π 模型、T 模型与三个参数

> [!summary] 核心结论
> 三个参数把非线性器件变成线性二端口：
> $$g_m=\frac{I_C}{V_T},\qquad r_\pi=\frac{\beta}{g_m}=\frac{\beta V_T}{I_C},\qquad r_o=\frac{V_A}{I_C}$$
> 混合 π 与 T 模型完全等价，只是画法不同；选哪个只看「哪个端口的阻抗更好读」。
> 两条速查规则（阻抗跨越 $\beta+1$ 倍缩放）能推出后面所有单级放大器的结论。

---
## 1. 小信号分析的三步

![[ec-bjt-small-signal-model-02.svg]]

1. **直流工作点**：电容开路、电感短路，解出 $I_C$、$V_{CE}$。
2. **参数提取**：代入三条公式得到 $g_m$、$r_\pi$、$r_o$。
3. **交流等效**：直流电压源接地（理想电压源的小信号是短路）、直流电流源开路、耦合与旁路电容短路，器件换成模型，然后用纯线性方法求解。

> [!warning] 最常见的错误
> 忘了第 3 步里「$V_{CC}$ 在小信号图里是地」。$V_{CC}$ 是一个固定电压，它的**变化量**为零，所以对交流而言它和地没有区别。$R_C$ 接在 $V_{CC}$ 上，在小信号图里就是接地。

---
## 2. 三个参数的来源

全都是在工作点对大信号方程求偏导：

$$
g_m = \frac{\partial I_C}{\partial V_{BE}}\bigg|_Q = \frac{I_C}{V_T}
$$

$$
r_\pi = \left(\frac{\partial I_B}{\partial V_{BE}}\right)^{-1}_Q
= \left(\frac{1}{\beta}\frac{\partial I_C}{\partial V_{BE}}\right)^{-1}
= \frac{\beta}{g_m} = \frac{\beta V_T}{I_C}
$$

$$
r_o = \left(\frac{\partial I_C}{\partial V_{CE}}\right)^{-1}_Q = \frac{V_A}{I_C}
$$

数值感觉（$I_C=1\,\mathrm{mA}$，$\beta=100$，$V_A=100\,\mathrm{V}$）：

| 参数 | 值 |
|---|---|
| $g_m$ | $38.5\,\mathrm{mS}$（即 $1/26\,\Omega$） |
| $r_\pi$ | $2.6\,\mathrm{k\Omega}$ |
| $r_o$ | $100\,\mathrm{k\Omega}$ |

注意 $r_\pi \ll r_o$ —— BJT 的输入阻抗是有限的（因为基极确实要吃电流），这是它与 MOS 最大的结构性差别。

---
## 3. 两个等价模型

![[ec-bjt-small-signal-model-01.svg]]

**混合 π 模型**：$r_\pi$ 接在 B–E 之间，受控源 $g_mv_\pi$ 从 C 流向 E，$r_o$ 与受控源并联。这是默认选择，尤其适合算共射级。

**T 模型**：把 $1/g_m$ 放在射极支路。它的好处是「从射极看进去是 $1/g_m$」这件事一眼可见，算共基级和射极跟随器时省事。

两者是同一组参数的不同画法，任何一个都能推出另一个。**不要试图记住两套结论，记一套 + 会换算就够了。**

---
## 4. 两条阻抗速查规则

这是本讲最实用的部分。后面所有单级放大器的输入/输出阻抗都能由它们直接读出：

$$
\boxed{\;\text{从基极看进去：} R_{in} = r_\pi + (\beta+1)R_E\;}
$$

$$
\boxed{\;\text{从射极看进去：} R_{in} = \frac{1}{g_m} + \frac{R_B}{\beta+1}\;}
$$

用一句话记：**阻抗从射极往基极方向看会被放大 $(\beta+1)$ 倍，从基极往射极方向看会被缩小 $(\beta+1)$ 倍。**

物理原因：基极电流只有射极电流的 $1/(\beta+1)$。同样的电压变化下电流小 $(\beta+1)$ 倍，看到的阻抗自然大 $(\beta+1)$ 倍。

直接推论：

- **基极是高阻节点**，射极是低阻节点。
- 射极跟随器 $R_{in}$ 高、$R_{out}$ 低 —— 天生的缓冲器。
- 共基级 $R_{in}=1/g_m$ 很低 —— 天生适合做电流输入或 $50\,\Omega$ 匹配。

---
## 5. 本征增益回顾

$$
g_m r_o = \frac{V_A}{V_T} \approx 3800\ (V_A=100\,\mathrm{V})
$$

这是单个 BJT 能提供的最大电压增益，与偏置电流无关。实际共射级达不到这个值，因为负载电阻总是与 $r_o$ 并联把它拉低。想接近本征增益，就得用「直流压降小、交流电阻大」的负载 —— 即电流源负载。

---
## 6. 与其他笔记的关系

- 参数来源：[[BJT Operating Regions and Large-Signal Model]]、[[BJT Output Characteristics and the Early Effect]]。
- 同一套线性化方法的第一次出现：[[Diode Models and Small-Signal Resistance]]。
- 直接应用：[[Common-Emitter Stage]]、[[Common-Base Stage and Emitter Follower]]。
- 更偏 IC 视角的 $g_m$/$r_o$ 直觉：[[Caltech Analog Circuit Design-115N-Small-Signal Model and gm-ro Intuition]]。
