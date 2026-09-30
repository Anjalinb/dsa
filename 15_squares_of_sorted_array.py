"""
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number
sorted in non-decreasing order.
"""
nums = [-7,-3,2,3,11]
squares=[x**2 for x in nums]
squares.sort()
print(squares)