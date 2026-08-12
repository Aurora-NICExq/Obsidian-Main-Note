---
aliases: [枚举, Enums, Rust 枚举, Option, match, if let, 模式匹配]
tags: [rust, enum]
up: "[[Rust MOC]]"
related: "[[Structs, Methods, and Associated Functions|结构体]], [[Ownership, Borrowing, and Slices|所有权]], [[Variables, Data Types, Functions, and Control Flow|变量与可变性]], [[Common Collections|常用集合]], [[Error Handling|错误处理]]"
down: "[[Common Collections|常用集合]]"
---
# Enums and Pattern Matching

> [!summary] 核心结论
> 枚举（`enum`）用来表达"一个值只能是若干变体之一"，并且**每个变体可以携带不同类型、数量的数据**。Rust 没有 `null`，而是用标准库枚举 `Option<T>` 表示"有值 `Some(T)` / 无值 `None`"，从类型层面强制你处理空值。取出枚举里的数据靠**模式匹配**：`match` 必须**穷举**所有变体（可用 `other` 绑定或 `_` 兜底），`if let` 则是只关心单一模式时 `match` 的简写。

前置知识：[[Structs, Methods, and Associated Functions|结构体]]（了解如何用 `struct` 组织数据）。

---

## 1. Defining an Enum (定义枚举)

枚举允许你列举出一个类型**所有可能的取值（变体，variant）**。定义用 `enum` 关键字，访问变体用 `::`：

```rust
enum IpAddrKind {
    V4, // 变体之间用逗号分隔
    V6,
}

let four = IpAddrKind::V4; // 用 :: 从枚举名访问变体
let six = IpAddrKind::V6;
```

`IpAddrKind::V4` 和 `IpAddrKind::V6` 都属于同一个类型 `IpAddrKind`，因此可以写一个统一接收该类型的函数。

## 2. Attaching Data to Variants (为变体绑定数据)

枚举真正的威力在于：**每个变体可以直接绑定数据**，不同变体的数据类型和数量还可以不同。这往往比"结构体 + 单独的枚举字段"更紧凑。

```rust
enum IpAddr {
    V4(u8, u8, u8, u8), // V4 绑定 4 个 u8
    V6(String),         // V6 绑定一个 String
}

let home = IpAddr::V4(127, 0, 0, 1);
let loopback = IpAddr::V6(String::from("::1"));
```

变体能绑定的数据形式很灵活：无数据、元组、甚至匿名结构体。和 `struct` 一样，也可以用 `impl` 为枚举定义方法：

```rust
enum Message {
    Quit,                       // 无数据
    Move { x: i32, y: i32 },    // 匿名结构体字段
    Write(String),              // 单个 String
    ChangeColor(i32, i32, i32), // 三个 i32
}

impl Message {
    fn call(&self) {
        // self 是调用方法的那个 Message 值
    }
}

let m = Message::Write(String::from("hello"));
m.call();
```

## 3. The `Option<T>` Enum (Option 枚举)

Rust **没有 `null`**。空值带来的最大问题是：你可能在"以为是有效值"的地方误用了空值。Rust 用标准库枚举 `Option<T>` 把"可能没有值"这件事**编码进类型系统**：

```rust
enum Option<T> {
    Some(T), // 有值，值被包在 Some 里
    None,    // 没有值
}
```

`Option<T>`、`Some`、`None` 都在 **Prelude（预导入模块）** 中，无需 `use` 即可直接使用：

```rust
let some_number = Some(5);          // 类型推断为 Option<i32>
let some_string = Some("a string"); // Option<&str>
let absent: Option<i32> = None;     // 用 None 时必须标注类型，否则编译器无法推断 T
```

### Why `Option<T>` Beats `null` (Option 比 null 好在哪)

关键在于 **`Option<T>` 和 `T` 是两个不同的类型**，编译器不允许你把 `Option<T>` 当成 `T` 直接使用：

```rust
let x: i8 = 5;
let y: Option<i8> = Some(5);

// let sum = x + y; // ❌ 编译错误：i8 与 Option<i8> 不是同一类型，不能相加
```

对比 C# 这类允许 `null` 的语言，下面的代码能通过编译，却会在**运行时**因空引用崩溃：

```csharp
string a = null;
string b = a + "12345"; // 编译通过，运行时可能抛出 NullReferenceException
```

在 Rust 中，只要一个值**不是** `Option<T>`，编译器就已经保证它一定有值。想使用 `Option<T>` 里的 `T`，你**必须先显式地把它从 `Some` 中取出并处理 `None`**——这正是下面 `match` / `if let` 要做的事。

> [!note] `Option<T>` 与 `Some(T)` 的区别
> - **`Option<T>`** 是**类型**（那个枚举本身），描述"一个可能有 `T`、也可能没有的值"。
> - **`Some(T)`** 是 `Option<T>` 的一个**变体 / 构造器**，把一个具体的 `T` 值包进去；`None` 是另一个变体，表示无值。
> - 一句话：`Option<T>` 回答"这是什么类型"，`Some(5)` / `None` 回答"这个值具体是哪种情况"。

## 4. The `match` Control Flow Operator (match 控制流运算符)

`match` 允许把一个值与**一系列模式**逐一比对，执行首个匹配成功的分支。匹配分支对应的表达式，其值会作为整个 `match` 表达式的返回值。

