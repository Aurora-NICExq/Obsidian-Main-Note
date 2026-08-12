---
tags:
  - AnalogCircuitDesign
  - SmallSignal
  - MOSFET
  - BJT
source_srt: "srt字幕文件/加州理工学院【中英⚡模拟电路设计|2019 Analog Circuit Design】 - 015 - p14 115N. Small-signal model, MOS vs. BJT, core transistor behavior, transconduc.srt"
---

# Caltech｜模拟电路设计（2019）115N：小信号模型（Small-Signal）与 $g_m/r_o$ 的直觉

这节课的重心从“器件方程有多精确”转向“电路设计真正关心什么”。很多时候你不需要完整的非线性解析式；你更需要的是：在某个偏置点附近，输出对输入的**斜率**是多少——也就是小信号参数（$g_m,r_o$ 等）。

---

## 1) 小信号是什么：在工作点附近做线性化

把电压/电流分解为“直流偏置 + 小扰动”（课堂用大小写/小写区分）：
$$
v(t)=V_Q+v(t),\qquad i(t)=I_Q+i(t).
$$

如果器件关系是非线性的 $I=I(V)$，那么在 $V_Q$ 附近可以用一阶泰勒展开：
$$
i \approx \left.\frac{dI}{dV}\right|_{Q}\,v.
$$

这个导数就是你之后在放大器里天天用的“增益源头”：跨导 $g_m$、电阻（导纳）等。讲座也强调：小信号模型一旦建立，就能把问题交给线性电路分析工具（节点分析、叠加、等效定理……）。

---

## 2) BJT：指数律 → $g_m=\dfrac{I_C}{V_T}$（附经典数值例子）

前向有源区近似：
$$
I_C \approx I_S e^{V_{BE}/V_T},\qquad V_T=\frac{kT}{q}\approx 25.8\text{ mV @ 300K}.
$$
对 $V_{BE}$ 求导：
$$
g_m:=\frac{\partial I_C}{\partial V_{BE}} \approx \frac{I_C}{V_T}.
$$

讲座给的“必须背下来的数量级”：
- 若 $I_C=1\text{ mA}$，则
  $$
  g_m \approx \frac{1\text{ mA}}{25\text{ mV}} \approx 40\text{ mS}
  $$
  对应“等效小电阻”
  $$
  r_e:=\frac{1}{g_m}\approx 25\ \Omega.
  $$

此外，BJT 还会有输出电阻 $r_o$（早期效应）：
$$
r_o \approx \frac{V_A}{I_C}.
$$

> 通俗理解：BJT 的“好东西”就是这个很大的 $g_m$（单位电流能换来很陡的斜率）；而 $r_o$、寄生电容等很多时候是你不得不忍受的“坏东西”。

---

## 3) MOSFET：不求“全局精确”，但要会抽 $g_m$ 与 $r_o$

讲座强调：MOSFET 的 $I_D(V_{GS})$ 可能是二次的、线性的、介于两者之间；对电路而言最关键仍是工作点的导数：
$$
g_m:=\frac{\partial I_D}{\partial V_{GS}}.
$$

常见近似（建立手感）：
- 长沟道饱和区（平方律）：
  $$
  I_D\approx \frac12\mu C_{ox}\frac{W}{L}V_{ov}^2,\quad V_{ov}=V_{GS}-V_T
  $$
  $$
  g_m\approx \mu C_{ox}\frac{W}{L}V_{ov}=\frac{2I_D}{V_{ov}}.
  $$
- 速度饱和深时：$I_D$ 对 $V_{ov}$ 更接近线性 ⇒ $g_m$ 的依赖会变化（课堂提到“跨导由最大速度决定”）。

MOSFET 的输出电阻来自沟道长度调制：
$$
r_o \approx \frac{1}{\lambda I_D}.
$$

---

## 4) “电流控制还是电压控制？”——关键不在口号，在阻抗

讲座问了一个经典陷阱：BJT 是“电流控制电流源”还是“电压控制电流源”？

结论不是二选一，而是：
> 这取决于你怎么驱动它、源阻抗多大、输入端口阻抗多高。

更稳妥的说法是：
- 高阻抗驱动/感知 ⇒ 更像“电压驱动/电压传感”
- 低阻抗驱动/感知 ⇒ 更像“电流驱动/电流传感”

这条原则会反复出现：很多“到底像电压源还是电流源”的争论，最终都归结为端口阻抗。

---

## 5) MOS vs BJT：为什么看起来 BJT 更“强”，但 MOS 更常见

讲座抛出一个很现实的问题：
> BJT 在相同电流下往往能给更大的 $g_m$（更强的增益能力），那为什么现实里大多数晶体管是 MOS？

课堂给出的关键理由之一：
- MOS 栅极几乎不需要直流电流（输入阻抗高），驱动更容易
- 工艺与系统层面的优势（尤其 CMOS 的开关与集成生态）让 MOS 成为主流

学习者视角：模拟设计里经常是在“BJT 的 $g_m$ 优势”和“MOS 的系统级优势（驱动/功耗/可扩展集成）”之间做取舍。

