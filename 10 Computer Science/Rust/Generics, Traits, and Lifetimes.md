---
aliases: [泛型, Trait, 生命周期, Generics, Traits, Lifetimes, trait bound, impl Trait]
tags: [rust, generics, traits, lifetimes]
up: "[[Rust MOC]]"
related: "[[Error Handling|错误处理]], [[Ownership, Borrowing, and Slices|所有权与借用]], [[Structs, Methods, and Associated Functions|结构体]], [[Enums and Pattern Matching|枚举]], [[Writing Automated Tests|自动化测试]]"
down: "[[Writing Automated Tests|自动化测试]]"
---
# Generics, Traits, and Lifetimes

> [!summary] 核心结论
> **泛型**用类型参数（如 `T`）写可复用的代码模板；**Trait** 描述共享行为，**Trait bound** 约束“`T` 必须具备哪些能力”；**生命周期**标注引用能活多久，防止悬垂引用。三者常一起出现：函数签名里可以同时有泛型类型、Trait bound 和生命周期参数。编译期会做单态化（monomorphization），运行时没有“装箱后的泛型开销”。

前置知识：[[Ownership, Borrowing, and Slices|所有权与借用]]、[[Structs, Methods, and Associated Functions|结构体]]、[[Enums and Pattern Matching|枚举与 Option/Result]]。

---

## 1. Removing Duplication by Extracting Functions（提取函数消除重复）

重复代码的危害：容易改漏、需求变更时要改多处。消除步骤：

1. 识别重复代码
2. 提取到函数，在签名里写清输入与返回值
3. 用函数调用替换原来的重复片段

当重复的不只是“同一段逻辑”，而是“同一段逻辑作用在不同类型上”时，单靠提取函数不够——这时需要**泛型**。

## 2. Generics（泛型）

泛型是具体类型或其它属性的**抽象占位符**：你写的是模板，编译器再为实际用到的具体类型生成代码。

类型参数命名习惯：

- 通常很短，常用单个字母
- 使用 CamelCase；`T` 是 `Type` 的缩写
- 多个参数时用有含义的字母，如 `T`、`E`（Error）、`K`/`V`（Key/Value）

### 2.1 Generics in Function Definitions（函数中的泛型）

```rust
fn largest<T: PartialOrd>(list: &[T]) -> &T {
    let mut largest = &list[0];
    for item in list {
        if item > largest {
            largest = item;
        }
    }
    largest
}
```

`<T: PartialOrd>` 表示：`T` 必须实现 `PartialOrd`，才能用 `>` 比较。没有这个 bound，`item > largest` 无法通过编译。

### 2.2 Generics in Structs（结构体中的泛型）

```rust
struct Point<T> {
    x: T,
    y: T,
}

let integer = Point { x: 5, y: 10 };       // Point<i32>
let float = Point { x: 1.0, y: 4.0 };      // Point<f64>
// let wont_work = Point { x: 5, y: 4.0 }; // ❌ x、y 必须是同一 T
```

需要字段类型不同时，用**多个**类型参数：

```rust
struct Point<T, U> {
    x: T,
    y: U,
}

let p = Point { x: 5, y: 4.0 }; // Point<i32, f64>
```

### 2.3 Generics in Enums（枚举中的泛型）

标准库里最常见的例子：

```rust
enum Option<T> {
    Some(T),
    None,
}

enum Result<T, E> {
    Ok(T),
    Err(E),
}
```

变体可以携带泛型数据；`Option` 一个类型参数，`Result` 两个。

### 2.4 Generics in Method Definitions（方法中的泛型）

在 `impl` 后声明类型参数，表示为该泛型类型实现方法：

```rust
struct Point<T> {
    x: T,
    y: T,
}

impl<T> Point<T> {
    fn x(&self) -> &T {
        &self.x
    }
}

// 只为特定具体类型实现额外方法
impl Point<f32> {
    fn distance_from_origin(&self) -> f32 {
        (self.x.powi(2) + self.y.powi(2)).sqrt()
    }
}
```

注意：

- `impl<T> Point<T>`：对**所有** `T` 都有的方法
- `impl Point<f32>`：仅 `Point<f32>` 才有的方法
- 结构体的类型参数可以和方法自己的类型参数**不同**（例如方法把 `Point<T, U>` 混成另一种组合）

