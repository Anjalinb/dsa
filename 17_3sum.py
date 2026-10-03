"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j,
 i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.
"""
nums = [-1,0,1,2,-1,-4]
lst=[]


for i in range(0,len(nums)-2):
    for j in range(i+1,len(nums)-1):
        for k in range(j+1,len(nums)):
            if nums[i]+nums[j]+nums[k]==0:
                triplet=sorted([nums[i],nums[j],nums[k]])
                if triplet not in lst:
                    lst.append([nums[i],nums[j],nums[k]])
        
            

print(lst)