'''
katherinemumu
Apr 22 2020
This program will print the contents of a URL to the console
'''

from http.client import HTTPConnection

conn = HTTPConnection("example.com")
conn.request("GET", "/")  
result = conn.getresponse()
# retrieves the entire contents.  
contents = result.read() 
print(contents)
