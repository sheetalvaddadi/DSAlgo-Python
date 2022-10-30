def quick_sort(nums, start, end):
    if(start<end):
        partition_pos = partition (nums, start, end)
        quick_sort(nums, start, partition_pos -1)
        quick_sort(nums, partition_pos +1, end)


def partition(nums, start, end):
    p1 = start
    p2 = end - 1
    pivot = nums[end]

    while(p1<p2):
        while (p1 < end and nums[p1]<pivot):
            p1+=1
        while(p2 > start and nums[p2]>=pivot):
            p2-=1
        if (p1<p2):
            nums[p1], nums[p2] = nums[p2], nums[p1]
    if (nums[p1]>pivot):
        nums[p1], nums[end] = nums[end], nums[p1]
    return p1

if __name__ =="__main__":
    nums = [16, 2, 3, 4, 25, 367,23, 14, 35, 43, 5, 6, 7, 54, 3, 1]
    quick_sort(nums, 0, len(nums) - 1)
    print(nums)



