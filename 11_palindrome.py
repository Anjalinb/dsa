"""
Using pointers
"""

s = "A man, a plan, a canal: Panama"
text=""
for i in s:
    if i.isalnum():
        text+=i.lower()

l=0
r=len(text)-1
while l!=r:
    if text[l]==text[r]:
        l+=1
        r-=1
    else:
        print("False")
        break
else:
    print("True")



