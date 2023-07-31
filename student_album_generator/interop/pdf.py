from pypdf import PdfWriter


def merge_pdfs(pdf_paths: list[str], output_path: str) -> None:
    merger = PdfWriter()
    for pdf in pdf_paths:
        merger.append(pdf)

    merger.write(output_path)
    merger.close()
    print(f"Merged PDF: {output_path}")
