'''
katherinemumu
Apr 24 2020
This program will input a number, and will display an error if it is not a number
'''

ok = True

while ok:
    try:
        n = int(input("Enter a number: "))
        print("thanks for entering a number")
        ok = False
    except ValueError:
        print("not a number.")

