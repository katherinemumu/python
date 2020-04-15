'''
katherinemumu
Apr 15 2020
This program will check whether a file exists
'''

import os.path

open("abc.txt", "w")
print(os.path.isfile("abc.txt"))