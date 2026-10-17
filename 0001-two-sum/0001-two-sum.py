class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        t1=len(nums)
       # if t1>2:
        #    t1-=1
        #else:
         #   t1=t1    
        t=list()
        for x in range(t1):
           x1=target-nums[x]
           if x1 in nums :
            x1=nums.index(x1)
            if x>x1 or x<x1 :
                t.append(x1)
                t.append(x)
                return t
  
       

        

        