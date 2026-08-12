---
tags:
  - AnalogCircuitDesign
  - MOSFET
  - Amplifier
  - SourceDegeneration
  - SmallSignal
  - OutputResistance
source_srt: "srt字幕文件/加州理工学院【中英⚡模拟电路设计|2019 Analog Circuit Design】 - 023 - p22 123N. (Pt. 1) MOS amplifier stages： Source degeneration, input and output im.srt"
---

# Caltech｜模拟电路设计（2019）123N（Part 1）：MOS 共源放大器、源退化（Source Degeneration）与输入/输出阻抗

这一讲把“单管放大级”从 BJT 平移到 MOSFET：同样追求增益、线性、阻抗特性，但**器件的 $I$–$V$ 形式不同**（BJT 指数，MOS 常用二次近似），所以设计直觉与“敏感参数”也不同。

---

## 1) 基本共源（无退化）：大信号下天然非线性，且强依赖器件参数

最基本的 NMOS 共源（电阻负载 $R_D$）：
$$
V_{out}=V_{DD}-I_D R_D.
$$
若在饱和区用平方律近似：
$$
I_D \approx \frac{\mu C_{ox}}{2}\frac{W}{L}(V_{GS}-V_T)^2.
$$
讲座强调的问题和共射极完全同构：
- $I_D(V_{GS})$ 非线性（此处是“二次/速度饱和等”）
- 增益与工作点强相关
- 还强依赖 $\mu, C_{ox}, W/L, V_T$ 等内部参数

---

## 2) 源退化：在源极加电阻，把“非线性”用局部负反馈压住

做法：源极串一个 $R_S$（老师说也可理解为“终端 1 退化”）。

直觉（讲座的关键一句）：
> 我们想让电路更线性，并且更多由外部参数控制，而不是由晶体管内部参数控制。

核心等式就是“输入被分掉”：
$$
v_{in}=v_{gs}+i_d R_S.
$$
当输入试图让 $i_d$ 增大时，$i_dR_S$ 同步增大 ⇒ 抬高源电位 ⇒ **削弱 $v_{gs}$ 的增加** ⇒ 负反馈成立。

---

## 3) 小信号增益：被同一个因子缩小（更适合设计）

先忽略沟道长度调制（$r_o\to\infty$）与体效应（$g_{mb}=0$），共源带源退化的常用近似：
$$
A_v \approx -\frac{g_m R_D}{1+g_m R_S}
      = -\frac{R_D}{R_S+\frac{1}{g_m}}.
$$
讲座特别提到：从“设计”角度，**写成电阻比**更直观——你是在用 $R_S$ 把增益“钳住”，不再完全由 $g_m$ 漂移决定。

---

## 4) 输入电阻：经典低频 MOS 模型下近似无穷大

讲座给的通用流程：加测试电压/电流，测另一端，取比值。

对 MOS 栅极（低频、理想模型），测试电压下栅电流近似为 0：
$$
R_{in}\to\infty.
$$
老师还用类比把它说成“$\beta\to\infty$”（因为 $\alpha=1\Rightarrow \beta=\alpha/(1-\alpha)\to\infty$）。

---

## 5) 输出电阻：源退化会把 $r_o$ 放大（体效应会再乘一个小因子）

讲座推进到“必须会算”的输出电阻：把独立源置零、在输出端加测试源，利用小信号模型求 $r_{out}$。

结论（以 $r_o$ 为主）：
- 源退化会让输出电阻变大，近似可写成
$$
r_{out}\approx r_o\bigl(1+g_m R_S(1+\chi)\bigr),
\quad \chi\equiv \frac{g_{mb}}{g_m}.
$$
其中 $\chi$ 来自体效应（讲座称 backgate effect），典型量级 $0.1\sim0.2$，老师把它归类为“10% 级别的二阶项”。

同时讲座也指出一个很有用的记忆点：
> 输出电阻的放大因子，和增益被缩小的因子，本质上是同一类“$1+g_mR_S$”结构。

---

## 6) 体效应（Body effect）在这里为什么会冒出来？

讲座用一句话复习体效应：$V_T$ 会随 $V_{SB}$ 改变，本质上是耗尽层宽度变化引起的场变化（强反转条件 $2\phi_F$ 之类的细节在前面讲过）。

工程上记住两点就够用：
- 集成电路里体端通常接固定电位（例如衬底/阱），源极未必在同电位 ⇒ $V_{SB}\neq 0$ 很常见
- 一旦源节点不再是交流地（比如源退化/共模分析），体效应更容易进入小信号等效

---

## 7) 一个“5 秒估算”的例子：用 $R_S$ 把增益钳到目标

假设（数量级）：
- $g_m=5\text{ mS}\Rightarrow 1/g_m=200\Omega$
- $R_D=10\text{k}\Omega$
- 选 $R_S=1\text{k}\Omega$

则
$$
A_v\approx -\frac{10\text{k}}{1\text{k}+0.2\text{k}}\approx -8.3.
$$
直觉：只要 $R_S \gg 1/g_m$，增益主要由 $R_D/R_S$ 决定 ⇒ 对工艺/温度导致的 $g_m$ 漂移更不敏感。

