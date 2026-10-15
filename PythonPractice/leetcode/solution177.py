import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N <= 0:
        return pd.DataFrame({f"getNthHighestSalary({N})": [None]})

    sorted_salaries = (
        employee
        .drop_duplicates(subset=["salary"])
        .sort_values("salary", ascending=False)
        .reset_index()
    )

    if len(sorted_salaries) < N:
        result = None
    else:
        result = sorted_salaries.loc[N - 1, "salary"]

    return pd.DataFrame({f"getNthHighestSalary({N})": [result]})