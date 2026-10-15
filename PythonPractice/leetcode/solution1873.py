import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    mask = (employees["employee_id"] % 2 == 0) | (employees["name"].str.startswith("M"))
    df = (
        employees
        .assign(bonus=employees.where(~mask, 0))
        [["employee_id", "bonus"]]
        .sort_values("employee_id")
        .reset_index(drop=True)
    )
    return df
