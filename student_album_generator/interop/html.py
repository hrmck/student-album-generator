import dominate
from dominate.tags import *
import pandas as pd
from pathlib import Path
from config import (
    SCHOOL_NAME,
    IMAGE_FOLDER,
    abs_image_folder,
    CSS_FOLDER,
    IMAGE_EXTENSION,
)
from utils import get_selenium_file_path
from config import HTML_FOLDER, SCHOOL_BADGE_IMAGE_NAME


def __get_css_path(use_relative_path: bool = False) -> str:
    return "/" + CSS_FOLDER if use_relative_path else get_selenium_file_path(CSS_FOLDER)


def __display_academic_year(year: str) -> str:
    return f"{year}-{int(year) + 1}"


def __generate_right_html(
    student_df: pd.DataFrame,
    teacher_df: pd.DataFrame,
    use_relative_path: bool = False,
) -> str:
    def get_image_path(use_relative_path: bool = False) -> str:
        img_folder = (
            "/" + IMAGE_FOLDER
            if use_relative_path
            else get_selenium_file_path(IMAGE_FOLDER)
        )

        return (
            f"{img_folder}/{SCHOOL_BADGE_IMAGE_NAME}"
            if Path(f"{abs_image_folder}/{SCHOOL_BADGE_IMAGE_NAME}").exists()
            else f"{img_folder}/school-badge-not-found.jpg"
        )

    doc = dominate.document()

    with doc.head:
        link(
            rel="stylesheet",
            href=f"{__get_css_path(use_relative_path)}/right-style.css",
        )
        link(
            rel="stylesheet",
            href="https://fonts.googleapis.com/css?family=Noto+Sans+HK",
        )

    with doc:
        with header():
            img(src=get_image_path(use_relative_path))

            with h1(cls="text-center"):
                span(SCHOOL_NAME)
                span(
                    f"{student_df['class'].iloc[0]} ({__display_academic_year(teacher_df['academic_year'].iloc[0])})"
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


def __generate_left_html(
    class_df: pd.DataFrame, use_relative_path: bool = False
) -> str:
    def get_image_path(student_id: str, use_relative_path: bool = False) -> str:
        img_folder = (
            "/" + IMAGE_FOLDER
            if use_relative_path
            else get_selenium_file_path(IMAGE_FOLDER)
        )
        return (
            f"{img_folder}/{student_id}.{IMAGE_EXTENSION}"
            if Path(f"{abs_image_folder}/{student_id}.{IMAGE_EXTENSION}").exists()
            else f"{img_folder}/student-not-found.jpg"
        )

    report_title = f"{SCHOOL_NAME} {__display_academic_year(class_df['academic_year'].iloc[0])} Class: {class_df['class'].iloc[0]}"
    doc = dominate.document(title=report_title)

    with doc.head:
        link(
            rel="stylesheet", href=f"{__get_css_path(use_relative_path)}/left-style.css"
        )

    with doc:
        h1(report_title)

        with div(cls="photo-grid"):
            for student in class_df.itertuples():
                with div(cls="student-unit"):
                    img(
                        src=get_image_path(student.student_id, use_relative_path),
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


def generate_htmls(
    student_df: pd.DataFrame,
    class_teacher_df: pd.DataFrame,
    generate_as_reference: bool = False,
) -> list[str]:
    """Generate report (in HTML format) from student and class teacher data.

    Args:
        student_df (pd.DataFrame): Student data from CSV file, in DataFrame format.
        class_teacher_df (pd.DataFrame): Class teacher data from CSV file, in DataFrame format.
        generate_as_reference (bool, optional): Generate HTML for reference or not (i.e. for converting into PDF). Defaults to False.

    Returns:
        list[str]: List of HTML file paths.
    """

    def write_html(path: str, html_str: str) -> None:
        with open(path, "w") as output_file:
            output_file.write(html_str)
            print(f"Write HTML: {path}")

    html_paths = []
    for klass in class_teacher_df["class"]:
        left_html_path = f"{HTML_FOLDER}/{klass}-left.html"
        write_html(
            path=left_html_path,
            html_str=__generate_left_html(
                class_df=student_df[student_df["class"] == klass],
                use_relative_path=generate_as_reference,
            ),
        )
        html_paths.append(left_html_path)

        right_html_path = f"{HTML_FOLDER}/{klass}-right.html"
        write_html(
            path=right_html_path,
            html_str=__generate_right_html(
                student_df=student_df[student_df["class"] == klass],
                teacher_df=class_teacher_df[class_teacher_df["class"] == klass],
                use_relative_path=generate_as_reference,
            ),
        )
        html_paths.append(right_html_path)

    return html_paths
