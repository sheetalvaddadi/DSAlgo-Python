def cycle_sort(start, nums):
    for i,num in enumerate(nums):
        req_index = num-start
        if (i != req_index):
            nums[i], nums[req_index] = nums[req_index], nums[i]
    return nums

if __name__ =="__main__":
    print(cycle_sort(1, [1,3,4,5,2,7,8,6,9]))
1,5,4,3,2,7,8
