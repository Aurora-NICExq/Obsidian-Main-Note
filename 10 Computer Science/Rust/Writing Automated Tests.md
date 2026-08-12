---
aliases: [编写自动化测试, 自动化测试, Rust Testing, cargo test, unit test, integration test]
tags: [rust, testing]
up: "[[Rust MOC]]"
related: "[[Rust Compiler and Cargo|Cargo 与编译器]], [[Error Handling|错误处理]], [[Packages, Crates, and Modules|模块与可见性]], [[Building a CLI Search Tool (minigrep)|minigrep]], [[Functional Language Features Closures and Iterators|闭包与迭代器]]"
down: "[[Building a CLI Search Tool (minigrep)|minigrep]]"
---
# Writing Automated Tests

> [!summary] 核心结论
> Rust 测试就是标了 `#[test]` 的函数：准备数据 → 调用被测代码 → **断言**结果。失败通常表现为 panic（或返回 `Err`）。日常用 `cargo test`；默认**并行**跑、**捕获**通过测试的 stdout。组织上分**单元测试**（与代码同文件、`#[cfg(test)]` 模块，可测私有项）和**集成测试**（`tests/` 目录，只测公有 API）。

前置知识：[[Rust Compiler and Cargo|Cargo]]、[[Error Handling|panic! 与 Result]]、[[Packages, Crates, and Modules|模块与 `use`]]。

---

## 1. What a Test Is（测试是什么）

测试是用来验证**非测试代码**行为是否符合预期的函数。函数体通常三步：

1. **准备**数据 / 状态（Arrange）
2. **运行**被测代码（Act）
3. **断言**结果（Assert）

### 1.1 Anatomy: the `#[test]` Attribute

Attribute（属性）是附着在代码上的元数据。在函数上加 `#[test]`，就把它登记为测试函数：

```rust
#[test]
fn it_works() {
    let result = 2 + 2;
    assert_eq!(result, 4);
}
```

### 1.2 Running with `cargo test`

```bash
cargo test
```

Cargo 会构建一个 **test runner**，运行所有带 `#[test]` 的函数并汇报成败。用 `cargo new --lib` 创建库时，模板里会带一个 `tests` 模块和一个示例测试；你可以加任意多个测试模块或函数。

### 1.3 How Failure Is Detected

- 测试线程里发生 **panic** → 该测试失败  
- 每个测试默认跑在**独立线程**；主线程发现子线程挂了，就标记失败  

因此 `assert!` 失败（内部会 panic）、你主动 `panic!`、或未捕获的 unwind，都会让测试红。

---

## 2. Assertions（断言）

### 2.1 `assert!`

标准库宏：参数为 `true` 则通过，否则 panic。

```rust
assert!(result.contains("Carol"));
```

### 2.2 `assert_eq!` and `assert_ne!`

比较两个值是否相等 / 不等（底层用 `==` / `!=`）。失败时会**自动打印**左右两边的值，调试比纯 `assert!` 更方便。左右类型需实现 `PartialEq` 和 `Debug`。

```rust
assert_eq!(2 + 2, 4);
assert_ne!(add(2, 2), 5);
```

### 2.3 Custom Failure Messages

三个宏都可以在必填参数后再跟格式化字符串（与 `format!` 相同）：

```rust
pub fn greeting(name: &str) -> String {
    format!("Hello {name}!")
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn greeting_contains_name() {
        let result = greeting("Carol");
        assert!(
            result.contains("Carol"),
            "Greeting did not contain name, value was `{result}`"
        );
    }
}
```

`assert!`：第 1 个参数是条件，自定义消息从第 2 个起。`assert_eq!` / `assert_ne!`：前两个是比较对象，之后才是消息。

---

## 3. Checking for Panics: `#[should_panic]`

除了检查返回值，还应验证**预期会出错**的路径是否真的 panic（例如非法输入）。

```rust
pub struct Guess {
    value: u32,
}

impl Guess {
    pub fn new(value: u32) -> Guess {
        if !(1..=100).contains(&value) {
            panic!("Guess value must be between 1 and 100, got {value}.");
        }
        Guess { value }
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    #[should_panic]
    fn greater_than_100() {
        Guess::new(200);
    }

    // 更精确：失败消息须包含指定文字
    #[test]
    #[should_panic(expected = "between 1 and 100")]
    fn greater_than_100_with_expected() {
        Guess::new(200);
    }
}
```

`expected` 用来避免“随便某个 panic”也算通过——消息里要包含你指定的片段。

---

## 4. Writing Tests that Return `Result<T, E>`

不一定非要 panic 才失败：测试也可以返回 `Result`：

