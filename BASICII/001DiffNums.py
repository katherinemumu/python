'''
katherinemumu
Apr 27 2020
This program will determine whether all the numbers are the same in a list
'''

def same(l):
    a = set(l)
    if (len(a) == len(l)):
        return True
    else:
        return False

def main():
    print(same([1, 2, 3]))
    print(same([1, 1, 2]))

if __name__ == '__main__': main()