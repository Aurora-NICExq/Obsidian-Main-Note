---
title: "Half-Wave and Full-Wave Rectifiers"
aliases: ["整流电路", "半波整流", "桥式整流", "纹波"]
tags: [electronic_circuits, ee, diode, rectifier]
up: "[[Electronic Circuits I MOC]]"
down: ["[[Zener Regulators, Limiters and Voltage Doublers]]"]
related: ["[[Diode Models and Small-Signal Resistance]]", "[[Introduction to RC Circuits]]"]
---
# Half-Wave and Full-Wave Rectifiers

## 整流电路：半波、滤波电容与桥式全波

> [!summary] 核心结论
> 整流是二极管最直接的应用：利用单向导电性把交流削成单极性，再用电容把它「填平」。
> 三条要记住的量化结论：纹波 $V_R\approx\dfrac{V_p-V_{D,on}}{R_LC_1f_{in}}$；半波的 PIV $=V_p$、桥式的 PIV $=V_p$（但串两个管，压降 $2V_{D,on}$）；桥式的纹波频率是输入的两倍。

---
## 1. 半波整流

![[ec-half-wave-and-full-wave-rectifiers-01.svg]]

正半周二极管导通，输出跟随输入（低一个 $V_{D,on}$）；负半周二极管反偏截止，输出为零。

$$
v_{out} = \begin{cases}
v_{in} - V_{D,on}, & v_{in} > V_{D,on}\\
0, & \text{否则}
\end{cases}
$$

两个设计参数：

- **峰值输出** $= V_p - V_{D,on}$。低压场合这个 $0.7\,\mathrm{V}$ 的损失占比很大，所以低压整流常用肖特基二极管（$V_{D,on}\approx0.3\,\mathrm{V}$）。
- **PIV（peak inverse voltage）** $= V_p$。负半周二极管两端承受的反压峰值，选型时必须留裕量，否则击穿。

单看这个电路没什么用——输出还是脉动的。真正让它变成电源的是下一步。

---
## 2. 加滤波电容：从脉动到直流

![[ec-half-wave-and-full-wave-rectifiers-02.svg]]

并上电容后，电路的行为分成两段：

- **充电段**：$v_{in}$ 接近峰值且高于电容电压时，二极管导通，电容被充到峰值。这一段很短。
- **放电段**：其余时间二极管反偏截止，电容以 $\tau=R_LC_1$ 向负载放电。

如果 $R_LC_1 \gg T_{in}$（这是设计的必要条件），放电近似线性，纹波峰峰值：

$$
V_R \approx \frac{V_p - V_{D,on}}{R_L C_1 f_{in}}
= \frac{I_L}{C_1 f_{in}}
$$

第二个写法更好用：**纹波 = 负载电流 / (电容 × 频率)**。

> [!example] 数值感觉
> $60\,\mathrm{Hz}$、负载 $100\,\mathrm{mA}$、要求纹波 $<0.5\,\mathrm{V}$：
> $$C_1 > \frac{0.1}{0.5\times 60} \approx 3300\,\mathrm{\mu F}$$
> 这就是为什么线性电源里总有几个又大又贵的电解电容。

> [!warning] 大电容的代价
> 充电段越短，同样的电荷就要在越短时间内灌进去 —— 峰值充电电流可以是平均负载电流的几十倍。这对二极管的浪涌额定、变压器和 EMI 都是实打实的压力。「加大电容」不是免费的。

---
## 3. 桥式全波整流

![[ec-half-wave-and-full-wave-rectifiers-03.svg]]

四个二极管，每个半周都有一对导通：

- 正半周：$D_1, D_2$ 导通
- 负半周：$D_3, D_4$ 导通

不论哪个半周，电流都从下往上灌进顶部轨道，所以 $R_L$ 上的极性始终不变。

| | 半波 | 桥式全波 |
|---|---|---|
| 输出峰值 | $V_p - V_{D,on}$ | $V_p - 2V_{D,on}$ |
| 纹波频率 | $f_{in}$ | $2f_{in}$ |
| 同纹波所需电容 | $C$ | $C/2$ |
| 二极管数 | 1 | 4 |
| 需要中心抽头变压器 | 否 | 否 |

核心权衡：**多串一个二极管的压降，换来一半的电容**。在市电整流（$V_p\approx 310\,\mathrm{V}$）里 $1.4\,\mathrm{V}$ 完全可忽略，所以桥式是标准方案；在低压（$5\,\mathrm{V}$）场合这个损失就很痛，往往改用同步整流。

> [!note] 中心抽头全波整流
> 还有一种用两个二极管 + 中心抽头变压器的全波方案，压降只有 $1\times V_{D,on}$，但需要一个更贵的变压器，且每个二极管的 PIV 达到 $2V_p$。桥式赢在不挑变压器。

---
## 4. 分析整流电路的套路

1. 用**理想二极管**模型确定每个时段哪些管子导通。
2. 换成**恒压降**模型算出各段的输出电平。
3. 若有电容，把「充电快、放电慢」拆成两段，用 $I=C\,dV/dt$ 算纹波（见 [[Introduction to RC Circuits]]）。
4. 检查每个二极管的 PIV 和峰值电流是否在额定范围内。

---
## 5. 与其他笔记的关系

- 用到的二极管模型：[[Diode Models and Small-Signal Resistance]]。
- RC 放电的数学：[[Introduction to RC Circuits]]、[[Source-Free and Driven RC Response]]。
- 整流之后还要稳压：[[Zener Regulators, Limiters and Voltage Doublers]]。
