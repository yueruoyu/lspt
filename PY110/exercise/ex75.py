# Some people believe that Fridays that fall on the 13th day of the month are unlucky days. Write a function that takes a year as an argument and returns the number of Friday the 13ths in that year. You may assume that the year is greater than 1752, which is when the United Kingdom adopted the modern Gregorian Calendar. You may also assume that the same calendar will remain in use for the foreseeable future.

# ExamplesCopy Code

import datetime

def friday_the_13ths(year):
    count = 0
    for month in range(1, 13):
        if datetime.date(year, month, 13).weekday() == 4:
            count += 1
    return count




print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True
# Hint 1: Helper Module
# Use the datetime.date function to determine whether the 13th of a given month falls on a Friday.
