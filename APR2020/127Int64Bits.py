'''
katherinemumu
Apr 25 2020
This program will check whether an integer will fit in 64 bits
'''

int_val = 30
if int_val.bit_length() <= 63:
    print((-2 ** 63).bit_length())
    print((2 ** 63).bit_length())