```rust
impl<T, U> Point<T, U> {
    fn mixup<V, W>(self, other: Point<V, W>) -> Point<T, W> {
        Point {
            x: self.x,
            y: other.y,
        }
    }
}
```

> [!note] 单态化（Monomorphization）
> 编译器会把泛型代码展开成实际用到的具体类型版本。因此泛型既复用源码，又通常没有动态分发的运行时开销。

## 3. Traits（Trait：共享行为）

Trait 告诉编译器：某种类型具有哪些**可与其它类型共享**的功能。

| 概念 | 作用 |
| ---- | ---- |
| **Trait** | 抽象地定义一组共享行为（方法签名） |
| **Trait bound** | 约束泛型参数“必须实现某 Trait” |

### 3.1 Defining a Trait（定义 Trait）

用 `trait` 关键字把方法签名放在一起；通常只有签名、以 `;` 结尾，由实现者提供具体逻辑：

```rust
pub trait Summary {
    fn summarize(&self) -> String;
}
```

一个 Trait 可以有多个方法，每个签名一行。

### 3.2 Implementing a Trait on a Type（在类型上实现 Trait）

语法：`impl TraitName for TypeName`。块里必须实现 Trait 要求的方法：

```rust
pub struct NewsArticle {
    pub headline: String,
    pub location: String,
    pub author: String,
    pub content: String,
}

impl Summary for NewsArticle {
    fn summarize(&self) -> String {
        format!("{}, by {} ({})", self.headline, self.author, self.location)
    }
}

pub struct Tweet {
    pub username: String,
    pub content: String,
    pub reply: bool,
    pub retweet: bool,
}

impl Summary for Tweet {
    fn summarize(&self) -> String {
        format!("{}: {}", self.username, self.content)
    }
}
```

### 3.3 Orphan Rule（孤儿规则 / 实现约束）

只有在满足以下条件之一时，才能为类型实现某个 Trait：

- 该 **类型** 定义在当前 crate，或
- 该 **Trait** 定义在当前 crate

这样可以避免两个 crate 各自为同一外部类型实现同一外部 Trait 而冲突。

### 3.4 Default Implementations（默认实现）

Trait 方法可以提供默认实现；类型可以选择覆盖，也可以直接用默认版：

```rust
pub trait Summary {
    fn summarize_author(&self) -> String;

    fn summarize(&self) -> String {
        format!("(Read more from {}...)", self.summarize_author())
    }
}
```

默认实现可以调用同一 Trait 里**其它**方法——即便那些方法没有默认实现。实现者只需实现 `summarize_author`，就能免费得到 `summarize`。

### 3.5 Traits as Parameters（Trait 作为参数）

两种常见写法：

```rust
// impl Trait：简单场景够用
pub fn notify(item: impl Summary) {
    println!("Breaking news! {}", item.summarize());
}

// Trait bound：更通用，适合复杂签名
pub fn notify<T: Summary>(item: T) {
    println!("Breaking news! {}", item.summarize());
}
```

`impl Trait` 是 Trait bound 的语法糖。需要同一函数里表达更细的关系时，用显式 bound 更清晰。

### 3.6 Multiple Trait Bounds with `+`（用 `+` 约束多个 Trait）

```rust
pub fn notify(item: impl Summary + Display) {
    println!("Breaking news! {}", item.summarize());
}

pub fn notify<T: Summary + Display>(item: T) {
    println!("Breaking news! {}", item.summarize());
}
```

两个参数要求**同一具体类型**时，用泛型 bound（两个 `impl Summary` 参数可以是不同类型）：

```rust
pub fn notify<T: Summary>(item1: T, item2: T) { /* ... */ }
```

### 3.7 `where` Clauses（where 子句）

bounds 一多，签名会很难读；可挪到 `where`：

```rust
fn some_function<T, U>(t: T, u: U) -> i32
where
    T: Display + Clone,
    U: Clone + Debug,
{
    // ...
    0
}
```

### 3.8 Returning Types that Implement Traits（返回 impl Trait）