- 返回 `Ok(())` → 通过  
- 返回 `Err(...)` → 失败  

```rust
#[test]
fn it_works() -> Result<(), String> {
    if 2 + 2 == 4 {
        Ok(())
    } else {
        Err(String::from("two plus two does not equal four"))
    }
}
```

这样能在测试里直接用 `?`。**不要**在返回 `Result` 的测试上再标 `#[should_panic]`——两者语义冲突。

---

## 5. Controlling How Tests Run（控制运行方式）

默认行为：

- **并行**跑全部测试  
- **捕获**通过测试的标准输出（失败时才打印，方便盯结果）

命令行参数分两类：

| 位置 | 作用对象 |
| ---- | -------- |
| `cargo test` 后面、`--` 前面 | 交给 Cargo（如按名称筛选） |
| `--` **后面** | 交给测试可执行文件（如线程数、是否显示输出） |

```bash
cargo test --help          # Cargo 侧
cargo test -- --help       # 测试二进制侧
```

### 5.1 Parallel vs Serial

默认多线程并行，速度快，但测试之间**不能互相依赖**，也不能抢同一份共享状态（同一文件、同一环境变量、同一工作目录等）。

串行或限制线程数：

```bash
cargo test -- --test-threads=1
```

### 5.2 Showing Function Output

通过时，`println!` 等输出默认被吃掉；失败时会一并打出。想无论成败都看见输出：

```bash
cargo test -- --show-output
# 或
cargo test -- --nocapture
```

### 5.3 Running a Subset by Name

把名称（或名称的一部分）传给 `cargo test`，只跑匹配的测试：

```bash
cargo test greater_than_100
cargo test greeting          # 名字里带 greeting 的都会跑
```

### 5.4 Ignoring Tests: `#[ignore]`

耗时长或不想默认跑的测试可标 `#[ignore]`：平时 `cargo test` 会跳过它们。

```rust
#[test]
fn it_works() { /* ... */ }

#[test]
#[ignore]
fn expensive_test() { /* ... */ }
```

```bash
cargo test                   # 跑未 ignore 的
cargo test -- --ignored      # 只跑被 ignore 的
cargo test -- --include-ignored  # 全部都跑
```

---

## 6. Test Organization（单元测试 vs 集成测试）

| | 单元测试（Unit） | 集成测试（Integration） |
| --- | --- | --- |
| 位置 | 与源码同文件（常 `mod tests`） | 项目根下 `tests/` 目录，每个文件是独立 crate |
| 配置 | 模块上 `#[cfg(test)]` | 本身只在 `cargo test` 时参与，一般不必再标 cfg |
| 可见性 | 可测**私有**函数（`use super::*`） | 只能当**外部用户**，测公有 API |
| 用途 | 细粒度、内部逻辑 | 多模块协作、对外契约 |

### 6.1 Unit Tests and `#[cfg(test)]`

```rust
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn adds_two_numbers() {
        assert_eq!(add(2, 3), 5);
    }
}
```

`cfg` = configuration：下面的条目只在指定配置下才编译。Rust 在跑测试时打开 `test` 配置，因此：

- `cargo test`：编译并运行该模块（含 helper 与 `#[test]`）  
- `cargo build` / 发布构建：**不会**把测试模块打进产物  

集成测试在单独目录，不依赖在业务模块上贴 `#[cfg(test)]`。

### 6.2 Integration Tests（简述）

在 package 根创建 `tests/`，例如 `tests/integration_test.rs`：

```rust
use my_crate; // 像外部依赖一样 use 你的库

#[test]
fn it_adds_two() {
    assert_eq!(my_crate::add(2, 2), 4);
}
```

`tests/` 下每个文件是独立的集成测试 crate；公共 helper 可放在 `tests/common/mod.rs` 这类模块里（不要标成带 `#[test]` 的可执行测试文件名习惯即可）。二进制 crate 若没有 `lib.rs`，集成测试无法 `use` 库 API——常见做法是把逻辑放进 library，binary 只做薄封装。

---

## 7. Cheatsheet（命令速查）

```bash
cargo test
cargo test <filter>
cargo test -- --test-threads=1
cargo test -- --show-output
cargo test -- --ignored
cargo test -- --include-ignored
```

---

> [!important] 一句话总结
> `#[test]` + 断言（或 `Result`）写行为规格；`#[should_panic]` 测恐慌路径；`cargo test` 默认并行且安静，用 `--` 后参数调线程 / 输出 / ignore；单元测试贴着代码用 `#[cfg(test)]`，集成测试站在 `tests/` 只打公有 API。
