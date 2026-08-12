---
aliases:
  - 存储层次与缓存
  - Memory Hierarchy
  - Caches
  - 高速缓存
  - AMAT
tags: [cs, computer_architecture]
up: "[[Computer Organization and Architecture (MIT 6.004) MOC]]"
related:
  - "[[Virtual Memory]]"
  - "[[Pipelining the Processor]]"
  - "[[Single-Cycle Processor Datapath]]"
  - "[[Performance and Design Tradeoffs]]"
down:
  - "[[Virtual Memory]]"
---
# 存储层次与缓存

> [!summary] 核心结论
> CPU 与大容量 DRAM 之间存在巨大延迟鸿沟。利用**时间局部性**与**空间局部性**，在靠近处理器处放小而快的 **Cache**，以 **cache line（块）** 为单位搬运数据。命中率、命中时间与缺失代价共同决定 **AMAT**。组织方式（直接映射 / 组相联 / 全相联）与写策略（写通 / 写回）在命中率、硬件成本与一致性复杂度之间折中——这是 6.004 / Computation Structures 记忆系统的核心工程语言。

> 底本：[Computation Structures](https://computationstructures.org/) / MIT 6.004（存储层次与 Cache）。

---
## 1. 为什么需要存储层次

理想存储器：无限大、无限快、永不丢数据——物理上不可能。现实按**容量 ↔ 延迟 ↔ 成本**折中分层：

| 层 | 典型介质 | 相对延迟 | 容量 |
|----|----------|----------|------|
| 寄存器 | 片上 FF | 1 cycle | 极少 |
| L1 / L2 Cache | SRAM | 数～数十 cycle | KB～MB |
| 主存 | DRAM | 百 cycle 量级 | GB |
| 外存 | SSD / HDD | 十万～百万+ | TB |

上层是下层的**缓存**；正确性靠一致性协议与写策略，性能靠局部性。

![[coa-cache.svg]]

---
## 2. 局部性（Locality）

### 2.1 时间局部性（Temporal）

刚访问过的地址，短期内很可能再访问（循环变量、栈顶、热点代码）。

### 2.2 空间局部性（Spatial）

访问 $A$ 后，很可能访问 $A$ 附近地址（数组顺序扫描、顺序取指）。因此一次缺失拉一整块 **block / line**（常见 32–64 B），把邻居一并带上。

> [!tip] 编程含义
> 顺序扫描、分块（tiling）、减少跳转式随机访问，本质是在**喂养** Cache 的局部性假设。

---
## 3. Cache 行与地址拆分

主存按固定大小 $B$ 字节分块。CPU 地址拆成：

$$
\text{Address} = \underbrace{\text{tag}}_{\text{哪一块}} \;\|\; \underbrace{\text{index}}_{\text{映射到哪组/行}} \;\|\; \underbrace{\text{offset}}_{\text{块内字节}}.
$$

- **offset**：$\log_2 B$ 位，选块内字节。
- **index**：选出候选集合（直接映射时即唯一行）。
- **tag**：与行内保存的 tag 比较，判断是否命中。

每行还带 **valid** 位；写回策略下还有 **dirty** 位。

---
## 4. Hit / Miss 与三类缺失

- **Hit**：所需块已在 Cache → 按命中时间 $t_{\mathrm{hit}}$ 返回。
- **Miss**：不在 → 向下一层取块，付 **miss penalty** $t_{\mathrm{miss}}$，再完成访问（通常同时填 Cache）。

经典三类缺失（3C）：

1. **Compulsory（冷缺失）**：第一次见到该块。
2. **Capacity**：工作集大于 Cache 容量，即使全相联也会挤出。
3. **Conflict**：在有限相联度下，多块争同一组/行，即使总容量够仍缺失。

增大相联度主要压 Conflict；增大容量压 Capacity；预取等可减 Compulsory 的有效影响。

---
## 5. 映射方式

设 Cache 有 $S$ 组、每组 $E$ 路（way）、每行 $B$ 字节，则容量 $C=S\cdot E\cdot B$。

### 5.1 直接映射（Direct-mapped，$E=1$）

每个主存块只能放进唯一一行：$\mathrm{index}=(\mathrm{block\#}\bmod S)$。硬件简单、命中快，但易 Conflict（两热点块撞同一行）。

### 5.2 组相联（Set-associative，$1<E<S\cdot E$ 的常见折中）

块映射到某一组，组内 $E$ 路任选一路存放。替换策略：LRU、伪 LRU、随机等。$E=2,4,8$ 在实践中很常见。

### 5.3 全相联（Fully associative，$S=1$）

块可放任意行；无 index，整块号作 tag。Conflict 最小，但比较器多、能耗/面积大，多用于小 TLB 或极小 Cache。

$$
E\uparrow \;\Rightarrow\; \text{Conflict}\downarrow,\;\text{比较/多路选择成本}\uparrow.
$$

---
## 6. 写策略与分配

### 6.1 Write-through（写通）

命中写同时更新 Cache 与下一级。简单、利于一致性；总线写流量大。常配 **write buffer** 掩盖写延迟。

### 6.2 Write-back（写回）

只改 Cache，置 dirty；逐出时若 dirty 才写回。减写下级流量；需处理脏行与多核一致性（MESI 等，6.004 点到为止）。

### 6.3 Write-allocate vs No-write-allocate

写缺失时：先把块读入再写（write-allocate，常与写回配对），或只写下级不入 Cache（no-write-allocate，偶与写通配对）。

---
## 7. AMAT：把层次折成一个数

平均存储器访问时间：

$$
\mathrm{AMAT}=t_{\mathrm{hit}}+m\cdot t_{\mathrm{miss}},
$$

其中 $m$ 为缺失率（miss rate）。多层时可递归：

$$
\mathrm{AMAT}_{L1}=t_{L1}+m_{L1}\cdot\mathrm{AMAT}_{L2}.
$$

> [!example] 数量级直觉
> $t_{\mathrm{hit}}=1$，$t_{\mathrm{miss}}=100$，$m=0.05$ $\Rightarrow$ $\mathrm{AMAT}=1+5=6$。把 $m$ 降到 $0.01$ 则 $\mathrm{AMAT}=2$——**缺失率**往往比再抠一点命中延迟更划算（在合理范围内）。

与 [[Performance and Design Tradeoffs]] 衔接：Cache 影响有效 CPI（load/store 停顿）与程序可见延迟。

---
## 8. 与流水线 / 程序的交界

- 指令 Cache（I$）与数据 Cache（D$）常分离（哈佛结构在流水线前端常见）。
- 缺失 → 流水线 **stall**；写后读经 Cache 转发需与旁路逻辑协调（见 [[Pipelining the Processor]]）。
- 别名、自修改代码、DMA 一致性：设备写主存后 CPU Cache 可能仍持旧副本——嵌入式里要显式 clean/invalidate（见 [[STM32 MOC]] 相关实践）。

---
## 9. 设计旋钮速查

| 旋钮 | 通常效果 |
|------|----------|
| 增大 $B$ | 利空间局部性；过大浪费带宽、冲突更糟 |
| 增大 $C$ | 降 Capacity miss；成本/命中时间↑ |
| 增大 $E$ | 降 Conflict；比较逻辑↑ |
| 写回 | 减写流量；控制更复杂 |
| 多级 Cache | 用 L2 降 $t_{\mathrm{miss}}$ 有效值 |

---
## 10. 工作例：地址 → tag / index / offset

> [!example] 直接映射 Cache
> - 字长地址 32 bit（字节寻址）。
> - 容量 $C=256\,\mathrm{B}$，块大小 $B=16\,\mathrm{B}$，直接映射（$E=1$）。
> - 则块数 $S=C/B=16$ → **index = 4 bit**；**offset = $\log_2 16=4$ bit**；**tag = 32−4−4=24 bit**。
> - 访问地址 `0x0000_12F4`。

拆分步骤：offset = 低 4 bit；index = 接下来 4 bit；其余为 tag。

> [!example] 自检
> （1）写出该地址的 tag、index、offset（建议 hex 或 bin）。
> （2）若 Cache 第 `index` 行 valid=1 且 tag 匹配 → hit 还是 miss？
> （3）另一地址 `0x0000_13F4` 与 `0x0000_12F4` 是否可能 **conflict miss**（撞同一行）？

> [!success]- 参考答案
> （1）`0x000012F4` = `...0001_0010_1111_0100`：offset=`0x4`（低 4 bit=`0100`）；index=`0xF`（接下来 `1111`）；tag=`0x000012`（高 24 bit，含 `0x12` 的高半与前面的 0）。更稳妥按位移：offset = addr & 0xF = `0x4`；index = (addr >> 4) & 0xF = `0xF`；tag = addr >> 8 = `0x000012`。
> （2）valid 且 tag==`0x000012` → **hit**；否则 miss，按 index=`0xF` 填/替换该行。
> （3）`0x000013F4`：offset=`0x4`，index=`0xF`，tag=`0x000013`。**同一 index、不同 tag** → 直接映射下互挤，经典 **conflict**。

---
## 11. 工作例：AMAT 数值

> [!example] 单级
> $t_{\mathrm{hit}}=2$ cycle，$t_{\mathrm{miss}}=40$ cycle（含取块），miss rate $m=0.03$。
> $$
> \mathrm{AMAT}=2+0.03\times 40=3.2\text{ cycle}.
> $$

> [!example] 自检
> （1）若加 L2：$t_{L1}=2$，$m_{L1}=0.03$，$t_{L2}=10$，$m_{L2}=0.2$（相对 L1 miss），DRAM=$100$。写 $\mathrm{AMAT}_{L1}$。
> （2）把 $m_{L1}$ 降到 $0.01$（其余同单级题）时 AMAT？相对降 $t_{\mathrm{hit}}$ 到 1 但 $m$ 仍 0.03，哪个更划算？

> [!success]- 参考答案
> （1）$\mathrm{AMAT}_{L2}=10+0.2\times 100=30$；$\mathrm{AMAT}_{L1}=2+0.03\times 30=2.9$ cycle。
> （2）单级 $m=0.01$：$\mathrm{AMAT}=2+0.4=2.4$。若 $t_{\mathrm{hit}}=1$、$m=0.03$：$\mathrm{AMAT}=1+1.2=2.2$——略好；但若 miss penalty 更大，降 $m$ 通常更稳。课内抓住：**AMAT 对 $m$ 往往更敏感**。

---
## 12. 本节清单

1. 用时间/空间局部性解释为何 Cache 有效，以及为何以 **line** 为单位填充。
2. 会拆分 tag / index / offset，并区分 direct-mapped、set-associative、fully associative。
3. 能叙述 hit/miss 与 3C 缺失类型。
4. 对比 write-through 与 write-back，以及 allocate 策略的常见搭配。
5. 会写并解释 $\mathrm{AMAT}=t_{\mathrm{hit}}+m\cdot t_{\mathrm{miss}}$（含多层直觉）。
6. 能对给定 $C,B,E$ 与地址算出 tag/index/offset，并完成 AMAT 数值题。

## 参考

- MIT 6.004 *Computation Structures*：Memory hierarchy / Caches（[computationstructures.org](https://computationstructures.org/)）
- MIT OCW 6.004：[Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/)
