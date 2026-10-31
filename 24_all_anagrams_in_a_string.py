"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s.
 You may return the answer in any order.
"""

s = "cbaebabacd"
p = "abc"

result=[]

for i in range(len(s)-len(p)+1):
    substring=s[i:i+len(p)]
    if sorted(substring)==sorted(p):
        result.append(i)


print(result)