import dominate
from dominate.tags import *
from pandas import DataFrame
from pathlib import Path
from config import (
    SCHOOL_NAME,
    IMAGE_FOLDER,
    export_image_folder,
)
from utils import get_css_path, display_academic_year


def __get_icon_image_path(use_relative_path: bool = False) -> str:
    img_folder = "/" + IMAGE_FOLDER if use_relative_path else export_image_folder

    return (
        f"{img_folder}/school-badge.jpg"
        if Path(f"{img_folder}/school-badge.jpg").exists()
        else f"{img_folder}/school-badge-not-found.jpg"
    )


def generate(
    teacher_df: DataFrame,
    student_df: DataFrame,
    use_relative_path: bool = False,
) -> str:
    doc = dominate.document()

    with doc.head:
        link(
            rel="stylesheet", href=f"{get_css_path(use_relative_path)}/right-style.css"
        )
        link(
            rel="stylesheet",
            href="https://fonts.googleapis.com/css?family=Noto+Sans+HK",
        )

    with doc:
        with header():
            img(src=__get_icon_image_path(use_relative_path))

            with h1(cls="text-center"):
                span(SCHOOL_NAME)
                span(
                    f"{student_df['class'].iloc[0]} ({display_academic_year(teacher_df['academic_year'].iloc[0])})"
                )

            with div(cls="class-teacher text-right"):
                p("Class Teachers:", cls="text-bold")
                with p():
                    span(teacher_df["class_teacher_1"].iloc[0])
                    span(teacher_df["class_teacher_2"].iloc[0])

        with table():
            with thead():
                th("No.", cls="row-class-no text-center")
                th("Name", cls="row-name")
                # dummy cols are used instead of colspan
                # because it's difficult to adjust col widths
                th(cls="row-christian-name")
                th(cls="row-chi-name")
                th("House", cls="row-house text-center")
                th("Remarks", cls="row-remarks")

            with tbody():
                for student in student_df.itertuples():
                    with tr():
                        td(student.class_no, cls="text-center dashed-right-border")
                        td(student.name, cls="dashed-right-border no-left-border")
                        td(
                            student.christian_name,
                            cls="dashed-right-border no-left-border",
                        )
                        td(student.chi_name, cls="dashed-right-border no-left-border")
                        td(
                            student.house,
                            cls="text-center dashed-right-border no-left-border",
                        )
                        td(cls="no-left-border")

    return str(doc)
