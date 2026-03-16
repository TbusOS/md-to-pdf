import markdown
import fitz
import re
import shutil
import tempfile
from pathlib import Path


DEFAULT_CSS_PATH = Path(__file__).parent / "default.css"


def get_default_css():
    return DEFAULT_CSS_PATH.read_text(encoding="utf-8")


def md_to_html(md_content, css):
    html_body = markdown.markdown(
        md_content, extensions=["tables", "fenced_code"]
    )
    return (
        f"<html><head><meta charset='utf-8'>"
        f"<style>{css}</style></head>"
        f"<body>{html_body}</body></html>"
    )


def html_to_pdf(html_string, pdf_path, base_url=None):
    from weasyprint import HTML

    HTML(string=html_string, base_url=base_url).write_pdf(pdf_path)


def add_bookmarks(pdf_path, md_content):
    doc = fitz.open(pdf_path)
    toc = []
    headings = re.findall(r"^(#{1,3})\s+(.+)$", md_content, re.MULTILINE)
    page_texts = [page.get_text() for page in doc]

    for prefix, title in headings:
        level = len(prefix)
        clean_title = re.sub(r"[`*\[\]]", "", title).strip()
        target_page = 0
        for i, text in enumerate(page_texts):
            if clean_title[:20] in text:
                target_page = i
                break
        toc.append([level, clean_title, target_page + 1])

    if toc:
        doc.set_toc(toc)
        tmp_path = pdf_path + ".tmp"
        doc.save(tmp_path, deflate=True)
        doc.close()
        shutil.move(tmp_path, pdf_path)
    else:
        doc.close()


def convert(md_path, pdf_path, css=None, page_size="A4", bookmarks=True):
    """Convert a single markdown file to PDF."""
    md_path = str(md_path)
    pdf_path = str(pdf_path)
    md_content = Path(md_path).read_text(encoding="utf-8")

    if css is None:
        css_content = get_default_css()
        if page_size != "A4":
            css_content = css_content.replace("size: A4;", f"size: {page_size};")
    else:
        css_content = css

    html = md_to_html(md_content, css_content)
    base_url = str(Path(md_path).parent.resolve())
    html_to_pdf(html, pdf_path, base_url=base_url)

    if bookmarks:
        add_bookmarks(pdf_path, md_content)


def merge_pdfs(pdf_paths, output_path):
    """Merge multiple PDFs into one, combining bookmarks."""
    merged = fitz.open()
    toc = []
    page_offset = 0

    for pdf_path in pdf_paths:
        doc = fitz.open(pdf_path)
        merged.insert_pdf(doc)
        for level, title, page in doc.get_toc():
            toc.append([level, title, page + page_offset])
        page_offset += len(doc)
        doc.close()

    if toc:
        merged.set_toc(toc)
    merged.save(output_path, deflate=True)
    merged.close()
