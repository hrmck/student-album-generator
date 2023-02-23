from input import read_student_data, read_class_teacher_data
from interop.html import generate_htmls
from interop.pdf import html_to_pdf, merge_pdfs
from utils import get_filename_wo_extension
from pathlib import Path

student_data = read_student_data(path="csv/sample-student-data.csv")
class_teacher_data = read_class_teacher_data(path="csv/sample-class-data.csv")
html_paths = generate_htmls(
    student_df=student_data, class_teacher_df=class_teacher_data
)
pdf_paths = []
for html_path in html_paths:
    pdf_path = f"pdf/{get_filename_wo_extension(html_path)}.pdf"
    html_to_pdf(html_path=html_path, pdf_path=pdf_path)
    pdf_paths.append(pdf_path)

merge_pdfs(pdf_paths=pdf_paths, output_path="pdf/merged.pdf")
