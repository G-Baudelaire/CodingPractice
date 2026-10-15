import pandas as pd


def categorize_products(activities: pd.DataFrame) -> pd.DataFrame:
    return (
        activities.drop_duplicates()
        .sort_values(["sell_date", "product"])
        .groupby("sell_date")
        .agg(
            num_sold=("product", "nunique"),
            products=("product", lambda product: ",".join(product))
        )
        .reset_index()
    )
