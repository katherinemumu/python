"""
katherinemumu
Apr 14 2020
Write a Python program to calculate number of days between two dates.
"""

import datetime as dt

date1 = dt.date(2014, 7, 2)
date2 = dt.date(2014, 7, 11)

diff = date2 - date1

print(diff)