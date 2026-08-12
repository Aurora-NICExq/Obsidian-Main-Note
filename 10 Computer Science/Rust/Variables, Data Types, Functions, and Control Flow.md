---
aliases: [Rust 变量, 变量与可变性, Rust 基础语法, mut, shadowing, Rust 数据类型, Rust 控制流]
tags: [rust, basics]
up: "[[Rust MOC]]"
related: "[[Ownership, Borrowing, and Slices|所有权、引用与切片]], [[Structs, Methods, and Associated Functions|结构体]], [[Enums and Pattern Matching|枚举与模式匹配]]"
down: "[[Ownership, Borrowing, and Slices|所有权、引用与切片]]"
---
# Variables, Data Types, Functions, and Control Flow

> [!summary] 核心结论
> Rust 变量用 `let` 声明且默认不可变；`mut` 允许重新赋值，shadowing（遮蔽）则用新的 `let` 创建一个同名新变量，并且可以改变类型。Rust 是静态类型语言，基础数据由标量与复合类型构成。函数体和控制流大量使用“表达式”，块的最后一个无分号表达式就是块的值。

---

## 1. Variables and Mutability（变量与可变性）

```rust
let x = 5;
// x = 6; // ❌ 默认不可变

let mut y = 5;
y = 6;    // ✅ y 被声明为可变
```

不可变并不等于“常量”：不可变变量仍可由运行时表达式初始化，只是绑定完成后不能再次赋值。

### Constants（常量）

常量用 `const` 声明，名称按惯例使用全大写加下划线，并且**必须显式标注类型**：

```rust
const THREE_HOURS_IN_SECONDS: u32 = 60 * 60 * 3;
```

常量表达式必须能在编译期求值，不能加 `mut`。

### Shadowing（遮蔽）

再次使用 `let` 可以创建同名的新变量，新绑定会遮蔽旧绑定：

```rust
let spaces = "   ";
let spaces = spaces.len(); // &str 被遮蔽为 usize
```

| `mut` | shadowing |
| --- | --- |
| 修改同一个绑定 | 创建一个新绑定 |
| 类型不能改变 | 类型可以改变 |
| 后续仍可再次赋值 | 新绑定默认仍不可变 |

## 2. Type Annotations and Inference（类型标注与推断）

Rust 是静态类型语言，但编译器通常可以根据初始值和使用方式推断类型。存在多个可能类型时需要显式标注：

```rust
let guess: u32 = "42".parse().expect("not a number");
```

没有 `: u32` 时，`parse` 无法知道应解析成哪种数值类型。

## 3. Scalar Types（标量类型）

一个标量类型表示单个值。

| 类别 | 常用类型 | 说明 |
| --- | --- | --- |
| 整数 | `i8`…`i128`、`u8`…`u128`、`isize`、`usize` | `i` 为有符号，`u` 为无符号 |
| 浮点 | `f32`、`f64` | 默认推断为 `f64` |
| 布尔 | `bool` | 只有 `true` 和 `false` |
| 字符 | `char` | Unicode 标量值，占 4 字节 |

```rust
let count: u32 = 98_222; // 下划线只提高可读性
let byte: u8 = b'A';
let ratio = 2.5;         // f64
let enabled = true;
let crab = '🦀';          // char 使用单引号
```

> [!warning]
> `char` 表示一个 Unicode 标量值，但用户看到的“一个字符”可能由多个标量值组成。字符串也不能用整数直接索引，详见 [[Common Collections#3. String and UTF-8（String 与 UTF-8）|String 与 UTF-8]]。

## 4. Compound Types（复合类型）

### Tuple（元组）

元组长度固定，但元素可以有不同类型：

```rust
let tup: (i32, f64, u8) = (500, 6.4, 2);

let (x, y, z) = tup; // 解构
let first = tup.0;    // 按索引访问
```

不包含元素的元组 `()` 称为**单元类型（unit type）**，其唯一值也是 `()`，常用来表示“没有有意义的返回值”。

### Array（数组）

数组长度固定，所有元素类型相同，数据通常位于栈上：

```rust
let a: [i32; 5] = [1, 2, 3, 4, 5];
let zeros = [0; 5]; // 等价于 [0, 0, 0, 0, 0]

let first = a[0];
```

需要运行时增长或缩短的序列时使用 `Vec<T>`，见 [[Common Collections#2. Vector（动态数组）|Vector]]。

## 5. Functions, Statements, and Expressions（函数、语句与表达式）

函数用 `fn` 声明，函数名和变量名按惯例使用 `snake_case`。参数类型必须显式写出：

```rust
fn add_one(x: i32) -> i32 {
    x + 1
}
```

- **语句（statement）**执行动作，不产生可供外层使用的值，例如 `let x = 5;`。
- **表达式（expression）**求值得到一个值，例如 `x + 1`、函数调用、代码块和 `if`。
- 块的最后一个表达式不加分号时，会成为块的值。

```rust
let y = {
    let x = 3;
    x + 1
}; // y == 4
```

若把 `x + 1` 写成 `x + 1;`，它就变成表达式语句，块的值随之变成 `()`，无法再赋给需要整数的变量。

### Returning Values（返回值）

返回类型写在 `->` 后。通常用末尾表达式返回，也可以用 `return` 提前返回：

```rust
fn classify(n: i32) -> &'static str {
    if n < 0 {
        return "negative";
    }
    "zero or positive"
}
```

## 6. `if` Expressions（条件表达式）

`if` 条件必须是 `bool`，Rust 不会把整数自动当作真假值：

```rust
let number = 3;

if number < 5 {
    println!("less than five");
} else {
    println!("five or greater");
}
```

因为 `if` 是表达式，可以直接用于赋值；所有分支必须产生兼容的类型：

```rust
let condition = true;
let number = if condition { 5 } else { 6 };
```

## 7. Loops（循环）

Rust 提供 `loop`、`while` 和 `for`。

### `loop` and `break`

`loop` 无限重复，直到 `break`。`break 表达式` 可以把值作为整个循环的结果返回：

```rust
let mut counter = 0;

let result = loop {
    counter += 1;
    if counter == 10 {
        break counter * 2;
    }
};
```

嵌套循环可用循环标签指定 `break`/`continue` 的目标：

```rust
'outer: loop {
    loop {
        break 'outer;
    }
}
```

### `while`

```rust
let mut number = 3;

while number != 0 {
    println!("{number}");
    number -= 1;
}
```

### `for` and Ranges（遍历与范围）

遍历集合时优先用 `for`，它不会要求手动管理索引：

```rust
let values = [10, 20, 30];

for value in values {
    println!("{value}");
}

for number in (1..=3).rev() {
    println!("{number}");
}
```

- `1..4` 产生 `1, 2, 3`，不包含右端点。
- `1..=4` 产生 `1, 2, 3, 4`，包含右端点。

---

> [!important] 一句话总结
> `let` 默认不可变，`mut` 修改原绑定，shadowing 创建同名新绑定；类型由编译器推断但始终在编译期确定；函数、块、`if` 和 `loop` 都可产生值，末尾表达式是否带分号会直接影响返回类型。
