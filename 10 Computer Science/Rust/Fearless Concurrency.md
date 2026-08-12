---
aliases: [无畏并发, 并发, Fearless Concurrency, 线程, Mutex, Channel, Send Sync]
tags: [rust, concurrency]
up: "[[Rust MOC]]"
related: "[[Ownership, Borrowing, and Slices|所有权]], [[Smart Pointers|智能指针]], [[Error Handling|错误处理]], [[Functional Language Features Closures and Iterators|move 闭包]]"
down: "[[Object-Oriented Features|面向对象特性]]"
---
# Fearless Concurrency

> [!summary] 核心结论
> Rust 在编译期消灭数据竞争：线程间要么**消息传递**（`channel`，所有权转移），要么**共享状态加锁**（`Mutex`/`Arc`）。类型系统用 `Send` / `Sync` 标记能否安全跨线程转移或共享。恐惧来自竞态；Rust 用所有权让许多错误直接编不过。

对应《The Book》**第 16 章**。前置：[[Ownership, Borrowing, and Slices|所有权]]、[[Smart Pointers|Rc / 内部可变性]]、[[Functional Language Features Closures and Iterators|move 闭包]]。

---

## 1. Threads（线程）

```rust
use std::thread;
use std::time::Duration;

let handle = thread::spawn(|| {
    for i in 1..10 {
        println!("hi number {i} from the spawned thread!");
        thread::sleep(Duration::from_millis(1));
    }
});

handle.join().unwrap(); // 等子线程结束
```

闭包若用主线程数据，通常要 `move` 把所有权迁进子线程（否则借用可能活不过主线程）。

---

## 2. Message Passing（消息传递）

“勿以共享内存通信；应以通信共享内存。”

```rust
use std::sync::mpsc; // multiple producer, single consumer

let (tx, rx) = mpsc::channel();
thread::spawn(move || {
    tx.send(String::from("hi")).unwrap();
});
let received = rx.recv().unwrap(); // 阻塞等待
println!("Got: {received}");
```

- `send` 拿走值的所有权 → 发送后原线程不能再用  
- `recv` 阻塞；`try_recv` 不阻塞  
- `tx.clone()` 可得多个生产者  

---

## 3. Shared State（共享状态）

多人可写同一数据时用锁。

### 3.1 `Mutex<T>`

```rust
use std::sync::Mutex;

let m = Mutex::new(5);
{
    let mut num = m.lock().unwrap(); // MutexGuard
    *num = 6;
} // guard drop → 解锁
```

拿不到锁会阻塞；另一线程 panic 带着锁时，`lock` 返回 `PoisonError`。

### 3.2 `Arc<T>` — 多线程引用计数

`Rc` 不能跨线程。多线程共享用 `Arc`（Atomic Rc）：

```rust
use std::sync::{Arc, Mutex};
use std::thread;

let counter = Arc::new(Mutex::new(0));
let mut handles = vec![];

for _ in 0..10 {
    let counter = Arc::clone(&counter);
    handles.push(thread::spawn(move || {
        let mut num = counter.lock().unwrap();
        *num += 1;
    }));
}
for h in handles {
    h.join().unwrap();
}
```

| 单线程 | 多线程近似 |
| ------ | ---------- |
| `Rc<T>` | `Arc<T>` |
| `RefCell<T>` | `Mutex<T>`（或 `RwLock`） |
| `Rc<RefCell<T>>` | `Arc<Mutex<T>>` |

---

## 4. `Send` and `Sync`

- **`Send`**：所有权可以转移到另一线程  
- **`Sync`**：`&T` 可以安全发给另一线程（即 `T` 可被多线程共享引用）  

绝大多数类型都是 `Send + Sync`。`Rc`、裸指针、未保护的内部可变性等则不是。手写并发原语通常需要 `unsafe`，应用代码优先组合标准库类型。

---

## 5. Mental Model（选型）

| 需求 | 倾向 |
| ---- | ---- |
| 任务独立、结果汇总 | `channel` 传所有权 |
| 多线程改同一状态 | `Arc<Mutex<T>>` |
| 只读共享 | `Arc<T>` |
| 单线程多所有权 | `Rc`（不要用线程） |

---

> [!important] 一句话总结
> 线程用 `spawn`/`join`；通信优先 channel 转移所有权；共享则 `Arc` + `Mutex`；`Send`/`Sync` 是编译器的跨线程通行证。
