class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n=len(digits)-1
        value=0
        for i in digits:
            value+=i*(10**n)
            n-=1
        x=[int(num) for num in str(value+1)]
        return x