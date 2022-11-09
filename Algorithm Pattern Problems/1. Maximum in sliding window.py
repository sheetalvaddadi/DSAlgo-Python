def find_max_sliding_window(nums, window_size):
    result =[]
    lp =0
    rp = window_size
    while rp<len(nums)+1:
        result.append(max(nums[lp:rp]))
        lp+=1
        rp+=1
    return result
print(find_max_sliding_window([1,2,3,4,5],3))