import pandas as pd


def get_mortality_data(gender: str) -> pd.DataFrame:
    if gender.lower() == "male":
        table_id = "M"
    elif gender.lower() == "female":
        table_id = "F"
    else:
        raise KeyError("You've entered a gender for which there is no table")

    # https://www.ssa.gov/oact/HistEst/PerLifeTables/2017/PerLifeTables2017.html
    return pd.read_csv(
        f"https://www.ssa.gov/oact/HistEst/PerLifeTables/2017/PerLifeTables_{table_id}_Hist_TR2017.csv",
        skiprows=4,
    )
