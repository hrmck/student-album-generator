import pandas as pd
from pathlib import Path
import student_album_generator.generate_left_html as generate_left_html
import html_to_pdf
import combine_pdf
from icecream import ic

SCHOOL_NAME = "Holy Trinity College"
# fmt: off
CLASSES = [
    "1A", "1B", "1C", "1D", "1E",
    # "2A", "2B", "2C", "2D", "2E",
    # "3A", "3B", "3C", "3D", "3E",
    # "4A", "4B", "4C", "4D", "4E",
    # "5A", "5B", "5C", "5D", "5E",
    # "6A", "6B", "6C", "6D", "6E"
]
# fmt: on
html_folder = "html-report"


def display_academic_year(year: str) -> str:
    return f"{year}-{int(year) + 1}"


def write_html(output_path: str, html_str: str) -> None:
    with open(output_path, "w") as output_file:
        output_file.write(html_str)


df = pd.read_csv("csv/sample-student-data.csv", header=0)
df["family_name"] = df.apply(lambda row: str.split(row["name"], maxsplit=1)[0], axis=1)

pdf_paths = []

for klass in CLASSES:
    klass_df = df[df["class"] == klass]

    # generate html report
    report_title = f"{SCHOOL_NAME} {display_academic_year(klass_df['academic_year'].iloc[0])} Class: {klass_df['class'].iloc[0]}"

    html_relative = generate_left_html.generate(
        report_title=report_title, klass_df=klass_df, use_relative_path=True
    )
    html = generate_left_html.generate(report_title=report_title, klass_df=klass_df)
    write_html(f"{html_folder}/{klass}-left-preview.html", html_relative)
    write_html(f"{html_folder}/{klass}-left.html", html)
    html_to_pdf.generate_pdf(
        html_path=f"file:///{Path.cwd()}/{html_folder}/{klass}-left.html",
        pdf_path=f"pdf/{klass}-left.pdf",
    )
    pdf_paths.append(f"pdf/{klass}-left.pdf")

combine_pdf.merge(pdf_paths)
