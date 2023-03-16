def binary_search(nums, target, start, end):
    if(start<=end):
        mid = (start+end)//2
        if(target == nums[mid]):
            return mid
        elif(target<nums[mid]):
            return binary_search(nums, target,start,mid-1 )
        else:
            return binary_search(nums, target, mid+1, end)
    else:
        return -7

cli = [1,3,4,5,6,7,8,9,11,13,15]
print(binary_search(cli,868,0,len(cli)-1))