"""
Given an integer array nums sorted in non-decreasing order,
 remove the duplicates in-place such that each unique element appears only once.
   The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates,
 return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order.
 The remaining elements beyond index k - 1 can be ignored.
"""
# nums=[0,0,1,1,1,2,2,3,3,4]
# nums_set=set(nums)
# j=0
# for i in nums_set:
#     nums.insert(j,i)
#     j+=1

# print(len(nums_set),",nums=",nums)

"CRCT METHOD"
nums=[0,0,1,1,1,2,2,3,3,4]
if not nums:
    print("0")
l=0

for r in range(1,len(nums)):
    if nums[l]!=nums[r]:
        l+=1
        nums[l]=nums[r]

print(l+1,nums[:l+1])


