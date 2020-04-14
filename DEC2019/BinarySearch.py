'''
this program will do binary search!!
'''
l = [1,3,19,25,123,1234]

print(l)
x = int(input("Enter something you want to search for: "))

bottom = 0
top = len(l) - 1
found = False

while (not found and bottom <= top):
    middle = (bottom + top) // 2
    if x == l[middle]:
        found = True
        print("The index is", middle)
    elif x > l[middle]:
        bottom = middle + 1
    else:
        top = middle - 1

if not found:
    print("The element is not in the list.")
