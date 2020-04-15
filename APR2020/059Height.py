'''
katherinemumu
Apr 15 2020
This program will convert height from feet and inches to centimetres
'''

print("Enter your height:")
feet = int(input("Enter feet: "))
inches = int(input("Enter inches: "))

inches += feet * 12

height_cm = round(inches * 2.54, 1)

print("Your height is %d cm"%height_cm)