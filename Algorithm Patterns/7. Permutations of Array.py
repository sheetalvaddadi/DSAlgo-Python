def permute(nums):
    result = []

    if (len(nums) == 1):
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)
        perms = permute(nums)

        for perm in perms:
            perm.append(n)
        result.extend(perms)
        nums.append(n)
    return result

print(permute([1,2,3]))

'''
[[3, 2, 1], [2, 3, 1], [1, 3, 2], [3, 1, 2], [2, 1, 3], [1, 2, 3]]
'''