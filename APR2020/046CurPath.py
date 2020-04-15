'''
katherinemumu
Apr 15 2020
This program will determine the current path and the name of the file that it is executing
'''

import os
print("Current File Name : ",os.path.realpath(__file__))