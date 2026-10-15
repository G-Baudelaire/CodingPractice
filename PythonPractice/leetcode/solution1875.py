import pandas as pd


def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    mask = (employees["employee_id"] % 2 == 1) & (employees["name"].str.startswith("M"))
    output = employees[["employee_id"]]
    output["bonus"] = employees["salary"].where(mask, 0)
    return output.sort_values("employee_id", ascending=True)
