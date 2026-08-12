---
aliases: [错误处理, Error Handling, panic, Result, unwrap, expect, ?, 可恢复错误]
tags: [rust, error-handling]
up: "[[Rust MOC]]"
related: "[[Enums and Pattern Matching|枚举与 Option]], [[Packages, Crates, and Modules|模块与可见性]], [[Common Collections|常用集合]], [[Generics, Traits, and Lifetimes|泛型 Trait 与生命周期]]"
down: "[[Generics, Traits, and Lifetimes|泛型 Trait 与生命周期]]"
---
# Error Handling

> [!summary] 核心结论
> Rust 把错误分成两类：**不可恢复**用 `panic!`（打印信息 → 展开/中止调用栈 → 退出）；**可恢复**用 `Result<T, E>`（`Ok(T)` / `Err(E)`），在类型层面强制你处理失败。传播失败用 `?`；`unwrap` / `expect` 是"失败就 panic"的快捷方式。定义可能失败的函数时，**优先返回 `Result`**，只有在程序无法继续、或调用方必须保证前提成立时才 `panic!`。

前置知识：[[Enums and Pattern Matching#3. The `Option<T>` Enum (Option 枚举)|Option]]、[[Enums and Pattern Matching#4. The `match` Control Flow Operator (match 控制流运算符)|match]]。

---

## 1. Two Kinds of Errors (两类错误)

Rust 的可靠性很大程度来自：多数问题在**编译期**就被拦住；运行时仍可能失败的情况，则按是否可恢复区分处理：

| 类型 | 典型例子 | 处理方式 |
| ---- | -------- | -------- |
| **可恢复（recoverable）** | 文件未找到、可重试的网络错误 | `Result<T, E>` |
| **不可恢复（unrecoverable）** | 越界访问等 bug | `panic!` 宏 |

Rust **没有**类似其它语言的异常机制：可恢复走 `Result`，不可恢复走 `panic!`。

## 2. Unrecoverable Errors with `panic!`（不可恢复错误）

### 2.1 What `panic!` Does（panic 时发生什么）

执行 `panic!` 时，程序会：

1. 打印一条错误信息
2. **展开（unwind）** 调用栈，清理沿途函数里的数据
3. 退出程序

```rust
fn main() {
    panic!("crash and burn");
}
```

`panic!` 可能来自你自己写的代码，也可能来自依赖库。通过**回溯（backtrace）**可以定位是谁触发了它。

### 2.2 Unwind vs Abort（展开 与 中止）

默认策略是**展开调用栈**：沿栈往回走，清理每个遇到的函数中的数据——工作量大，但更干净。

也可以选择**立即中止（abort）**：不做清理，直接停掉进程，交给操作系统回收内存。适合想把二进制文件做得更小的场景。

在 `Cargo.toml` 对应的 profile 里设置：

```toml
[profile.release]
panic = 'abort'
```

### 2.3 Backtraces with `RUST_BACKTRACE`（回溯信息）

设置环境变量 `RUST_BACKTRACE` 可打印完整调用栈，用来定位是哪一行触发了 panic：

```bash
RUST_BACKTRACE=1 cargo run
```

值为 `full` 时信息更详细。需要带调试符号的构建（`cargo run` 默认 debug 构建即可）。

## 3. Recoverable Errors with `Result`（可恢复错误）

### 3.1 The `Result<T, E>` Enum

```rust
enum Result<T, E> {
    Ok(T),  // 成功：携带类型为 T 的值
    Err(E), // 失败：携带类型为 E 的错误
}
```

- `T`：成功时 `Ok` 里的数据类型
- `E`：失败时 `Err` 里的错误类型

`Result`、`Ok`、`Err` 都在 Prelude 中，无需 `use`。

打开文件就是典型的可恢复操作——文件可能不存在：

```rust
use std::fs::File;

fn main() {
    let f = File::open("hello.txt"); // 类型是 Result<File, std::io::Error>
}
```

### 3.2 Handling `Result` with `match`

用 `match` 穷举 `Ok` / `Err`，和处理 `Option` 同一套思路：

```rust
use std::fs::File;

fn main() {
    let f = File::open("hello.txt");

    let f = match f {
        Ok(file) => file,
        Err(error) => {
            panic!("Error opening file: {:?}", error);
        }
    };
}
```

### 3.3 Matching on Different Errors（按错误种类分支）

很多错误类型还能再细分。例如 `std::io::Error` 提供 `kind()`，可区分"文件不存在"和其它 IO 错误——不存在就尝试创建，其它情况再 panic：

```rust
use std::fs::File;
use std::io::ErrorKind;

fn main() {
    let f = File::open("hello.txt");

    let f = match f {
        Ok(file) => file,
        Err(error) => match error.kind() {
            ErrorKind::NotFound => match File::create("hello.txt") {
                Ok(fc) => fc,
                Err(e) => panic!("Error creating file: {:?}", e),
            },
            other_error => {
                panic!("Error opening the file: {:?}", other_error);
            }
        },
    };
}
```

嵌套 `match` 能写清逻辑，但偏冗长；实际代码里常用闭包方法（如 `unwrap_or_else`）简化，语义不变。

### 3.4 Shortcuts: `unwrap` and `expect`

| 方法 | 行为 |
| ---- | ---- |
| `unwrap()` | `Ok` → 取出值；`Err` → 调用 `panic!`（信息由标准库给出） |
| `expect("msg")` | 同上，但 panic 时使用**你指定的**错误信息 |

```rust
use std::fs::File;

fn main() {
    // 失败就 panic，信息较笼统
    let f = File::open("hello.txt").unwrap();

    // 失败就 panic，并带上自定义说明——调试时更易定位
    let f = File::open("hello.txt").expect("Failed to open hello.txt");
}
```

原型、示例、或你能**确定**操作不会失败时，用它们很方便；库代码或正式错误处理路径里，更宜返回 `Result` 或显式 `match`。

## 4. Propagating Errors（传播错误）

### 4.1 Returning `Err` to the Caller

调用方往往比当前函数更清楚该怎么处理失败。这时不必自己 panic，而是把 `Err` **原样返回**给上层：

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut f = match File::open("hello.txt") {
        Ok(file) => file,
        Err(e) => return Err(e), // 失败：把错误交给调用方
    };

    let mut s = String::new();

    match f.read_to_string(&mut s) {
        Ok(_) => Ok(s),     // 成功：返回用户名
        Err(e) => Err(e),   // 读失败：同样向上传播
    }
}
```

### 4.2 The `?` Operator（`?` 运算符）

`?` 是上面"传播 Err"模式的语法糖：

- 若是 `Ok(v)`：取出 `v`，继续往后执行
- 若是 `Err(e)`：从当前函数 **提前返回** `Err(e)`（必要时先做错误类型转换，见下节）

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut f = File::open("hello.txt")?;
    let mut s = String::new();
    f.read_to_string(&mut s)?;
    Ok(s)
}
```

还可以链式调用，进一步缩短：

```rust
use std::fs::File;
use std::io::{self, Read};

fn read_username_from_file() -> Result<String, io::Error> {
    let mut s = String::new();
    File::open("hello.txt")?.read_to_string(&mut s)?;
    Ok(s)
}
```

读整个文件为字符串时，标准库已有更短写法：

```rust
use std::fs;
use std::io;

fn read_username_from_file() -> Result<String, io::Error> {
    fs::read_to_string("hello.txt")
}
```

> [!note] `?` 只能用在返回 `Result`（或实现了 `Try` 的类型，如 `Option`）的函数里
> 在返回 `()` 的 `main` 里直接写 `?` 会编译失败。可以把 `main` 改成返回 `Result`，或在 `main` 里用 `match` / `unwrap` 处理。

### 4.3 `?` and the `From` Trait（错误类型转换）

`?` 在返回 `Err` 前，会调用 `From::from`，把实际错误转换成**当前函数返回类型里的 `E`**。只要实现了相应的 `From`，不同错误类型就能在一条 `?` 链里统一向上传。

```rust
use std::convert::From;
// From 定义在 std::convert 中；很多错误类型已提供 From 实现
// ? 遇到 Err(e) 时大致等价于：return Err(From::from(e));
```

这让函数签名可以写一个较宽的错误类型（或自定义错误枚举），内部仍用 `?` 简洁地传播多种来源的失败。

## 5. When to `panic!` vs Return `Result`（何时 panic）

| 场景 | 更合适的选择 |
| ---- | ------------ |
| 定义**可能失败**、且调用方或许能恢复的函数 | 返回 `Result<T, E>` |
| 示例、原型、测试；或失败即表示**程序 bug** | `panic!` / `unwrap` / `expect` |
| 调用方传入了违反 API 约定的值（如越界索引） | 可 `panic!`（与 `Vec` 的 `[]` 类似） |
| 外部输入、IO、网络等**预期会发生**的失败 | `Result`，让调用方决定 |

> [!tip] 经验法则
> **优先返回 `Result`**；只有在"继续执行下去没有意义"或"这是编程错误"时才 `panic!`。

---

> [!important] 一句话总结
> 不可恢复 → `panic!`（可配 unwind/abort，用 `RUST_BACKTRACE` 查栈）；可恢复 → `Result` + `match` / `?`；`unwrap`/`expect` 是失败即崩的捷径；能恢复就别崩，把选择权交给调用方。
