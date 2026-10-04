"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value.
 Any answer with a calculation error less than 10-5 will be accepted.
"""
nums = [1,12,-5,-6,50,3]
k = 4
l=0
r=k-1
average=float('-inf')
while r<len(nums):
    calc=sum(nums[l:r+1])/k
    if calc>average:
        average=calc
    l+=1
    r+=1

print(average)

