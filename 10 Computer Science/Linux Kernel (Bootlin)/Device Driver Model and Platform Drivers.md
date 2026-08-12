---
aliases:
  - 设备驱动模型
  - platform driver
  - probe
  - driver model
tags: [cs, linux_kernel]
up: "[[Linux Kernel (Bootlin) MOC]]"
related:
  - "[[Hardware Description and Device Tree]]"
  - "[[Character Device Drivers]]"
  - "[[Interrupt Management]]"
down:
  - "[[Character Device Drivers]]"
---
# 设备驱动模型与 Platform 驱动

> [!summary] 核心结论
> Linux **device model** 用 **bus / device / driver** 三角：总线匹配成功后调 **`probe`**，卸载或设备消失走 **`remove`**。嵌入式最常见 **platform bus**：设备来自 DT，驱动提供 `platform_driver` + `of_match_table`。优先 **`devm_*`** 托管资源。`EPROBE_DEFER` 表示依赖尚未就绪，核心会重试——不是“永远失败”。

> 底本：Bootlin — Linux device and driver model / Platform drivers。

![[lk-device-model.svg]]

---
## 1. 三角关系

| 对象 | 含义 |
|---|---|
| `struct device` | 一个硬件实例（地址、IRQ、父节点、PM…） |
| `struct device_driver` | 一类硬件的代码（匹配表、probe/remove） |
| bus | 匹配算法 + 遍历（platform、i2c、spi、pci…） |

sysfs：`/sys/devices`、`/sys/bus/platform/drivers/<name>/`。

---
## 2. 一条完整 platform 路径

> [!example] DT ↔ 驱动最小闭环
> **DTS**
> ```dts
> demo@10000000 {
> 	compatible = "vendor,demo";
> 	reg = <0x10000000 0x1000>;
> 	interrupts = <GIC_SPI 40 IRQ_TYPE_LEVEL_HIGH>;
> 	status = "okay";
> };
> ```
> **驱动（节选）**
> ```c
> struct demo_priv {
> 	void __iomem *base;
> 	int irq;
> };
>
> static int demo_probe(struct platform_device *pdev)
> {
> 	struct demo_priv *priv;
> 	int ret;
>
> 	priv = devm_kzalloc(&pdev->dev, sizeof(*priv), GFP_KERNEL);
> 	if (!priv)
> 		return -ENOMEM;
>
> 	priv->base = devm_platform_ioremap_resource(pdev, 0);
> 	if (IS_ERR(priv->base))
> 		return PTR_ERR(priv->base);
>
> 	priv->irq = platform_get_irq(pdev, 0);
> 	if (priv->irq < 0)
> 		return priv->irq;
>
> 	ret = devm_request_irq(&pdev->dev, priv->irq, demo_isr,
> 			       0, "demo", priv);
> 	if (ret)
> 		return ret;
>
> 	platform_set_drvdata(pdev, priv);
> 	/* 还可在此注册 cdev / 读芯片 ID 校验 */
> 	return 0;
> }
>
> static const struct of_device_id demo_of[] = {
> 	{ .compatible = "vendor,demo" },
> 	{ /* sentinel */ }
> };
> MODULE_DEVICE_TABLE(of, demo_of);
>
> static struct platform_driver demo_drv = {
> 	.probe = demo_probe,
> 	.driver = {
> 		.name = "vendor-demo",
> 		.of_match_table = demo_of,
> 	},
> };
> module_platform_driver(demo_drv);
> ```
> **成功标志**：`dmesg` 无报错；`/sys/bus/platform/devices/10000000.demo/driver` 链到你的驱动。

---
## 3. `devm_*` 与错误路径

`devm_kzalloc` / `devm_ioremap_resource` / `devm_request_irq`：在 `probe` 失败或 `remove` 时按登记 **逆序** 释放。

> [!warning] 不能盲目套
> - 非 `devm` 分配仍要手写回滚。
> - 把 `drvdata` 指到非 `devm` 内存又在失败路径提前 return，易 UAF。
> - `remove` 里若还有异步 work，须先 `cancel_*_sync` 再让 `devm` 拆 IRQ。

---
## 4. 生命周期陷阱

| 现象 | 常见原因 |
|---|---|
| 从不 probe | `status=disabled`、compatible 拼写、驱动未加载 |
| 反复 defer | 时钟/供电/GPIO/子驱动尚未 ready → `-EPROBE_DEFER` |
| 启动挂死 | 关键驱动是模块且无 initramfs |
| remove 后 oops | 定时器/IRQ/work 仍在跑 |

> [!example] `EPROBE_DEFER` 心智模型
> `probe` 里 `clk_get` 失败且错误是 defer → 返回 `-EPROBE_DEFER` → 驱动核心稍后重试。若你把 defer 误译成 `-ENOENT` 并放弃，设备可能永远不绑。

---
## 5. 其它总线一瞥

- **I2C/SPI**：`i2c_driver`/`spi_driver`，`reg` 是从地址而非 MMIO。
- **PCI**：Vendor/Device ID；资源来自 BAR。
- 用户态接口常在 probe 里注册 cdev/netdev（见 [[Character Device Drivers]]）。

---
## 6. 自检

1. 谁调用 `probe`？何时 `remove`？
2. `EPROBE_DEFER` 典型因何出现？
3. platform MMIO 基址通常从哪里来？

> [!success]- 参考答案
> 1. 总线匹配成功后由驱动核心调用 `probe`；模块卸载、设备 unbind/热拔（若支持）走 `remove`。
> 2. 依赖的时钟、pinctrl、供电、父设备等尚未 probe 成功。
> 3. DT `reg`（或板级 `resource`）→ `platform_get_resource` / `devm_platform_ioremap_resource`。
