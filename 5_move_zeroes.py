"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order
 of the non-zero elements.

Note that you must do this in-place without making a copy of the array.
"""

nums = [0,1,0,3,12,13,0,56,4,5,0]
for i in nums:
    if i==0:
        nums.remove(i)
        nums.append(i)

print(nums)