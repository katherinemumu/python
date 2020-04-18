'''
katherinemumu
Apr 18 2020
This program will find the file path
'''

def absolute_file_path(path_fname):
        import os
        return os.path.abspath('path_fname')        
print("Absolute file path: ",absolute_file_path("abc.txt"))