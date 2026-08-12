---
title: "Introduction to Microelectronics"
aliases: ["微电子学导论", "Microelectronics Intro", "放大器基本概念"]
tags: [electronic_circuits, ee, amplifier]
up: "[[Electronic Circuits I MOC]]"
down: ["[[Basic Physics of Semiconductors]]"]
related: ["[[Signals and Systems MOC]]", "[[Basic Circuit Theory MOC]]"]
---
# Introduction to Microelectronics

## 微电子学导论：模拟与数字、放大器抽象、课程地图

> [!summary] 核心结论
> 电子电路这门课要回答的只有一个问题：**怎么用非线性器件（二极管、BJT、MOSFET）搭出一个线性的、可预测的放大器**。
> 全课的主线是「器件物理 → 大信号模型 → 工作点 → 小信号线性化 → 放大器指标」，后面每一讲都是这条链条上的一环。

---
## 1. 为什么要有放大器

传感器给出的信号通常小得可怜：麦克风几个 mV，天线接收的射频信号在 μV 量级，心电信号更小。而后级（ADC、扬声器、显示器）需要的是伏特级。中间这一段落差就是放大器的工作。

放大器的三个核心指标从一开始就要建立：

| 指标 | 含义 | 理想值 |
|---|---|---|
| 电压增益 $A_v$ | $v_{out}/v_{in}$ | 按需求设计 |
| 输入阻抗 $R_{in}$ | 从输入端口看进去的电阻 | $\infty$（不从信号源取电流） |
| 输出阻抗 $R_{out}$ | 从输出端口看进去的戴维南电阻 | $0$（负载不影响增益） |

![[ec-introduction-to-microelectronics-02.svg]]

实际电路里两处分压都在吃增益：

$$
v_{out}=A_v\,v_s\cdot\underbrace{\frac{R_{in}}{R_{in}+R_S}}_{\text{输入分压}}\cdot\underbrace{\frac{R_L}{R_L+R_{out}}}_{\text{输出分压}}
$$

这个式子解释了后面很多拓扑存在的理由：射极跟随器（$R_{in}$ 高、$R_{out}$ 低）之所以有用，正是因为它专门去消除这两个分压因子，哪怕它自己的电压增益还不到 1。

---
## 2. 模拟信号与数字信号

![[ec-introduction-to-microelectronics-01.svg]]

两者的根本差别不在波形，而在**噪声怎么处理**：

- 模拟：取值连续，任何叠加上来的扰动都不可分辨地变成误差，且逐级累积。
- 数字：只区分两个电平，只要噪声没把电平推过判决门限，下一级重新整形后噪声就被**完全**丢弃。

代价是数字系统需要更高的带宽和更多的器件。所以真实系统总是混合的：模拟前端（低噪声放大 + 滤波）→ ADC → 数字处理 → DAC → 模拟输出级。这门课讲的是前后两端那些不可替代的模拟电路。

> [!note] 与信号与系统的分工
> [[Signals and Systems MOC]] 关心的是「给定一个 LTI 系统，输入输出怎么算」；这门课关心的是「怎么用晶体管把那个 LTI 系统真的做出来，以及它在什么条件下才近似 LTI」。

---
## 3. 全课的方法论：大信号 → 工作点 → 小信号

这是整门课反复出现的三步，值得在第一讲就记牢：

1. **大信号分析**：用器件的非线性 $I$–$V$ 方程和直流电源，解出静态工作点 $Q$（各端电流电压）。此时电容视作开路。
2. **参数提取**：在 $Q$ 点对 $I$–$V$ 求偏导，得到小信号参数（$g_m$、$r_\pi$、$r_o$…）。
3. **小信号分析**：把直流源接地、耦合电容短路、器件换成线性等效模型，然后用**纯线性电路方法**（节点法、叠加、戴维南）求增益和阻抗。

第 3 步之所以合法，是因为在 $Q$ 点附近做了一阶泰勒展开：

$$
i(V_Q+v)\approx I(V_Q)+\left.\frac{\partial i}{\partial v}\right|_{Q}\cdot v
$$

小信号成立的前提就是那个「$v$ 足够小」——对 BJT 是 $v_{be}\ll V_T\approx26\,\mathrm{mV}$。一旦信号大到这个近似失效，就会出现失真，那属于大信号问题。

---
## 4. 课程地图

| 阶段 | 讲次 | 你会得到什么 |
|---|---|---|
| 半导体物理 | [[Basic Physics of Semiconductors]]、[[Carrier Drift and Diffusion]] | 载流子从哪来、怎么动 |
| PN 结与二极管 | [[PN Junction in Equilibrium & Reverse Bias]] → [[Zener Regulators, Limiters and Voltage Doublers]] | 第一个非线性器件，以及三种精度的模型 |
| BJT | [[Bipolar Transistor Structure and Operation]] → [[BJT Biasing Schemes]] | 第一个放大器件，$g_m$ 的由来 |
| BJT 放大器 | [[Common-Emitter Stage]] → [[Common-Base Stage and Emitter Follower]] | 三种组态的增益与阻抗 |
| MOSFET 及其放大器 | [[MOSFET Structure and Operation]] → [[Common-Gate Stage and Source Follower]] | 集成电路真正用的器件 |

---
## 5. 与其他笔记的关系

- 线性电路工具（KCL/KVL、戴维南、节点法）见 [[Basic Circuit Theory MOC]]，本课默认你已经会用。
- 频域视角、波特图、LTI 性质见 [[Signals and Systems MOC]]。
- 同一批主题的另一套讲法（Caltech 版，偏 IC 设计视角）见 [[Caltech Analog Circuit Design-119N-Amplifier Basics (1)-Gain and Three-Terminal Devices]]。
