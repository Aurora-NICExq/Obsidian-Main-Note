---
aliases:
  - Device Tree
  - 设备树
  - DTB
  - DTS
  - OF
tags: [cs, linux_kernel]
up: "[[Linux Kernel (Bootlin) MOC]]"
related:
  - "[[Device Driver Model and Platform Drivers]]"
  - "[[Kernel Configuration Build and Boot]]"
  - "[[STM32 MOC]]"
down:
  - "[[Device Driver Model and Platform Drivers]]"
---
# 硬件描述与 Device Tree

> [!summary] 核心结论
> 在 ARM/RISC-V 等平台，**Device Tree** 用数据描述板上有什么设备、寄存器基址、中断、时钟与拓扑，避免把板级差异写死进内核。源是 **DTS** → **DTB**，Bootloader 传给内核；驱动通过 OF/`platform` 匹配 **`compatible`** 取得资源。口诀：**代码描述如何驱动某类硬件；DT 描述这块板上有哪几个、地址是什么**。

> 底本：Bootlin — Describing hardware / Device Tree。

![[lk-device-tree.svg]]

---
## 1. 为什么需要 DT

许多 SoC 外设挂在 **不可自枚举** 的总线上。旧 board-file 把基址写死在 C 里；DT 外置板级数据，同一内核镜像可配不同 DTB。

---
## 2. 完整节点直觉

```dts
soc {
	uart0: serial@40011000 {
		compatible = "vendor,uart-1.0", "vendor,uart";
		reg = <0x40011000 0x400>;
		interrupts = <GIC_SPI 32 IRQ_TYPE_LEVEL_HIGH>;
		clocks = <&rcc CLK_UART0>;
		pinctrl-names = "default";
		pinctrl-0 = <&uart0_pins>;
		status = "okay";
	};
};
```

| 属性 | 驱动侧含义 |
|---|---|
| `compatible` | `of_match_table` 主键（先具体后通用） |
| `reg` | MMIO 基址/长度 → `platform_get_resource` |
| `interrupts` | → `platform_get_irq` |
| `clocks` / `resets` | 依赖其它驱动；未就绪可 `EPROBE_DEFER` |
| `status` | `disabled` → 不创建 device，不 probe |

Bindings：`Documentation/devicetree/bindings/`（现代为 YAML schema）。

---
## 3. 编译与传递

```bash
# 内核树内
make ARCH=arm64 dtbs
# 或
dtc -I dts -O dtb -o board.dtb board.dts
```

U-Boot：加载 `Image` + `board.dtb`，`booti` 时传入。运行时可看 `/proc/device-tree`（若启用）。

---
## 4. 与驱动联调的一条路径

> [!example] “驱动没 probe” 检查单
> 1. DTB 是否真的是你改的那份？（Bootloader 路径搞错很常见）
> 2. 节点 `status` 是否 `okay`？
> 3. `compatible` 字符串是否与驱动表 **逐字** 一致？
> 4. 驱动是否编进内核/已 `modprobe`？
> 5. `dmesg` 是否有 `EPROBE_DEFER` 反复跳？（缺 clock/pinctrl）
> 6. `/sys/bus/platform/devices/` 下有无该设备？`driver` 链接是否为空？

---
## 5. DT 不是万能

- USB/PCI 等可枚举总线仍以总线协议为主；DT 描述宿主控制器或固定拓扑。
- x86 笔记本/服务器常用 ACPI；本课以 DT 为主。
- 错误地址可能在 `ioremap` 后第一次 `readl` 才炸——DT 错不等于编译失败。

---
## 6. 自检

1. 同一 UART IP、两板基址不同——改驱动还是改 DTS？
2. `compatible` 为何允许多个字符串？
3. 根设备驱动是模块、只在 DT 描述——启动还缺什么？

> [!success]- 参考答案
> 1. 改 DTS 的 `reg`（及中断等）；驱动应通过资源 API 取址，不写死。
> 2. 回退匹配：先匹配最具体兼容串，老驱动可只声明较通用串。
> 3. initramfs（或把驱动改 `=y`），以便挂根前加载模块。
