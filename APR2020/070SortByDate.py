'''
katherinemumu
Apr 21 2020
This program will sort files by date
'''

import glob
import os

files = glob.glob("*.txt")
files.sort(key=os.path.getmtime)
print("\n".join(files))