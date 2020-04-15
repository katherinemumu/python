'''
katherinemumu
Apr 15 2020
This program will print to stderr
i dont really get this but okay maybe one day ill figure it out
'''

from __future__ import print_function
import sys

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

eprint("abc", "efg", "xyz", sep="--")