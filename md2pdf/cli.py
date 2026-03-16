import argparse
import os
import sys
import tempfile
from pathlib import Path

from . import __version__
from .converter import convert, merge_pdfs

EXAMPLES = """
examples:
  md2pdf README.md                        Convert to README.pdf
  md2pdf README.md -o doc.pdf             Specify output path
  md2pdf ch1.md ch2.md ch3.md -o book.pdf Merge multiple files
  md2pdf README.md --css style.css        Use custom stylesheet
  md2pdf README.md --page-size letter     Use Letter page size
  md2pdf README.md --no-bookmarks         Disable bookmarks
"""


def main():
    parser = argparse.ArgumentParser(
        prog="md2pdf",
        description="Convert Markdown files to PDF with auto-generated bookmarks and CJK support.",
        epilog=EXAMPLES,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "-v", "--version", action="version", version=f"%(prog)s {__version__}"
    )
    parser.add_argument(
        "inputs", nargs="+", metavar="INPUT", help="Markdown file(s) to convert"
    )
    parser.add_argument("-o", "--output", help="output PDF path (default: <input>.pdf)")
    parser.add_argument("--css", help="custom CSS file for styling")
    parser.add_argument(
        "--page-size", default="A4", help="page size, e.g. A4, letter (default: A4)"
    )
    parser.add_argument(
        "--no-bookmarks", action="store_true", help="disable bookmark generation"
    )

    args = parser.parse_args()

    for f in args.inputs:
        if not os.path.isfile(f):
            print(f"Error: file not found: {f}", file=sys.stderr)
            sys.exit(1)

    css_content = None
    if args.css:
        css_path = Path(args.css)
        if not css_path.is_file():
            print(f"Error: CSS file not found: {args.css}", file=sys.stderr)
            sys.exit(1)
        css_content = css_path.read_text(encoding="utf-8")

    bookmarks = not args.no_bookmarks

    if len(args.inputs) == 1:
        input_path = args.inputs[0]
        output_path = args.output or str(Path(input_path).with_suffix(".pdf"))
        convert(
            input_path,
            output_path,
            css=css_content,
            page_size=args.page_size,
            bookmarks=bookmarks,
        )
        print(output_path)
    else:
        output_path = args.output
        if not output_path:
            print(
                "Error: -o/--output is required when converting multiple files",
                file=sys.stderr,
            )
            sys.exit(1)

        with tempfile.TemporaryDirectory() as tmpdir:
            tmp_pdfs = []
            for i, input_path in enumerate(args.inputs):
                tmp_pdf = os.path.join(tmpdir, f"part_{i}.pdf")
                convert(
                    input_path,
                    tmp_pdf,
                    css=css_content,
                    page_size=args.page_size,
                    bookmarks=bookmarks,
                )
                tmp_pdfs.append(tmp_pdf)

            merge_pdfs(tmp_pdfs, output_path)
            print(output_path)


if __name__ == "__main__":
    main()
