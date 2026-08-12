---
title: "PN Junction in Equilibrium & Reverse Bias"
aliases: ["PN 结平衡与反偏", "耗尽区", "内建电势", "结电容"]
tags: [electronic_circuits, ee, pn_junction, diode]
up: "[[Electronic Circuits I MOC]]"
down: ["[[PN Junction Forward Bias and the Diode Equation]]"]
related: ["[[Carrier Drift and Diffusion]]", "[[Caltech Analog Circuit Design-104N-PN Junction Depletion and Diode Equation]]", "[[Caltech Analog Circuit Design-105N-Junction Capacitance and Doping Profiles]]"]
---
# PN Junction in Equilibrium & Reverse Bias

## PN 结（一）：平衡态、耗尽区与反偏结电容

> [!summary] 核心结论
> 把 $p$ 型和 $n$ 型接在一起，交界处的载流子扩散走后留下固定的电离杂质，形成**耗尽区**和一个内建电势
> $V_0=V_T\ln\dfrac{N_AN_D}{n_i^2}$。平衡的本质是漂移流与扩散流精确抵消，净电流为零 —— 注意这**不是**「什么都没发生」，而是两股大电流的抵消。
> 反偏时耗尽区展宽、结电容按 $1/\sqrt{V_0+V_R}$ 变小。

---
## 1. 平衡态是怎么建立的

$p$ 区空穴多、$n$ 区电子多，接触瞬间两者都往对面扩散。扩散走之后，留下的不是中性区，而是**失去了抵消对象的固定电离杂质**：$p$ 侧留下带负电的受主离子 $N_A^-$，$n$ 侧留下带正电的施主离子 $N_D^+$。

这些固定电荷建立起一个电场，方向恰好阻止进一步扩散。当这个「反向推力」大到与扩散趋势相等时，系统达到平衡：

$$
J_n = \underbrace{q\mu_n n E}_{\text{漂移}} + \underbrace{qD_n\dfrac{dn}{dx}}_{\text{扩散}} = 0
$$

> [!important] 平衡不等于静止
> 两股流各自都很大，只是净和为零。这一点决定了后面正偏时的行为：**只需要一点点外加电压破坏这个平衡，净电流就会指数级地涨起来**。

---
## 2. 四联图：从掺杂到电势

![[ec-pn-junction-in-equilibrium-reverse-bias-01.svg]]

这四张图之间是严格的微积分关系，值得逐层理解：

| 层 | 量 | 与上一层的关系 |
|---|---|---|
| (b) | 电荷密度 $\rho(x)$ | 耗尽近似：区内全是电离杂质，区外严格中性 |
| (c) | 电场 $E(x)$ | $\dfrac{dE}{dx}=\dfrac{\rho}{\varepsilon_s}$ —— $\rho$ 是常数，所以 $E$ 是三角形 |
| (d) | 电势 $V(x)$ | $E=-\dfrac{dV}{dx}$ —— $E$ 是三角形，所以 $V$ 是分段抛物线 |

两个关键约束：

**电荷守恒**（耗尽区整体电中性）：

$$
N_A x_p = N_D x_n
$$

所以**掺杂轻的一侧耗尽得更深**。极端情况 $p^+n$ 结（$N_A\gg N_D$）里，耗尽区几乎全部落在 $n$ 侧——这个结论在 BJT 和 MOS 的结构设计里反复被利用。

**内建电势**：

$$
V_0 = V_T\ln\frac{N_AN_D}{n_i^2}
$$

代入典型值 $N_A=N_D=10^{16}\,\mathrm{cm^{-3}}$、$n_i=1.08\times10^{10}\,\mathrm{cm^{-3}}$：

$$
V_0 = 0.026\times\ln\frac{10^{32}}{1.17\times10^{20}} \approx 0.75\,\mathrm{V}
$$

注意 $V_0$ 对掺杂只有对数依赖——掺杂改十倍，$V_0$ 才变 $60\,\mathrm{mV}$。所以硅结的内建电势总是在 $0.6\sim0.8\,\mathrm{V}$ 这个窄区间里。

> [!warning] $V_0$ 不能用万用表测出来
> 你没法把探针接上去读到 $0.75\,\mathrm{V}$。因为探针与半导体的接触本身又产生新的接触电势，整个闭合回路的电势差之和必须为零（否则就是永动机）。$V_0$ 只是**内部**的能带弯曲。

---
## 3. 耗尽区宽度

解泊松方程得到：

$$
W = x_p + x_n = \sqrt{\frac{2\varepsilon_s}{q}\left(\frac{1}{N_A}+\frac{1}{N_D}\right)V_0}
$$

典型量级：$10^{16}\,\mathrm{cm^{-3}}$ 掺杂下 $W$ 约 $0.3\,\mathrm{\mu m}$。

---
## 4. 反偏：耗尽区展宽

外加反偏电压 $V_R$（$n$ 侧接正）与内建电势同向叠加，总势垒变成 $V_0+V_R$：

$$
W(V_R) = \sqrt{\frac{2\varepsilon_s}{q}\left(\frac{1}{N_A}+\frac{1}{N_D}\right)(V_0+V_R)}
$$

势垒升高 $\Rightarrow$ 扩散流被进一步压制 $\Rightarrow$ 只剩下极小的反向饱和电流 $I_S$（由少子的产生-复合决定，nA 甚至 pA 量级）。

---
## 5. 结电容：反偏 PN 结是一个压控电容

![[ec-pn-junction-in-equilibrium-reverse-bias-02.svg]]

耗尽区是绝缘的，两侧的中性区是导电的 —— 这就是一个平行板电容，只不过「极板间距」$W$ 由电压控制：

$$
C_j = \frac{\varepsilon_s A}{W}
= \frac{C_{j0}}{\sqrt{1 + V_R/V_0}}
$$

其中 $C_{j0}$ 是零偏结电容。突变结的指数是 $1/2$，缓变结约 $1/3$。

这个「压控电容」有两重身份：

- **有用**：做成 varactor（变容二极管），是 LC 压控振荡器（VCO）的调谐元件。
- **有害**：所有晶体管内部的 pn 结都带着这个电容，它是限制放大器带宽的主要寄生。$C_j$ 越大，节点的 RC 时间常数越大。

> [!note] 一个设计上的张力
> 想要低电容就要小面积、轻掺杂；想要大电流就要大面积。这个矛盾贯穿整个模拟 IC 设计。

---
## 6. 与其他笔记的关系

- 平衡条件的物理来源：[[Carrier Drift and Diffusion]]。
- 下一讲把结正偏，得到二极管方程：[[PN Junction Forward Bias and the Diode Equation]]。
- 结电容与掺杂剖面的更细讨论：[[Caltech Analog Circuit Design-105N-Junction Capacitance and Doping Profiles]]。
