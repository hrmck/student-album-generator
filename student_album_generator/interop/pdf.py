from pyhtml2pdf import converter
from pypdf import PdfWriter


def merge_pdfs(pdf_paths: list[str], output_path: str) -> None:
    merger = PdfWriter()
    for pdf in pdf_paths:
        merger.append(pdf)

    merger.write(output_path)
    merger.close()


def html_to_pdf(html_path: str, pdf_path: str) -> None:
    converter.convert(source=html_path, target=pdf_path)
