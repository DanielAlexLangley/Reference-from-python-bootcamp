
# DOCSTRING:
# add a note about your own function
# must be below the def line
# docstrings can be as many lines as we want

def is_leap(year):
    """Check if year is
    leap year or not"""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    """This is a docstring."""
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    return month_days[month - 1]


year_ = int(input("Enter a year: "))
month_ = int(input("Enter a month: "))
days = days_in_month(year_, month_)
print(days)
