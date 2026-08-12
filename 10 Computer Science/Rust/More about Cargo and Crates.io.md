---
aliases: [Cargo 进阶, crates.io, 发布 crate, 文档注释, More about Cargo]
tags: [rust, cargo, crates-io]
up: "[[Rust MOC]]"
related: "[[Rust Compiler and Cargo|Cargo 基础]], [[Packages, Crates, and Modules|包与模块]], [[Functional Language Features Closures and Iterators|闭包与迭代器]]"
down: "[[Smart Pointers|智能指针]]"
---
# More about Cargo and Crates.io

> [!summary] 核心结论
> Cargo 不止能 build/test：可用 **release profile** 调优化，用 **workspaces** 管多包，用 **`cargo doc` / 文档注释** 生成 API 文档，用 **`cargo publish`** 把库发到 crates.io，并用语义化版本约束依赖。分享代码时还可通过 Git / 路径依赖引入未上架的 crate。

对应《The Book》**第 14 章**。前置：[[Rust Compiler and Cargo|Cargo 基础]]、[[Packages, Crates, and Modules|包与模块]]。

---

## 1. Release Profiles（构建配置）

Cargo 内置 profile，常见：

| Profile | 命令 | 特点 |
| ------- | ---- | ---- |
| `dev` | `cargo build` | 少优化、快编译、多调试信息 |
| `release` | `cargo build --release` | 多优化、慢编译、适合发布 |

在 `Cargo.toml` 可覆盖：

```toml
[profile.release]
opt-level = 3
```

`opt-level`：`0`–`3`，以及 `"s"` / `"z"`（偏体积）。细节见 [Cargo Book Profiles](https://doc.rust-lang.org/cargo/reference/profiles.html)。

---

## 2. Workspaces（工作空间）

多个相关 package 放在同一 workspace：共享一个 `Cargo.lock` 与 `target/`，依赖只编译一份。

```toml
# 根 Cargo.toml
[workspace]
resolver = "2"
members = ["adder", "add_one"]
```

```bash
cargo new adder
cargo new add_one --lib
cargo run -p adder          # 指定成员包
cargo test --workspace      # 测所有成员
```

成员之间在各自 `Cargo.toml` 用路径依赖：`add_one = { path = "../add_one" }`。

---

## 3. Documentation Comments（文档注释）

`///` 给其后的项写文档；`//!` 给**包含它的 crate / 模块**写文档。支持 Markdown。

```rust
/// Adds one to the number given.
///
/// # Examples
///
/// ```
/// let arg = 5;
/// let answer = my_crate::add_one(arg);
/// assert_eq!(6, answer);
/// ```
pub fn add_one(x: i32) -> i32 {
    x + 1
}
```

```bash
cargo doc --open     # 生成并打开 HTML 文档（含依赖）
cargo test           # 文档里的示例代码也会当测试跑
```

常用标题约定：`# Examples`、`# Panics`、`# Errors`、`# Safety`。

`pub use` 可在 crate 根**重导出**，让文档呈现更整齐的公共 API。

---

## 4. Publishing to crates.io（发布）

1. 在 [crates.io](https://crates.io) 用 GitHub / 邮箱账号，拿 API token：`cargo login`  
2. `Cargo.toml` 填好 `name`、`version`、`edition`、`description`、`license` 等元数据  
3. `cargo publish`（名字全局唯一；版本遵循语义化）

```toml
[package]
name = "my_crate"
version = "0.1.0"
edition = "2024"
description = "A short description"
license = "MIT OR Apache-2.0"
```

已发布版本**不可覆盖**；修 bug 需升版本再发。可用 `cargo yank` 标记某版本不可新依赖（已下载的不受影响）。

---

## 5. Dependency Specs Beyond crates.io（其它依赖来源）

```toml
[dependencies]
# crates.io（默认）
regex = "1.10"

# Git
reno = { git = "https://github.com/example/reno" }

# 本地路径（开发中）
my_lib = { path = "../my_lib" }
```

版本要求常用：`"0.8.0"`、`"^0.8"`、`">=0.8.0, <0.9.0"`（Cargo 默认兼容语义见文档）。

---

## 6. Cargo install（安装二进制）

```bash
cargo install ripgrep
```

从 crates.io（或指定来源）编译并安装**二进制 crate**到 `~/.cargo/bin`。只适用于有 binary target 的包，不是装库到项目。

---

## 7. Extending with Custom Commands（自定义子命令）

`$PATH` 里名为 `cargo-something` 的二进制可通过 `cargo something` 调用——生态里的 `cargo-clippy`、`cargo-fmt` 等同理。

---

> [!important] 一句话总结
> Profile 管怎么编，workspace 管多包，文档注释 + `cargo doc`/`test` 管说明，`publish`/`yank` 管上架，路径与 Git 依赖管私有协作。
