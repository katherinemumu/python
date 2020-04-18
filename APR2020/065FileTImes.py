'''
katherinemumu
Apr 18 2020
This program will output the file modifications
'''

import os.path, time
print("Last modified: %s" % time.ctime(os.path.getmtime("abc.txt")))
print("Created: %s" % time.ctime(os.path.getctime("abc.txt")))

