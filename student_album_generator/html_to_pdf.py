from pyhtml2pdf import converter


def generate_pdf(html_path: str, pdf_path: str) -> None:
    converter.convert(source=html_path, target=pdf_path)
