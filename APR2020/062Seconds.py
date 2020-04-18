'''
katherinemumu
Apr 18 2020
This program will convert days, hours, minutes, seconds into seconds
'''

days = int(input("Enter days: ")) * 3600 * 24
hours = int(input("Enter hours: ")) * 3600
minutes = int(input("Enter minutes: ")) * 60
seconds = int(input("Enter seconds: ")) 

total = days + hours + minutes + seconds

print("The total number of seconds is %i" %total)