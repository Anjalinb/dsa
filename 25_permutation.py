"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""

s1 = "abe"
s2 = "eidbaooo"

for i in range(len(s2)-len(s1)+1):
    substring=s2[i:i+len(s1)]
    if sorted(substring)==sorted(s1):
        print(True)
        break
else:
    print(False)