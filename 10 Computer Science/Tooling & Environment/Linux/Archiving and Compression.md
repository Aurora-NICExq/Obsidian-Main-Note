---
aliases: [压缩和解压, Archiving and Compression, tar, zip, gzip]
tags: [linux, archiving]
up: "[[Linux MOC]]"
related: "[[File Operations|文件操作]], [[File Transfer (wget, curl)|文件下载]], [[File System and Navigation|文件系统与导航]]"
down: ""
---
# Archiving and Compression

> [!summary] 核心结论
> Linux 上最常用的是 `tar`（打包 + 可选 gzip 压缩，产出 `.tar.gz`）和 `zip`/`unzip`。`tar` 的关键在于一组单字母选项的组合，最容易踩的坑是：**`-f` 必须放在选项最后**、紧跟文件名。

前置知识：[[File Operations|文件操作]]（路径与目录）。

---

## 1. Common Archive Formats (常见压缩格式)

| Format | Typical platforms |
| ------ | ----------------- |
| `zip`  | Linux / Windows / macOS |
| `7z`   | Windows |
| `rar`  | Windows |
| `tar`  | Linux / macOS (archiving) |
| `gzip` | Linux / macOS (compression) |

The ubiquitous `.tar.gz` is a two-step combination: **`tar` bundles files into one
archive, then `gzip` compresses that archive**.

## 2. `tar` Flags (tar 常用选项)

| Flag | Meaning |
| ---- | ------- |
| `-c` | **Create** an archive (compression mode) |
| `-x` | **Extract** an archive |
| `-v` | **Verbose** — show progress / the files being processed |
| `-f` | The archive **file** name — **must be the last flag**, immediately followed by the filename |
| `-z` | Use **gzip** (for `.tar.gz`); omit for a plain tarball |
| `-C` | Extract **to** a target directory |

## 3. Creating Archives (打包压缩)

```bash
tar -cvf backup.tar dir/             # plain tar archive of dir/
tar -zcvf backup.tar.gz dir/         # tar + gzip → backup.tar.gz
```

Reading `-zcvf`: `z` gzip, `c` create, `v` verbose, `f` file (so `backup.tar.gz` is the
output name).

## 4. Extracting Archives (解压)

```bash
tar -xvf test.tar                          # extract to the current directory
tar -xvf test.tar -C /home/itheima         # extract to a target directory
tar -zxvf test.tar.gz -C /home/itheima     # gzip archive → target directory
```

> [!warning] tar 常见陷阱
> - **`-f` must come last** in the flag cluster, with the archive filename right after it
>   (`-zcvf name.tar.gz`, not `-zfcv`).
> - Put **`-z` at the front** of the cluster.
> - Use **`-C` separately** from the other extraction flags, followed by the destination
>   directory.

## 5. `zip` and `unzip` (zip 压缩与解压)

```
zip [-r] <archive.zip> <file1> <file2> ... <fileN>
unzip [-d <target-dir>] <archive.zip>
```

- **`zip -r`** — required when the content **includes a directory** (recursive), same idea
  as `-r` in `cp`/`rm`.
- **`unzip -d`** — extract to a specified directory (the counterpart of `tar`'s `-C`).

```bash
zip -r site.zip www/            # compress the www/ directory
unzip site.zip -d /var/         # extract into /var/
```

---

> [!important] 一句话总结
> 记 `tar -zcvf 名字.tar.gz 目录/` 压缩、`tar -zxvf 名字.tar.gz -C 目标/` 解压；铁律是"`-f` 永远在最后，后面紧跟文件名"。zip 世界则是 `zip -r` 与 `unzip -d`。
