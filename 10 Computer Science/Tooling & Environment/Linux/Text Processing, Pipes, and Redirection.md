---
aliases: [grep wc 管道符, Text Processing Pipes and Redirection, grep, wc, pipes, redirection, echo tail]
tags: [linux, shell]
up: "[[Linux MOC]]"
related: "[[File Operations|文件操作]], [[File System and Navigation|文件系统与导航]], [[Environment Variables|环境变量]], [[System Monitoring|系统监控]]"
down: ""
---
# Text Processing, Pipes, and Redirection

> [!summary] 核心结论
> Shell 把命令的输出当作"数据流"来处理：`grep` 按关键字过滤行、`wc` 统计行/词/字节、管道 `|` 把上一条命令的输出喂给下一条、重定向 `>`/`>>` 把输出写入文件、`echo` 输出文本、命令替换 `` `cmd` ``/`$(cmd)` 把命令结果嵌进文本、`tail -f` 实时跟踪文件末尾。这些组合在一起就是 Linux"小工具拼装"的精髓。

前置知识：[[File Operations|文件操作]]（cat / 文件路径）。

---

## 1. `grep` — Filter Lines by Keyword (按关键字过滤)

```
grep [-n] <keyword> <file-path>
```

- **`-n`** — prefix each matching line with its **line number**.
- **keyword** — required; quote it with `" "` if it contains spaces or special characters.
- **file-path** — required; the file to search. It can also be the input end of a **pipe**
  (see §3).

## 2. `wc` — Count Lines, Words, Bytes (数量统计)

```
wc [-c -m -l -w] <file-path>
```

| Option | Counts |
| ------ | ------ |
| `-c`   | bytes |
| `-m`   | characters |
| `-l`   | lines |
| `-w`   | words |

The file path can likewise be replaced by piped input.

## 3. The Pipe `|` (管道符)

```
command1 | command2
```

The pipe sends `command1`'s output **not to the screen, but into `command2`** as its input.
This is the heart of composing small tools. For example, count how many processes contain
`tail`:

```bash
ps -ef | grep tail | wc -l
```

## 4. `echo` — Print Text (输出文本)

```
echo <content>
```

No options; a single argument is printed to the terminal. Quote complex content with
`" "`.

### Command Substitution (命令替换)

Wrapping a command in **backticks** runs it and substitutes the result:

```bash
echo `pwd`        # prints the current working directory
```

The modern, more readable form is `$(...)`:

```bash
echo $(pwd)
```

- Without backticks/`$()` → the text is printed literally.
- With them → the inner command runs first, and its output is substituted in.

## 5. Redirection `>` and `>>` (重定向符)

| Operator | Behaviour |
| -------- | --------- |
| `>`      | **Overwrite** the target file with the left command's output |
| `>>`     | **Append** the left command's output to the end of the file |

```bash
echo "hello" > a.txt     # overwrites a.txt
echo "world" >> a.txt    # appends to a.txt, keeping existing content
```

## 6. `tail` — Watch the End of a File (查看文件尾部)

```
tail [-f -num] <file-path>
```

- **`-f`** — **follow**: keep the file open and stream new lines as they are appended.
  Essential for watching logs live (`tail -f /var/log/syslog`).
- **`-num`** — show the last `num` lines (default 10).

---

> [!important] 一句话总结
> "过滤用 `grep`、统计用 `wc`、串联用 `|`、落盘用 `>`/`>>`、嵌结果用 `$()`、追日志用 `tail -f`" —— 把命令当数据流拼装，是 Linux 命令行的核心思维。
