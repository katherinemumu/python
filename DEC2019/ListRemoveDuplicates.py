'''
will remove duplicates from a list
'''

a = [1,1,1,3,5,6,7,8,8,8]

b = list(set(a))

print(b)

y = []

for i in a:
    if i not in y:
        y.append(i)

print(y)
