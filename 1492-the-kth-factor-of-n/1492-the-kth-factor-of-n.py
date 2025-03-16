class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        lst=[factor for factor in range(1,n+1) if n%factor==0]
        if k>len(lst):
            return -1
        return lst[k-1]
