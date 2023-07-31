from input import read_student_data, read_class_teacher_data
from interop.html import generate_htmls
from interop.pdf import html_to_pdf, merge_pdfs
from pathlib import Path

# e.g. STUDENT_CSV = "sample-student-data.csv"
STUDENT_CSV = "sample-student-data.csv"
# e.g. CLASS_TEACHER_CSV = "sample-class-data.csv"
CLASS_TEACHER_CSV = "sample-class-data.csv"

student_data = read_student_data(path=f"csv/{STUDENT_CSV}")
class_teacher_data = read_class_teacher_data(path=f"csv/{CLASS_TEACHER_CSV}")
html_paths = generate_htmls(
    student_df=student_data, class_teacher_df=class_teacher_data
)
pdf_paths = []
for html_path in html_paths:
    pdf_path = f"pdf/{Path(html_path).stem}.pdf"
    html_to_pdf(html_path=html_path, pdf_path=pdf_path)
    pdf_paths.append(pdf_path)

merge_pdfs(pdf_paths=pdf_paths, output_path="pdf/merged.pdf")
