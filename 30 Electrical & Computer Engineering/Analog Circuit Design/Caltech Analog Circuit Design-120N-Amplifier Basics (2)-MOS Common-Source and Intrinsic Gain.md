---
tags:
  - AnalogCircuitDesign
  - Amplifier
  - MOSFET
  - SmallSignal
source_srt: "srt字幕文件/加州理工学院【中英⚡模拟电路设计|2019 Analog Circuit Design】 - 020 - p19 120N. (Pt.2) Amplifier Fundamentals, MOS, BJT, and ATD (arbitrary 3-terminal.srt"
---

# Caltech｜模拟电路设计（2019）120N（Part 2）：MOS 共源放大器、$g_m$/$r_o$ 与“最大内在增益”

这节课把 Part 1 的放大器框架完整套到 MOSFET：从大信号 $I_D$ 模型出发，抽取小信号参数 $g_m,r_o$，再得到共源级的增益表达式，并讨论如何通过设计去提高 $g_m r_o$。

---

## 1) 大信号回顾：MOSFET 的 $I_D$ 模型与沟道长度调制

讲座把 MOS 的饱和区写成“平方/线性两种可能”，但强调：形式细节不是最关键，关键是你能在工作点取导数。

典型长沟道饱和（平方律）：
$$
I_D \approx \frac12\mu C_{ox}\frac{W}{L}(V_{GS}-V_T)^2\,(1+\lambda V_{DS})
$$
其中 $\lambda$ 是沟道长度调制系数（类似 BJT 的 Early 效应）。

速度饱和深时，$I_D$ 对 $V_{ov}$ 可能更接近线性（课堂提到“变线性”），但依然可做小信号化。

---

## 2) 小信号参数：$g_m$ 与 $r_o$

### 跨导
$$
g_m := \frac{\partial I_D}{\partial V_{GS}}\Big|_{Q}
$$

### 输出电阻（来自 $I_D$ 对 $V_{DS}$ 的依赖）
$$
r_o := \left(\frac{\partial I_D}{\partial V_{DS}}\Big|_{Q}\right)^{-1}
\approx \frac{1}{\lambda I_D}.
$$

---

## 3) 共源极（common source）电压放大器：和共射极完全同构

结构（课堂命名）：
- 源极近似交流地
- 漏极上接负载电阻 $R_D$ 到 $V_{DD}$
- 输入加在栅极，输出取漏极

小信号等效：
> 一个受控电流源 $g_m v_{in}$ 拉着输出节点，通过 $R_D$ 与 $r_o$ 把电流转换成电压。

于是电压增益：
$$
A_v \approx -g_m\,(R_D\parallel R_L\parallel r_o).
$$
讲座强调“这是线性电路”，所以你可以用节点分析、叠加、等效变换等所有线性工具。

---

## 4) 最大内在增益：$A_{v0}\sim g_m r_o$，以及怎么把它做大

如果外部负载很理想（例如有效电阻很大），增益上限来自晶体管本身：
$$
A_{v0}\approx g_m r_o.
$$

讲座把“设计怎么做大”翻译成对 $g_m$ 与 $r_o$ 的操作：

### 提高 $r_o$
- $r_o\approx 1/(\lambda I_D)$
  - 减小 $\lambda$（通常通过增大沟道长度 $L$）
  - 在不违反速度/噪声/带宽要求下减小 $I_D$

### 提高 $g_m$（或提高 $g_m/I_D$）
在长沟道强反型下：
$$
g_m \approx \frac{2I_D}{V_{ov}}
\quad\Rightarrow\quad
g_m r_o \approx \frac{2}{\lambda V_{ov}}.
$$
因此：
- 降低 $V_{ov}$（更“弱驱动”）会提高 $g_m r_o$（但会牺牲速度/摆幅裕量）

讲座还提到一个非常实用的工程建议：
> 如果你不需要很快、但很需要增益，亚阈值/弱反型往往能给你更高的 $g_m/I_D$，从而获得更大的内在增益。

---

## 5) 重要观念：即使模型不完美，$g_m$ 仍然总能定义

课堂反复强调：
> 无论 $I_D(V_{GS})$ 是二次、线性还是别的形状，**小信号 $g_m$ 就是工作点的导数**。

这也是小信号方法的强大之处：你不需要对全局非线性完全精确，很多设计指标只需要局部线性化参数。

