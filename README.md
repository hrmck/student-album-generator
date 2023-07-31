# Student Album Generator
A Python program to generate student photo album and name list.

## Prerequisite

You will need the following:
- Python 3.9.X for running this Python project
- [Poetry](https://python-poetry.org/docs/) for installing required Python modules
- [Selenium Chrome Webdriver](https://chromedriver.chromium.org/downloads) for converting HTML files into PDF files

If you are using Ubuntu, you can refer to [this tutorial](https://cloudbytes.dev/snippets/run-selenium-and-chrome-on-wsl2) on installing Poetry and Selenium Chrome Webdriver.

### On installing Selenium Chrome Webdriver

1. Figure which architecture your computer is (useful for determining which file to download in step 3)
2. Figure which Chrome version the browser is using ([video tutorial for how](https://youtu.be/Xjv1sY630Uc?t=308))
3. Download the zip file, place it in the project root directory (win32 -> Windows, linux64 -> Linux-based, not sure for Mac)
4. Unzip the file, the directory should look like this:
```
(project root)
├── chromedriver
│   └── stable
│       ├── chromedriver
│       └── LICENSE.chromedriver
├── css
├── csv
├── html-report
└── ...
```
(The above diagram is generated using: https://tree.nathanfriend.io/)

## Installation

Clone this repository, then move to project root directory, and install dependencies.

```
git clone https://github.com/hrmck/student-album-generator.git
cd student_album_generator
poetry install
```
## Data Preparation

The following data is needed:
1. Photos that are named by "student ID.jpeg" (e.g. s123456.jpeg)
2. A CSV file containing student data of all classes
3. A CSV file containing class teacher data of all classes

Please store the photos into `img` folder, and CSV files into `csv` folder.
After storing the csv files, edit STUDENT_CSV and CLASS_TEACHER_CSV values in `student_album_generator\run.py` to allow the program choosing the csv files.

### Notes on photos
It is assumed that the images are in jpeg format, with a dimension of 300x400.
The image extension can be edited from IMAGE_EXTENSION in `student_album_generator\config.py` file.
As long as the aspect ratio stays 3:4, the css files should work and don't break the formatting. 

### Examples

The below are excerpts from the csv files created for testing, showing how the data should look like.

#### Student Data (in CSV format)
```csv
academic_year,student_id,name,chi_name,christian_name,class,class_no,primary_school,house
2023,s120000,Au Hoi Ching,區凱晴,Amelia,1A,1,ABC Primary School,K
2023,s120001,Au Lok Ching,區樂晴,Amy,1A,2,ABC Primary School,L
2023,s120002,Au Hiu Ching,區曉晴,Aurora,1A,3,ABC Primary School,T
2023,s120003,Au Tsz Ching Addison,區芷晴,,1A,4,ABC Primary School,C
2023,s120004,Chan Hoi Ching,陳凱晴,Adele,1A,5,BCD Primary School,L
2023,s120005,Chan Lok Ching,陳樂晴,Ashley,1A,6,BCD Primary School,C
2023,s120006,Chan Hiu Ching,陳曉晴,Alice,1A,7,BCD Primary School,K
2023,s120007,Chan Tsz Ching,陳芷晴,Athena,1A,8,BCD Primary School,T
```
#### Class Teacher Data (in CSV format)
```csv
academic_year,class,class_teacher_1,class_teacher_2
2023,1A,Chris WONG,Christina WANG
2023,1B,Peter CHAN,Matthew CHEUNG
2023,1C,Beatrice YIP,Mace YAN
2023,1D,Amy CHIU,Charlie HO
2023,1E,Dora YEUNG,Brinley TSANG
```
## Run

```
# Linux
poetry run python3 student_album_generator/run.py

# Windows
poetry run py student_album_generator/run.py
```

Check the results from `pdf` folder!
