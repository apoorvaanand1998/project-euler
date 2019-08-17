#############################################################################################################
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)? #
#############################################################################################################

month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
day = 1
counter = 0

for year in range(1900, 2001):
    month_days[1] = 29 if ((year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)) else 28
    for month in range(12):
        for date in range(1, month_days[month]+1):
            if day > 7:
                day = 1
            if day == 7 and date == 1:
                counter += 1
            day += 1

print(counter - 2)  ## Subtracted by 2 because year 1900 has 2 months where 1st of month is a Sunday
