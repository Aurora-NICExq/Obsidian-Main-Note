---
aliases:
  - 性能与设计权衡
  - Performance Measures
  - Latency Throughput
  - CPI Amdahl
  - Area Power Performance
  - L07 Performance Measures
tags: [cs, computer_architecture]
up: "[[Computer Organization and Architecture (MIT 6.004) MOC]]"
related:
  - "[[Sequential Logic and Finite State Machines]]"
  - "[[Combinational Logic]]"
  - "[[Instruction Set Architecture]]"
---
# 性能与设计权衡

> [!summary] 核心结论
> 电路层看 **延迟（latency）** 与 **吞吐（throughput）**：组合块 latency $\approx t_{\mathrm{PD}}$，吞吐 $\approx 1/t_{\mathrm{PD}}$；流水线用寄存器切开长路径，吞吐升、单任务延迟往往不降反升。处理器层常用
> $$
> T_{\mathrm{CPU}} = \mathrm{IC}\times\mathrm{CPI}\times T_{\mathrm{clk}}.
> $$
> 加速受 **Amdahl 定律** 束缚：不可并行 / 不可优化部分会封顶整体增益。真实芯片在 **面积、功耗、性能** 三维上折中，而不是单点最优。

> 底本：MIT 6.004 *Computation Structures* L07 Performance Measures；处理器时间公式与 Amdahl 为体系结构通用工具（与 6.004 后续流水线 / 平行单元衔接）。见 computationstructures.org。

---
## 1. 延迟与吞吐

对处理“一件工作”的系统：

| 量 | 含义 | 组合电路（无流水） |
|----|------|-------------------|
| **Latency** | 从输入合法到对应输出合法的时间 | $t_{\mathrm{PD}}$ |
| **Throughput** | 单位时间完成的工作数 | $1/t_{\mathrm{PD}}$ |

二者相关但不等价：流水线可以提高吞吐，却可能增加端到端延迟（更多级 × 时钟周期）。

> [!tip] 工科提问顺序
> 先问指标是 latency 还是 throughput（交互延迟 vs 服务器 QPS），再选流水、缓存、并行哪一刀。

---
## 2. 流水线直觉（与 6.004 L07）

把长组合路径切成 $K$ 段，段间插寄存器，得到 $K$-流水线：

- 时钟周期由**最慢那段**的 $t_{\mathrm{PD}}$ 决定；
- 吞吐 $\approx 1/t_{\mathrm{CLK}}$（理想、满流水）；
- 延迟 $\approx K\cdot t_{\mathrm{CLK}}$。

代价：寄存器面积与功耗、流水线寄存器开销、控制/冒险（后续流水线笔记展开）。未流水的组合电路可视为 $K=0$ 的退化情形。

---
## 3. CPU 时间铁律

对一段程序：
$$
T_{\mathrm{CPU}} = \underbrace{\mathrm{IC}}_{\text{指令数}}
\times \underbrace{\mathrm{CPI}}_{\text{平均每指令周期数}}
\times \underbrace{T_{\mathrm{clk}}}_{\text{时钟周期}}
= \frac{\mathrm{IC}\times\mathrm{CPI}}{f_{\mathrm{clk}}}.
$$

![[coa-performance.svg]]

三维都能动，且常互相耦合：

| 旋钮 | 典型手段 | 常副作用 |
|------|----------|----------|
| 降 IC | 更好算法、更强 ISA、编译优化 | 单指令可能更复杂 → CPI↑ |
| 降 CPI | 流水线、缓存、分支预测、超标量 | 硬件面积/功耗↑；冒险时 CPI 回升 |
| 降 $T_{\mathrm{clk}}$ | 更深流水、更快工艺、短路关键路径 | 级数↑、开销↑；功耗↑ |

> [!example] 谁更快？
> 机器 A：$f=2\,\mathrm{GHz}$，$\mathrm{CPI}=2$，程序 $\mathrm{IC}=10^9$。
> $$
> T_A=10^9\cdot 2\cdot 0.5\,\mathrm{ns}=1\,\mathrm{s}.
> $$
> 机器 B：$f=1\,\mathrm{GHz}$，$\mathrm{CPI}=1.2$，同程序若 $\mathrm{IC}$ 相同：
> $$
> T_B=10^9\cdot 1.2\cdot 1\,\mathrm{ns}=1.2\,\mathrm{s}.
> $$
> 只比主频会误判——必须带上 CPI 与 IC。

---
## 4. Amdahl 定律（简述）

若系统中可加速部分占比为 $f$（$0\le f\le 1$），该部分加速 $s$ 倍，则整体加速比
$$
S_{\mathrm{overall}}=\frac{1}{(1-f)+f/s}\le\frac{1}{1-f}.
$$
$s\to\infty$ 时上界为 $1/(1-f)$：**串行或未优化残差**决定天花板。

