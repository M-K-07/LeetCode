class Solution:
    def myAtoi(self, s: str) -> int:
        res = 0
        isStart=True
        sign = 1
        for i in s:
            if i==" " and isStart:
                continue
            elif i=='-' and isStart:
                sign=-1
                isStart=False
            elif i=='+' and isStart:
                sign=1
                isStart=False
            elif '0'<=i<='9':
                res=res*10+ ord(i)-ord('0')
                isStart=False
            else:
                break

        result=sign*res

        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result
           