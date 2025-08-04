class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        hash_map={}
        for i in nums:
            if i in hash_map.keys():
                hash_map[i]+=1
            else:
                hash_map[i]=1
        
        for key,val in hash_map.items():
            if val%2!=0:
                return False
        return True
        