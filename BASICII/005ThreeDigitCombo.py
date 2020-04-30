'''
katherinemumu
Apr 28 2020
This program will print out all the combinations of 3 digits
'''

nums = []
for num in range(1000):
    num = str(num).zfill(3)
    print(num)
    nums.append(num)
print(nums)