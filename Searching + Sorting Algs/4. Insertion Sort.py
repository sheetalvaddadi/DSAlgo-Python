def inserion_sort(nums):
    for i in range(1, len(nums)):
        min_swap = i
        while (nums[min_swap-1]> nums[min_swap] and min_swap>0):
            nums[min_swap-1], nums[min_swap] = nums[min_swap], nums[min_swap-1]
            min_swap-=1
    return nums

if __name__ =="__main__":
    print(inserion_sort([0,3,7,2,5,8,4,6,0,1]))