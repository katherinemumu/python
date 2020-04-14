"""
katherinemumu
Apr 14 2020
This program will test whether a letter is a vowel or not
"""

def isVowel(a):
    s = "aeiou"
    if a in s:
        print("Yes! it is a vowel")
    else:
        print("No, it is not a vowel")

b = input("Enter a letter: ")
isVowel(b)
