'''
katherinemumu
Apr 22 2020
This program will get system command output
'''
'''
import subprocess
# file and directory listing
returned_text = subprocess.check_output("dir", shell=True, universal_newlines=True)
print("dir command to list file and directory")
print(returned_text)
'''
print("hi")