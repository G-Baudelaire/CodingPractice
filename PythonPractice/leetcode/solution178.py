import pandas as pd


def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    sorted_df = (
        employee
        .drop_duplicates(subset=["salary"])
        .sort_values("salary", ascending=False)
        .reset_index(drop=True)
    )

    if len(sorted_df) < 2:
        result = None
    else:
        result = sorted_df.loc[1, "salary"]

    return pd.DataFrame({"SecondHighestSalary": [result]})