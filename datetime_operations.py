# strftime(format)

"""
    %a: abbreviation of the day of the week. For example, Wed - from the word Wednesday (English names are used by default)

    %A: full day of the week, e.g., Wednesday

    %b: abbreviation of the month. For example, Oct (short for October)

    %B: full month name, e.g., October

    %d: day of the month, followed by a zero, e.g., 01

    %m: month number followed by a zero, e.g., 05

    %y: year as a 2-digit number

    %Y: year as 4 numbers

    %H: hour in 24-hour format, e.g., 13

    %I: hour in 12-hour format, e.g., 01

    %M: minute

    %S: second

    %f: microsecond

    %p: pointer AM/PM

    %c: date and time formatted to the current locale

    %x: date formatted to current locale

    %X: time formatted to current locale
"""

from datetime import datetime
now = datetime.now()
print(now.strftime("%Y-%m-%d"))          # 2017-05-03
print(now.strftime("%d/%m/%Y"))          # 03/05/2017
print(now.strftime("%d/%m/%y"))          # 03/05/17
print(now.strftime("%d %B %Y (%A)"))     # 03 May 2017 (Wednesday)
print(now.strftime("%d/%m/%y %I:%M"))    # 03/05/17 01:36


from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, "")

now = datetime.now()
print(now.strftime("%d %B %Y (%A)"))     # 05 December 2022 (Monday)


# timedelta([days] [, seconds] [, microseconds] [, milliseconds] [, minutes] [, hours] [, weeks])

from datetime import timedelta

three_hours = timedelta(hours=3)
print(three_hours)
three_hours_thirty_minutes = timedelta(hours=3, minutes=30)

two_days = timedelta(2)

two_days_three_hours_thirty_minutes = timedelta(days=2, hours=3, minutes=30)


from datetime import timedelta, datetime

now = datetime.now()
till_ten_hours_fifteen_minutes = now - timedelta(hours=10, minutes=15)
print(till_ten_hours_fifteen_minutes)


"""
    timedelta:
    
    days - amount of days
    seconds - amout of seconds
    microseconds - amount of microseconds
    total_seconds() - total amount of time in seconds
"""

from datetime import timedelta, datetime

now = datetime.now()
twenty_two_may = datetime(2017, 5, 22)
period = twenty_two_may - now
print("{} days  {} seconds   {} microseconds".format(period.days, period.seconds, period.microseconds))

print("Total: {} seconds".format(period.total_seconds()))


# Date comparison

from datetime import datetime

now = datetime.now()
deadline = datetime(2017, 5, 22)
if now > deadline:
    print("Deadline has expired")
elif now.day == deadline.day and now.month == deadline.month and now.year == deadline.year:
    print("Deadline for the project today")
else:
    period = deadline - now
    print("{} days left".format(period.days))
