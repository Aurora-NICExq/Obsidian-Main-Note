---
aliases:
  - 时序逻辑与有限状态机
  - Sequential Logic
  - Finite State Machines
  - Flip-Flops Registers
  - Moore Mealy
  - L05 Sequential Logic
  - L06 Finite State Machines
tags: [cs, computer_architecture]
up: "[[Computer Organization and Architecture (MIT 6.004) MOC]]"
related:
  - "[[Combinational Logic]]"
  - "[[Performance and Design Tradeoffs]]"
down:
  - "[[Performance and Design Tradeoffs]]"
---
# 时序逻辑与有限状态机

> [!summary] 核心结论
> 时序系统 = **组合逻辑** + **状态存储**。边沿触发的寄存器（由触发器构成）在时钟沿采样下一状态；周期内组合逻辑根据“当前状态 + 输入”算出“下一状态 + 输出”。**FSM** 把行为抽象成有限状态、转移与输出：Moore 输出主要看状态，Mealy 还看输入。状态编码（二进制 / 独热等）在触发器位数与组合复杂度之间权衡。

> 底本：MIT 6.004 *Computation Structures* L05 Sequential Logic、L06 Finite State Machines；见 computationstructures.org。

---
## 1. 为什么需要状态

组合逻辑无记忆：同一输入永远同一输出。协议、控制器、CPU 的取指–译码–执行都需要“现在走到哪一步”。办法：用 $K$ bit 存储当前状态，至多 $2^K$ 种可能。

骨架：

$$
\begin{aligned}
\text{next\_state} &= \delta(\text{current\_state},\,\text{inputs}),\\
\text{outputs} &= \lambda(\text{current\_state},\,\text{inputs})\quad\text{（Mealy；Moore 则不显式依赖 inputs）}.
\end{aligned}
$$
$\delta,\lambda$ 本身是组合函数。

![[coa-fsm.svg]]

---
## 2. 锁存器、触发器与寄存器

### 2.1 层次直觉

| 元件 | 行为（工程口径） |
|------|------------------|
| **锁存器（latch）** | 电平敏感：使能有效时透明，跟随输入；使能无效时保持 |
| **触发器（flip-flop）** | 边沿敏感：仅在时钟沿采样 $D$，其余时间保持 $Q$ |
| **寄存器（register）** | 多位触发器并行，共用时钟；一次装入一个字 |

D 触发器是构建同步时序系统的默认砖块：数据通路与 FSM 状态盒几乎都画成“带时钟的方框”。

> [!tip] 与数电笔记
> 门级 SR/JK、主从结构、时序参数表，见 `Digital Electronics` 的 [[Latches]]、[[Flip-Flops]]、[[Shift Registers]]、[[Counters]]；本节强调 6.004 的系统抽象：寄存器 + 组合云。

### 2.2 同步纪律（简述）

理想同步设计：

1. 所有状态只存在寄存器里；
2. 寄存器之间只有无环组合逻辑；
3. 同一时钟域内，用同一边沿采样。

时钟周期 $t_{\mathrm{CLK}}$ 必须长到让组合逻辑在下一沿到来前算完（再留建立时间裕量）。细节进入 [[Performance and Design Tradeoffs]]。

---
## 3. 时序约束一句话

对寄存器–组合–寄存器路径：
$$
t_{\mathrm{CLK}} \ge t_{\mathrm{clk\to q}}+t_{\mathrm{PD,combo}}+t_{\mathrm{setup}}
$$
（还要满足保持时间：$t_{\mathrm{hold}}$ 与污染延迟 $t_{\mathrm{CD}}$ 相关）。违反建立 → 功能错误 / 亚稳态风险；违反保持 → 即使降频也修不好。

> [!tip] 同一时钟域
> 跨时钟域不能只靠“加长组合路径”；需要同步器或握手——那是后续 SoC / 异步接口话题。

---
## 4. FSM 抽象

FSM 描述**对外行为**，不必先画门：

- 有限状态集 $S$，初始状态 $s_0$；
- 输入字母表、输出字母表；
- 转移函数 $\delta:S\times\mathrm{Inputs}\to S$；
- 输出函数 $\lambda$（见下）。

实现：用 $|S|$ 的编码占满状态寄存器；ROM / 门网实现 $\delta,\lambda$。

> [!example] 简易交通灯 / 串行识别器
> 状态 = “当前阶段”；输入 = 传感器或串行比特；输出 = 灯色或 “匹配成功”。画状态图 → 列转移表 → 编码 → 写布尔式 / 填 ROM。

---
## 5. Moore 与 Mealy

| | Moore | Mealy |
|--|-------|-------|
| 输出依赖 | 主要（或仅）当前状态 | 当前状态 **和** 当前输入 |
| 输出变化时刻 | 通常随状态在时钟沿后更新 | 输入一变，输出可立即变（经组合延迟） |
| 状态数 | 往往更多 | 往往更少 |
| 设计直觉 | 输出更“稳”、好同步 | 反应更快、接口要小心毛刺 |

