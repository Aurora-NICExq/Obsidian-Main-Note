# 学习笔记 Study Notes

这是一个用 [Obsidian](https://obsidian.md) 管理的个人学习笔记库，收录约 **495 篇** Markdown 笔记，主要使用中文写作，涵盖计算机科学、数学、电子工程、读书笔记与语言等领域。

> 这是**内容仓库**而非软件项目：没有构建、测试或打包步骤。"维护"指的是编辑、整理笔记及其附件，然后提交。

**离线优先**：本库的全部工作流都以无网络环境为前提 —— 图表预先渲染为 SVG 而非依赖在线插件，不使用任何需要联网的插件。

## 目录结构 Structure

顶层文件夹采用**数字前缀编号**强制排序，留空的编号（如 `60`、`70`、`80`）是为新学科预留的。学科**标题用英文**，内部子文件夹仍用中文。

| 文件夹 | 笔记数 | 内容 |
| --- | ---: | --- |
| `00 Meta & Reference/` | 4 | 库元信息：`Maps of Content/`（MOC 索引）与 `Syntax Cheatsheets/`（LaTeX、Markdown 速查） |
| `10 Computer Science/` | 107 | C 语言、数据结构（C）、算法（MIT 6.006 / CLRS）、Rust、深度学习（MIT 6.7960）、工具与环境（Linux、CLI） |
| `20 Mathematics/` | 96 | 微积分、多元微积分、线性代数（MIT 18.06）、实分析（MIT 18.01） |
| `30 Electrical & Computer Engineering/` | 86 | 电路理论、模拟电路（Caltech）、数字电子、信号与系统、嵌入式系统（STM32、FreeRTOS、控制算法） |
| `40 Book Notes/` | 199 | 电子书精读笔记：精神分析、经济学、马克思主义、哲学 |
| `50 Languages/` | 3 | 英语（雅思）、法语 |
| `90 Assets/` | — | 全局 `attachments/` 附件、`diagrams/`（180 个预生成 SVG）与 `scripts/`（图表生成脚本） |

## 笔记约定 Conventions

- **扩展名必须是 `.md`**：Obsidian 只索引 `.md`。存成 `.markdown` 会被当作附件，从搜索与关系图中消失，且所有 `[[wikilink]]` 静默失效。
- **Frontmatter**：使用 YAML frontmatter，完整约定为
  `aliases:`（检索同义词，含中文）、`tags:`（学科）、`up:`（所属 MOC）、`related:` / `down:`（同级与后续笔记）。最低要求是 `tags:`。
- **标题层级**：每篇一个 `# H1`（与文件名对应），小节用 `## N.` / `### N.M`。多数笔记在首个小节前有 `> [!summary] 核心结论` callout。
- **图片嵌入**：优先使用 Obsidian wikilink 嵌入 `![[截屏....png]]`（不带路径，由 Obsidian 解析）。
- **附件位置**：`app.json` 设置了 `attachmentFolderPath: "attachments"`，粘贴的图片落在笔记同级的 `attachments/` 文件夹；跨学科图片放 `90 Assets/attachments/`。
- **图表即预生成 SVG**：不依赖实时渲染插件。可编辑源码 + 生成产物一并保留，管线在 `90 Assets/scripts/`：
  - TikZ → `tikz_to_svg/convert_all.py`（XeLaTeX，回退 `tectonic`）→ `tikz-*.svg`
  - Mermaid → `mermaid_to_d2/convert_all.py`（`d2`）→ `d2-*.svg`
  - 信号与系统的坐标图 → `signals_and_systems/`（matplotlib）→ `ss-*.svg`

  产物统一落在 `90 Assets/diagrams/<领域>/`，以 `![[tikz-….svg]]` 嵌入。
- **数学公式**：全文使用行内 / `$$` LaTeX（由 latex-suite 插件辅助输入）。

## 索引 Maps of Content

17 个 MOC 作为各自文件夹的目录页：frontmatter 带 `tags: [<subject>, MOC]` 与列出全部笔记的 `down:`，正文按主题分组，通常附一张学习顺序图。笔记用 `up:` 反向指回。**新增笔记时两个方向都要同步。**

尚无 MOC 的文件夹（按规模）：`Algorithms (CLRS)`、`Analog Circuit Design`、`C Programming`、`Digital Electronics`。

## 使用插件 Plugins

templater · dataview · omnisearch · obsidian-outliner · latex-suite · code-styler · iconize · minimal-settings（style-settings 已安装未启用）

含插件语法（dataview 查询）的内容需在安装对应插件的 Obsidian 中才能正确渲染。

## 注意 Notes

- 在 Obsidian 内重命名 / 移动笔记会自动更新 wikilink（`alwaysUpdateLinks: true`）；若通过终端或外部工具操作，需**手动**修复所有 `[[...]]` 与 `![[...]]` 引用。
- iCloud / 同步冲突会产生带尾部 ` 2` 的重复文件（如 `截屏... 2.png`）及 `.DS_Store`，均为可清理的垃圾。
- 截图被 SVG 图表替换后，记得删除失去引用的 PNG，避免堆积孤儿附件。