> [!example] 只优化 40%
> $f=0.4$，哪怕 $s=\infty$，$S\le 1/0.6\approx 1.67$。把精力只砸在非热点上，收益极薄。

推论：先测量瓶颈（热点指令、缓存缺失、I/O），再决定优化；并行化同理——串行段封顶加速。

---
## 5. 面积 / 功耗 / 性能三角

芯片与板级设计很少“只要最快”：

1. **面积（Area）**  
   门数、SRAM 容量、金属层、封装尺寸 → 成本与良率。更大 cache / 更宽 ALU / 更多核：性能潜力↑，面积↑。

2. **功耗（Power）与能量**  
   动态功耗粗估 $P_{\mathrm{dyn}}\propto C V^2 f$；静态漏电随工艺变显著。电池设备看能量/任务；数据中心看 TDP 与电费。降压降频省电但性能跌。

3. **性能（Performance）**  
   按场景选 latency 或 throughput；用 $T_{\mathrm{CPU}}$ 或 Spec 类基准，避免只报主频。

常见折中例子：

- 更深流水：频率↑，但 CPI 可能因冒险变差，设计复杂度↑；
- 更大 cache：命中率↑（CPI↓），但面积/能耗↑，命中延迟也可能↑；
- 多核：吞吐↑，单线程 latency 未必降，且受 Amdahl 与同步开销限制。

> [!warning] 局部最优陷阱
> 把关键路径砍短却使 IC 暴涨，或把主频拉高却让 cache 缺失惩罚（以周期计）变大——三者乘积才是墙钟时间。

---
## 6. 基准与比较时的坑

1. **用墙钟 / $T_{\mathrm{CPU}}$，不要只用 MHz**：见上例。
2. **同一可执行语义**：改 ISA 或编译选项会同时动 IC 与 CPI，必须报告完整配置。
3. **峰值 vs 持续**：Turbo、热节流、冷缓存首跑都会扭曲数字。
4. **几何平均**常用于多程序套件；算术平均会被极端值绑架——读别人的“平均加速”时先问怎么平均的。

速度up 定义要写清参照系：
$$
\mathrm{Speedup}=\frac{T_{\mathrm{old}}}{T_{\mathrm{new}}}.
$$

---
## 7. 与前后章节的接口

- **组合 / 时序**： $t_{\mathrm{PD}}$ 与 $t_{\mathrm{CLK}}$ 约束直接来自 [[Combinational Logic]]、[[Sequential Logic and Finite State Machines]]。
- **ISA / 汇编**：指令选择与调用约定影响 IC；见 [[Instruction Set Architecture]]。
- **流水线 CPU**：用吞吐换结构复杂度；性能公式里 CPI 反映停顿。
- **存储层次**：cache / VM 通过平均访存时间进入有效 CPI。
- **并行**：多发射、多核、向量——吞吐手段，仍受 Amdahl 与互连/一致性成本约束。

---
## 8. 工作例：$T_{\mathrm{CPU}}$ 与 Amdahl 联算

> [!example] 题目
> 程序 $\mathrm{IC}=8\times 10^8$。机器 X：$f=2.5\,\mathrm{GHz}$，$\mathrm{CPI}=1.6$。
> （1）求 $T_{\mathrm{CPU}}$。
> （2）优化后 30% 的指令类 CPI 降为原来的一半（其余指令 CPI 不变；近似：可加速部分占执行时间 $f=0.3$，加速比 $s=2$）。整体加速比与新 $T$？
> （3）若只能无限加速这 30%，加速比上界？

> [!success]- 参考答案
> （1）$T_{\mathrm{clk}}=0.4\,\mathrm{ns}$；$T=8\times 10^8\times 1.6\times 0.4\times 10^{-9}=0.512\,\mathrm{s}$。
> （2）$S=1/(0.7+0.3/2)=1/(0.7+0.15)=1/0.85\approx 1.176$；新 $T\approx 0.512/1.176\approx 0.435\,\mathrm{s}$。
> （3）$S\le 1/0.7\approx 1.43$。

---
## 9. 本节清单

1. 区分 latency 与 throughput；说明流水线如何改二者。
2. 会用 $T_{\mathrm{CPU}}=\mathrm{IC}\times\mathrm{CPI}\times T_{\mathrm{clk}}$ 做数量级比较；不单凭主频下结论。
3. 会写 Amdahl 公式并算简单上界；能解释“先找 $f$”。
4. 能用面积 / 功耗 / 性能三角评价一种改动的利弊（至少两点副作用）。
5. 能独立完成 CPU 时间 + Amdahl 联算自检题。

## 参考

- MIT 6.004 *Computation Structures*, L07 Performance Measures — https://computationstructures.org/lectures/performance/performance.html
- 课程笔记：https://computationstructures.org/notes/performance/notes.html
- MIT OCW：https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/
- （通用）Amdahl, G.M., “Validity of the single processor approach…”；Hennessy & Patterson 中 CPU 时间分解
