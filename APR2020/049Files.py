'''
katherinemumu
Apr 15 2020
This program will list out the files in a directory
'''

from os import listdir
from os.path import isfile, join
files_list = [f for f in listdir('/home') if isfile(join('/home', f))]
print(files_list); 
