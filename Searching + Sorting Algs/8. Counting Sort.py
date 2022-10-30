def counting_sort(nums):
    size = len(nums)
    result = [0] * size
    count = [0] * 10

    for num in nums:
        count[num] +=1

    for j in range(1,10):
        count[j] += count[j-1]

    m = size -1
    while (m >=0):
        result[count[nums[m]]-1] = nums[m]
        count[nums[m]] -=1
        m-=1

    for m in range(size):
        nums[m] = result[m]

    return result
if __name__ == "__main__":
    print(counting_sort([3,3,2,3,4,5,6,4,1,2,2,4]))