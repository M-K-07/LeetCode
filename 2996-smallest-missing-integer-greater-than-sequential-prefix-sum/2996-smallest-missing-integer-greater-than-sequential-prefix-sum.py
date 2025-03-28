class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        res=nums[0]
        for i in range(len(nums)-1):
            if nums[i]+1==nums[i+1]:
                res+=nums[i+1]
            else:
                break
        while True:
            if res in nums:
                res+=1
            else:
                return res

