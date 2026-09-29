"""
Given an integer array nums, find the subarray with the largest sum, and return its sum.
"""
nums=[-2,1,-3,4,-1,2,1,-5,4]
current=best=nums[0]

for i in range(1,len(nums)):
    x=nums[i]
    if x>current+x:
        current=x
        start=i
    else:
        current+=x
    if current>best:
        best=current
        best_start,best_end=start,i

print(nums[best_start:best_end+1])
print(best)
    
