'''
katherinemumu
May 25 2020
This program will print out all the permutations of a list of numbers
'''

nums = [1, 2, 3]
results = [[]]

def permute(nums):
    result_perms = [[]]
    for n in nums:
        new_perms = []
        for perm in result_perms:
            for i in range(len(perm)+1):
                new_perms.append(perm[:i] + [n] + perm[i:])
                result_perms = new_perms
    return result_perms

results = permute(nums)
print(results)