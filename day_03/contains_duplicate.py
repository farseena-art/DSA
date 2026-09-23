"""
Given an integer array nums,
return true if any value appears at least twice in the array,
and return false if every element is distinct.

"""

nums = [1,2,3,1]

if len(nums) != len(set(nums)):

    print(True)

else: 

    print(False)    