class Linear:
    def linear_search(self, nums, target, pointer):
        if(pointer<len(nums)):
            if(nums[pointer] == target):
                return pointer
            else:
                return self.linear_search(nums, target, pointer+1)
        return -1000

if __name__ =="__main__":
    l=Linear()
    print(l.linear_search([1,2,4,45,2,600,23], 2, 0))
