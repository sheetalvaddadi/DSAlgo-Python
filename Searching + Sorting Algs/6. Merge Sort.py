def merge_sort(nums):
    if len(nums)>1:
        mid = (0+len(nums))//2
        left_nums = nums[:mid]
        right_nums = nums[mid:]

        merge_sort(left_nums)
        merge_sort(right_nums)

        i= 0 # left array
        j = 0  #right array
        k_merged = 0 #merged array

        while(i < len(left_nums) and j < len(right_nums)):
            if (left_nums[i] < right_nums[j]):
                nums[k_merged] = left_nums[i]
                i+=1
                k_merged += 1
            else:
                nums[k_merged]= right_nums[j]
                j+=1
                k_merged += 1

        while (i < len(left_nums)):
            nums[k_merged] = left_nums[i]
            i+=1
            k_merged+=1
        while (j <len(right_nums)):
            nums[k_merged] = right_nums[j]
            j+=1
            k_merged+=1

        return nums

if __name__ == "__main__":
    print(merge_sort([4,3,5,6,1,2,1,6,7,5,4,3,7,8,3,2,22,3,4,6]))






