from pathlib import Path
from typing import Final

SCHOOL_NAME = "Holy Trinity College"
HTML_FOLDER = "html-report"
IMAGE_FOLDER = "img"
CSS_FOLDER = "css"

abs_image_folder: Final = f"{Path.cwd()}/{IMAGE_FOLDER}"
abs_css_folder: Final = f"{Path.cwd()}/{CSS_FOLDER}"
