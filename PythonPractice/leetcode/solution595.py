import pandas as pd


def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    _big_countries = world[(world["area"] >= 3000000) | (world["population"] >= 25000000)]
    return _big_countries[["name", "population", "area"]]
