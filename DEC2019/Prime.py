'''
this program will ask the user to enter a number and will see if it is
prime or not
'''
def is_prime(n):
    if len(divisors(n)) == 2:
        return True
    else:
        return False

def divisors(num): 
    l = []
    for i in range (1, num+1):
        if num % i == 0:
            l.append(i)
    return l

n = int(input("Enter a number: "))

p = is_prime(n)

if p:
    print("The number is prime.")
else:
    print("The number is not prime.")
