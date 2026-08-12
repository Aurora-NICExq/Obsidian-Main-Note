---
aliases:
  - 汇编与栈
  - Calling Convention
  - Stack Frame
  - Assembly Language Procedures and Stacks
  - 过程调用
tags: [cs, computer_architecture]
up: "[[Computer Organization and Architecture (MIT 6.004) MOC]]"
related:
  - "[[Instruction Set Architecture]]"
  - "[[Single-Cycle Processor Datapath]]"
down:
  - "[[Single-Cycle Processor Datapath]]"
---
# 汇编、过程与栈

> [!summary] 核心结论
> 汇编是 ISA 的助记符；机器码是同一语义的位串。过程调用靠 **调用约定（calling convention）**：谁传参、谁保存寄存器、返回值放哪、返回地址如何恢复。栈帧（stack frame）在内存中为每次调用保存 $LP$、被调用者保存寄存器、局部变量与溢出区；递归只是「同一过程、多层帧」。区分 **叶函数**（不再调用别人）与 **非叶函数**，能决定要不要保存 $LP$、要不要建完整帧。

> 底本：MIT 6.004 Computation Structures（assembly / procedures），OCW。

---
## 1. 汇编 vs 机器码

| | 汇编（assembly） | 机器码（machine code） |
|--|------------------|------------------------|
| 形式 | 文本助记符 + 标号 | 二进制字（Beta 为 32 bit） |
| 谁读 | 人 / 汇编器 | CPU 取指单元 |
| 信息 | 同一 ISA 语义 | 同一 ISA 语义 |

汇编器做：符号表、标号 → 相对地址、指令模板填域。链接器再解析跨文件符号。CPU **从不**「执行汇编」——只执行已编码的指令字。

例：
```text
ADD R1, R2, R3      ; 汇编
; → opcode | Rc=1 | Ra=2 | Rb=3 | ...
```

---
## 2. 为什么需要调用约定

高级语言 `f(a,b)` 编译后变成一串指令。若无统一约定，调用者与被调用者会对「参数在寄存器还是栈」「`R1` 会不会被毁掉」产生分歧。约定通常规定：

1. **参数传递**：前几个参数进哪些寄存器，其余压栈。
2. **返回值**：哪个寄存器。
3. **返回地址**：谁写入 $LP$（通常 `BEQ`/`BNE`/`JMP` 带链接，或显式 `MOVE LP, PC+…` 风格）。
4. **寄存器分类**：
   - **调用者保存（caller-saved）**：调用前若还需要，由调用者先存栈。
   - **被调用者保存（callee-saved）**：被调用者若使用，入口保存、出口恢复。
5. **栈对齐 / 红区**（视 ABI；课程版可简化）。

Beta 教学 ABI 常近似：参数与返回值用低编号寄存器；$SP$、$LP$、$BP$ 角色如 [[Instruction Set Architecture]] 所述。

---
## 3. 栈与栈帧

栈是一块向下增长的内存区域，$SP$ 指向「当前栈顶」。每次过程调用可分配一个 **帧**：

![[coa-stack-frame.svg]]

典型布局（高地址 → 低地址，示意）：

1. 调用者帧（caller frame）
2. 传入的栈参数（若有）
3. 保存的返回地址 $LP$ / 旧帧指针 $BP$
4. 被调用者保存的寄存器
5. 局部变量与寄存器溢出（spill）
6. 为即将发起的子调用预留的出参区（outgoing args）

帧指针 $BP$ 可选：有了 $BP$，局部变量可用 **相对 $BP$ 的固定偏移** 寻址，即使中途 $SP$ 因 `alloca` 或压栈而变化也稳定。无 $BP$ 时则全程相对 $SP$，编译器须精确跟踪偏移。

---
## 4. 一次调用的时间线

设 `caller` 调用 `callee`：

### 4.1 调用者（prologue to call）

