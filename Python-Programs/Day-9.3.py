def is_leap_year(year):
    """
    Determine if a given year is a leap year.

    A year is a leap year if it is divisible by 4, except for years which are both divisible by 100 and not divisible by 400.
    
    Args:
    year (int): The year to check.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


def days_in_month(year, month):
    """
    Calculate the number of days in a given month of a specific year.

    Takes into account leap years for the month of February.

    Args:
    year (int): The year.
    month (int): The month (1-12).

    Returns:
    int: The number of days in the month.
    """
    # List of days in each month for a non-leap year
    days_in_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # If it's a leap year and the month is February, return 29 days
    if is_leap_year(year) and month == 2:
        return 29
    else:
        return days_in_list[month - 1]


# Prompt the user to input a year
year = int(input("Enter a year: "))

# Prompt the user to input a month
month = int(input("Enter a month: "))

# Calculate the number of days in the specified month and year
days = days_in_month(year, month)

# Output the result to the user
print(f"The number of days in month {month} of year {year} is: {days}")
