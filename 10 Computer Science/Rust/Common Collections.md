---
aliases: [Rust 集合, 常用的集合, Vector, Vec, String, HashMap, Rust 字符串]
tags: [rust, collections]
up: "[[Rust MOC]]"
related: "[[Ownership, Borrowing, and Slices|所有权、借用与切片]], [[Enums and Pattern Matching|Option 与模式匹配]], [[Variables, Data Types, Functions, and Control Flow|变量与基础语法]]"
down: "[[Packages, Crates, and Modules|包、Crate 与模块]]"
---
# Common Collections

> [!summary] 核心结论
> `Vec<T>` 存放同类型、可增长的连续元素；`String` 是拥有所有权、可增长的 UTF-8 字节序列；`HashMap<K, V>` 按键查找值。集合数据在堆上，并遵循所有权：插入可能移动值，修改需要 `mut`，引用元素时要防止扩容或其它修改使引用失效。

前置知识：[[Ownership, Borrowing, and Slices|所有权、借用与切片]]、[[Enums and Pattern Matching#3. The `Option<T>` Enum (Option 枚举)|Option]]。

---
## 1. Collection Overview（集合总览）

| 类型 | 结构 | 适合场景 |
| --- | --- | --- |
| `Vec<T>` | 有顺序、同类型、按索引访问 | 动态列表、缓冲区 |
| `String` | 拥有所有权的 UTF-8 字节序列 | 可增长和修改的文本 |
| `HashMap<K, V>` | 键值对、按键查找 | 映射、计数、缓存 |

它们都是泛型类型。`Vec<i32>` 与 `Vec<String>` 是不同的具体类型；同一个 Vector 不能直接混装不同类型的值。

---
## 2. Vector（动态数组）

### 2.1 Creating and Updating（创建与更新）

空 Vector 没有初始值可供推断，通常要标注元素类型：

```rust
let empty: Vec<i32> = Vec::new();
let values = vec![1, 2, 3]; // 编译器推断为 Vec<i32>
```

修改集合前，绑定必须可变：

```rust
let mut values = Vec::new();
values.push(10);
values.push(20);

let last = values.pop(); // Option<i32>，此处是 Some(20)
```

Vector 离开作用域时，自身和它拥有的所有元素都会被清理：

```rust
{
    let names = vec![String::from("Ada"), String::from("Linus")];
    println!("{}", names.len());
} // names、两个 String 及其堆数据都在这里 drop
```

### 2.2 Reading Elements: Index vs `get`（读取元素）

```rust
let values = vec![10, 20, 30];

let second = &values[1];
println!("{second}");

match values.get(1) {
    Some(value) => println!("{value}"),
    None => println!("index out of bounds"),
}
```

| 方式 | 返回类型 | 越界行为 |
| --- | --- | --- |
| `&v[index]` | `&T` | 运行时 panic |
| `v.get(index)` | `Option<&T>` | 返回 `None` |

索引一定有效时可用 `[]`；索引来自用户输入或外部数据时优先用 `get`。

### 2.3 Borrowing and Reallocation（借用与扩容）

下面代码无法编译：

```rust
let mut values = vec![1, 2, 3];
let first = &values[0];

// values.push(4); // 编译错误：first 后面仍会被使用
// println!("{first}");
```

原因有两层：

1. `first` 是共享引用，其有效期间不能通过 `push` 可变借用 `values`。
2. `push` 可能因容量不足把元素搬到新的堆内存，旧的元素引用会悬垂。

把 `first` 的最后一次使用放到 `push` 之前即可：

```rust
let mut values = vec![1, 2, 3];
let first = &values[0];
println!("{first}");

values.push(4); // 此时 first 的借用已经结束
```

### 2.4 Iterating and Mutating（遍历与修改）

```rust
let mut values = vec![100, 32, 57];

for value in &values {       // 产生 &i32，不消费 Vector
    println!("{value}");
}

for value in &mut values {   // 产生 &mut i32
    *value += 50;            // * 解引用后修改元素
}
```

`for value in values` 会消费 Vector；之后还要用集合时，应遍历 `&values`。

### 2.5 Storing Multiple Shapes with an Enum（用枚举统一多种数据）

Vector 元素必须同类型，但一个枚举的不同变体可携带不同数据：

```rust
enum SpreadsheetCell {
    Int(i32),
    Float(f64),
    Text(String),
}

let row = vec![
    SpreadsheetCell::Int(3),
    SpreadsheetCell::Text(String::from("blue")),
    SpreadsheetCell::Float(10.12),
];
```

这里每个元素类型都是 `SpreadsheetCell`。处理时用 [[Enums and Pattern Matching#4. The `match` Control Flow Operator (match 控制流运算符)|match]] 判断具体变体。

---
## 3. String and UTF-8（String 与 UTF-8）

Rust 常见的字符串形式：

- `String`：拥有数据、可增长，通常分配在堆上。
- `&str`：借用一段有效 UTF-8 文本，不拥有数据；字符串字面量是 `&'static str`。

### 3.1 Creating Strings（创建字符串）

```rust
let empty = String::new();
let s1 = String::from("hello");
let s2 = "hello".to_string();
```

`String::from` 与 `.to_string()` 都创建拥有所有权的字符串。

### 3.2 Appending Text（追加文本）

```rust
let mut text = String::from("hello");
text.push_str(", world"); // 参数是 &str，不取得该切片的所有权
text.push('!');           // 参数是单个 char
```

`push_str` 只借用参数，传入的 `String` 仍可继续使用：

```rust
let suffix = String::from(" world");
let mut text = String::from("hello");
text.push_str(&suffix);

println!("{suffix}"); // suffix 没有被移动
```

### 3.3 Concatenation: `+` vs `format!`（拼接）

```rust
let s1 = String::from("Hello, ");
let s2 = String::from("world!");
let s3 = s1 + &s2;

// println!("{s1}"); // 编译错误：s1 已移动进 + 运算
println!("{s2}");    // s2 只是被借用
println!("{s3}");
```

`+` 的行为近似 `fn add(self, rhs: &str) -> String`：左操作数按值传入并被消费，右操作数只借用。`&String` 能自动强制转换为 `&str`。

拼接多个字符串时，`format!` 更清晰且不会取得参数所有权：

```rust
let s1 = String::from("tic");
let s2 = String::from("tac");
let s3 = String::from("toe");

let result = format!("{s1}-{s2}-{s3}");
```

### 3.4 No Integer Indexing（不能用整数索引字符串）

`String` 是 UTF-8 字节序列，不保证一个可见字符等于一个字节，因此禁止 `s[0]`：

```rust
let hello = String::from("你好");
println!("bytes = {}", hello.len()); // 6，而不是 2
```

按需求选择遍历层次：

```rust
for ch in "你好".chars() {
    println!("{ch}"); // Unicode 标量值：你、好
}

for byte in "你好".bytes() {
    println!("{byte}"); // UTF-8 原始字节
}
```

`chars()` 也不等于完整的“用户可见字符”分割；某些字形由多个 Unicode 标量值组成。按用户感知的字素簇处理时通常需要专门的 Unicode crate。

字符串可以切片，但边界必须落在 UTF-8 字符边界上：

```rust
let hello = "你好";
let first = &hello[0..3]; // "你"；0..1 会 panic
```

---
## 4. HashMap（键值映射）

`HashMap<K, V>` 用哈希函数决定键值在内存中的存放位置，适合“按任意类型的键查找”，而不是按整数索引。它不在 prelude 中，需要显式导入：

```rust
use std::collections::HashMap;

let mut scores = HashMap::new();
scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Yellow"), 50);
```

同一个 map 的键必须同类型，值也必须同类型。每个键同一时刻只对应一个值；map 大小可变。

### 4.1 Creating with `collect`（用 collect 创建）

也可以在元组 Vector 上用 `collect` 组建 HashMap：

```rust
use std::collections::HashMap;

let teams = vec![
    (String::from("Blue"), 10),
    (String::from("Yellow"), 50),
];
let scores: HashMap<_, _> = teams.into_iter().collect();
```

`HashMap<_, _>` 让编译器根据元组元素推断键值类型。

### 4.2 Ownership and Lookup（所有权与查找）

对实现 `Copy` 的值，`insert` 会复制；对 `String` 等拥有堆数据的值，默认会移动所有权：

```rust
let team = String::from("Blue");
let score = 10;

let mut scores = HashMap::new();
scores.insert(team, score);

// println!("{team}"); // 编译错误：String 已移动进 map
println!("{score}");   // i32 实现 Copy，仍可使用
```

若插入的是引用，值本身不会移动，但 map 的生命周期不能超过被引用的数据：

```rust
let field_name = String::from("Favorite color");
let field_value = String::from("Blue");

let mut map = HashMap::new();
map.insert(&field_name, &field_value);

println!("{field_name}: {field_value}"); // 仍可使用
```

`get` 返回 `Option<&V>`：

```rust
let team_name = String::from("Blue");
let score = scores.get(&team_name).copied().unwrap_or(0);
```

### 4.3 Iterating（遍历）

```rust
for (key, value) in &scores {
    println!("{key}: {value}");
}
```

哈希映射的遍历顺序不应视为固定顺序。

### 4.4 Updating（更新值）

键已存在时，常见三种策略：

| 策略 | 写法 |
| --- | --- |
| 替换现有值 | `insert`（再次插入同键） |
| 保留现有值，忽略新值 | `entry(k).or_insert(v)` |
| 合并现有值与新值 | `entry(k).or_insert(...)` 再通过 `&mut V` 修改 |

`insert` 会覆盖：

```rust
scores.insert(String::from("Blue"), 10);
scores.insert(String::from("Blue"), 25); // Blue 变为 25
```

只在键不存在时插入，用 `entry(...).or_insert(...)`：

```rust
scores.entry(String::from("Yellow")).or_insert(50); // 插入 50
scores.entry(String::from("Blue")).or_insert(50);   // Blue 已存在，保持原值
```

`or_insert` 返回 `&mut V`，适合基于旧值合并更新。例如统计单词频率：

```rust
use std::collections::HashMap;

let text = "hello world wonderful world";
let mut counts = HashMap::new();

for word in text.split_whitespace() {
    let count = counts.entry(word).or_insert(0);
    *count += 1;
}
```

---
## 5. Choosing an Access Pattern（访问方式速查）

| 需求 | 推荐写法 |
| --- | --- |
| 已知 Vector 索引一定有效 | `&v[index]` |
| 索引可能越界 | `v.get(index)` 并处理 `Option` |
| 只读遍历集合 | `for x in &collection` |
| 原地修改每个元素 | `for x in &mut collection` |
| 获取 HashMap 中可能不存在的值 | `map.get(key)` |
| 不存在才插入或基于旧值修改 | `map.entry(key).or_insert(default)` |
| 拼接多个字符串 | `format!` |
| 按 Unicode 标量值遍历字符串 | `.chars()` |

---
> [!important] 一句话总结
> 顺序数据用 `Vec<T>`，可变文本用 `String`，按键查找用 `HashMap<K, V>`；读元素时先考虑越界与 `Option`，修改集合时先考虑借用是否仍有效，处理字符串时始终记住索引单位是 UTF-8 字节而不是“第几个字”。

---
## 参见
- [[Rust MOC]]
- [[Ownership, Borrowing, and Slices|所有权、借用与切片]]
- [[Enums and Pattern Matching|Option 与模式匹配]]
- [[Packages, Crates, and Modules|包、Crate 与模块]]
