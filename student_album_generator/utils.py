from config import IMAGE_FOLDER, export_image_folder, CSS_FOLDER, export_css_folder


def get_css_path(use_relative_path: bool = False) -> str:
    return "/" + CSS_FOLDER if use_relative_path else export_css_folder


def display_academic_year(year: str) -> str:
    return f"{year}-{int(year) + 1}"
