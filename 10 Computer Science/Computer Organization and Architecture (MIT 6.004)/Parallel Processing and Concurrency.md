---
aliases:
  - 并行与并发
  - Parallel Processing
  - Concurrency
  - 多核
  - 同步
tags: [cs, computer_architecture]
up: "[[Computer Organization and Architecture (MIT 6.004) MOC]]"
related:
  - "[[Interrupts Devices and IO]]"
  - "[[Memory Hierarchy and Caches]]"
  - "[[Virtual Memory]]"
  - "[[Performance and Design Tradeoffs]]"
down: ""
---
# 并行处理与并发

> [!summary] 核心结论
> 单核频率与 ILP 撞墙后，性能靠 **多核 / 多线程** 挖吞吐。共享内存模型下，线程经 Cache 一致性看见同一地址空间，但**数据竞争**必须用 **锁、原子操作** 等同步手段约束。并行带来通信与同步开销；**Amdahl 定律** 指出串行残差限制加速比。6.004 在此建立“硬件能并行什么、软件必须保证什么”的接口直觉，而非展开完整并行算法课。

> 底本：[Computation Structures](https://computationstructures.org/) / MIT 6.004（Parallelism & synchronization 导论）。

---
## 1. 为何并行

[[Performance and Design Tradeoffs]] 中的 CPU 时间公式

$$
T=\mathrm{IC}\times\mathrm{CPI}\times T_{\mathrm{clk}}
$$

在单线程上可压的空间有限：$T_{\mathrm{clk}}$ 受功率与线延迟约束，CPI 受依赖与存储层次约束。转向：

- **多核（multicore）**：多套流水线 + 私有 L1（常共享 LLC）。
- **同时多线程（SMT）**：一核多硬件上下文，填补停顿槽。
- **向量 / SIMD**：一条指令多数据（课内点到为止）。

目标从“单任务最低延迟”扩展到“吞吐与能效”。

![[coa-parallel.svg]]

---
## 2. 共享内存模型

典型芯片多处理器（CMP）：

- 各核有私有 Cache；经总线 / 互连接 **共享主存**（及共享末级 Cache）。
- 进程内多线程默认共享同一 VA 空间（见 [[Virtual Memory]]）→ 通过普通 load/store 通信。
- 硬件 **Cache 一致性协议**（MESI 等）试图维持“每个地址在逻辑上只有一个当前值”的幻象——但**何时对其他线程可见**仍由内存模型与同步原语定义。

> [!tip] 并发 vs 并行
> **并发（concurrency）**：逻辑上多个任务交替/交错推进（单核也可）。**并行（parallelism）**：同一时刻多硬件真正同时执行。软件竞态两者都会遇到。

---
## 3. 数据竞争与正确性

两线程无同步地一写一读（或双写）同一变量 → **data race**：结果依赖交织，可出现撕裂值、丢失更新。

经典丢失更新：

$$
\texttt{count++} \equiv \text{load }c;\; c\leftarrow c+1;\; \text{store }c.
$$

两核交错执行 → 可能只加一次。正确性需要：**互斥** 或 **原子 RMW**。

---
## 4. 同步：锁与原子

### 4.1 锁（Lock / Mutex）

- `lock()`：获得互斥；失败则等待（自旋或休眠）。
- 临界区只被一个持有者执行。
- `unlock()`：释放，唤醒等待者。

实现依赖硬件原语：`test-and-set`、`compare-and-swap (CAS)`、`LL/SC` 等 **原子 read-modify-write**。纯 load/store 在弱假设下难以实现互斥（需认真读内存模型；课内强调“需要原子性支持”即可）。

### 4.2 原子变量直觉

对计数器、旗标，可用 atomic add / CAS 避免粗粒度锁；仍需理解 **顺序与可见性**（acquire/release 等），否则周围读写仍可乱序观测。

### 4.3 死锁与优先级

多锁嵌套：顺序不一致 → 死锁。实时系统中还有优先级反转（可用优先级继承等缓解）——与 [[Interrupts Devices and IO]] 中 ISR 与线程共享数据相同族问题。

---
## 5. 通信模式

| 模式 | 机制 | 特点 |
|------|------|------|
| 共享变量 | load/store + 同步 | 低延迟；易竞态 |
| 消息传递 | send/receive（网络 / 邮箱） | 显式通信；拷贝开销 |
| 生产者–消费者 | 有界缓冲 + 空/满条件 | 结构化同步 |

共享内存机器上消息传递可在用户态用缓冲模拟；分布式则只能消息或 RDMA 类机制。

通信 **带宽 / 延迟** 往往限制可扩展规模：计算/通信比过低时，加核不加速。

---
## 6. 扩展性界限

### 6.1 Amdahl 定律

可并行比例 $f$，核数 $N$，理想加速比

$$
S(N)=\frac{1}{(1-f)+f/N}\le\frac{1}{1-f}.
$$

即使 $N\to\infty$，串行残差 $1-f$ 封顶。**先减少串行与同步热点，再堆核。**

### 6.2 实际开销

- 同步：锁竞争、缓存行 **false sharing**（无关变量落同一 cache line，来回作废）。
- 一致性流量：写使其他核 Cache 行无效 → 带宽与延迟。
- 负载不均衡：最慢 worker 决定完成时间。
- 能耗：暗硅与功耗墙限制同时点亮的核数。

> [!example] False sharing
> 每线程写 `counter[tid]`，若数组紧密排列，可能共享一行 → 表现像激烈争用。填充对齐到 line 边界可消解。

---
## 7. 与课程其它块的连接

- **Cache**（[[Memory Hierarchy and Caches]]）：一致性与 false sharing 是多核版“存储层次税”。
- **中断 / OS**：调度把线程迁核 → 迁移后冷 Cache；自旋锁在关抢占假设下语义不同。
- **流水线**：单核 ILP 是“指令级并行”；多核是“线程级并行”——层次不同，可叠加。

---
## 8. 设计清单（工程直觉）

1. 先测串行瓶颈（Amdahl），再并行。
2. 最小化共享可变状态；能私有就私有。
3. 临界区要短；优先无锁/原子仅用于简单更新。
4. 注意 cache line 对齐与 false sharing。
5. 用工具查 data race（TSAN 等）——课内概念，课外实践。

---
## 9. 工作例：丢失更新与锁修复

> [!example] 竞态交织
> 共享 `count=0`。线程 T0、T1 各执行一次 `count++`（load / +1 / store，非原子）：
>
> | 时间 | T0 | T1 | `count` 内存 |
> |------|----|----|--------------|
> | 1 | load → 0 | | 0 |
> | 2 | | load → 0 | 0 |
> | 3 | add → 1 | | 0 |
> | 4 | | add → 1 | 0 |
> | 5 | store 1 | | 1 |
> | 6 | | store 1 | **1**（期望 2）|

> [!example] 修复素描
> ```text
> lock(mutex);
> count = count + 1;   // 临界区：同一时刻仅一线程
> unlock(mutex);
> ```
> 或 `atomic_fetch_add(&count, 1)`（硬件 RMW）。锁保证 mutual exclusion；原子加把三步收成不可分割更新。

> [!example] 自检
> （1）上表若 T0 在时刻 3 就 store，再让 T1 load，最终 `count`？还是 data race 吗？
> （2）两把锁 `lockA`/`lockB`：T0 先 A 后 B，T1 先 B 后 A——可能发生什么？
> （3）Amdahl：$f=0.8$（可并行），$N=8$ 核，理想 $S(8)$？上界？

> [!success]- 参考答案
> （1）T0 store 后内存为 1，T1 load 得 1，再 store 2 → **结果偶可正确**，但仍是 **data race**（无同步的并发读写）；换另一种交织仍可能丢更新。正确性不能靠“碰巧”。
> （2）**死锁**：循环等待对方持有的锁。
> （3）$S(8)=1/(0.2+0.8/8)=1/(0.2+0.1)=1/0.3\approx 3.33$；上界 $1/0.2=5$。

---
## 10. 本节清单

1. 说明多核共享内存 + 私有 Cache 的基本图景及一致性直觉。
2. 能举丢失更新例子，并说明锁 / CAS 如何修复。
3. 区分并发与并行；列出共享内存与消息传递的利弊。
4. 会写 Amdahl 公式并解释 $S\le 1/(1-f)$。
5. 认识 false sharing、锁竞争与通信开销对扩展性的限制。
6. 能画出两线程 `count++` 的错误交织表，并写出加锁修复。

## 参考

- MIT 6.004 *Computation Structures*：Parallel processing / synchronization 导论（[computationstructures.org](https://computationstructures.org/)）
- MIT OCW 6.004：[Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/)
- 性能折中背景：[[Performance and Design Tradeoffs]]
