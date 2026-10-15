import pandas as pd


def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    mask = patients["conditions"].str.contains(r"(^|\s)DIAB1\w*")
    return patients[mask]