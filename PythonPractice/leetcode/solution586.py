import pandas as pd


def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    return orders["customer_id"].mode().to_frame()
