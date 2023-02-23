from pathlib import Path


def get_selenium_file_path(path: str) -> str:
    """Converts the given file path into Selenium-compatible path.

    Args:
        path (str): The file path to convert

    Returns:
        str: The file path that can be read by Selenium.
    """

    return f"file:///{Path.cwd()}/{path}"
