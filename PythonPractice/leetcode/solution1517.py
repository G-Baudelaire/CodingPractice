import pandas as pd


def valid_emails(users: pd.DataFrame) -> pd.DataFrame:
    mask = users["mail"].str.match(r"[a-Z][a-Z0-9\_\.\-]*\@leetcode\.com")
    return users[mask]