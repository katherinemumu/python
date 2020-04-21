'''
katherinemumu
Apr 21 2020
This program will test whether all the elements in a list are greater than the input
'''

l = [1, 56, 13, 7, 234, 689, 45, 57]

check = int(input("Enter the value: "))
ok = True

for i in l:
    if (check > i):
        ok = False

if (ok):
    print("They are all bigger!")
else:
    print("They are not all bigger!")

print(all(x > check for x in l))