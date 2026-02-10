def leap_year(year):
    leap = False

    if year > 0:
        if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
            leap = True
        elif year % 4 == 0 and year % 100 == 0 and year % 400 != 0:
            leap = False
        elif year % 4 == 0 and year % 100 != 0:
            leap = True
        elif year % 4 != 0:
            leap = False
    else:
        raise ValueError('Does not exist negative years')
    return leap