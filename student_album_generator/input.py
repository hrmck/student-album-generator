import pandas as pd


def read_student_data(path: str) -> pd.DataFrame:
    try:
        student_df = pd.read_csv(path, header=0)
        # some students don't have christian name
        student_df["christian_name"].fillna("", inplace=True)
        # extract first word from name as family name
        student_df["family_name"] = student_df.apply(
            lambda row: str.split(row["name"], maxsplit=1)[0], axis=1
        )
        return student_df
    except FileNotFoundError:
        print(f"Cannot locate file {path}. Please check if the csv file exists.")


def read_class_teacher_data(path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(path, header=0)
    except FileNotFoundError:
        print(f"Cannot locate file {path}. Please check if the csv file exists.")
