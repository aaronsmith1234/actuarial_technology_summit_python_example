from .data_sources import get_mortality_data
import pandas as pd


def determine_expected_benefit_for_one_person(
    age: int, gender: str, benefit_amt: int, mort_table: pd.DataFrame = None
):
    if mort_table is None:
        # load mortality tables
        male_mort = get_mortality_data(
            "male"
        )  # intentionally wrong, has multiple years in it......
        female_mort = get_mortality_data(
            "female"
        )  # intentionally wrong, has multiple years in it......

        if gender == "male":
            mortality_to_use = male_mort
        elif gender == "female":
            mortality_to_use = female_mort
        else:
            raise KeyError("No table exists for specified gender")
    else:
        mortality_to_use = mort_table

    mort_rate = mortality_to_use.loc[mortality_to_use["x"] == age, "q(x)"].item()
    expected_benefit = benefit_amt * mort_rate
    return expected_benefit
