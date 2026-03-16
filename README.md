# md2pdf

Convert Markdown files to PDF with auto-generated bookmarks and CJK support.

[中文文档](README_zh.md)

## Features

- **Bookmarks** — Automatically generates PDF bookmarks from h1/h2/h3 headings
- **CJK support** — Built-in font stack for Chinese, Japanese, Korean text
- **Merge** — Combine multiple Markdown files into a single PDF with unified bookmarks
- **Custom CSS** — Full control over page layout, fonts, and styling
- **Page size** — A4, Letter, or any CSS page size

## Installation

### Prerequisites

WeasyPrint depends on system libraries. Install them first:

**Debian / Ubuntu:**

```bash
sudo apt install libpango1.0-dev libcairo2-dev libgdk-pixbuf2.0-dev
```

**macOS (Homebrew):**

```bash
brew install pango cairo gdk-pixbuf
```

**Arch Linux:**

```bash
sudo pacman -S pango cairo gdk-pixbuf2
```

### Install md2pdf

```bash
pip install md2pdf-bookmarks
```

Or install from source:

```bash
git clone https://github.com/TbusOS/md-to-pdf.git
cd md-to-pdf
pip install .
```

## Usage

### Basic conversion

```bash
md2pdf README.md
```

Output: `README.pdf` in the same directory.

### Specify output path

```bash
md2pdf README.md -o output.pdf
```

### Merge multiple files

```bash
md2pdf ch1.md ch2.md ch3.md -o book.pdf
```

All files are converted and merged into a single PDF. Bookmarks from each file are combined.

### Custom stylesheet

```bash
md2pdf README.md --css custom.css
```

The CSS file controls all styling including page size, margins, fonts, and colors. See [Custom CSS](#custom-css) for details.

### Change page size

```bash
md2pdf README.md --page-size letter
```

Supports any valid CSS page size: `A4`, `letter`, `A3`, `legal`, etc.

### Disable bookmarks

```bash
md2pdf README.md --no-bookmarks
```

### Full options

```
usage: md2pdf [-h] [-v] [-o OUTPUT] [--css CSS] [--page-size PAGE_SIZE]
              [--no-bookmarks]
              INPUT [INPUT ...]

positional arguments:
  INPUT                 Markdown file(s) to convert

optional arguments:
  -h, --help            show this help message and exit
  -v, --version         show program's version number and exit
  -o OUTPUT, --output OUTPUT
                        output PDF path (default: <input>.pdf)
  --css CSS             custom CSS file for styling
  --page-size PAGE_SIZE
                        page size, e.g. A4, letter (default: A4)
  --no-bookmarks        disable bookmark generation
```

## Python API

```python
from md2pdf import convert, merge_pdfs

# Single file
convert("README.md", "README.pdf")

# With options
convert("doc.md", "doc.pdf", page_size="letter", bookmarks=True)

# Custom CSS
css = open("style.css").read()
convert("doc.md", "doc.pdf", css=css)

# Merge multiple PDFs
merge_pdfs(["part1.pdf", "part2.pdf"], "merged.pdf")
```

## Custom CSS

Create a CSS file to control the PDF appearance:

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

When using `--css`, you have full control. The default stylesheet is replaced entirely.

## Default CJK fonts

The built-in stylesheet uses this font stack:

```
Noto Sans CJK SC → WenQuanYi Micro Hei → SimHei → PingFang SC → Microsoft YaHei → sans-serif
```

This covers common CJK fonts across Linux, macOS, and Windows. For best results, install [Noto Sans CJK](https://github.com/notofonts/noto-cjk/releases).

## Cursor Skill

This repo includes a [Cursor](https://www.cursor.com/) Skill in the `skill/` directory, which enables Cursor's AI agent to use `md2pdf` automatically when you ask it to convert Markdown to PDF.

To install the skill, symlink or copy it to your Cursor skills directory:

```bash
ln -s "$(pwd)/skill" ~/.cursor/skills/md-to-pdf
```

Or copy it:

```bash
cp -r skill ~/.cursor/skills/md-to-pdf
```

After installation, the AI agent will automatically invoke `md2pdf` when you request Markdown-to-PDF conversion.

## License

[MIT](LICENSE)
