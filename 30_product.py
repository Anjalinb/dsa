"""
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all
 the elements of nums except nums[i].

 Time complexity=o(n)
"""

nums = [1,2,3,4]
ans=[]

for i in nums:
    product=1
    for j in range(len(nums)):
        if i==nums[j]:
            continue
        else:
            product*=nums[j]
    ans.append(product)

print(ans)



