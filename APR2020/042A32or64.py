'''
katherinemumu
Apr 15 2020
This program will determine whether the Python shell is executing 32 or 64 bit
'''

import struct
print(struct.calcsize("P") * 8)