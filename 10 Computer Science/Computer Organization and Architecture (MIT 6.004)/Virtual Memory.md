---
aliases:
  - 虚拟内存
  - Virtual Memory
  - VA/PA
  - 页表
  - TLB
tags: [cs, computer_architecture]
up: "[[Computer Organization and Architecture (MIT 6.004) MOC]]"
related:
  - "[[Memory Hierarchy and Caches]]"
  - "[[Interrupts Devices and IO]]"
  - "[[Assembly Language Procedures and Stacks]]"
  - "[[Parallel Processing and Concurrency]]"
down:
  - "[[Interrupts Devices and IO]]"
---
# 虚拟内存

> [!summary] 核心结论
> **虚拟地址（VA）** 让每个进程以为自己拥有完整、连续的地址空间；硬件用 **页表** 把 VA 译成 **物理地址（PA）**，并用 **TLB** 缓存近期翻译。缺页（page fault）走 OS；页级权限位实现**隔离与保护**。虚拟内存把“大而慢的磁盘/闪存作后备 + 小而快的 DRAM 作 Cache”推到地址翻译层——与 [[Memory Hierarchy and Caches]] 同一局部性逻辑，粒度是 **page** 而非 cache line。

> 底本：[Computation Structures](https://computationstructures.org/) / MIT 6.004（Virtual memory）。

---
## 1. VA 与 PA

- **VA（Virtual Address）**：程序 / CPU 流水线“看见”的地址（指针、PC、栈指针）。
- **PA（Physical Address）**：接到 DRAM 控制器、真实选中芯片行列的地址。

没有虚拟内存时，程序直接用 PA——多进程难隔离、难重定位、难共享库。有 VM 后：编译器可假设固定 VA 布局（如代码在低地址、栈向下长），装载与换页由 OS + MMU 完成。

![[coa-virtual-memory.svg]]

---
## 2. 分页（Paging）

固定页大小 $P$（常见 $4\,\mathrm{KiB}$；$2\,\mathrm{MiB}$ 大页等为扩展）。VA 拆成：

$$
\mathrm{VA}=\underbrace{\mathrm{VPN}}_{\text{virtual page number}} \;\|\; \underbrace{\mathrm{offset}}_{\log_2 P\text{ 位}}.
$$

页内偏移在翻译时**原样保留**；只需把 VPN 映射为 **PPN（physical page number）**：

$$
\mathrm{PA}=\mathrm{PPN}\,\|\,\mathrm{offset}.
$$

> [!tip] 与 Cache 块的对比
> Cache line $\sim$ 几十字节，硬件自动填充；Page $\sim$ 数 KiB，缺失由 OS 处理、可换出到磁盘。两者常**串联**：先 VA→PA（TLB），再用 PA 查 Cache（或 VIVT 等变体，课内以物理索引直觉为主）。

---
## 3. 页表（Page Table）

每个进程一份（逻辑上的）页表：$\mathrm{VPN}\mapsto$ 页表项（PTE）。PTE 典型字段：

| 字段 | 含义 |
|------|------|
| valid / present | 该 VPN 是否映射到常驻物理页 |
| PPN | 物理页框号 |
| R/W / X（或 NX） | 读 / 写 / 执行权限 |
| user / supervisor | 用户态是否可访问 |
| accessed / dirty | 供替换与写回策略使用 |
| 缓存属性等 | 可缓存 / MMIO 等（实现相关） |

单级页表：若 VA 为 32 位、$P=4\,\mathrm{KiB}$，则 VPN 20 位 → 约 $2^{20}$ 项；稀疏地址空间浪费巨大。故实用系统用**多级页表**（目录→中间→叶），只为已用的 VPN 分配中间节点。

---
## 4. 地址翻译路径

一次 load/store / 取指的概念路径：

1. 从 VA 取出 VPN、offset。
2. 查 **TLB**（见下）；命中则得 PPN + 权限，拼 PA。
3. TLB 缺失 → 硬件页表行走（page walk）或 trap 到 OS（视实现）；填 TLB。
4. 用 PA 访问 Cache / 内存；若 PTE 无效 → **page fault**。

翻译与数据访问的延迟叠加进有效 CPI——故 TLB 命中率极关键。

---
## 5. TLB（Translation Lookaside Buffer）

TLB 是翻译结果的小 Cache：存 $(\mathrm{VPN}\to\mathrm{PTE})$ 或等价信息，通常 **全相联或高相联**、条目很少（数十～数百）。

- **TLB hit**：1 cycle 量级完成翻译。
- **TLB miss**：页表行走（可能多次访存）或软 miss 处理；成本远高于 Cache 命中。

上下文切换时：换页表基址寄存器（如 PTBR / CR3）；常 **flush TLB** 或用 **ASID / PCID** 避免全清。多核下 shootdown：改映射后需让其他核的 TLB 失效。

$$
\text{有效访存} \approx \text{翻译}+\text{数据层次（AMAT）}.
$$

---
## 6. 缺页与换页

**Page fault** 例外：访问的 VPN 无有效 PTE，或权限不允许。

典型处理流程（概念）：

1. 硬件保存 PC / 原因码，陷入 OS（见 [[Interrupts Devices and IO]]）。
2. OS 判断：非法访问 → 杀进程 / 信号；合法但未驻留 → 选物理页框，可能 **换出（evict）** 脏页到交换区。
3. 从磁盘 / 文件读入目标页，更新 PTE，刷 TLB。
4. 从故障指令 **重启**（精确异常语义）。

工作集过大 → 抖动（thrashing）：大部分时间在换页而非计算。

---
## 7. 保护与隔离

VM 的系统价值不亚于“扩展容量”：

1. **进程隔离**：进程 A 的 VA 不能直接指到 B 的物理页（除非显式共享映射）。
2. **用户 / 内核分离**：内核页标为 supervisor-only；用户态访问触发 fault → 保护 OS。
3. **细粒度权限**：代码页 RX、数据页 RW、栈 NX 防简单代码注入；COW（copy-on-write）共享页在写时复制。
4. **内存映射 I/O 与文件**：`mmap` 把文件或设备寄存器映入 VA；设备区通常标为不可缓存（与 Cache 策略交互）。

无 MMU 的 MCU（部分 STM32 配置）则靠 MPU 或不做进程级隔离——对比见 [[STM32 MOC]]。

---
## 8. 共享与别名

- **共享库 / 共享内存**：不同进程的不同 VPN 可映到同一 PPN（权限可不同）。
- **别名（aliasing）**：同一物理页多个 VA；Cache 若按 VA 索引需注意一致性。课内强调“翻译后再用 PA 查数据 Cache”的清晰模型。

---
## 9. 与存储层次的统一视角

| | Cache | Virtual Memory |
|--|-------|----------------|
| 块 | line | page |
| 缺失处理 | 硬件填 | OS + 可能磁盘 |
| 加速结构 | tag 阵列 | TLB |
| 主要目标 | 降延迟 | 隔离 + 扩展 + 降延迟 |

两者叠加：现代 CPU 几乎总是 **VA →（TLB）→ PA → Cache/DRAM**。

---
## 10. 工作例：32-bit VA 拆分与一次翻译

> [!example] 给定参数
> - VA 宽 32 bit；页大小 $P=4\,\mathrm{KiB}=2^{12}$ B → **offset = 12 bit**，**VPN = 20 bit**。
> - 某次 load 的 VA = `0x0040A2C4`。
> - 页表（简化单级）查得：VPN 对应 PTE 有效，PPN = `0x0007A`，权限 R/W、user。
>
> **步骤**
> 1. 拆 VA：`0x0040A2C4` = VPN \| offset。
> 2. 用 VPN 查 TLB / 页表得 PPN。
> 3. PA = PPN \| offset（offset 原样保留）。

> [!example] 自检
> （1）写出 VPN 与 offset 的十六进制（或二进制位宽核对）。
> （2）拼出物理地址 PA。
> （3）若 PTE.valid=0，硬件下一步是什么？程序是否立刻看到“正确数据”？

> [!success]- 参考答案
> （1）`0x0040A2C4`：低 12 bit offset = `0x2C4`；高 20 bit VPN = `0x0040A`。（检：`0x0040A << 12 | 0x2C4 = 0x0040A2C4`。）
> （2）PPN=`0x0007A` → PA = `0x0007A2C4`（PPN 置于高位，宽度以物理地址位数为准；此处示意 PA 仍写到与页框对齐的形式）。
> （3）**page fault**：陷入 OS；若合法则换页、填 PTE/TLB，再**重启**故障指令。在 fault 处理完成前，该 load **不会**得到正确用户数据。

---
## 11. 工作例：TLB hit / miss 成本素描

> [!example] 数量假设（教学用）
> - TLB hit：翻译 $\approx 1$ cycle，随后数据 Cache hit $\approx 1$ cycle → 有效约 **2** cycle/访存。
> - TLB miss + 硬件页表行走：假设 2 级页表，每次访存 20 cycle（已在 Cache 未命中 DRAM），行走 2 次 → $+40$；再数据访问 1 cycle → 约 **42** cycle。
> - 若再 page fault 读盘：毫秒级（$10^{6+}$ cycle）——数量级上淹没一切。
>
> 设 TLB hit rate $h_{\mathrm{TLB}}=0.99$，无缺页，数据均 Cache hit：
> $$
> T_{\mathrm{avg}}\approx h_{\mathrm{TLB}}\cdot 2 + (1-h_{\mathrm{TLB}})\cdot 42 = 0.99\cdot 2 + 0.01\cdot 42 = 2.4\text{ cycle}.
> $$

> [!example] 自检
> （1）若 $h_{\mathrm{TLB}}$ 降到 $0.90$，其它不变，$T_{\mathrm{avg}}$？
> （2）为何上下文切换后常看到一串 TLB miss，却不一定伴随 page fault？

> [!success]- 参考答案
> （1）$T_{\mathrm{avg}}=0.9\cdot 2+0.1\cdot 42=6.0$ cycle——TLB 命中率从 99%→90% 就让平均翻译+访存从 2.4 涨到 6。
> （2）换 CR3/PTBR 后旧 TLB 项作废（或 ASID 不匹配）→ 冷 TLB miss，但页仍在 DRAM、PTE 有效 → **只走路页表，不换页**。Page fault 仅当 present/valid 失败或权限失败。

---
## 12. 本节清单

1. 说清 VA / PA、VPN / PPN / offset 的拆分与拼接。
2. 能描述 PTE 关键字段及多级页表为何必要。
3. 解释 TLB 的角色、miss 代价与上下文切换时的处理直觉。
4. 会走一遍 page fault：检测 → OS → 换页 → 重启指令。
5. 用权限位与地址空间说明保护 / 隔离 / 共享库。
6. 会做 32-bit VA 的 VPN/offset 拆分与 PA 拼接，并估算 TLB hit/miss 平均成本。

## 参考

- MIT 6.004 *Computation Structures*：Virtual memory / page tables / TLB（[computationstructures.org](https://computationstructures.org/)）
- MIT OCW 6.004：[Computation Structures](https://ocw.mit.edu/courses/6-004-computation-structures-spring-2017/)
