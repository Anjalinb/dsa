numbers = [2,3,4]
target = 6

for i in numbers:
    diff=target-i
    if diff in numbers and diff!=i:
        print(numbers.index(i),numbers.index(diff))
        break