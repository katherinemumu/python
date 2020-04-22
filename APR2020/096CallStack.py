'''
katherinemumu
Apr 21 2020
This program will print out the call stack
'''

import traceback
print()
def f1():return abc()
def abc():traceback.print_stack()
f1()
print()