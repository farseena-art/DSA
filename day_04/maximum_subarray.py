"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.

"""

nums = [5,4,-1,7,8]

cur_sum = 0

max_sum = nums[0]

num = len(nums)

for i in range(num):

    cur_sum += nums[i]

    max_sum = max(max_sum,cur_sum)

    if cur_sum < 0:

        cur_sum = 0

print(max_sum)