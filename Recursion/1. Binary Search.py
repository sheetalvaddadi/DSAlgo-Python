class BinarySearch:
    def search(self, nums, target, start, end):
        mid = (start+end)//2
        if(start<=end):
            if(nums[mid]==target):
                return mid
            elif(target<nums[mid]):
                return self.search(nums, target, start, mid-1)
            elif(target>nums[mid]):
                return self.search(nums, target, mid+1, end)
        else:
            return -1
if __name__ =="__main__":
    bs1 = BinarySearch();
    nums = [1,3,4,5,6,7,8,9,10]
    print(bs1.search(nums, 9, 0, len(nums)-1))