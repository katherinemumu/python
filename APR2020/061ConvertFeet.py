'''
katherinemumu
Apr 18 2020
This program will convert an amount in feet to inches, yards and miles
'''

def feet(ft):
    d_inches = ft * 12
    d_yards = ft / 3.0
    d_miles = ft / 5280.0
    return (d_inches, d_yards, d_miles)

fet = int(input("Enter feet: "))
data = feet(fet)
print("The amount is %i feet." %data[0])
print("The amount is %.2f yards." %data[1])
print("The amount is %.2f miles." %data[2])