import example_package as pkg


def test_male_age_65_2014_table():
    gender = "male"
    benefit_amt = 1000
    age = 65
    year = 2014
    all_tables = pkg.get_mortality_data(gender)
    data_2014 = all_tables.loc[all_tables["Year"] == year]
    result = pkg.determine_expected_benefit_for_one_person(
        age, gender, benefit_amt, data_2014
    )
    assert result == (0.015826 * benefit_amt)


def test_female_age_35_2012_table():
    gender = "female"
    benefit_amt = 1000
    age = 35
    year = 2012
    all_tables = pkg.get_mortality_data(gender)
    data_2014 = all_tables.loc[all_tables["Year"] == year]
    result = pkg.determine_expected_benefit_for_one_person(
        age, gender, benefit_amt, data_2014
    )
    assert result == (0.000883 * benefit_amt)
