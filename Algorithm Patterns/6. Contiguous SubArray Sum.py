def checkSubarraySum(nums,k):
    remainder = {0: -1}  # map the remainder to end index
    total = 0
    count = 0
    for i, num in enumerate(nums):
        total += num
        r = total % k
        if (r not in remainder):
            remainder[r] = i

        elif (i - remainder[r] > 1):
            return True
    return False

print(checkSubarraySum([3,2,2,1,3,5,6,4],3))
