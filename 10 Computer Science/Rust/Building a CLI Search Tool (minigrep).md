---
aliases: [minigrep, Rust grep, I/O 项目, 命令行搜索, Building a Command Line Program]
tags: [rust, cli, io, project]
up: "[[Rust MOC]]"
related: "[[Writing Automated Tests|自动化测试]], [[Error Handling|错误处理]], [[Packages, Crates, and Modules|模块与可见性]], [[Generics, Traits, and Lifetimes|生命周期]], [[Ownership, Borrowing, and Slices|所有权]], [[Functional Language Features Closures and Iterators|闭包与迭代器]]"
down: "[[Functional Language Features Closures and Iterators|闭包与迭代器]]"
---
# Building a CLI Search Tool (minigrep)

> [!summary] 核心结论
> 官方书 *The Rust Programming Language* 第 12–13 章用 **minigrep** 做一个迷你 `grep`：从命令行读查询词与文件名，读文件，按行搜索并打印。实践要点是 **binary + library 拆分**（`main` 只做参数与退出码，逻辑在 `lib`）、用 `Config` 聚合配置、用 `Result` + `?` 处理 I/O、用生命周期让 `search` 返回指向文件内容的 `&str`，再用环境变量切换大小写敏感，并用单元测试锁住搜索行为。

实例路径：`~/Developer/rust_grep/minigrep`（对应书中 I/O 项目练习）。