1. 若需要，把 caller-saved 寄存器压栈。
2. 把参数放入约定寄存器 / 压栈。
3. 执行带链接的跳转：保存返回地址到 $LP$，PC ← 入口。

### 4.2 被调用者入口（prologue）

```text
PUSH  BP          ; 可选：保存旧帧指针
MOVE  BP, SP      ; 建立新帧
ALLOCATE n        ; SP ← SP - n，为 locals 留空间
PUSH  <callee-saved regs used>
```

（具体是 `ST`/`LD` 与立刻数，而非伪指令；此处用伪码强调结构。）

### 4.3 函数体

用寄存器与 `BP/SP` 相对地址完成计算；若再调用别人，重复「调用者步骤」。

### 4.4 被调用者出口（epilogue）

```text
MOVE  <ret>, Rv   ; 返回值写入约定寄存器
POP   <callee-saved>
MOVE  SP, BP      ; 撕掉 locals
POP   BP
JMP   (LP)        ; 返回
```

### 4.5 调用者（after return）

从返回值寄存器取结果；若曾保存 caller-saved，则弹出恢复。

---
## 5. 递归

递归 **不需要** 特殊硬件：每次调用压入新帧，$SP$ 下降；返回时帧弹出，$SP$ 回升。正确性依赖：

- 每层有自己的 locals / 保存寄存器副本；
- 返回地址链正确（每层自己的 $LP$ 保存在自己的帧里——非叶递归必须保存 $LP$）；
- 基例不再调用，最终开始连续返回。

> [!example] 阶乘示意
> `fact(n)` 若 $n>0$ 则调用 `fact(n-1)`：栈上叠 $n$ 层帧，每层保存自己的 $n$ 与 $LP$；回到上层再做乘法。深度过大 → 栈溢出（与 ISA 无关，是资源问题）。

尾递归可优化成跳转而不增长栈，但是否优化属于编译器，不是 ISA 强制。

---
## 6. 叶函数 vs 非叶函数

| | 叶（leaf） | 非叶（non-leaf） |
|--|------------|------------------|
| 定义 | 过程体内 **不再调用** 其它过程 | 会 `call` 别人 |
| $LP$ | 可一直留在 $LP$ 寄存器 | **必须** 在 prologue 把 $LP$ 存进帧（否则子调用覆盖） |
| 帧大小 | 往往更小；可能无完整帧 | 通常需保存 $LP$、部分 callee-saved、出参区 |
| 优化 | 可用「叶子优化」少访存 | 保守建帧 |

判断流程：

1. 扫描过程：有无 `JMP`/`BEQ` 到其它入口？有 → 非叶。
2. 非叶：入口 `ST LP, …(SP)`，出口再 `LD LP, …` 后返回。
3. 叶：若只用 caller-saved 与少量临时寄存器，甚至可 $SP$ 不动。

> [!tip] 调试直觉
> 崩溃时回溯（backtrace）就是沿保存的 $BP$ 链或 DWARF 信息走帧；没有规范帧，回溯会断。

---
## 7. 与 ISA / 硬件的接口

过程机制 **几乎全是软件约定**，硬件只提供：

- 通用寄存器与 $R31=0$；
- `LD`/`ST` 读写内存；
- 改变 PC 的分支 / 跳转，以及把返回地址写入 $LP$ 的能力。

没有「call 指令必须自动压栈」的硬性要求（CISC 常有；RISC 常拆开）。因此同一 Beta ISA 上可以有不同 ABI——只要调用双方一致。

异常 / 中断会另用 $XP$ 等保存 PC，并切到内核栈；那是「被迫的过程」，约定更严，见后续系统笔记。

---
## 8. 常见坑

1. **忘记保存 $LP$**（非叶）→ 子调用返回后跳回错误地址。
2. **栈不平衡**：prologue 减的字节数与 epilogue 加的不一致 → 返回后 $SP$ 错，后续全毁。
3. **调用者 / 被调用者保存搞反**：以为 `R5` 跨调用仍在，实际已被 callee 当临时寄存器用掉。
4. **未对齐访问**（若实现要求字对齐）→ 总线或异常。
5. **在帧内取地址后 $SP$ 又变**：应用 $BP$ 或重新计算偏移。

