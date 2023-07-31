import base64
import json

from config import abs_chrome_driver_folder
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.support.ui import WebDriverWait
from utils import get_selenium_file_path

webdriver_options = Options()
webdriver_prefs = {}

webdriver_options.add_argument("--headless")
webdriver_options.add_argument("--disable-gpu")
webdriver_options.add_argument("--no-sandbox")
webdriver_options.add_argument("--disable-dev-shm-usage")
webdriver_options.experimental_options["prefs"] = webdriver_prefs

webdriver_prefs["profile.default_content_settings"] = {"images": 2}


def html_to_pdf(html_path: str, pdf_path: str) -> None:
    """Converts HTML into PDF file.

    Args:
        html_path (str): The file path to the HTML file to be converted.
        pdf_path (str): The file path to store the PDF file.
    """
    with webdriver.Chrome(
        service=Service(abs_chrome_driver_folder), options=webdriver_options
    ) as driver:
        driver.get(get_selenium_file_path(html_path))
        TIMEOUT_SEC = 2
        try:
            WebDriverWait(driver, TIMEOUT_SEC).until(
                staleness_of(driver.find_element(by=By.TAG_NAME, value="html"))
            )
        except TimeoutException:
            calculated_print_options = {
                "landscape": False,
                "displayHeaderFooter": False,
                "printBackground": True,
                "preferCSSPageSize": True,
            }
            result = __send_devtools(
                driver, "Page.printToPDF", calculated_print_options
            )
            with open(pdf_path, "wb") as file:
                file.write(base64.b64decode(result["data"]))
                print(f"Converted: {html_path} -> {pdf_path}")


def __send_devtools(driver, cmd, params={}):
    resource = "/session/%s/chromium/send_command_and_get_result" % driver.session_id
    url = driver.command_executor._url + resource
    body = json.dumps({"cmd": cmd, "params": params})
    response = driver.command_executor._request("POST", url, body)

    if not response:
        raise Exception(response.get("value"))

    return response.get("value")
