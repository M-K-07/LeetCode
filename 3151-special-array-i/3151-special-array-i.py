class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        else:
            for i in range(len(nums)-1):
                if (nums[i]+nums[i+1])%2==0:
                    return False 
                    break
            else:
                return True