import dominate
from dominate.tags import *
from pandas import DataFrame
from pathlib import Path
from config import SCHOOL_NAME, IMAGE_FOLDER, abs_image_folder, export_image_folder
from utils import get_css_path, display_academic_year


PHOTO_NUM_IN_ONE_ROW = 7


def __get_image_path(student_id: str, use_relative_path: bool = False) -> str:
    img_folder = "/" + IMAGE_FOLDER if use_relative_path else export_image_folder
    return (
        f"{img_folder}/{student_id}.jpg"
        if Path(f"{abs_image_folder}/{student_id}.jpg").exists()
        else f"{img_folder}/student-not-found.jpg"
    )


def generate(klass_df: DataFrame, use_relative_path: bool = False) -> str:
    report_title = f"{SCHOOL_NAME} {display_academic_year(klass_df['academic_year'].iloc[0])} Class: {klass_df['class'].iloc[0]}"
    doc = dominate.document(title=report_title)

    with doc.head:
        link(rel="stylesheet", href=f"{get_css_path(use_relative_path)}/left-style.css")

    with doc:
        h1(report_title)

        with div(cls="photo-grid"):
            for student in klass_df.itertuples():
                with div(cls="student-unit"):
                    img(
                        src=__get_image_path(student.student_id, use_relative_path),
                    )
                    with div(cls="student-info"):
                        with p():
                            span(student.class_no)
                            span(
                                f"{student.christian_name} {student.family_name}"
                                if student.christian_name
                                else student.name
                            )

                        p(student.primary_school, cls="primary-sch")
    return str(doc)
