"""
Given an integer array nums, 
move all 0's to the end of it while maintaining the relative order of the non-zero elements.

"""


nums = [0,1,0,3,12]

n = len(nums)

for i in range(n):

    if 0 in nums:

        nums.append(nums.pop(nums.index(0)))

print(nums)        








# non_zeros = []

# for num in nums:

#     if num[0]!=0:

#         non_zeros.append(num)