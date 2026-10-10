"""
You are given a string s and an integer k. You can choose any character of the string and change it to any
 other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above
 operations.
"""
#count.get(key, 0) returns the value for that key if it exists. Otherwise, it returns 0.
s= "AABABBA"
k = 1
left=0
right=0
max_freq=0
max_len=0
count={}

for right in range(len(s)):
    count[s[right]]=count.get(s[right],0)+1
    max_freq=max(max_freq,count[s[right]])
    while (right-left+1)-max_freq>k:
        count[s[left]]-=1
        left+=1
    max_len=max(max_len,right-left+1)

print(max_len)
