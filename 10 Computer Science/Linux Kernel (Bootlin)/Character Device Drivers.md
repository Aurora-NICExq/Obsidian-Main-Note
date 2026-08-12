---
aliases:
  - 字符设备
  - cdev
  - file_operations
  - miscdevice
tags: [cs, linux_kernel]
up: "[[Linux Kernel (Bootlin) MOC]]"
related:
  - "[[Device Driver Model and Platform Drivers]]"
  - "[[Loadable Kernel Modules]]"
  - "[[Sleeping Waiting and Deferred Work]]"
down:
  - "[[Kernel Memory Management]]"
---
# 字符设备驱动

> [!summary] 核心结论
> **字符设备**经 `/dev/node` → VFS → **`file_operations`** 暴露给用户态。注册：设备号 → `cdev_init`/`cdev_add` → `device_create`（或 **`miscdevice`**）。`read`/`write` 必须处理部分传输、阻塞/非阻塞、`copy_*_user` 失败；永不直接解引用 `__user` 指针。

> 底本：Bootlin — Character device drivers。

![[lk-char-fops.svg]]

---
## 1. 调用链

```
open/read/...  →  VFS  →  f_op->read  →  驱动
                 struct file *filp
```

`filp->private_data` 常在 `open` 里挂私有结构。

---
## 2. 注册套路

```c
alloc_chrdev_region(&dev, 0, 1, "mydev");
cdev_init(&priv->cdev, &my_fops);
priv->cdev.owner = THIS_MODULE;
cdev_add(&priv->cdev, dev, 1);
device_create(cls, NULL, dev, NULL, "mydev"); /* → /dev/mydev */
```

卸载逆序：`device_destroy` → `cdev_del` → `unregister_chrdev_region`。

> [!tip] `misc_register`
> 单一简单设备可用 misc（主设备号 10），少写 class/区域样板。

---
## 3. `file_operations` 要点

| 方法 | 注意 |
|---|---|
| `open`/`release` | 分配/释放 `private_data`；`stream_open` |
| `read`/`write` | `copy_to_user`/`copy_from_user`；返回已传字节或负 errno |
| `unlocked_ioctl` | 命令号、方向、大小；必要时 `compat_ioctl` |
| `poll` | 注册 wait queue，供 select/epoll |
| `mmap` | 注意缓存属性与权限 |

> [!example] 阻塞读的正确骨架
> ```c
> static ssize_t my_read(struct file *f, char __user *buf,
>                        size_t n, loff_t *ppos)
> {
> 	struct my_priv *p = f->private_data;
> 	ssize_t ret;
>
> 	if (n == 0)
> 		return 0;
>
> 	ret = wait_event_interruptible(p->wq, p->have_data ||
> 				       (f->f_flags & O_NONBLOCK));
> 	if (ret)
> 		return ret;
>
> 	if (!p->have_data) {
> 		if (f->f_flags & O_NONBLOCK)
> 			return -EAGAIN;
> 	}
>
> 	n = min(n, p->datalen);
> 	if (copy_to_user(buf, p->data, n))
> 		return -EFAULT;
> 	p->have_data = false;
> 	return n;
> }
> ```
> ISR 或 bottom half 里置 `have_data` 并 `wake_up_interruptible(&p->wq)`。

> [!warning] 永不信任用户指针
> `copy_to_user` 失败返回 `-EFAULT`。长度来自用户时防整数溢出（`n * size`）。

---
## 4. 与 platform `probe` 的关系

`probe`：ioremap、IRQ、分配 priv、注册 cdev。  
`remove`：先拒绝新 open / 醒来阻塞读者，再注销 cdev，再拆硬件。

---
## 5. 自检

1. `copy_to_user` 失败应返回什么？
2. 为何用 `unlocked_ioctl` 而非老 `ioctl`？
3. `O_NONBLOCK` 且无数据时 `read` 应返回什么？

> [!success]- 参考答案
> 1. `-EFAULT`（不要假装传成功）。
> 2. 大内核锁 BKL 已移除；`unlocked_ioctl` 自行做并发保护。
> 3. `-EAGAIN`（或 `-EWOULDBLOCK`）。
