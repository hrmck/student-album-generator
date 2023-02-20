from config import IMAGE_FOLDER, abs_image_folder, CSS_FOLDER, abs_css_folder


def get_css_path(use_relative_path: bool = False) -> str:
    return "/" + CSS_FOLDER if use_relative_path else abs_css_folder
