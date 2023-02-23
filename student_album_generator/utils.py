from pathlib import Path


def get_selenium_file_path(path: str) -> str:
    return f"file:///{Path.cwd()}/{path}"
