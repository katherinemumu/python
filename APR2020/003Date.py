"""
katherinemumu
Apr 13 2020
This program prints out today's date
"""

import datetime
import sys
print(sys.version)

print("Current date: ")
now = datetime.datetime.now()
print(now.strftime("%Y/%m/%d %H:%M:%S"))