```rust
fn returns_summarizable() -> impl Summary {
    Tweet {
        username: String::from("horse_ebooks"),
        content: String::from("of course, as you probably already know, people"),
        reply: false,
        retweet: false,
    }
}
```

> [!warning] `impl Trait` 返回值只能是**同一种**确定类型
> 不能在 `if` / `else` 里分别返回 `NewsArticle` 和 `Tweet`——即便二者都实现了 `Summary`。若需要返回多种类型，改用 `Box<dyn Summary>` 等 trait object（后续专题）。

### 3.9 Conditionally Implementing Methods（有条件地实现方法）

在 `impl` 上加 Trait bound，可以只为实现了某些 Trait 的 `T` 提供方法：

```rust
use std::fmt::Display;

struct Pair<T> {
    x: T,
    y: T,
}

impl<T> Pair<T> {
    fn new(x: T, y: T) -> Self {
        Self { x, y }
    }
}

impl<T: Display + PartialOrd> Pair<T> {
    fn cmp_display(&self) {
        if self.x >= self.y {
            println!("The largest member is x = {}", self.x);
        } else {
            println!("The largest member is y = {}", self.y);
        }
    }
}
```

也可以写 **blanket implementation**：为“所有已实现某 Trait 的类型”再实现另一个 Trait（标准库大量使用，如 `impl<T: Display> ToString for T`）。

## 4. Lifetimes（生命周期）

