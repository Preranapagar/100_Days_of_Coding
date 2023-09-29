#use of datetime module

from datetime import datetime
from datetime import date
from datetime import timedelta

Today = datetime.today()
print("Today :", Today)
print(type(Today))

Today_date = date.today()
print("Today's date :", Today_date)
print(type(Today_date))

print("Month :", Today_date.month)
print("Year :", Today_date.year)
print("Day :", Today_date.day)

Chritsmas = date(Today_date.year, 12, 25)
print("Chritsmas Day :", Chritsmas)

#number of days remain for Chritsmas

days_to_christmas = (Chritsmas - Today_date).days

print("Number of days for Chritsmas :", days_to_christmas)

eta = timedelta(days = 2, hours = 3)
print(Today)
result = Today + eta
print(result)