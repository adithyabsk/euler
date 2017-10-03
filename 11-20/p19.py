#!/usr/bin/env python

# 1 Jan 1900 was a Monday.
# 
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# 
# A leap year occurs on any year evenly divisible by 4, 
# but not on a century unless it is divisible by 400.

from datetime import date, timedelta

d1 = date(1901, 1, 1)
d2 = date(2000, 12, 31)

delta = d2 - d1

days = [d1 + timedelta(days=i) for i in range(delta.days + 1)]
sundays = [1 for d in days if d.day == 1 and d.weekday() == 6]

print sum(sundays)