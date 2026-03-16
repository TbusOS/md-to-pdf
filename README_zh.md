# md2pdf

将 Markdown 文件转换为 PDF，自动生成书签，支持中日韩文字。

## 功能特性

- **自动书签** — 从 h1/h2/h3 标题自动生成 PDF 书签导航
- **CJK 支持** — 内置中日韩字体栈，开箱即用
- **多文件合并** — 将多个 Markdown 文件合并为一个 PDF，书签自动拼接
- **自定义样式** — 通过 CSS 完全控制页面布局、字体和配色
- **纸张大小** — 支持 A4、Letter 等任意 CSS 页面尺寸

## 安装

### 系统依赖

md2pdf 基于 WeasyPrint，需要先安装以下系统库：

**Debian / Ubuntu：**

```bash
sudo apt install libpango1.0-dev libcairo2-dev libgdk-pixbuf2.0-dev
```

**macOS (Homebrew)：**

```bash
brew install pango cairo gdk-pixbuf
```

**Arch Linux：**

```bash
sudo pacman -S pango cairo gdk-pixbuf2
```

### 安装 md2pdf

```bash
pip install md2pdf-bookmarks
```

或从源码安装：

```bash
git clone https://github.com/TbusOS/md-to-pdf.git
cd md-to-pdf
pip install .
```

## 使用方法

### 基本转换

```bash
md2pdf README.md
```

输出 `README.pdf` 到同一目录。

### 指定输出路径

```bash
md2pdf README.md -o output.pdf
```

### 合并多个文件

```bash
md2pdf ch1.md ch2.md ch3.md -o book.pdf
```

所有文件依次转换并合并为一个 PDF，各文件的书签自动拼接。

### 自定义样式

```bash
md2pdf README.md --css custom.css
```

CSS 文件控制所有样式，包括页面大小、边距、字体和颜色。详见[自定义 CSS](#自定义-css) 章节。

### 修改纸张大小

```bash
md2pdf README.md --page-size letter
```

支持任意合法的 CSS 页面尺寸：`A4`、`letter`、`A3`、`legal` 等。

### 禁用书签

```bash
md2pdf README.md --no-bookmarks
```

### 完整参数

```
用法: md2pdf [-h] [-v] [-o OUTPUT] [--css CSS] [--page-size PAGE_SIZE]
             [--no-bookmarks]
             INPUT [INPUT ...]

位置参数:
  INPUT                 要转换的 Markdown 文件（支持多个）

可选参数:
  -h, --help            显示帮助信息
  -v, --version         显示版本号
  -o OUTPUT, --output OUTPUT
                        输出 PDF 路径（默认: <输入文件名>.pdf）
  --css CSS             自定义 CSS 样式文件
  --page-size PAGE_SIZE
                        纸张大小，如 A4、letter（默认: A4）
  --no-bookmarks        禁用书签生成
```

## Python API

除了命令行，也可以作为 Python 库调用：

```python
from md2pdf import convert, merge_pdfs

# 单文件转换
convert("README.md", "README.pdf")

# 指定选项
convert("doc.md", "doc.pdf", page_size="letter", bookmarks=True)

# 自定义 CSS
css = open("style.css").read()
convert("doc.md", "doc.pdf", css=css)

# 合并多个 PDF
merge_pdfs(["part1.pdf", "part2.pdf"], "merged.pdf")
```

## 自定义 CSS

创建 CSS 文件来控制 PDF 的外观：

```css
@page {
    size: A4;
    margin: 2.5cm;
}

body {
    font-family: "Georgia", serif;
    font-size: 11pt;
    line-height: 1.8;
}

h1 {
    font-size: 24pt;
    color: #2c3e50;
}

code {
    background-color: #f8f8f8;
    padding: 2px 6px;
    border-radius: 3px;
}
```

使用 `--css` 时，默认样式表会被完全替换，你拥有完全的控制权。

## 默认 CJK 字体

内置样式表使用以下字体栈：

```
Noto Sans CJK SC → WenQuanYi Micro Hei → SimHei → PingFang SC → Microsoft YaHei → sans-serif
```

覆盖 Linux、macOS、Windows 上的常见中文字体。推荐安装 [Noto Sans CJK](https://github.com/notofonts/noto-cjk/releases) 以获得最佳效果。

## Cursor Skill

本仓库在 `skill/` 目录下包含一个 [Cursor](https://www.cursor.com/) Skill，让 Cursor 的 AI 代理在你要求将 Markdown 转为 PDF 时自动调用 `md2pdf`。

安装方式 — 软链接或复制到 Cursor skills 目录：

```bash
ln -s "$(pwd)/skill" ~/.cursor/skills/md-to-pdf
```

或直接复制：

```bash
cp -r skill ~/.cursor/skills/md-to-pdf
```

安装后，当你让 AI 转换 Markdown 为 PDF 时，它会自动使用 `md2pdf` 命令。

## 许可证

[MIT](LICENSE)
