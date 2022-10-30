def subarrays(nums):
    subarrays = []

    for i in range(len(nums)):
        temp = []
        for j in range(i, len(nums)):
            temp.append(nums[j])
            subarrays.append(temp.copy())
    return subarrays

print(subarrays([1,2,3,4,5,5]))
'''
[[1], [1, 2], [1, 2, 3], [1, 2, 3, 4], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 5], [2], [2, 3], [2, 3, 4], [2, 3, 4, 5], [2, 3, 4, 5, 5], [3], [3, 4], [3, 4, 5], [3, 4, 5, 5], [4], [4, 5], [4, 5, 5], [5], [5, 5], [5]]

'''