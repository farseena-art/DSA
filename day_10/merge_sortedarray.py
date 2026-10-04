"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 

and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

"""

nums1 = [1,2,3,0,0,0]

m = 3

nums2 = [2,5,6] 

n = 3

n = len(nums1) - m

for i in range(n):

    nums1.pop()

nums1.extend(nums2)

nums1.sort()

print(nums1)

