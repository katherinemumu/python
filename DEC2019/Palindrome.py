'''
this program will produce a string and will see if it is a palindrome
'''

s = input("Enter a string: ")
yes = True

for i in range(len(s)):
    if yes:
        yes = s[i] == s[-i-1]

print(yes)
        
