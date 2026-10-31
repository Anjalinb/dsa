def IsAnagram(s,p):

    if sorted(s)==sorted(p):
        print(True)
    else:
        print(False)

IsAnagram("rat","tar")