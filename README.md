# Student Album Generator
A Python program to generate student photo album and name list.

## Prerequisite

You will need the following:
- [Poetry](https://python-poetry.org/docs/) for installing required Python modules
- [Selenium Chrome Webdriver](https://chromedriver.chromium.org/downloads) for converting HTML files into PDF files

If you are using Ubuntu, you can refer to [this tutorial](https://cloudbytes.dev/snippets/run-selenium-and-chrome-on-wsl2).
 
## Installation

Clone this repository, move to project root directory, install dependencies

```
git clone https://github.com/hrmck/student-album-generator.git
cd student_album_generator
poetry install
```
## Data Preparation

The following data is needed:
1. Photos that are named by "student ID.jpg" (e.g. s123456.jpg)
2. A CSV file containing student data
3. A CSV file containing class teacher data

Please store the photos into `img` folder, and CSV files into `csv` folder.

TODO: Provide sample data for csv files

## Execution

```
poetry run python3 student_album_generator/run.py
```

Then check the results from `pdf` folder!
