'''
katherinemumu
May 25 2020
This program will print out all the possibilities of a 2 digit string given a map of strings (??)
'''

string_maps = {
"1": "abc",
"2": "def",
"3": "ghi",
"4": "jkl",
"5": "mno",
"6": "pqrs",
"7": "tuv",
"8": "wxy",
"9": "z"
}

def lettercombo(digits):
    first = string_maps[digits[0]]
    second = string_maps[digits[1]]
    result = []
    for f in first:
        for s in second:
            result.append(f+s)
    return result

print(lettercombo('29'))
print(lettercombo('47'))