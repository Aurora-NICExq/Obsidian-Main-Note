---
aliases:
  - 内核配置与编译
  - Kconfig
  - 内核启动
  - make menuconfig
tags: [cs, linux_kernel]
up: "[[Linux Kernel (Bootlin) MOC]]"
related:
  - "[[Kernel Introduction and Source Tree]]"
  - "[[Loadable Kernel Modules]]"
down:
  - "[[Loadable Kernel Modules]]"
---
# 内核配置、编译与启动

> [!summary] 核心结论
> 用 **Kconfig** 选择特性（`menuconfig`/`defconfig`）生成 `.config`；`make` 产出 **vmlinux**（带符号的 ELF）与可启动镜像（如 `Image`/`zImage`/`bzImage`）以及可选的 **模块 `.ko`**。启动链大致是：固件/Bootloader →（可选 DT）→ 解压/加载内核 → `start_kernel` → `init`。交叉编译时 `ARCH=` + `CROSS_COMPILE=` 必须与目标板一致；**正在运行的内核**与**要加载的模块**必须同源同配置。

> 底本：Bootlin — Kernel configuration and building / Booting。

---
## 1. 配置：Kconfig → `.config`

- 每个子系统目录有 `Kconfig`；选项：`bool` / `tristate`（y/m/n）/ `string` 等。
- 常用目标：`make defconfig`、厂商 `*_defconfig`、`menuconfig`/`nconfig`、`oldconfig`。
- 结果写入 `.config`；构建系统据此决定编译哪些 `.o`、是否打成模块。

> [!example] 读一条 Kconfig
> ```
> config MY_UART
> 	tristate "My UART support"
> 	depends on OF && HAS_IOMEM
> 	help
> 	  Driver for ...
> ```
> - `tristate`：可 `y`（内建）/`m`（模块）/`n`。
> - `depends on`：不满足则不可选；菜单里会隐藏或变灰。
> - 选 `m` 后通常还要在 `Makefile` 有 `obj-$(CONFIG_MY_UART) += my_uart.o`。

> [!warning] 配置一致性
> 已运行内核与“正在编译的模块”必须同源同配置（或严格兼容），否则 `vermagic` / 符号版本对不上会拒绝加载。发行版用 `linux-headers-$(uname -r)` 对齐。

---
## 2. 编译产物

| 产物 | 含义 |
|---|---|
| `vmlinux` | 未压缩、带调试符号的内核 ELF（分析 oops 用） |
| `Image` / `zImage` / `bzImage` | arch 相关可启动镜像 |
| `*.ko` | 可加载模块 |
| `System.map` | 符号地址表 |
| `Module.symvers` | 导出符号 CRC（外模块链接需要） |

```bash
make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- -j$(nproc)
make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- modules
```

---
## 3. 模块与内建

- `=y`：链进镜像（启动即在）。
- `=m`：单独 `.ko`，运行时 `modprobe`。
- **根设备、控制台、早期时钟** 等启动关键路径：应 `=y` 或放进 **initramfs**，否则可能挂在无法挂根。

详见 [[Loadable Kernel Modules]]。

---
## 4. 启动链（逐步）

1. **ROM/固件**：上电、找 Bootloader。
2. **Bootloader**（U-Boot 等）：加载内核、（嵌入式）加载 **DTB**、设 `bootargs`、跳转。
3. **早期汇编**：临时页表/关 MMU 视 arch 而定 → 进 C。
4. **`start_kernel()`**：IRQ、调度、时间、驱动 initcalls…
5. **挂根 / 跑 init**：`root=`、`init=`；其后才是用户态。

> [!example] 排障：内核起来了但进不了用户态
> - 有 `Kernel panic - not syncing: VFS: Unable to mount root` → 根设备驱动未进镜像/initramfs，或 `root=` 写错。
> - 有串口输出停在某一 initcall → 查最后一条 `printk`，对照 `initcall_debug` 启动参数。
> - 完全无输出 → 先查 `console=`、早期 console、波特率与 DT `stdout-path`。

---
## 5. initramfs 直觉

根驱动或组装步骤尚未就绪时，用 **initramfs** 提供早期用户态：加载模块 → 组装根 → `switch_root`。发行版安装镜像与嵌入式救援根都常见。

---
## 6. 自检

1. `tristate` 的 `m` 与 `y` 对启动依赖型驱动意味着什么？
2. 为什么调试 oops 时常要匹配的 `vmlinux`？
3. DTB 一般在启动链哪一环交给内核？

> [!success]- 参考答案
> 1. `y` 启动即可用；`m` 需在用到前 `modprobe`（或由 initramfs/systemd 拉起）——根设备若只是 `m` 且无 initramfs，通常挂死。
> 2. oops 给的是地址；需与 **同一构建** 的 `vmlinux`/映射才能 `addr2line`/解码栈。
> 3. Bootloader 加载后、跳进内核入口时（或 EFI stub 等价路径）把 DTB 地址传给内核。
