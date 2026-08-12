---
title: "Common-Base Stage and Emitter Follower"
aliases: ["共基级", "射极跟随器", "Common-Base", "Emitter Follower", "共集电极"]
tags: [electronic_circuits, ee, bjt, amplifier]
up: "[[Electronic Circuits I MOC]]"
down: ["[[MOSFET Structure and Operation]]"]
related: ["[[Common-Emitter Stage]]", "[[CE with Emitter Degeneration and Source Resistance]]", "[[Caltech Analog Circuit Design-122N-BJT Amplifiers (2)-Emitter Follower Common-Base and Cascode]]"]
---
# Common-Base Stage and Emitter Follower

## BJT 三种组态（完结）：共基级与射极跟随器

> [!summary] 核心结论
> 三种组态是同一个器件换了「哪个端做输入、哪个端做输出」而已，但性格截然不同：
> - **共射**：电压增益大、反相，$R_{in}$ 中、$R_{out}$ 中 —— 通用放大级
> - **共基**：电压增益大、**同相**，$R_{in}=1/g_m$ **极低**，$R_{out}=R_C$ —— 电流缓冲 / 阻抗匹配 / cascode 上管
> - **射随**：电压增益 $\lesssim 1$，$R_{in}$ **极高**、$R_{out}$ **极低** —— 缓冲器，不放大电压只改变阻抗
>
> 所有结论都能由上一讲的两条阻抗速查规则直接读出。

---
## 1. 两种组态的电路

![[ec-common-base-stage-and-emitter-follower-01.svg]]

---
## 2. 共基级（CB）

输入加在**射极**，基极接固定偏压（交流地），输出取自集电极。

**输入阻抗**：由速查规则二，$R_B=0$：

$$
R_{in} = \frac{1}{g_m} = \frac{V_T}{I_C}
$$

$I_C = 0.5\,\mathrm{mA}$ 时恰好 $52\,\Omega$ —— 这就是共基级最经典的用途：**给 $50\,\Omega$ 传输线或天线做输入匹配**，调偏置电流就能调匹配。

**电压增益**：射极电流 $i_e = v_{in}/(1/g_m) = g_mv_{in}$，集电极电流同向流出，在 $R_C$ 上产生

$$
\boxed{\;A_v = +g_mR_C\;}
$$

注意是**正号**：$v_{in}\uparrow$（射极电位升高）$\Rightarrow V_{BE}\downarrow \Rightarrow I_C\downarrow \Rightarrow v_{out}\uparrow$。共基级不反相。

**输出阻抗**：$R_{out} = R_C \parallel r_o$，与共射级相同。

**电流增益**：$\alpha = \beta/(\beta+1) \approx 1$。共基级是一个近乎理想的**电流缓冲器**：电流几乎原封不动地从低阻的射极搬到高阻的集电极。

### 共基级的真正价值

单独用得不多，但它是 **cascode** 的上半部分。把共基级叠在共射级之上：

- 下管（共射）的集电极看到的负载是上管的 $1/g_m$（很低）$\Rightarrow$ 下管的电压增益接近 1 $\Rightarrow$ **密勒效应被消除**，带宽大幅提升。
- 从上管集电极看进去的输出电阻变成 $\approx g_mr_o^2$ $\Rightarrow$ 增益大幅提升。

一个结构同时解决带宽和增益，这是模拟 IC 里使用频率最高的技巧之一。

---
## 3. 射极跟随器（EF / 共集）

输入加在基极，输出取自射极，集电极接 $V_{CC}$（交流地）。

**电压增益**：射极上的分压

$$
\boxed{\;A_v = \frac{R_E}{R_E + 1/g_m} \;\lesssim\; 1\;}
$$

永远小于 1，但通常很接近 1（$R_E \gg 1/g_m$ 时）。「跟随」这个名字就是这么来的：射极电位紧跟基极电位，只差一个近似恒定的 $V_{BE}\approx0.7\,\mathrm{V}$。

**输入阻抗**（速查规则一）：

$$
R_{in} = r_\pi + (\beta+1)(R_E\parallel R_L)
$$

**输出阻抗**（速查规则二）：

$$
R_{out} = \left(\frac{1}{g_m} + \frac{R_S}{\beta+1}\right) \parallel R_E
$$

$I_C=1\,\mathrm{mA}$、$\beta=100$、$R_S=10\,\mathrm{k\Omega}$ 时：$R_{out}\approx 26 + 99 = 125\,\Omega$。

### 为什么一个「不放大」的电路这么重要

回到第一讲那条式子：

$$
v_{out}=A_v\,v_s\cdot\frac{R_{in}}{R_{in}+R_S}\cdot\frac{R_L}{R_L+R_{out}}
$$

射随器把 $R_{in}$ 做得极高、$R_{out}$ 做得极低，专门消灭这两个分压因子。放在链路的前面就是**阻抗变换器**，放在最后就是**输出级**。

典型用法：一个高增益共射级（$R_{out}$ 高，带不动负载）后面接一个射随器 —— 增益由前级提供，驱动能力由后级提供。

> [!note] 电平移位
> 射随器的输出比输入低一个 $V_{BE}$。用 pnp 射随器则是高一个 $V_{EB}$。级联 npn/pnp 射随器可以做直流电平的精确平移，这在直接耦合的多级放大器里很常用。

---
## 4. 三种组态汇总

| | 共射 (CE) | 共基 (CB) | 射随 (EF) |
|---|---|---|---|
| 输入端 | 基极 | 射极 | 基极 |
| 输出端 | 集电极 | 集电极 | 射极 |
| $A_v$ | $-g_m(R_C\parallel r_o)$ | $+g_mR_C$ | $\dfrac{R_E}{R_E+1/g_m}\lesssim 1$ |
| 相位 | 反相 | 同相 | 同相 |
| $R_{in}$ | $r_\pi$（中） | $1/g_m$（**极低**） | $r_\pi+(\beta+1)R_E$（**极高**） |
| $R_{out}$ | $R_C\parallel r_o$（中） | $R_C\parallel r_o$（中） | $\dfrac{1}{g_m}+\dfrac{R_S}{\beta+1}$（**极低**） |
| 电流增益 | $\beta$ | $\approx 1$ | $\beta+1$ |
| 典型用途 | 通用增益级 | 阻抗匹配、cascode | 缓冲、输出级 |

**记忆线索**：接地的那个端子决定组态名，而**输入端决定 $R_{in}$**（基极高、射极低），**输出端决定 $R_{out}$**（集电极高、射极低）。

---
## 5. 与其他笔记的关系

- 前两讲：[[Common-Emitter Stage]]、[[CE with Emitter Degeneration and Source Resistance]]。
- 阻抗速查规则的来源：[[BJT Small-Signal Model]]。
- MOS 里的完全对应版本：[[Common-Gate Stage and Source Follower]]。
- cascode 的详细讨论：[[Caltech Analog Circuit Design-122N-BJT Amplifiers (2)-Emitter Follower Common-Base and Cascode]]。
