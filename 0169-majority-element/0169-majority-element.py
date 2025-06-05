class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elem=-1
        cnt=0
        for i in nums:
            if i==elem:
                cnt+=1
            elif cnt==0:
                elem=i
                cnt+=1
            elif i!=elem and cnt!=0:
                cnt-=1
        return elem
            