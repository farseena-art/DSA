""" Leetcode - 136

Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

"""

nums = [4,1,2,1,2]

result = 0

for num in nums:

    result ^= num

print(result)    