---
title: "Common-Emitter Stage"
aliases: ["共射级", "CE Stage", "共射极放大器"]
tags: [electronic_circuits, ee, bjt, amplifier]
up: "[[Electronic Circuits I MOC]]"
down: ["[[CE with Emitter Degeneration and Source Resistance]]"]
related: ["[[BJT Small-Signal Model]]", "[[BJT Biasing Schemes]]", "[[Caltech Analog Circuit Design-121N-BJT Common-Emitter and Emitter Degeneration]]"]
---
# Common-Emitter Stage

## 共射级：增益、阻抗与摆幅

> [!summary] 核心结论
> $$A_v = -g_m(R_C\parallel r_o),\qquad R_{in}=r_\pi,\qquad R_{out}=R_C\parallel r_o$$
> 把 $g_m=I_C/V_T$ 代进去得到本讲最重要的一条直觉：
> $$|A_v| = \frac{I_CR_C}{V_T} = \frac{V_{R_C}}{V_T}$$
> **增益 = $R_C$ 上的直流压降 ÷ 26 mV**。增益上限被电源电压直接卡死，这条约束推动了后面所有更复杂的拓扑。

---
## 1. 电路与工作原理

![[ec-common-emitter-stage-01.svg]]

射极交流接地，输入加在基极，输出取自集电极。

定性理解：$v_{in}\uparrow \Rightarrow V_{BE}\uparrow \Rightarrow I_C\uparrow \Rightarrow R_C$ 上压降$\uparrow \Rightarrow v_{out}=V_{CC}-I_CR_C\downarrow$。

所以共射级是**反相**放大器 —— 那个负号不是记号约定，是物理事实。

---
## 2. 小信号推导

![[ec-common-emitter-stage-02.svg]]

用混合 π 模型。输出节点的 KCL（$v_\pi = v_{in}$，因为射极接地）：

$$
g_m v_\pi + \frac{v_{out}}{r_o} + \frac{v_{out}}{R_C} = 0
$$

$$
\boxed{\;A_v = \frac{v_{out}}{v_{in}} = -g_m\,(R_C\parallel r_o)\;}
$$

**输入阻抗**：从基极看进去，射极接地（$R_E=0$），由速查规则得

$$
R_{in} = r_\pi = \frac{\beta V_T}{I_C}
$$

**输出阻抗**：$v_{in}$ 置零 $\Rightarrow v_\pi=0 \Rightarrow$ 受控源变成开路，只剩

$$
R_{out} = R_C\parallel r_o
$$

---
## 3. 「增益 = 压降 / 26 mV」

这是共射级最该记住的一条。忽略 $r_o$（当 $R_C\ll r_o$ 时）：

$$
|A_v| = g_mR_C = \frac{I_C}{V_T}R_C = \frac{I_CR_C}{V_T} = \frac{V_{R_C}}{V_T}
$$

推论一串：

- **增益与 $I_C$ 无关**（只要 $V_{R_C}$ 不变）。加大电流的同时按比例减小 $R_C$，增益一点不变 —— 只是带宽变好、噪声变低、功耗变大。
- **增益被电源卡死**。$V_{R_C} < V_{CC}$，所以 $|A_v| < V_{CC}/V_T$。$V_{CC}=3\,\mathrm{V}$ 时理论上限 $115$，实际留摆幅后只能做到 $50\sim 60$。
- **想要更高增益只有一条路**：换一个「直流压降小、但交流电阻大」的负载 —— 这正是电流源负载和 cascode 的动机。

用电流源负载时增益趋于本征增益：

$$
|A_v|_{max} = g_mr_o = \frac{V_A}{V_T} \approx 3800
$$

---
## 4. 输出摆幅

上摆的限制：$v_{out}$ 不能超过 $V_{CC}$。
下摆的限制：$V_{CE}$ 不能低于 $V_{CE,sat}\approx 0.2\,\mathrm{V}$，否则进饱和、波形削底。

$$
V_{CE,Q} - V_{CE,sat} \;\ge\; \hat{v}_{out}
$$

设计上通常把 $V_{CE,Q}$ 放在能让上下摆幅对称的位置。

---
## 5. 共射级的缺点

诚实地列出来，因为后面每一个拓扑都是在补其中某一条：

| 缺点 | 后果 | 解法 |
|---|---|---|
| $R_{in}=r_\pi$ 不算高（kΩ 级） | 高阻信号源被分压 | 前面加射极跟随器 |
| $R_{out}=R_C$ 不算低 | 带不动低阻负载 | 后面加射极跟随器 |
| 增益依赖 $g_m$，而 $g_m$ 依赖 $I_C$、温度 | 增益不精确 | 加 $R_E$ 退化 |
| 大信号下 $I_C$ 指数非线性 | 失真 | 加 $R_E$ 退化 |
| 增益 × 摆幅被 $V_{CC}$ 卡死 | 低压下做不出高增益 | 电流源负载、cascode |
| 密勒效应（$C_\mu$ 被增益放大） | 带宽差 | cascode |

---
## 6. 与 MOS 共源级的对照

结构完全同构，把 $r_\pi\to\infty$ 即可：

| | 共射级 (BJT) | 共源级 (MOS) |
|---|---|---|
| $A_v$ | $-g_m(R_C\parallel r_o)$ | $-g_m(R_D\parallel r_o)$ |
| $R_{in}$ | $r_\pi$（有限） | $\infty$（直流） |
| $R_{out}$ | $R_C\parallel r_o$ | $R_D\parallel r_o$ |
| $g_m$ | $I_C/V_T$ | $\sqrt{2\mu_nC_{ox}(W/L)I_D}$ |
| 本征增益 | $V_A/V_T$，与 $I$ 无关 | $2/(\lambda V_{ov})$，可设计 |

详见 [[MOS Biasing and the Common-Source Stage]]。

---
## 7. 与其他笔记的关系

- 前置：[[BJT Small-Signal Model]]、[[BJT Biasing Schemes]]。
- 下一讲加上射极电阻：[[CE with Emitter Degeneration and Source Resistance]]。
- 另外两种组态：[[Common-Base Stage and Emitter Follower]]。
- Caltech 版讲法：[[Caltech Analog Circuit Design-121N-BJT Common-Emitter and Emitter Degeneration]]。
