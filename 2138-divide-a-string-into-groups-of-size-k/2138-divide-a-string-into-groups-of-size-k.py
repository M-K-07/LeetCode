class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        a=[]
        for i in range(0,len(s),k):
            if len(s[i:i+k])==k:
                a.append(s[i:i+k])
            else:
                diff=k-len(s[i:i+k])
                a.append(s[i:i+k]+(diff*fill))
        return a