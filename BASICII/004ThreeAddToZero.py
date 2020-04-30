'''
katherinemumu
Apr 28 2020
This program will find a unique triplet of numbers that add to zero
'''

def all_diff(a, b, c):
    '''
    Returns true if a, b, and c are not all the same
    and false otherwise
    '''
    return a != b and a != c and b != c

def three_sum(nums):
    result = []
    nums.sort()
    for i in range(len(nums)):
        l = i + 1
        r = len(nums) - 1
        
        while(l < r):
            sum = nums[i] + nums[l] + nums[r]
            if (sum == 0 and all_diff(nums[i], nums[l], nums[r])):
                result.append((nums[i], nums[l], nums[r]))
                break
            elif (sum < 0):
                l += 1
            else:
                r -= 1
    return result
            
x = [0, 0, 0, 1, -6, 4, 2, -1, 2, 0, -2, 0 ]
y = [5, -2, -3, 1, 1, 0, -10, 6, 4, -1]
print(three_sum(x))
print(three_sum(y))