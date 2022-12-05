import datetime

# date(year, month, day)

yesterday = datetime.date(2021,12, 4)
print(yesterday)


from datetime import date

today = date.today()
print(today)
print("{}.{}.{}".format(today.day, today.month, today.year))


# time([hour] [, min] [, sec] [, microsec])

from datetime import time

current_time = time()
print(current_time)

current_time = time(16, 25)
print(current_time)

current_time = time(16, 25, 45)
print(current_time)


# datetime(year, month, day [, hour] [, min] [, sec] [, microsec])

from datetime import datetime

deadline = datetime(2017, 5, 10)
print(deadline)

deadline = datetime(2017, 5, 10, 4, 30)
print(deadline)


# Method now()

from datetime import datetime

now = datetime.now()
print(now)

print("{}.{}.{}  {}:{}".format(now.day, now.month, now.year, now.hour, now.minute))

print(now.date())
print(now.time())


# String to date
"""
strptime(str, format)

    %d: day as int
    %m: month's number
    %y: year as 2 digits
    %Y: year as 4 digits
    %H: hours 24 format
    %M: minute
    %S: second
"""

from datetime import datetime
deadline = datetime.strptime("22/05/2017", "%d/%m/%Y")
print(deadline)

deadline = datetime.strptime("22/05/2017 12:30", "%d/%m/%Y %H:%M")
print(deadline)

deadline = datetime.strptime("05-22-2017 12:30", "%m-%d-%Y %H:%M")
print(deadline)