---
## 9. 工作例：栈帧地址走查（call / return）

> [!example] 初始与约定
> 字 = 4 B；栈向下增长。调用前：
> - $SP = 0x1000$（指向“下一空闲低地址”之上的旧顶，此处约定：**$SP$ 为当前栈顶已用字地址**，push 先 $SP{-}{=}4$ 再存——与具体 ABI 差 4 时只影响常数，不改结构）。
> - 为清晰用伪操作：`push x` ≡ `$SP\leftarrow SP-4$; Mem[SP]←x`；`pop` 相反。
>
> `main` 调用非叶 `foo`；`foo` 再调用叶 `bar`。`foo` 需保存 $LP$、旧 $BP$，并分配 8 B locals。

| 步骤 | 动作 | $SP$（示意） | 备注 |
|------|------|---------------|------|
| 0 | 调用前 | `0x1000` | main 帧顶 |
| 1 | `push` 参数（若有） | `0x0FFC` | 可选 |
| 2 | `call foo`：链结 $LP\leftarrow$ 返回地址 | `0x0FFC` | PC→foo；$LP$=main 中下一条 |
| 3 | foo prologue：`push BP`；`BP←SP` | `0x0FF8` | 旧 BP 入栈 |
| 4 | `push LP` | `0x0FF4` | 非叶：保存返回 main 的地址 |
| 5 | `SP←SP-8`（locals） | `0x0FEC` | 局部变量区 |
| 6 | `call bar`：新 $LP\leftarrow$ 返回 foo 内 | `0x0FEC` | **覆盖** $LP$ 寄存器；帧内已有副本 |
| 7 | bar 叶：几乎不建帧，算完 `JMP (LP)` | `0x0FEC` | 回到 foo |
| 8 | foo epilogue：`SP←BP` 路径恢复；`pop LP`；`pop BP`；`JMP (LP)` | 回到 `0x1000` 一带 | 返回 main |

地址链直觉：每次 call 多一层帧，$SP$ 下降；return 逐层抬升。递归 $n$ 层 ≈ $n$ 倍帧大小消耗。

> [!example] 自检
> （1）步骤 6 若不在步骤 4 保存 $LP$，`bar` 返回后 `foo` 再 `JMP (LP)` 会跳到哪？
> （2）若 foo locals 改为 16 B，步骤 5 后 $SP$ 是多少？
> （3）叶函数 bar 为何通常不必 `push LP`？

> [!success]- 参考答案
> （1）$LP$ 已被 `call bar` 写成“foo 内返回点”；`bar` 返回后若 foo 未从栈恢复**原先**指向 main 的 $LP$，最终会错误跳转（常跳回 foo 自己或垃圾）。**非叶必须存 $LP$。**
> （2）$SP=0x0FF4-16=0x0FE4$（在步骤 4 后为 `0x0FF4` 的前提下）。
> （3）bar 不再 call 别人，$LP$ 寄存器一直保持“返回 foo”的值，不被覆盖。

---
## 10. 本节清单

1. 说清汇编与机器码同语义、不同表示。
2. 能列出 calling convention 的五要素（参数、返回值、返回地址、两类寄存器、栈）。
3. 对照 `coa-stack-frame.svg` 指出 $LP$、locals、outgoing args 的位置。
4. 会写（伪码）非叶函数的 prologue / epilogue。
5. 能解释递归为何「只是多层帧」，以及叶 vs 非叶对 $LP$ 的不同处理。
6. 能沿 call/return 追踪 $SP$（及 $LP$ 保存）的变化。

## 参考

- MIT 6.004 *Computation Structures*, assembly language & stack frames (OCW)
- System V ABI / 各架构 calling convention 文档（对照用）
- Patterson & Hennessy, *COD*：procedures and the stack
