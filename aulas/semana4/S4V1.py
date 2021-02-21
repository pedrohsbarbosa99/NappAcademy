"""
* S4V1 - Módulo Datetime

"""

import datetime

hoje1 = datetime.datetime.today()

hoje1
datetime.datetime(2021, 2, 21, 15, 12, 16, 227582)

from datetime import datetime

hoje2 = datetime.today()

hoje2
datetime.datetime(2021, 2, 21, 15, 12, 49, 868)

from datetime import date


hoje3 = date.today()

hoje3
datetime.date(2021, 2, 21)

from datetime import datetime, date, time, timezone

d = date(2005, 7, 14)

d
datetime.date(2005, 7, 14)

str_data = "15/02/21 16:30"

dt = datetime.strptime(str_data, "%d/%m/%y %H:%M")

dt
datetime.datetime(2021, 2, 15, 16, 30)

dt.time()
datetime.time(16, 30)

dt.timetuple()
time.struct_time(tm_year=2021, tm_mon=2, tm_mday=15, tm_hour=16, tm_min=30, tm_sec=0, tm_wday=0, tm_yday=46, tm_isdst=-1)

from datetime import timedelta

delta = timedelta(days=50, seconds=27, microseconds=10, milliseconds=29000, minutes=5, hours=8, weeks=2)

delta
datetime.timedelta(days=64, seconds=29156, microseconds=10)

print(delta)
# 64 days, 8:05:56.000010

import time

today = date.today()

today == date.fromtimestamp(time.time())
True

today
datetime.date(2021, 2, 21)

my_birthday = date(today.year, 3, 30)

my_birthday
datetime.date(2021, 3, 30)

my_birthday = date(today.year, 3, 16)

my_birthday
datetime.date(2021, 3, 16)

if my_birthday < today:
    my_birthday = my_birthday.replace(year=today.year + 1)

my_birthday
datetime.date(2021, 3, 16)

time_to_birthday = abs(my_birthday - today)

time_to_birthday
datetime.timedelta(days=23)

dt1 = date(2014, 5, 12)

dt1
datetime.date(2014, 5, 12)

dt2 = date.today()

dt2 - dt1
datetime.timedelta(days=2477)

dif = dt2 - dt1

dif.days
2477