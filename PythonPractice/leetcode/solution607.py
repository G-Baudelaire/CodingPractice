import pandas as pd


def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    selling_to_red = (
        orders.merge(company, on="com_id", how="left")
        .query("name == 'RED'")
        ["sales_id"]
        .unique()
    )

    return sales_person[~sales_person["sales_id"].isin(selling_to_red)][["name"]]