前置：[[Packages, Crates, and Modules|包与模块]]、[[Error Handling|Result / ?]]、[[Writing Automated Tests|测试]]、[[Generics, Traits, and Lifetimes#4.3 Lifetimes in Function Signatures（函数签名中的生命周期）|函数中的生命周期]]。

---

## 1. 项目目标与用法

在文件中查找包含查询串的行，打印到标准输出。

```bash
cd ~/Developer/rust_grep/minigrep
cargo run -- <query> <filename>
# 例：
cargo run -- nobody poem.txt
```

大小写不敏感（本实现）：设置环境变量 `CASE_INSENSITIVE`（任意值即可，只要变量存在）：

```bash
CASE_INSENSITIVE=1 cargo run -- rUsT poem.txt
```

示例文本 `poem.txt` 是狄金森诗句片段，用来手动试跑。

---

## 2. 目录与职责拆分

```text
minigrep/
├── Cargo.toml
├── poem.txt
└── src/
    ├── main.rs   # binary：读参数、调库、处理退出
    └── lib.rs    # library：Config、run、search、测试
```

| 文件 | 职责 |
| ---- | ---- |
| `main.rs` | `env::args` → `Config::new` → `run`；出错打印并 `process::exit(1)` |
| `lib.rs` | 可测试的核心逻辑；`main` 保持很薄 |

> [!tip] 为什么拆成 lib？
> 集成 / 单元测试可以直接 `use minigrep::...`；逻辑不绑死在 `main` 里。书中强调：**binary 做启动，library 做业务**。

`Cargo.toml` 里 package 名是 `minigrep`，因此库 crate 名也是 `minigrep`。

---

## 3. `main`：参数、错误与退出码

```rust
use minigrep::Config;
use std::env;
use std::process;

fn main() {
    let args: Vec<String> = env::args().collect();

    let config = Config::new(&args).unwrap_or_else(|err| {
        println!("Problem parsing arguments: {err}");
        process::exit(1);
    });

    if let Err(e) = minigrep::run(config) {
        println!("Application error: {e}");
        process::exit(1);
    }
}
```

要点：

- `env::args()` 第 0 个是程序路径，真正参数从下标 1 开始  
- 解析失败用 `unwrap_or_else` 打印后退出，而不是 `unwrap` 直接 panic  
- 运行期错误用 `if let Err` + `exit(1)`，把“可恢复的失败”变成进程退出码  

---

## 4. `Config`：把参数收成一个结构

```rust
pub struct Config {
    pub query: String,
    pub filename: String,
    pub case_sensitive: bool,
}

impl Config {
    pub fn new(args: &[String]) -> Result<Config, &'static str> {
        if args.len() < 3 {
            return Err("Not enough arguments");
        }

        let query = args[1].clone();
        let filename = args[2].clone();
        // 环境变量存在 → 不区分大小写
        let case_sensitive = env::var("CASE_INSENSITIVE").is_err();

        Ok(Config {
            query,
            filename,
            case_sensitive,
        })
    }
}
```

| 字段 | 含义 |
| ---- | ---- |
| `query` | 要搜索的字符串 |
| `filename` | 目标文件路径 |
| `case_sensitive` | `true` 区分大小写；`CASE_INSENSITIVE` 设了则为 `false` |

`clone` 是因为 `args` 里是借用切片，而 `Config` 需要**拥有**自己的 `String`（之后 `main` 里的 `args` 可以结束）。

环境变量用 `env::var(...).is_err()`：变量**不存在** → 区分大小写；**存在** → 不区分。这是书里常见写法（只关心有没有，不关心具体值）。

---

## 5. `run`：读文件并打印匹配行

```rust
pub fn run(config: Config) -> Result<(), Box<dyn Error>> {
    let contents = fs::read_to_string(config.filename)?;

    let results = if config.case_sensitive {
        search(&config.query, &contents)
    } else {
        search_case_insensitive(&config.query, &contents)
    };

    for line in results {
        println!("{line}");
    }

    Ok(())
}
```

- `fs::read_to_string` 失败时 `?` 把错误向上传  
- 返回 `Result<(), Box<dyn Error>>`：调用方不必绑定某一种具体错误类型（见 [[Error Handling#4.3 `?` and the `From` Trait（错误类型转换）|? 与 From]]）  
- 按 `case_sensitive` 在两个搜索函数间分支  

---

## 6. `search` 与生命周期

```rust
pub fn search<'a>(query: &str, contents: &'a str) -> Vec<&'a str> {
    let mut results = Vec::new();

    for line in contents.lines() {
        if line.contains(query) {
            results.push(line);
        }
    }

    results
}
```

返回的每一行是 `contents` 里的切片，所以生命周期挂在 `contents` 上：`Vec<&'a str>`。`query` 只用来比较，不必和返回值共享同一个 `'a`。

大小写不敏感版：先把 `query` 转小写；每行临时 `to_lowercase()` 再 `contains`。返回的仍是**原始行**（大小写不变）：

```rust
pub fn search_case_insensitive<'a>(
    query: &str,
    contents: &'a str,
) -> Vec<&'a str> {
    let query = query.to_lowercase();
    let mut results = Vec::new();

    for line in contents.lines() {
        if line.to_lowercase().contains(&query) {
            results.push(line);
        }
    }

    results
}
```

注意：`query` 阴影成了拥有所有权的 `String`，`contains` 要写 `&query`。

---

## 7. 单元测试（锁住搜索行为）

测试写在 `lib.rs` 的 `#[cfg(test)] mod tests` 里，直接测私有/公有搜索函数：

```rust
#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn one_result() {
        let query = "duct";
        let contents = "\
Rust:
safe,fast,productive.
Duct type.
Pick three.";
        // 区分大小写：不匹配 "Duct"
        assert_eq!(vec!["safe,fast,productive."], search(query, contents));
    }

    #[test]
    fn case_insensitive() {
        let query = "rUsT";
        let contents = "\
Rust:
safe,fast,productive.
Duct type.
Trust me.";
        assert_eq!(
            vec!["Rust:", "Trust me."],
            search_case_insensitive(query, contents)
        );
    }
}
```

`one_result` 里故意放了 `Duct type.`：区分大小写时不应命中，用来防止以后改坏。

```bash
cargo test
```

---

## 8. 数据流总览

![[d2-building-a-cli-search-tool-minigrep-01.svg]]

| 概念 | 在本项目中的落点 |
| ---- | ---------------- |
| 模块 / 可见性 | `pub struct`、`pub fn`；`main` `use minigrep::...` |
| 错误处理 | `Result`、`?`、`Box<dyn Error>`、进程 `exit(1)` |
| 所有权 | `String::clone` 进 `Config`；文件内容一次读入 |
| 生命周期 | `search` 返回的行借用自 `contents` |
| 环境变量 | `CASE_INSENSITIVE` 切换搜索模式 |
| 测试 | `#[cfg(test)]` 测两种搜索 |

---

## 9. 可继续改进（书中后续方向）

当前实例已覆盖书中主线。常见延伸（不必一次做完）：

- 把错误信息打到 **stderr**（`eprintln!`），正常匹配仍用 `println!`  
- `Config::build` / 迭代器版 `args`（少一次 `collect` + `clone`）  
- 用迭代器改写 `search`（`filter` + `collect`）  
- 更多测试：零命中、多命中、空查询  

---

> [!important] 一句话总结
> minigrep = 薄 `main` + 可测的 `lib`：`Config` 吃参数与环境变量，`run` 读文件，`search` 用生命周期借出行切片；`Result` 处理 I/O，测试锁住大小写两种行为。这是把前面章节（模块、错误、生命周期、测试）串成一个真实小工具的练习。
