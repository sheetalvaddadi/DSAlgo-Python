def find_sum_of_three(nums, target):
   nums.sort()
   for i in range(0,len(nums)-2):
      lp = i+1
      rp = len(nums)-1

      while(lp<rp):
         sum = nums[i]+nums[lp]+nums[rp]

         if (sum == target):
            return True
         elif(sum>target):
            rp-=1
         else:
            lp+=1
   return False