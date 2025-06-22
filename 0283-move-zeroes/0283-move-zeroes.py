class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j=-1
        found_zero=False
        for k in range(len(nums)):
            if nums[k]==0:
                j=k
                found_zero=True
                break
        if found_zero:
            for i in range(j+1,len(nums)):
                if nums[i]!=0:
                    nums[i],nums[j]=nums[j],nums[i]
                    j+=1
        return nums