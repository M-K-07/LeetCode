class Solution:
    def myAtoi(self, s: str) -> int:
        res = ""
        sign = 1
        k = s.strip()
        if not k:
            return 0
        if k[0] is '-': 
            sign=-1
            k=k[1:]
        elif k[0] is '+':
            sign=1
            k=k[1:]
        
        for i in k:
            if i.isdigit():
                res+=i
            else:
                break 
        if not res:
            return 0
        result = int(res) * sign
                
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        return result
           