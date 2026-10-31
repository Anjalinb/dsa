"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the
 very left of the array to the very right. You can only see the k numbers in the window.
   Each time the sliding window moves right by one position.

Return the max sliding window.
"""


def slide_max(nums,k):
    l=0
    r=k
    max_lst=[]

    for i in range(len(nums)-k+1):
        sublist=nums[l:r]
        max_lst.append(max(sublist))
        l+=1
        r+=1

    print(max_lst)

slide_max([1,3,-1,-3,5,3,6,7],3)