6.004 实现图里：Moore 的输出逻辑只接在状态寄存器输出；Mealy 还把初级输入送进输出逻辑。

> [!warning] Mealy 毛刺
> 若输出直接驱动异步外设，输入噪声可能造成窄脉冲。对策：再同步、改为 Moore、或让后级只在时钟沿采样。

---
## 6. 状态编码

设需要 $M$ 个状态，至少 $\lceil\log_2 M\rceil$ 个触发器（二进制编码）。常用策略：

1. **二进制 / 紧凑编码**：触发器最少；下一状态逻辑可能复杂，ROM 地址短。
2. **独热（one-hot）**：$M$ 个触发器，恰好一位为 1；译码简单、FPGA 上常更快，但触发器多。
3. **格雷等特殊码**：相邻状态只变 1 bit，利于减少冒险（视应用）。

多 1 个状态位 → ROM 行数可能翻倍（若用 ROM 实现下一状态）——编码选择直接影响面积与关键路径。

> [!example] 5 态 FSM
> 二进制至少 3 bit（浪费 3 种码字，需定义非法码处理或默认转移）；独热用 5 bit。

---
## 7. 复位与非法状态

上电时触发器值可能随机。工程上几乎总要：

- **同步 / 异步复位**把状态寄存器拉到 $s_0$；
- 对未使用的编码规定默认转移（例如回到 $s_0$），避免掉进死状态。

独热编码若因 SEU / 毛刺变成“多热”，也需要检测或强制恢复——这是编码选择的另一面成本。

---
## 8. 从 FSM 到处理器控制

单周期 / 多周期 CPU 的控制器本质是大 FSM（或微码）：状态对应流水阶段或微操作；输出是各 MUX 选择、寄存器写使能、存储器读写等控制信号。数据通路是宽位寄存器 + ALU 等组合块；控制是窄位 FSM——同一张“组合 + 寄存器”图，只是位宽与含义不同。后续 [[Instruction Set Architecture]] 规定“要发出哪些控制语义”，控制器 FSM 负责在正确周期拉高对应使能。

---
## 9. 工作例：序列检测与时钟约束

> [!example] Moore 检测器（目标子串 `110`）
> 输入串行比特 $x$，检测到 `110` 时输出 $z=1$ 一拍（Moore：输出只看状态）。状态含义：
> - $S_0$：未匹配
> - $S_1$：已见 `1`
> - $S_2$：已见 `11`
> - $S_3$：已见 `110`（输出 1）
>
> 自检：（1）画转移：在 $S_2$ 若 $x=0$ 去哪？若 $x=1$ 去哪？（2）$S_3$ 吃到 $x=1$ 应去哪？
> （3）时序：$t_{\mathrm{clk\to q}}=0.3\,\mathrm{ns}$，$t_{\mathrm{PD,combo}}=1.2\,\mathrm{ns}$，$t_{\mathrm{setup}}=0.2\,\mathrm{ns}$，求 $t_{\mathrm{CLK}}$ 下界。

> [!success]- 参考答案
> （1）$S_2$+$x=0$ → $S_3$（刚凑齐 `110`）；$S_2$+$x=1$ → 仍停在“已见 `11`”的 $S_2$（末尾两个 1 可延续）。
> （2）$S_3$ 表示已识别；再来比特 1 更合理进入 $S_1$（当前比特是新前缀 `1`）。（具体编码可微调，但需覆盖重叠前缀。）
> （3）$t_{\mathrm{CLK}}\ge 0.3+1.2+0.2=1.7\,\mathrm{ns}$。

---
## 10. 本节清单

1. 能画寄存器 + 下一状态 / 输出组合逻辑的时序骨架，并解释时钟沿的作用。
2. 区分 latch（电平）与 flip-flop（边沿）；知道寄存器是并行 FF。
3. 会写 Moore / Mealy 的输出依赖差异及选用理由。
4. 会为小 FSM 做状态图 → 转移表 → 编码，并比较二进制与独热。
5. 记住建立时间对 $t_{\mathrm{CLK}}$ 的下界约束（公式级）；知道需要复位与非法码处理。
6. 能对简单序列检测器写转移，并用 $t_{\mathrm{clk\to q}}+t_{\mathrm{PD}}+t_{\mathrm{setup}}$ 估周期。

## 参考

- MIT 6.004 *Computation Structures*, L05 Sequential Logic；L06 Finite State Machines — https://computationstructures.org/lectures/sequential/sequential.html 、https://computationstructures.org/lectures/fsm/fsm.html
- 课程笔记（时序 / FSM）：https://computationstructures.org/
- MIT OCW：https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/