```rust
enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter,
}

fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => 1,   // 每个分支形如: 模式 => 表达式
        Coin::Nickel => 5,
        Coin::Dime => 10,
        Coin::Quarter => 25,
    } // 匹配到的分支的值，就是 value_in_cents 的返回值
}
```

若某个分支需要执行多行代码，用 `{}` 包裹，块的最后一个表达式作为该分支的值：

```rust
Coin::Penny => {
    println!("Lucky penny!");
    1 // 块的返回值
}
```

## 5. Patterns that Bind to Values (绑定值的模式)

匹配分支可以**绑定到被匹配值内部的数据**，从而把枚举变体里携带的值提取出来。例如让 `Quarter` 变体带上它的发行州：

```rust
// 让编译器为 UsState 自动实现 Debug，才能用 {:?} 打印
#[derive(Debug)]
enum UsState {
    Alabama,
    Alaska,
}

enum Coin {
    Penny,
    Nickel,
    Dime,
    Quarter(UsState), // Quarter 变体绑定了一个 UsState
}

fn value_in_cents(coin: Coin) -> u8 {
    match coin {
        Coin::Penny => 1,
        Coin::Nickel => 5,
        Coin::Dime => 10,
        // 匹配到 Quarter 时，把它内部的州绑定到变量 state
        Coin::Quarter(state) => {
            println!("State quarter from {:?}!", state);
            25
        }
    }
}
```

## 6. Matching `Option<T>` (匹配 Option)

把 §3 和 §4 结合起来：`match` 是从 `Option<T>` 中安全取值的标准手段。下面的 `plus_one` 对 `Some` 里的值加一，对 `None` 原样返回：

```rust
fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        None => None,           // 没有值，直接返回 None
        Some(i) => Some(i + 1), // 取出 i，加一后重新包进 Some
    }
}

let five = Some(5);
let six = plus_one(five);       // Some(6)
let none = plus_one(None);      // None
```

## 7. Exhaustiveness and Catch-all Patterns (穷举 与 通配符)

`match` **必须穷举所有可能**：如果漏掉某个变体（比如忘了处理 `None`），编译器会直接报错。这正是它安全的原因——你不可能"忘记处理空值"。

当不想逐一列出剩余取值时，有两种兜底写法：

| 写法 | 含义 | 是否使用该值 |
| ---- | ---- | ------------ |
| `other => ...` | 绑定其余所有值到变量 `other` | ✅ 用得到 |
| `_ => ...`     | 匹配其余所有值，但**忽略**具体值 | ❌ 用不到 |
| `_ => ()`      | 其余情况**什么都不做**（返回单元值 `()`） | ❌ |

```rust
let dice_roll = 9;

// 想使用"其余值" → 用具名变量 other 绑定
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
    other => move_player(other),
}

// 不关心具体值 → 用通配符 _
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
    _ => reroll(),
}

// 其余情况什么都不做
match dice_roll {
    3 => add_fancy_hat(),
    7 => remove_fancy_hat(),
    _ => (),
}
```

## 8. Concise Control Flow with `if let` (用 if let 简化控制流)

当你**只关心一种模式**、其余情况都想忽略时，`match` 里那句 `_ => ()` 显得啰嗦。`if let` 是它的语法糖：只处理匹配成功的那一支，可选地用 `else` 处理其余情况。

```rust
let config_max = Some(3u8);

// 用 match：为了穷举，被迫写一个 _ => () 分支
match config_max {
    Some(max) => println!("max is {}", max),
    _ => (),
}

// 用 if let：等价，但更简洁
if let Some(max) = config_max {
    println!("max is {}", max);
} else {
    println!("no max"); // else 可选，对应 match 里的 _
}
```

> [!tip] match 还是 if let？
> - 需要**穷举 / 编译器帮你查漏**时，用 `match`。
> - 只处理**一种情况**、其余无所谓时，用 `if let`，代码更短——但要意识到你放弃了穷举检查。

## 9. Other Concise Pattern Tools (其它简洁模式工具)

### `while let`

只要模式持续匹配就继续循环，常用于逐个取出 `Option<T>`：

```rust
let mut stack = vec![1, 2, 3];

while let Some(value) = stack.pop() {
    println!("{value}");
}
```

### `let ... else`

要求一个模式必须匹配，否则立即离开当前控制流；适合先处理失败路径，再让成功值在后续代码中可用：

```rust
fn print_double(value: Option<i32>) {
    let Some(number) = value else {
        println!("no value");
        return;
    };

    println!("{}", number * 2);
}
```

`else` 分支必须发散，例如执行 `return`、`break` 或 panic。

### `matches!`

只想得到“是否匹配”的布尔值时可用 `matches!` 宏：

```rust
let value = Some(3);
let has_small_number = matches!(value, Some(n) if n < 5);
assert!(has_small_number);
```

---

> [!important] 一句话总结
> 枚举 = "多选一"，变体能绑数据；`Option<T>` 用 `Some`/`None` 取代 `null`，且与 `T` 是不同类型，逼你先处理空值；取值靠模式匹配——`match` 必须穷举，只认一种模式时用 `if let`，重复匹配用 `while let`，失败即提前退出可用 `let ... else`。
