class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x>=0:
            n=x
            rev=0
            while n>0:
                d=n%10
                rev=rev*10+d
                n=n//10
            if rev>=(-2**31) and rev<=(2**31-1):
                return rev
            else:
                return 0 
        else:
            s=((str(x))[1:])[::-1]
            neg_rev=int(s)*(-1)
            if neg_rev>=(-2**31) and neg_rev<=(2**31-1):
                return neg_rev
            else:
                return 0