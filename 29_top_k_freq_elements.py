"""
Given an integer array nums and an integer k, return the k most frequent elements.
 You may return the answer in any order.
"""

nums = [1,1,1,2,2,3]
k = 2
counts={}

for i in nums:
    counts[i]=counts.get(i,0)+1

sorted_items=sorted(counts.items(),key=lambda item:item[1],reverse=True)

new=[num for num,val in sorted_items[:k]]

print(new)
