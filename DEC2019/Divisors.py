'''
this program is going to ask a user for a number and is then going to print
all the positive divisors of that number
'''

num = int(input("Enter a number: "))
l = []

for i in range (1, num+1):
    if num % i == 0:
        l.append(i)

print("The list of all the positive divisors of", num, "are", l)
    
