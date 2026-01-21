## 1. 上下标、括号、绝对值 

`a^2           % 上标：a² x_{n+1}       % 下标：x_{n+1} x^{2n+1}      % 组合上标 x_{ij}        % 组合下标  (1+2)         % 普通括号 \left( \frac{1}{x} \right)   % 会自动放大的括号  |x|           % 绝对值 \left| x^2 - 1 \right|`

---

## 2. 分数、根号

`\frac{a}{b}               % a/b \frac{x+1}{x-1}  \sqrt{x}                  % √x \sqrt{ x^2 + 1 }          % √(x²+1) \sqrt[3]{x}               % 三次根号`

---

## 3. 常见符号（集合、不等号、箭头）

`\leq \geq \neq \approx    % ≤ ≥ ≠ ≈ \in \notin                % ∈ ∉ \subset \subseteq         % ⊂ ⊆ \cup \cap                 % ∪ ∩ \forall \exists           % ∀ ∃ \rightarrow \Rightarrow   % → ⇒ \leftrightarrow           % ↔ \infty                    % ∞`

---

## 4. 希腊字母（常见到爆）

`\alpha, \beta, \gamma, \delta, \epsilon, \lambda, \mu, \sigma, \omega  \Delta, \Sigma, \Lambda, \Omega   % 大写`

用法示例：

`\lambda_1, \lambda_2, \dots, \lambda_n`

---

## 5. 极限、导数、积分（微积分核心三件套）

### 极限

`\lim_{x \to 0} \frac{\sin x}{x}  \lim_{n \to \infty} a_n`

### 导数 / 偏导

`f'(x)                    % 常用简写 f''(x)  \frac{df}{dx}, \frac{dy}{dx}   \frac{\partial f}{\partial x}     % 偏导 \frac{\partial^2 f}{\partial x^2} % 二阶偏导`

### 积分

`\int f(x)\,dx  \int_a^b f(x)\,dx  \iint_D f(x,y)\,dx\,dy       % 二重积分 \iiint_V f(x,y,z)\,dx\,dy\,dz % 三重积分`

`\ , \, \; \quad` 都是“空格”，常用 `\,` 让公式更好看。

---

## 6. 求和、连乘（常见在级数里）

`\sum_{i=1}^n i^2  \prod_{k=1}^n a_k`

---

## 7. 矩阵、向量、内积（线性代数必备）

### 列向量

`\begin{pmatrix} x_1 \\ x_2 \\ x_3 \end{pmatrix}`

### 矩阵

`\begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}`

如果你想要方括号形式：

`\begin{bmatrix} a_{11} & a_{12} & \dots & a_{1n} \\ a_{21} & a_{22} & \dots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \dots & a_{mn} \end{bmatrix}`

### 向量、内积、范数

`\vec{v}              % 带箭头的向量 v \mathbf{v}           % 加粗 v，表示向量  \langle x, y \rangle % 内积 <x, y> \|x\|                % 范数 ||x|| \|x\|_2              % 二范数`

---

## 8. 线性代数常见记号

`A^{-1}          % 逆矩阵 A^T             % 转置 \det(A)         % 行列式 \operatorname{rank}(A)  % 秩 \ker(A), \operatorname{Ker}(A)  % 核 \operatorname{Im}(A)            % 像空间 \lambda, \mu                    % 特征值常用符号`

---

## 9. 分段函数（在高数里经常出现）

`f(x) = \begin{cases} x^2, & x \ge 0, \\ -x,  & x < 0. \end{cases}`

记住 `cases` 环境里的每一行是 `表达式 & 条件 \\` 这样的结构。

---

## 10. 多行对齐公式（推导过程非常好用）

需要 `align` 环境（很多渲染器支持）：

`\begin{align} f(x) &= x^2 + 2x + 1 \\      &= (x+1)^2 \end{align}`

`&` 对齐位置，一般放在等号前。

