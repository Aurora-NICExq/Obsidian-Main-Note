---
aliases: [时间片, Time Slicing, 时间片轮转, configUSE_TIME_SLICING]
tags: [FreeRTOS, embedded, rtos]
up: "[[FreeRTOS Overview]]"
related:
  - "[[Preemptive and Cooperative Scheduling]]"
  - "[[Task States]]"
  - "[[Task Management]]"
  - "[[Processes and Scheduling|Linux 进程与调度]]"
---
# Time Slicing

 # Time Slicing

> [!summary] 核心结论
> FreeRTOS 的时间片只作用于**同优先级**就绪任务：开启 `configUSE_TIME_SLICING` 后，每个 SysTick 可轮转一次，让它们近似均分 CPU。片长由 `configTICK_RATE_HZ` 决定（tick 周期 = 一片）。它**不**削弱高优先级抢占。和 Linux 比：最像 `SCHED_RR`；**不像** CFS（CFS 用 vruntime 权重公平，不是固定时间片轮转）。

---

## 1. 时间片做什么

**时间片（Time Slicing）**：让优先级**相等**的多个任务，轮流获得近似均等的执行时间。

- 有更高优先级就绪 → 仍然立刻抢占（时间片管不到跨优先级）
- 同优先级、且都 Ready → 开时间片则按 tick 轮转；关时间片则当前任务一直跑到阻塞 / `taskYIELD`

属于「带时间片的抢占式」这一档，见 [[Preemptive and Cooperative Scheduling]]。

![[d2-time-slicing-01.svg]]

被轮转下去的任务：Running → Ready（不是 Blocked）。状态机见 [[Task States]]。

---

## 2. 怎么开 / 关

`FreeRTOSConfig.h`：

```c
/* 1 = 开启同优先级时间片；0 = 关闭 */
#define configUSE_TIME_SLICING 1
```

前提通常是抢占式已开：`configUSE_PREEMPTION 1`。协作式下讨论“时间片轮转”意义不大——本就不靠 tick 强行切同优先级任务。

---

## 3. 片长由谁定

时间片长度 ≈ **一个 tick 周期**，由 SysTick 频率决定：

```c
/* SysTick 中断频率 (Hz)；100 → 每 10 ms 一个 tick */
#define configTICK_RATE_HZ 100
```

| `configTICK_RATE_HZ` | 约片长 | 直观影响 |
| -------------------- | ------ | -------- |
| 100 | 10 ms | 切换少、响应粗一点 |
| 1000 | 1 ms | 同优先级轮得更勤、中断开销更大 |

`pdMS_TO_TICKS(ms)` 也依赖这个频率：延时、超时和“一片”共用同一套节拍。

底层：SysTick ISR（`xPortSysTickHandler`）里递增 tick，并在需要时请求 PendSV 做上下文切换——安装方式见 [[Installing Interrupt Handlers]]。

![[tikz-time-slicing-01.svg]]

---

## 4. 和 Linux 调度：联系与区别

对照笔记：[[Processes and Scheduling#Part 3: The Scheduler (调度器)]]。

### 4.1 一眼对照

| | FreeRTOS 时间片 | Linux |
| - | --------------- | ----- |
| **作用对象** | 同 `uxPriority` 的任务 | 视策略而定 |
| **机制** | 固定优先级 + 可选 RR（每 tick） | 默认 **CFS**（vruntime）；另有 RT 策略 |
| **最像谁** | — | **`SCHED_RR`**：同实时优先级 round-robin |
| **不像谁** | — | **CFS**：按权重分 CPU，不是“每片轮一人” |
| **关时间片时** | 同优先级一直跑到阻塞/让出 | 近似 **`SCHED_FIFO`** 同优先级“不轮转、跑到睡” |
| **优先级方向** | 数值越大越高（`0` 最低） | RT：数值越大越高；nice：越小越高 |
| **设计目标** | 嵌入式确定性、配置简单 | 通用 OS：吞吐 + 交互响应 |

### 4.2 联系（可迁移的直觉）

1. **“同优先级轮转”** 这条线和 Linux `SCHED_RR` 同构：都是固定优先级家族里的时间片 RR；可用 `sched_rr_get_interval()` 看 Linux RR 的片长直觉，对应 FreeRTOS 的 `1/configTICK_RATE_HZ`。
2. **“同优先级不轮转”** 和 `SCHED_FIFO` 接近：当前任务不睡就不把 CPU 让给同级其它人（Linux FIFO 同级按排队；FreeRTOS 关时间片则是当前一直跑）。
3. **高优先级抢占低优先级** 两边都有；FreeRTOS 默认整棵都是固定优先级抢占，Linux 则是 RT 永远压过普通进程（nice/CFS）。

### 4.3 区别（别混）

1. **Linux 日常默认不是时间片轮转**  
   普通进程走 **CFS**：选 **vruntime 最小** 的那个，用红黑树；nice 改的是**权重/份额**，不是 FreeRTOS 那种离散优先级档 + 可选 RR。把 FreeRTOS 时间片脑补成“Linux 也这样调度桌面进程”会错。

2. **公平性来源不同**  
   - FreeRTOS：同优先级靠 tick RR ≈ 均分；不同优先级**不**谈公平，高的永远先跑。  
   - CFS：用 vruntime + nice 权重追求**比例公平**；睡得多的还会被“补偿”，偏交互。

3. **实时语义**  
   FreeRTOS 应用任务整体更接近“全员固定优先级 RT 风格”。Linux 要把类似行为显式设成 `SCHED_FIFO` / `SCHED_RR`，并受 RT 带宽限制（`sched_rt_period_us` / `sched_rt_runtime_us`），防止饿死普通进程——MCU 上一般没有这层“给 CFS 留时间”的默认保护。

4. **片长与复杂度**  
   FreeRTOS：一片 = 一个 tick，全局一个 `configTICK_RATE_HZ`。  
   Linux：HZ/hrtimer、CFS 目标延迟、RR interval 等更细；还有多核 affinity / 负载均衡（同笔记 Part 4），FreeRTOS 单核课设通常不涉及。

![[d2-time-slicing-02.svg]]

---

## 5. 怎么选（FreeRTOS 侧）

| 需求 | 建议 |
| ---- | ---- |
| 多个同优先级 CPU 型任务都要“轮着跑” | `TIME_SLICING 1` |
| 同优先级希望跑完关键段再切、少切换 | `TIME_SLICING 0`，靠阻塞点切换 |
| 要严格响应 | 靠**提高优先级**，别指望时间片跨优先级帮忙 |
| 延时分辨率 vs 中断开销 | 调 `configTICK_RATE_HZ`（片长随之变） |

从 Linux 带过来的口诀：**FreeRTOS 时间片 ≈ 精简版 SCHED_RR；不要拿它去类比 CFS。**
