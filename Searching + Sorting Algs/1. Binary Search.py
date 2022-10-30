def binary_search(nums, target, start, end):
    if(start<=end):
        mid = (start+end)//2
        if(nums[mid] == target):
            return mid
        elif(nums[mid]<target):
            return binary_search(nums, target, mid+1, end)
        elif(nums[mid]> target):
            return binary_search(nums, target, start, mid -1)
    else:
        return -1

if __name__ =="__main__":
    nums = [1,3,4,5,6,7,8,34,56,67,78]
    print(binary_search(nums, 56, 0, len(nums)-1))

