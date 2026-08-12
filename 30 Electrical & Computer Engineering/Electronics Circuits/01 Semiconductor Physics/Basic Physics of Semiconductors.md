---
title: "Basic Physics of Semiconductors"
aliases: ["半导体物理基础", "能带与掺杂", "质量作用定律"]
tags: [electronic_circuits, ee, semiconductor]
up: "[[Electronic Circuits I MOC]]"
down: ["[[Carrier Drift and Diffusion]]"]
related: ["[[Introduction to Microelectronics]]", "[[Caltech Analog Circuit Design-101N-Bands Electrons and Holes]]", "[[Doping and Carrier Statistics]]"]
---
# Basic Physics of Semiconductors

## 半导体物理基础：能带、本征载流子与掺杂

> [!summary] 核心结论
> 半导体之所以有用，是因为它的导电能力**可以被人为调节数个数量级**：掺杂决定多子浓度，而少子浓度由 $np=n_i^2$ 自动确定。
> 记住三个数：Si 的带隙 $E_g\approx1.12\,\mathrm{eV}$，常温本征浓度 $n_i\approx1.08\times 10^{10}\,\mathrm{cm^{-3}}$，热电压 $V_T=kT/q\approx26\,\mathrm{mV}$。

---
## 1. 能带：为什么半导体夹在中间

![[ec-basic-physics-of-semiconductors-01.svg]]

电子只能占据允许的能带。价带里的电子被共价键束缚住，不导电；跳到导带的电子才能自由移动。三类材料的区别只在带隙 $E_g$ 的大小：

- 绝缘体：$E_g$ 太大（$\sim8\,\mathrm{eV}$），常温下几乎没有电子跳得上去。
- 导体：导带与价带交叠，电子随时可动。
- 半导体：$E_g$ 恰好「不大不小」——常温有少量电子跳上去，且这个数量对温度、掺杂、电场都极其敏感。

本征载流子浓度随温度指数变化：

$$
n_i \propto T^{3/2}\exp\!\left(-\frac{E_g}{2kT}\right)
$$

指数里的 $E_g/2kT$ 是这门课第一次出现「指数依赖」。后面二极管方程、$I_C$–$V_{BE}$ 关系全都是同一个玻尔兹曼因子的不同外衣。

> [!note] 温度的实际后果
> Si 的 $n_i$ 大约每升温 $10\,^\circ\mathrm{C}$ 翻一倍。这是二极管反向饱和电流 $I_S$ 强烈随温度变化（$I_S\propto n_i^2$，约每 $5\,^\circ\mathrm{C}$ 翻倍）的根源，也是后面偏置电路必须做温度补偿的原因。

---
## 2. 电子与空穴

价带里被电子留下的空位表现得像一个带正电、有有效质量的粒子，称为**空穴**。这不是数学把戏——空穴确实以自己的迁移率在晶格里移动，且比电子慢（Si 中约慢 3 倍）。

本征半导体里电子空穴成对产生：

$$
n = p = n_i
$$

---
## 3. 掺杂：把多子浓度提高几个数量级

![[ec-basic-physics-of-semiconductors-02.svg]]

- **$n$ 型**：掺五价元素（P、As）。每个施主原子贡献一个「多余」电子，$n\approx N_D$。
- **$p$ 型**：掺三价元素（B）。每个受主原子留下一个空位，$p\approx N_A$。

典型掺杂浓度 $10^{15}\sim10^{19}\,\mathrm{cm^{-3}}$，相比 $n_i\approx10^{10}\,\mathrm{cm^{-3}}$ 高出 5–9 个数量级。所以掺杂后的半导体，多子浓度基本就等于掺杂浓度，与温度关系不大（在正常工作温区内）。

---
## 4. 质量作用定律

热平衡下，无论怎么掺杂，都有：

$$
np = n_i^2
$$

这是这一讲最有用的一条公式。它的意思是：**把多子提上去，少子就被自动压下来**。

例：$n$ 型 Si，$N_D=10^{16}\,\mathrm{cm^{-3}}$，则

$$
n\approx10^{16}\,\mathrm{cm^{-3}},\qquad
p=\frac{n_i^2}{n}=\frac{(1.08\times10^{10})^2}{10^{16}}\approx1.2\times 10^{4}\,\mathrm{cm^{-3}}
$$

少子比多子少 12 个数量级。这就是为什么在 $n$ 区里可以放心地说「电流全由电子承担」。

而 PN 结、BJT 的工作恰恰**全靠少子**——正是因为少子的平衡浓度极低，注入一点点就能造成几个数量级的相对变化，才有了指数型的 $I$–$V$ 特性。

---
## 5. 电中性

掺杂后材料整体仍然电中性（施主原子失去电子后变成固定的正离子，与自由电子的负电荷抵消）：

$$
n + N_A^- = p + N_D^+
$$

联立 $np=n_i^2$ 可以解出任意掺杂下的精确 $n,p$。在 $N_D\gg n_i$ 时退化成 $n\approx N_D$。

这条式子在下一讲会用到：耗尽区之所以有净电荷，正是因为自由载流子被扫走后，**固定的电离杂质失去了抵消对象**。

---
## 6. 与其他笔记的关系

- 下一讲讲这些载流子怎么运动：[[Carrier Drift and Diffusion]]。
- 同主题的 Caltech 版讲法：[[Caltech Analog Circuit Design-101N-Bands Electrons and Holes]]、[[Doping and Carrier Statistics]]。
