class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        i=0
        sign = 1
        while i<len(s) and s[i]==" ":
            i+=1
            
        if i<len(s) and (s[i]=='-' or s[i]=="+"):
            sign=-1 if s[i]=='-' else 1
            i+=1

        while i<len(s) and s[i].isdigit():
            res=res*10+ ord(s[i])- ord('0')
            i+=1

        result=sign*res

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result
           