from pathlib import Path
from typing import Final

SCHOOL_NAME = "School Name Here"
HTML_FOLDER = "html-report"
IMAGE_FOLDER = "img"
CSS_FOLDER = "css"
CHROME_DRIVER_FOLDER = "chromedriver"
SCHOOL_BADGE_IMAGE_NAME = "school-badge.jpeg"
IMAGE_EXTENSION = "jpeg"

abs_image_folder: Final = f"{Path.cwd()}/{IMAGE_FOLDER}"
abs_css_folder: Final = f"{Path.cwd()}/{CSS_FOLDER}"
abs_chrome_driver_folder: Final = f"{Path.cwd()}/{CHROME_DRIVER_FOLDER}"
