def is_leap_year(year):
    """
    This will take the year and analyze it if the inserted year is leap or not...
    Pd: this is a docstring and is used to describe a function behavior
    """
    if not year % 4 == 0:
        return False
    if not year % 100 == 0:
        return True
    if not year % 400 == 0:
        return False
    return True