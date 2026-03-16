---
name: md-to-pdf
description: >-
  Convert Markdown files to PDF with bookmarks. Use when the user asks to
  generate PDF from Markdown, convert .md to .pdf, create PDF documents with
  table of contents or bookmarks, or merge multiple Markdown files into one PDF.
---

# Markdown to PDF Conversion

Use the `md2pdf` CLI tool to convert Markdown files to PDF with CJK support and auto-generated bookmarks.

## Installation

If `md2pdf` command is not available, install it:

```bash
pip3 install --user md2pdf-bookmarks
```

Or from source:

```bash
git clone https://github.com/TbusOS/md-to-pdf.git
cd md-to-pdf
pip3 install --user .
```

## Usage

### Single file

```bash
md2pdf README.md
# Output: README.pdf

md2pdf README.md -o output.pdf
```

### Multiple files merged into one

```bash
md2pdf ch1.md ch2.md ch3.md -o book.pdf
```

### Custom CSS

```bash
md2pdf README.md --css custom.css -o output.pdf
```

### Page size

```bash
md2pdf README.md --page-size letter -o output.pdf
```

### Disable bookmarks

```bash
md2pdf README.md --no-bookmarks -o output.pdf
```

## Python API

The tool can also be used as a Python library:

```python
from md2pdf import convert, merge_pdfs

convert("README.md", "README.pdf")
convert("doc.md", "doc.pdf", page_size="letter")
merge_pdfs(["a.pdf", "b.pdf"], "merged.pdf")
```

## Notes

- Default CSS supports CJK fonts (Noto Sans CJK SC, WenQuanYi, SimHei, PingFang SC, Microsoft YaHei)
- Bookmarks are auto-generated from h1/h2/h3 headings
- Relative image paths in Markdown are resolved correctly
- Custom CSS gives full control over page size, margins, and styling
