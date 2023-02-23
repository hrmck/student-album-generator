import pandas as pd


def read_student_data(path: str) -> pd.DataFrame:
    """Reads student data from the given csv file. Extracts students' family name from column "name" and stores as "family_name".

    Args:
        path (str): The path pointing to the csv file containing student data.

    Returns:
        pd.DataFrame: The student data containing fields such as name, class, class_no. Please refer to README for detailed information.
    """
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
    """Reads class teacher data from the given csv file.

    Args:
        path (str): The path pointing to the csv file container class teacher data.

    Returns:
        pd.DataFrame: The class teacher data containing fields such as class and class teacher names. Please refer to README for detailed information.
    """
    try:
        return pd.read_csv(path, header=0)
    except FileNotFoundError:
        print(f"Cannot locate file {path}. Please check if the csv file exists.")
