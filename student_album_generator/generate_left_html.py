import dominate
from dominate.tags import *
from pandas import DataFrame
from pathlib import Path

PHOTO_NUM_IN_ONE_ROW = 7
IMAGE_FOLDER = "img"
CSS_FOLDER = "css"


image_folder = f"file:///{Path.cwd()}/{IMAGE_FOLDER}"
css_folder = f"file:///{Path.cwd()}/{CSS_FOLDER}"


def __get_image_path(student_id: str, use_relative_path: bool = False) -> str:
    img_folder = "/" + IMAGE_FOLDER if use_relative_path else image_folder

    return (
        f"{img_folder}/{student_id}.jpg"
        if Path(f"{img_folder}/{student_id}.jpg")
        else f"{img_folder}/dummy.jpg"
    )


def __get_css_path(use_relative_path: bool = False) -> str:
    return "/" + CSS_FOLDER if use_relative_path else css_folder


def __generate_student_photo_info(
    student_id: str,
    class_no: str,
    christian_name: str,
    family_name: str,
    primary_school: str,
    use_relative_path: bool = False,
) -> list:
    return [
        div(
            img(
                src=__get_image_path(student_id, use_relative_path),
                cls="student-image",
            ),
            div(
                p(f"{class_no} {christian_name} {family_name}"),
                p(primary_school),
                cls="student-info",
            ),
            cls="student",
        )
    ]


def generate(
    report_title: str, klass_df: DataFrame, use_relative_path: bool = False
) -> str:
    doc = dominate.document(title=report_title)

    with doc.head:
        link(
            rel="stylesheet", href=f"{__get_css_path(use_relative_path)}/left-style.css"
        )

    with doc:
        h1(report_title)

        with div(id="student-photos"):
            for student in klass_df.itertuples():
                __generate_student_photo_info(
                    student.student_id,
                    student.class_no,
                    student.christian_name,
                    student.family_name,
                    student.primary_school,
                    use_relative_path,
                )

    return str(doc)
