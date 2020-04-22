'''
katherinemumu
Apr 22 2020
This program will print the name of the host on which the routine is running
'''

import socket

host_name = socket.gethostname()

print("Host name:", host_name)
