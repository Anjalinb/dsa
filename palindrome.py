s = "A man, a plan, a canal: Panama"
text=""
for i in s:
    if i.isalnum():
        text+=i.lower()

if text==text[::-1]:
    print("True")
else:
    print("False")


