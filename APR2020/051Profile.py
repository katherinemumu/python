'''
katherinemumu
Apr 15 2020
This program will determine the profiling of python programs
A profile is a set of statistics that describes how often and for how 
    long various parts of the program executed. 
    These statistics can be formatted into reports via the pstats module
'''

import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')



