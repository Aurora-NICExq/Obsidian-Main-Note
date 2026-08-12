---
aliases: [Rust 导航, Rust MOC, Rust Index]
tags: [rust, MOC]
up: ""
related: "[[Linux MOC|Linux MOC]], [[C_DataStruct MOC|C 数据结构]]"
down: "[[Rust Compiler and Cargo|Rust 工具链]], [[Variables, Data Types, Functions, and Control Flow|基础语法]], [[Ownership, Borrowing, and Slices|所有权]], [[Structs, Methods, and Associated Functions|结构体]], [[Enums and Pattern Matching|枚举与模式匹配]], [[Common Collections|常用集合]], [[Packages, Crates, and Modules|项目组织]], [[Error Handling|错误处理]], [[Generics, Traits, and Lifetimes|泛型 Trait 与生命周期]], [[Writing Automated Tests|自动化测试]], [[Building a CLI Search Tool (minigrep)|minigrep]], [[Functional Language Features Closures and Iterators|闭包与迭代器]], [[More about Cargo and Crates.io|Cargo 进阶]], [[Smart Pointers|智能指针]], [[Fearless Concurrency|并发]], [[Object-Oriented Features|OOP]], [[Patterns and Matching|模式进阶]], [[Advanced Features|高级特性]]"
---
# Rust MOC

> [!summary] 学习主线
> 按官方 [*The Rust Programming Language*](https://doc.rust-lang.org/book/) 主线整理：语法与所有权 → 类型与模块 → 错误 / 泛型 / 测试 → I/O 实战 → 闭包迭代器与 Cargo 进阶 → 智能指针与并发 → OOP / 模式 → **高级特性**。以下笔记对应书中章节，风格统一为 summary + 双语小节 + 可运行示例。

## 一、工具链与基础语法（Ch 1–3）

- [[Rust Compiler and Cargo|Rust Compiler and Cargo]]：`rustc`、Cargo 工作流、构建配置与编译错误
- [[Variables, Data Types, Functions, and Control Flow|Variables, Data Types, Functions, and Control Flow]]：变量、类型、函数、表达式与循环

## 二、所有权系统（Ch 4）

- [[Ownership, Borrowing, and Slices|Ownership, Borrowing, and Slices]]：move、`Copy`、`clone`、共享/可变借用与切片

## 三、自定义类型与模式匹配（Ch 5–6）

- [[Structs, Methods, and Associated Functions|Structs, Methods, and Associated Functions]]：字段、更新语法、方法与关联函数
- [[Enums and Pattern Matching|Enums and Pattern Matching]]：变体、`Option<T>`、`match` 与 `if let`

## 四、标准集合（Ch 8）

- [[Common Collections|Common Collections]]：`Vec<T>`、`String`、`HashMap<K, V>` 与集合中的所有权

## 五、项目组织（Ch 7）

- [[Packages, Crates, and Modules|Packages, Crates, and Modules]]：package、crate、模块树、可见性与 `use`

## 六、错误处理（Ch 9）

- [[Error Handling|Error Handling]]：`panic!`、`Result<T, E>`、`?` 传播与何时该 panic

## 七、泛型、Trait 与生命周期（Ch 10）

- [[Generics, Traits, and Lifetimes|Generics, Traits, and Lifetimes]]：类型参数、Trait / Trait bound、生命周期标注与省略

## 八、自动化测试（Ch 11）

- [[Writing Automated Tests|Writing Automated Tests]]：`#[test]`、断言、`should_panic`、`cargo test` 参数、单元 / 集成测试

## 九、I/O 实战项目（Ch 12）

- [[Building a CLI Search Tool (minigrep)|Building a CLI Search Tool (minigrep)]]：CLI 参数、`Config`、读文件、搜索与生命周期、环境变量、测试

## 十、函数式特性（Ch 13）

- [[Functional Language Features Closures and Iterators|Functional Language Features: Closures and Iterators]]：闭包捕获与 `Fn*` Trait、迭代器适配器 / 消费器、改进 minigrep

## 十一、Cargo 与 crates.io（Ch 14）

- [[More about Cargo and Crates.io|More about Cargo and Crates.io]]：profile、workspace、文档注释、发布与依赖来源

## 十二、智能指针（Ch 15）

- [[Smart Pointers|Smart Pointers]]：`Box`、`Deref`/`Drop`、`Rc`、`RefCell`、循环引用与 `Weak`

## 十三、无畏并发（Ch 16）

- [[Fearless Concurrency|Fearless Concurrency]]：线程、channel、`Mutex`/`Arc`、`Send`/`Sync`

## 十四、面向对象特性（Ch 17）

- [[Object-Oriented Features|Object-Oriented Features of Rust]]：封装、Trait Object、对象安全、状态模式

## 十五、模式进阶（Ch 18）

- [[Patterns and Matching|Patterns and Matching]]：模式出现位置、可辩驳性、解构 / 守卫 / `@`

## 十六、高级特性（Ch 19）

- [[Advanced Features|Advanced Features]]：`unsafe`、高级 Trait / 类型 / 函数、宏

## 推荐学习顺序

![[d2-rust-moc-01.svg]]

> [!tip]
> 章节编号按官方书；笔记文件名为英文以便检索。Ch 2 猜数字游戏未单独成篇（语法已含在 Ch 3）；学完 Ch 19 后书中还有最终项目（多线程 web server）等，需要时可再补。
