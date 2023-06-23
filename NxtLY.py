from calendar import isleap
from itertools import count, islice

def leep_years_from(year, amount=10):
    return islice((y for y in count(year) if isleap(y)), amount)

for leap_year in leep_years_from(2023):
    print("{} is a leap year".format(leap_year))