生命周期是另一类泛型：不描述类型**是什么**，而描述引用**能合法借用多久**，防止悬垂引用。它与 [[Ownership, Borrowing, and Slices#5. Shared References and Borrowing（共享引用与借用）|借用规则]] 配套——借用检查器在编译期核对：引用用到的地方，被借的数据一定还活着。

> [!important] 标注在说什么、不在说什么
> - **不改变**任何引用的实际存活时间；数据该 drop 还是会 drop。
> - **只描述关系**：“返回值至少和某个参数活得一样久”。
> - 写成泛型 `'a` 后，函数能接收**任意够长**的具体借用；调用处由编译器代入实际区域。

### 4.1 Dangling References（悬垂引用）

```rust
// ❌ 无法通过编译：r 在内层结束后仍指向已失效的 x
let r;
{
    let x = 5;
    r = &x;
}
println!("r: {r}");
```

借用检查器比较“引用要用多久”和“数据活多久”，拒绝这类代码。现代 Rust 还会按引用的**最后一次使用**收紧借用区间（NLL），见 [[Ownership, Borrowing, and Slices#Borrowing Rules（借用规则）|借用规则]]。

### 4.2 Annotation Syntax（标注语法）

| 项目 | 写法 |
| ---- | ---- |
| 参数名 | 以 `'` 开头，通常很短：`'a`、`'b`、`'input` |
| 不可变引用 | `&'a T`（`&` 与类型之间用空格分开标注：`&'a str`） |
| 可变引用 | `&'a mut T` |
| 声明位置 | 函数名与参数列表之间的 `<>`：`fn f<'a>(...)` |

```rust
&i32        // 普通引用
&'a i32     // 带显式生命周期的引用
&'a mut i32 // 带显式生命周期的可变引用
```

### 4.3 Lifetimes in Function Signatures（函数签名中的生命周期）

**输入生命周期**：出现在参数上的；**输出生命周期**：出现在返回值上的。从函数返回引用时，输出生命周期必须和**某一个（或若干）输入**对上号——不能凭空“造”出一个比所有参数都长的借用。

```rust
// 返回的引用与 x、y 中较短者活得一样久
fn longest<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() { x } else { y }
}
```

`'a` 的实际含义：存在一个生命周期，使 `x`、`y` 都至少活那么久，返回值也活那么久——调用时取二者中**较短**的那段。

```rust
let string1 = String::from("long string is long");
{
    let string2 = String::from("xyz");
    let result = longest(string1.as_str(), string2.as_str());
    println!("The longest string is {result}");
} // string2、result 都不能活过这里
```

若返回值**始终**来自某一个参数，只标注那一条边即可：

```rust
fn first<'a>(x: &'a str, _y: &str) -> &'a str {
    x // y 与返回值无关，不必共享 'a
}
```

怎么标取决于**函数实际返回谁的借用**；这不是固定公式，而是把数据流写进类型。

不能返回指向函数内部局部量的引用——它在返回前就已销毁：

```rust
// ❌ 无论怎么写 'a 都救不了：result 是本地 String
fn longest<'a>(x: &str, y: &str) -> &'a str {
    let result = String::from("really long string");
    result.as_str()
}
```

这类情况应返回**拥有所有权**的 `String`（或让调用方传入可写入的缓冲）。

### 4.4 Lifetimes in Structs（结构体中的生命周期）

结构体可以拥有数据，也可以只**持有引用**；持有引用时必须标注，保证实例不会比借来的数据活得更久：

```rust
struct ImportantExcerpt<'a> {
    part: &'a str, // 每个引用字段都要带生命周期
}

let novel = String::from("Call me Ishmael. Some years ago...");
let first_sentence = novel.split('.').next().unwrap();
let i = ImportantExcerpt {
    part: first_sentence,
};
// i 不能比 novel（以及 first_sentence 所借的那一段）活得更久
```

`'a` 是结构体类型的一部分：`ImportantExcerpt<'a>` 与某个具体借用区域绑定。

### 4.5 Lifetimes in Method Definitions（方法中的生命周期）

语法与泛型方法相同：字段上的生命周期在 `impl` 后声明，并写在结构体名后面。

```rust
impl<'a> ImportantExcerpt<'a> {
    // 通常靠省略规则，不必手写：返回值跟 &self 走
    fn level(&self) -> i32 {
        3
    }

    // 规则 3：返回的 &str 跟 &self 绑定，与 announcement 无关
    fn announce_and_return_part(&self, announcement: &str) -> &str {
        println!("Attention please: {announcement}");
        self.part
    }
}
```

方法签名里的引用要么挂在**字段的生命周期**上（如上返回 `self.part`），要么是与字段无关的独立借用（仅作参数用的 `announcement`）。

### 4.6 Lifetime Elision（生命周期省略规则）

许多常见模式不必手写。术语上：参数上的叫**输入生命周期**，返回值上的叫**输出生命周期**。编译器按三条规则推断；推不出再报错让你显式写：

1. 每个引用参数各得一个自己的生命周期参数
2. 若只有**一个**输入生命周期，则把它赋给所有输出生命周期
3. 若有多个输入生命周期，且其中一个是 `&self` / `&mut self`，则 `self` 的生命周期赋给所有输出

| 你写的 | 编译器看成 |
| ------ | ---------- |
| `fn first_word(s: &str) -> &str` | `fn first_word<'a>(s: &'a str) -> &'a str` |
| `fn f(x: &str, y: &str) -> &str` | 两个输入生命周期，规则 2/3 都不够用 → **必须手写**（如 `longest`） |
| `fn announce(&self, s: &str) -> &str` | 规则 3：返回值跟 `&self` 走 |

因此 `longest` 需要显式 `'a`：它有两个输入引用，返回值可能来自其中任一个，省略规则无法替你选。

### 4.7 The Static Lifetime（`'static`）

`'static` 表示可以活到**程序结束**。字符串字面量存在只读数据段，类型是 `&'static str`：

```rust
let s: &'static str = "I have a static lifetime.";
```

编译器报错时有时会建议 `'static`。先问：真的需要“永远有效”，还是该改短借用、换成拥有所有权的类型、或修正标注关系？多数业务 API 并不需要 `'static`。

### 4.8 Combining Generics, Trait Bounds, and Lifetimes（三者结合）

一个签名里可以同时出现生命周期、类型参数和 Trait bound：

```rust
use std::fmt::Display;

fn longest_with_an_announcement<'a, T>(
    x: &'a str,
    y: &'a str,
    ann: T,
) -> &'a str
where
    T: Display,
{
    println!("Announcement! {ann}");
    if x.len() > y.len() { x } else { y }
}
```

---

> [!important] 一句话总结
> 泛型解决“同一逻辑、不同类型”；Trait / Trait bound 解决“类型必须具备哪些行为”；生命周期解决“引用之间谁不能比谁活得更短”。标注只声明关系、不延长寿命；返回引用必须能追溯到某个输入（或 `'static`），结构体存引用就要把借用区域写进类型，其余能省略的交给三条 elision 规则。
