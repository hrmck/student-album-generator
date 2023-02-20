from pypdf import PdfWriter

# pdf_list = [
#     "pdf/1A-left.pdf",
#     "pdf/1B-left.pdf",
#     "pdf/1C-left.pdf",
#     "pdf/1D-left.pdf",
#     "pdf/1E-left.pdf",
# ]


def merge(pdf_paths: list[str]) -> None:
    merger = PdfWriter()
    for pdf in pdf_paths:
        merger.append(pdf)

    merger.write("merged.pdf")
    merger.close()
