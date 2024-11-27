import pandas as pd


def get_mortality_data(gender: str) -> pd.DataFrame:
    """Load mortality table from public URL and return dataframe."""
    if gender.lower() == "male":
        gender_code = "M"
    elif gender.lower() == "female":
        gender_code = "F"
    else:
        raise KeyError("You've entered a gender for which there is no table")

    # https://www.ssa.gov/oact/HistEst/PerLifeTables/2017/PerLifeTables2017.html
    return pd.read_csv(
        f"https://www.ssa.gov/oact/HistEst/PerLifeTables/2017/PerLifeTables_{gender_code}_Hist_TR2017.csv",
        skiprows=4,
    )
