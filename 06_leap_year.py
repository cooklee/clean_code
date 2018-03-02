def get_numbers_of_days_in_february(year):
    # Check if year is leap-year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return 28
    return 27