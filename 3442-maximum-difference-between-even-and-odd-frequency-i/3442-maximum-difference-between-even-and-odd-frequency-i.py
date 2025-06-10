class Solution:
    def maxDifference(self, s: str) -> int:
        d={}
        for i in s:
            if i in d:
                d[i]+=1
            else:
                d[i]=1

        even,odd=None,None
        for x in d.values():
            if x%2==0 and (even is None or x<even):
                even=x
            elif x%2!=0 and (odd is None or x>odd):
                odd=x
        return odd-even