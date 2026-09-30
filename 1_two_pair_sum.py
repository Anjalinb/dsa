nums = [2,7,11,15]
target = 9

for i in nums:
    diff=target-i
    if diff in nums and diff!=i:
        print(i,diff)
        break
