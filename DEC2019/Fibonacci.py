'''
this program will take in a number and generate the fibonnaci sequence for
that number
'''

n = int(input("Enter a number: "))

def fib (n):
    l = []
    for i in range(1,n+1):
        if i == 1:
            l.append(1)
        elif i == 2:
            l.append(1)
        else:
            l.append(l[i-2] + l[i-3])
    return l

print("The fin seq for", n, "is", fib(n))
        
