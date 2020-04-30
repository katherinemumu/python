'''
katherinemumu
Apr 29 2020
This program will count the number of each character in a string
'''

def countchar(s):
    lst = list(s)
    lst = list(set(s))
    lst.sort()
    count_char = []
    for i in lst:
        count_char.append(s.count(i))
    return list(zip(lst, count_char))

def countcharfile(filename):
    infile = open(filename, "rt")
    s = ""
    for line in infile:
        s += line.rstrip()
    return countchar(s)

def main():
    # print(countchar("aaabbbc"))
    print(countcharfile("simple.txt"))

if __name__ == '__main__': main()