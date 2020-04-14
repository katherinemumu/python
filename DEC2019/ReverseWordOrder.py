'''
this program will take a string with spaces in btwn them and will reverse
the order
'''

s = 'hi this is apple'

l = s.split(' ')
l.reverse()

s = ' '.join(l)

print(s)
