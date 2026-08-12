---
aliases: [模式进阶, Patterns and Matching, 高级模式, refutability, 模式语法]
tags: [rust, patterns]
up: "[[Rust MOC]]"
related: "[[Enums and Pattern Matching|枚举与 match]], [[Ownership, Borrowing, and Slices|引用]], [[Object-Oriented Features|OOP]], [[Advanced Features|高级特性]]"
down: "[[Advanced Features|Advanced Features]]"
---
# Patterns and Matching

> [!summary] 核心结论
> 模式不只出现在 `match`：还可用于 `let`、`if let`/`while let`、`for`、函数参数等。模式分**可辩驳**与**不可辩驳**；`match` 臂必须穷尽。语法包括字面量、变量、通配、解构结构体/枚举/元组、`|` 或模式、范围 `..=`、守卫、`@` 绑定等。

对应《The Book》**第 18 章**（在 [[Enums and Pattern Matching|第 6 章]] 基础上加深）。前置：[[Enums and Pattern Matching|match / if let]]、[[Structs, Methods, and Associated Functions|结构体]]。

---

## 1. All the Places Patterns Can Be Used（模式出现的位置）

```rust
// match
match x { None => (), Some(i) => println!("{i}") }

// if let / while let / let else
if let Some(x) = opt { /* ... */ }

// for：解构迭代元素
for (index, value) in v.iter().enumerate() { /* ... */ }

// let
let (a, b, c) = (1, 2, 3);

// 函数 / 闭包参数
fn print_point(&(x, y): &(i32, i32)) {
    println!("{x}, {y}");
}
```

---

## 2. Refutability（可辩驳性）

| 种类 | 含义 | 用在哪里 |
| ---- | ---- | -------- |
| **不可辩驳**（irrefutable） | 一定匹配成功，如 `x`、`(a, b)` | `let`、`for`、函数参数 |
| **可辩驳**（refutable） | 可能失败，如 `Some(x)` | `if let`、`while let`、`match` 臂 |

```rust
// ❌ let 不能用可辩驳模式
// let Some(x) = opt;

// ✅
if let Some(x) = opt { /* ... */ }
```

`match` 需要穷尽；只有一个不可辩驳臂时也合法，但通常不如 `let` 清晰。

---

## 3. Pattern Syntax（模式语法速查）

### 3.1 Literals, Names, Wildcards

```rust
match x {
    1 => println!("one"),
    2 => println!("two"),
    _ => println!("anything"),
}
```

`_` 忽略值；`_name` 仍绑定但表示“故意暂时不用”（避免未使用警告）。多个名字绑定同一值时注意所有权：一个臂里两个绑定可能冲突。

### 3.2 Multiple Patterns and Ranges

```rust
match x {
    1 | 2 => println!("one or two"),
    3..=5 => println!("three through five"),
    _ => (),
}
```

`char` 也可用 `'a'..='j'`。

### 3.3 Destructuring（解构）

```rust
struct Point { x: i32, y: i32 }

let p = Point { x: 0, y: 7 };
let Point { x: a, y: b } = p; // a=0, b=7
let Point { x, y } = p;       // 字段简写

match p {
    Point { x, y: 0 } => println!("on the x axis at {x}"),
    Point { x: 0, y } => println!("on the y axis at {y}"),
    Point { x, y } => println!("at ({x}, {y})"),
}
```

枚举、嵌套结构体、元组同理，可一层层拆。

### 3.4 Ignoring Parts

```rust
Some(_)           // 忽略内部
Point { x, .. }   // 其余字段
(first, .., last) // 元组两端
```

### 3.5 Match Guards（匹配守卫）

```rust
match num {
    Some(x) if x % 2 == 0 => println!("even"),
    Some(x) => println!("odd {x}"),
    None => (),
}
```

守卫是额外的 `if` 条件；使用 `|` 时守卫作用于整个或模式。

### 3.6 `@` Bindings

一边测试模式，一边把值绑到变量：

```rust
match msg {
    Message::Hello { id: id_variable @ 3..=7 } => {
        println!("id in range: {id_variable}");
    }
    Message::Hello { id: 10..=12 } => println!("in another range"),
    Message::Hello { id } => println!("other id: {id}"),
}
```

---

## 4. Reference Patterns（与借用）

在模式里可用 `ref` / `ref mut`（较旧风格）或依赖默认的按引用匹配（较新 edition 习惯与 `match` 的绑定模式有关）。需要时查当前 edition 的 binding mode；核心仍是：**模式可以解构，同时决定借用还是移动**。

---

> [!important] 一句话总结
> 模式无处不在；分清可辩驳与否；用解构、`|`、范围、`..`、守卫、`@` 精确描述形状。`match` 穷尽，`if let` 只关心一支。
