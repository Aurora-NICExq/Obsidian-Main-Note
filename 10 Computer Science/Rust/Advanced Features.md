---
aliases: [高级特性, Advanced Features, unsafe, 高级 Trait, 高级类型, 宏, macros]
tags: [rust, advanced, unsafe, macros]
up: "[[Rust MOC]]"
related: "[[Generics, Traits, and Lifetimes|Trait 与生命周期]], [[Smart Pointers|智能指针]], [[Fearless Concurrency|Send Sync]], [[Patterns and Matching|模式]], [[Object-Oriented Features|Trait Objects]]"
down: ""
---
# Advanced Features

> [!summary] 核心结论
> 第 19 章收纳不常用但强大的工具：**`unsafe`** 绕过借用检查的五项超能力（仍须程序员自己保证安全）；**高级 Trait**（关联类型、默认泛型参数、完全限定语法、超 Trait、newtype 上的外部 Trait）；**高级类型**（类型别名、never、动态大小类型与 `Sized`）；**高级函数/闭包**（函数指针、返回闭包）；**宏**（`macro_rules!` 声明宏与过程宏概览）。默认仍写安全 Rust；只有必要且边界清晰时才用这些特性。

对应《The Book》**第 19 章**。前置：建议学完第 15–18 章相关笔记。

---

## 1. Unsafe Rust

`unsafe` **不关闭借用检查器**，只是允许多做几件编译器无法证明安全的事。五项超能力：

1. 解引用裸指针  
2. 调用 `unsafe` 函数 / 方法  
3. 访问或修改可变静态变量  
4. 实现 `unsafe` Trait  
5. 访问 `union` 字段  

```rust
let mut num = 5;
let r1 = &num as *const i32;
let r2 = &mut num as *mut i32;

unsafe {
    println!("r1 is: {}", *r1);
    println!("r2 is: {}", *r2);
}
```

惯用做法：把 `unsafe` 缩到最小模块，对外提供**安全抽象**（像 `Vec` 内部有 unsafe，API 安全）。

`unsafe fn` 表示调用者须维护约定；调用处也要在 `unsafe` 块中。

---

## 2. Advanced Traits（高级 Trait）

### 2.1 Associated Types（关联类型）

```rust
pub trait Iterator {
    type Item;
    fn next(&mut self) -> Option<Self::Item>;
}
```

与泛型参数相比：实现者选定一个具体 `Item`，使用处写法更干净（不必处处写 `Iterator<Item = u32>`，除非需要）。

### 2.2 Default Generic Type Parameters（默认泛型参数）

```rust
trait Add<Rhs = Self> {
    type Output;
    fn add(self, rhs: Rhs) -> Self::Output;
}
```

可重载运算符；默认 `Rhs = Self` 表示通常与同类型相加。

### 2.3 Fully Qualified Syntax（完全限定语法）

当多个 Trait 有同名方法，或类型上有同名固有方法时：

```rust
<Dog as Animal>::baby_name()
```

形式：`<Type as Trait>::function(receiver, args...)`。

### 2.4 Supertraits（超 Trait）

```rust
trait OutlinePrint: fmt::Display {
    fn outline_print(&self) { /* 使用 to_string() */ }
}
```

实现 `OutlinePrint` 的类型必须同时实现 `Display`。

### 2.5 Newtype Pattern（newtype）

元组结构体包一层外部类型，可在本地为“新类型”实现外部 Trait（绕过孤儿规则），或限制 API（如只暴露 `Meters` 而非裸 `f64`）。

---

## 3. Advanced Types（高级类型）

### 3.1 Type Aliases

```rust
type Kilometers = i32;
type Result<T> = std::result::Result<T, std::io::Error>;
```

只是别名，**不是**新类型（无额外类型安全）。

### 3.2 The Never Type `!`

从不返回的函数（`panic!`、无限循环、`continue`）类型为 `!`，可强制转换为任意类型，便于 `match` 分支统一类型。

### 3.3 Dynamically Sized Types and `Sized`

`str`、`[T]`、`dyn Trait` 是 DST，大小运行时才知道，必须通过指针使用（`&str`、`Box<[T]>` 等）。

泛型默认隐式 `T: Sized`。若要允许 DST：

```rust
fn foo<T: ?Sized>(t: &T) { /* ... */ }
```

---

## 4. Advanced Functions and Closures

### 4.1 Function Pointers

```rust
fn add_one(x: i32) -> i32 { x + 1 }
fn do_twice(f: fn(i32) -> i32, arg: i32) -> i32 {
    f(arg) + f(arg)
}
do_twice(add_one, 5);
```

`fn` 是类型（函数指针）；闭包（不捕获环境时）可强制转换成 `fn`。需要捕获时用泛型 `F: Fn(...)`。

### 4.2 Returning Closures

闭包无固定大小的单一类型名，返回时常用：

```rust
fn returns_closure() -> Box<dyn Fn(i32) -> i32> {
    Box::new(|x| x + 1)
}
```

（在支持 `impl Trait` 返回位置的场景也可 `-> impl Fn(i32) -> i32`。）

---

## 5. Macros（宏）

宏在编译期展开，可写“可变参数”的抽象（如 `println!`、`vec!`）。

### 5.1 Declarative Macros with `macro_rules!`

```rust
#[macro_export]
macro_rules! vec {
    ( $( $x:expr ),* ) => {
        {
            let mut temp_vec = Vec::new();
            $( temp_vec.push($x); )*
            temp_vec
        }
    };
}
```

用模式匹配代码结构，生成更多代码。

### 5.2 Procedural Macros（过程宏，概念）

以 Rust 函数形式处理 TokenStream，三类：

| 种类 | 例子 |
| ---- | ---- |
| 自定义 derive | `#[derive(Debug)]` |
| 类属性宏 | `#[route(GET, "/")]` |
| 类函数宏 | `sql!(SELECT * FROM ...)` |

通常单独 crate（`proc-macro = true`）实现。应用开发者多用现成 derive；自己写过程宏属于进阶专题。

---

> [!important] 一句话总结
> `unsafe` 缩小边界并封装；关联类型 / newtype / 完全限定语法强化 Trait；别名、`!`、`?Sized` 处理类型边角；`fn` 与 `dyn Fn` 覆盖函数级抽象；宏做编译期代码生成。日常仍以安全、清晰的抽象为先。
