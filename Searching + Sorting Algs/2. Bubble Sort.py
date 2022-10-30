def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(len(nums) - i -1):
            if(nums[j]>nums[j+1]):
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

if __name__ == "__main__":
    print(bubble_sort([5,3,22,6,31,1,2,3,45,6,7,8,9,9,5,1,2]))