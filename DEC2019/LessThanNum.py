l = [1,7,6,123,78,345,9234,97,257]
print(l)

num = int(input("Enter a number to find all the numbers less than that in the list! "))
new_l = []

for i in range(len(l)):
    if l[i] < num:
        new_l.append(l[i])

print("This is a new list where all the elements are less than", num, new_l)
