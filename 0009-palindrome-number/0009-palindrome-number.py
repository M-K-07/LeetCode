class Solution:
    def isPalindrome(self, x: int) -> bool:
        n=x
        rev=0
        while n>0:
            digit=n%10
            rev=(rev*10)+digit
            n=n//10
        if x==rev:
            return True
        else:
            return False