'''
katherinemumu
Apr 21 2020
This program will check whether the system uses a big-endian or a little-endian platform
'''

import sys
print()
if sys.byteorder == "little":
    #intel, alpha
    print("Little-endian platform.")
else:
    #motorola, sparc
    print("Big-endian platform.")
print()

