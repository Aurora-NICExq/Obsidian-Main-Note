---
aliases: [Rust 编译器, rustc, Cargo, Rust 工具链, Cargo 常用命令]
tags: [rust, tooling, cargo]
up: "[[Rust MOC]]"
related: "[[Packages, Crates, and Modules|包、Crate 与模块]], [[Variables, Data Types, Functions, and Control Flow|变量与基础语法]], [[Writing Automated Tests|自动化测试]]"
down: "[[Packages, Crates, and Modules|包、Crate 与模块]]"
---
# Rust Compiler and Cargo

> [!summary] 核心结论
> `rustc` 直接把单个 crate 编译为可执行文件或库；实际项目通常交给 Cargo。Cargo 同时负责创建项目、解析依赖、调用编译器、运行测试和生成文档。日常开发优先使用 `cargo check` 快速查错，确认可运行时用 `cargo run`，发布前再用 `cargo build --release`。

---

## 1. Toolchain Overview（工具链总览）

| 工具 | 作用 |
| --- | --- |
| `rustup` | 安装、更新和切换 Rust 工具链 |
| `rustc` | Rust 编译器，直接编译一个 crate root |
| `cargo` | 项目、依赖、构建、测试和发布管理器 |
| `rustfmt` | 按官方风格格式化代码，通常由 `cargo fmt` 调用 |
| `clippy` | 提供比编译错误更深入的代码质量提示 |

查看当前环境：

```bash
rustc --version
cargo --version
rustup show
```

## 2. Compiling a Single File with `rustc`（编译单文件）

对于只包含一个文件的小实验，可以直接编译：

```bash
rustc main.rs
./main                 # Linux / macOS
```

`rustc main.rs` 把 `main.rs` 当作二进制 crate 的 **crate root**。这种方式适合验证语法，但不会自动管理第三方依赖；项目开发通常改用 Cargo。

## 3. Creating a Cargo Project（创建项目）

```bash
cargo new hello_rust       # 创建二进制项目
cargo new --lib my_lib     # 创建库项目
cd hello_rust
```

二进制项目的基本结构：

```text
hello_rust/
├── Cargo.toml       # package 元数据与依赖
└── src/
    └── main.rs      # binary crate root
```

`cargo init` 与 `cargo new` 类似，但用于把**现有目录**初始化为 Cargo 项目。

## 4. Everyday Cargo Workflow（常用开发流程）

| 命令 | 作用 | 是否生成可执行文件 |
| --- | --- | --- |
| `cargo check` | 只做类型检查和借用检查，反馈最快 | 否 |
| `cargo build` | 编译 debug 版本 | 是 |
| `cargo run` | 编译后运行默认二进制 | 是 |
| `cargo test` | 编译并运行测试 | 测试程序 |
| `cargo build --release` | 启用优化，编译 release 版本 | 是 |

常见工作节奏：

```bash
cargo check
cargo test
cargo run
```

默认构建产物位于：

```text
target/debug/       # cargo build / cargo run
target/release/     # cargo build --release
```

`target/` 可以随时重新生成，一般不提交到版本控制。

## 5. Debug and Release Profiles（构建配置）

- **debug**：编译快、保留调试信息、运行时通常较慢，适合开发。
- **release**：编译较慢但启用优化，适合性能测试和发布。

> [!warning]
> 比较程序性能时应使用 `cargo run --release` 或直接运行 `target/release/` 下的程序。debug 构建的性能不能代表正式版本。

可在 `Cargo.toml` 中调整 profile，例如：

```toml
[profile.release]
opt-level = 3
```

## 6. `Cargo.toml` and Dependencies（清单与依赖）

```toml
[package]
name = "hello_rust"
version = "0.1.0"
edition = "2024"

[dependencies]
```

- `[package]` 描述当前 package。
- `[dependencies]` 声明第三方 crate。
- `Cargo.lock` 记录实际解析出的精确依赖版本；应用项目通常应提交它。

添加依赖后，Cargo 会在下一次构建时解析并编译依赖：

```toml
[dependencies]
serde = { version = "1", features = ["derive"] }
```

模块系统和一个 package 内多个 crate 的规则见 [[Packages, Crates, and Modules]]。

## 7. Formatting, Linting, and Documentation（格式、检查与文档）

```bash
cargo fmt                 # 格式化当前 package
cargo fmt -- --check      # 只检查格式，不改文件
cargo clippy              # 静态检查与惯用写法建议
cargo doc --open          # 生成依赖与本项目文档并打开
```

若某组件尚未安装，可通过 rustup 补充：

```bash
rustup component add rustfmt clippy
```

## 8. Reading Compiler Errors（阅读编译错误）

Rust 的错误信息通常按以下顺序阅读：

1. 先看 `error[E....]` 与第一句错误摘要。
2. 看箭头 `-->` 指向的文件和行号。
3. 看带 `^` 的具体表达式与 `help:` 建议。
4. 若出现错误编号，可运行 `rustc --explain E0382` 查看长解释。

不要只修最后一条错误：后续错误可能是第一条错误的连锁反应，应从最前面开始处理。

---

> [!important] 一句话总结
> 单文件实验用 `rustc`，真实项目用 Cargo；开发时 `cargo check` 快速反馈，`cargo test` 验证行为，`cargo fmt`/`cargo clippy` 保持质量，正式构建用 `cargo build --release`。
