class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        flag=0
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if target==nums[mid]:
                flag=1
                return mid
            elif target>nums[mid]:
                low=mid+1
            else:
                high=mid-1
        if flag==0:
            return -1
