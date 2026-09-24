"""
Given a non-empty array of integers nums,
 every element appears twice except for one. Find that single one.
"""
nums = [4,1,2,1,2]
result=0
for i in nums:
    result=result^i
print(result)

"""
a ^ a = 0 for any number, and a ^ 0 = a
XOR is commutative and associative, so order doesn't matter
XOR-ing all elements together cancels out every pair, leaving only the number that appears once
"""
    