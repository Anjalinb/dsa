"""
Given an array of strings strs, group the anagrams together. You can return the answer in any order.
"""

strs = ["eat","tea","tan","ate","nat","bat"]

anagrams=[]
used=set()

for w1 in strs:
    if w1 in used:
        continue
    group=[w1]
    used.add(w1)

    for w2 in strs:
        if w2 not in used and sorted(w1)==sorted(w2):
            group.append(w2)
            used.add(w2)

    anagrams.append(group)


print(anagrams)
