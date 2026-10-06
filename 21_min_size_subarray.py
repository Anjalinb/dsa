"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray
 whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.
"""
target = 7
nums = [1,2,3,4,5]
length=len(nums)
status=False
for i in range(length+1):
    l=0
    r=i+1
    while(r<=length):
        if sum(nums[l:r])>=target:
            print(len(nums[l:r]))
            status=True
            break
        else:
            l+=1
            r+=1
    if status==True:
        break

if status==False:
    print("0")





