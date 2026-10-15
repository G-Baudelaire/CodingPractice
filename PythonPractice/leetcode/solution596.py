import pandas as pd


def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    df = courses.value_counts(subset=["class"]).reset_index()
    return df[df["count"] >= 5][["class"]]
