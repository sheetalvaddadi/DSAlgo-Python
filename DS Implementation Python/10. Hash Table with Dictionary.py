

dict = {}
nums = [1,1,2,4,5,6,2,7]
for x in nums:
    if (x in dict):
        dict[x] = [1,2,3,3,4,5]
    else:
        dict[x] = 1

print(dict)
