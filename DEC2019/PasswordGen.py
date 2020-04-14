'''
this is a password generator
'''

import random

lower = list('abcdefghijklmnopqrstuvwxyz')
upper = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
digit = list('1234567890')
symbol = list('!@#$%^&*()_=+/.,<>~`')
words = ['apple','banda','chip','dance','elit','france','grain','hi','ice',
         'jam','kitkat','lays','mom','nano','orange','pie','queen','race',
         'sun','tea','uni','verse','woman','xanny','yell','zoo']

length = random.randint(8,16)

x = int(input("Hi, do you want your password to be (1) strong or (2) weak?: " ))

if x == 2:
    password = random.choice(words) + random.choice(words)
elif x == 1:
    password = random.choice(words)
    for i in range (len(password), length):
        y = random.randint(1,4)
        if y == 1:
            password += random.choice(lower)
        elif y == 2:
            password += random.choice(upper)
        elif y == 3:
            password += random.choice(digit)
        else:
            password += random.choice(symbol)

print("Your password is", password)
    
