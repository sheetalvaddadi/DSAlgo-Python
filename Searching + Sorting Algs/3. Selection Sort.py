def selection_sort(nums):
    for i in range(len(nums)):
        min_swap= i
        for j in range (i+1, len(nums)):
            if(nums[j]<nums[min_swap]):
                nums[j], nums[min_swap] = nums[min_swap], nums[j]
    return nums

if __name__ == "__main__":
    print(selection_sort([1,8,5,4,34,52,3,1,2,4,5,6,45,87,6,93]))