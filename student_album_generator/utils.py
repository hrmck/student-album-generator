from config import CSS_FOLDER
from pathlib import Path


def get_css_path(use_relative_path: bool = False) -> str:
    return "/" + CSS_FOLDER if use_relative_path else get_selenium_file_path(CSS_FOLDER)


def get_filename_wo_extension(path: str) -> str:
    return Path(path).stem


def get_selenium_file_path(path: str) -> str:
    return f"file:///{Path.cwd()}/{path}"


def display_academic_year(year: str) -> str:
    return f"{year}-{int(year) + 1}"
