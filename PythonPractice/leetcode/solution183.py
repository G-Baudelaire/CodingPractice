import pandas as pd


def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    mask = ~customers["id"].isin(orders["customerId"])
    return (
        customers[mask]
        [["name"]]
        .rename(columns={"name": "Customsers"})
        .reset_index(drop=True)
    )
