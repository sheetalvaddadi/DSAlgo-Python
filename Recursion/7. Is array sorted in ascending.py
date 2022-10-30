class Sort:
    def checksorted(self, nums, p):
        if(nums[p]>nums[p+1]):
            return False
        elif(nums[p]<=nums[p+1] and p+1<len(nums)-1):
            return self.checksorted(nums, p+1)
        return True

if __name__ =="__main__":
    s1 = Sort()
    print(s1.checksorted([1,2,3,4,5,6,356], 0))