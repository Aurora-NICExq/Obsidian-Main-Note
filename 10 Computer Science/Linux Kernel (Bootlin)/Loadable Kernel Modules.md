---
aliases:
  - 内核模块
  - LKM
  - insmod
  - modprobe
tags: [cs, linux_kernel]
up: "[[Linux Kernel (Bootlin) MOC]]"
related:
  - "[[Kernel Configuration Build and Boot]]"
  - "[[Character Device Drivers]]"
down:
  - "[[Hardware Description and Device Tree]]"
---
# 可加载内核模块

> [!summary] 核心结论
> **LKM** 把代码编译成 `.ko`，运行时链入内核地址空间：`module_init` / `module_exit` 成对，加载失败必须回滚已申请资源。`insmod` 直接加载文件；`modprobe` 解析依赖。模块参数用 `module_param`；导出用 `EXPORT_SYMBOL[_GPL]`。模块与运行中内核的 **版本/配置** 必须匹配。

> 底本：Bootlin — Kernel modules。

![[lk-module-lifecycle.svg]]

---
## 1. 最小模块骨架

```c
#include <linux/module.h>
#include <linux/init.h>

static int __init m_init(void)
{
	pr_info("hello\n");
	return 0; /* 非 0 → 加载失败，不会调用 exit */
}
static void __exit m_exit(void)
{
	pr_info("bye\n");
}
module_init(m_init);
module_exit(m_exit);
MODULE_LICENSE("GPL");
MODULE_AUTHOR("you");
MODULE_DESCRIPTION("demo");
```

---
## 2. 构建外部模块

```make
obj-m += hello.o
KDIR ?= /lib/modules/$(shell uname -r)/build
all:
	$(MAKE) -C $(KDIR) M=$(PWD) modules
clean:
	$(MAKE) -C $(KDIR) M=$(PWD) clean
```

`KDIR` 必须指向 **与目标内核匹配** 的构建树（含 `.config`、生成头、`Module.symvers`）。

> [!example] 交叉编译外模块
> ```bash
> make ARCH=arm64 CROSS_COMPILE=aarch64-linux-gnu- \
>   -C /path/to/kernel M=$PWD modules
> ```
> 把 `.ko` 拷到板上后，`uname -r` 与 vermagic 仍须一致（或你自己编的同树内核）。

---
## 3. 加载与依赖

| 命令 | 行为 |
|---|---|
| `insmod foo.ko` | 加载指定文件，**不**自动拉依赖 |
| `modprobe foo` | 按名解析 `modules.dep` 并加载 |
| `rmmod` / `modprobe -r` | 卸载（引用计数 ≠0 失败） |
| `lsmod` | 已加载列表 |
| `modinfo foo.ko` | 参数、依赖、vermagic、许可证 |

---
## 4. 参数、符号、引用计数

```c
static int debug;
module_param(debug, int, 0644);
MODULE_PARM_DESC(debug, "enable verbose");
EXPORT_SYMBOL_GPL(my_helper);
```

- 加载：`insmod foo.ko debug=1`；或 `/sys/module/foo/parameters/debug`。
- 设备 `open` 时常 `try_module_get`，`release` 时 `module_put`，防止使用中被 `rmmod`。

---
## 5. 失败路径（必练）

> [!example] init 中途失败必须回滚
> ```c
> static int __init m_init(void)
> {
> 	int ret;
> 	ret = alloc_chrdev_region(...);
> 	if (ret) return ret;
> 	ret = request_irq(...);
> 	if (ret) goto err_chrdev;
> 	ret = misc_register(...);
> 	if (ret) goto err_irq;
> 	return 0;
> err_irq:
> 	free_irq(...);
> err_chrdev:
> 	unregister_chrdev_region(...);
> 	return ret;
> }
> ```
> 加载失败时 **不会** 调用 `module_exit`。泄漏的 IRQ/映射会直到重启才消失。

> [!warning] 常见翻车
> - `MODULE_LICENSE` 缺失/非 GPL → 污染内核 taint；可能用不了 `EXPORT_SYMBOL_GPL`。
> - `rmmod` 时还有 workqueue/定时器在跑 → UAF；要用 `cancel_work_sync` 等。
> - 只 `insmod` 忘了依赖模块 → `Unknown symbol in module`。

---
## 6. 自检

1. 为何发行版强调 headers 与 running kernel 一致？
2. `insmod` 与 `modprobe` 差在哪？
3. `module_init` 返回 `-ENOMEM` 后会调用 `module_exit` 吗？

> [!success]- 参考答案
> 1. 外模块针对该构建的配置、头文件与 `Module.symvers` 编译；不一致则 vermagic/CRC 失败或运行期 ABI 错乱。
> 2. `insmod` 只加载给定文件；`modprobe` 按模块名解析依赖并加载。
> 3. 不会。必须在 `init` 自己的错误路径释放已申请资源。
