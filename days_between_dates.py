def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        return year, month, day + 1
    elif month < 12:
        return year, month + 1, 1
    else:
        return year + 1, 1, 1

nextDay(2019,12,29)

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    if year1 > year2:
        return 0
    if year1 == year2 and (month1 > month2):
        return 0
    elif (year1 == year2) and (month1 == month2) and (day1 >= day2):
        return 0
    else:
        return 1


dateIsBefore(2019,4,23,2019,4,23)

def daysBetweenDates(year1, month1, day1, year2, month2, day2):

    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while(dateIsBefore(year1, month1, day1, year2, month2, day2)):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1

    return days

daysBetweenDates(2019, 6, 30, 2019, 6, 29)

def isLeapYear(year):
    if (year % 400) == 0:
        return True
    elif (year % 100) == 0:
        return False
    elif (year % 4) == 0:
        return True
    else: 
        return False

isLeapYear(1800)

def daysInMonth(year, month):
    if isLeapYear(year) and month == 2:
        days = 29
    elif month in [1, 3, 5, 7, 8, 10, 12]:    
        days = 31
    elif month in [4, 6, 9, 11]:
        days = 30
    else: 
        days = 28

    return days


daysInMonth(2004, 5)

def test():
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 1) == 0
    assert daysBetweenDates(2013, 1, 1, 2013, 1, 2) == 1
    assert nextDay(2013, 1, 1) == (2013, 1, 2)
    print('test finished')

test()