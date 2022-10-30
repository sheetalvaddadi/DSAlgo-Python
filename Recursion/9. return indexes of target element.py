class ReturnList:
    def returnindeces(self, nums, target, pointer,result):
        if(pointer<len(nums)):
            if(nums[pointer] == target):
                result.append(pointer)
            return self.returnindeces(nums, target, pointer+1, result)
        return result

if __name__ =="__main__":
    r1 = ReturnList()
    print(r1.returnindeces([2,2,4,5,1,2,3,6,7,8], 2, 0, []))