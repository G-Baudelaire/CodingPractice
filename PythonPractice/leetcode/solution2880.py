import pandas as pd


def selectData(students: pd.DataFrame) -> pd.DataFrame:
    mask = students["student_id"] == 101
    return students.loc[mask, ["name", "age"]]