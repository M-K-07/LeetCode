class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_num=0
        for i in range (len(s)):
            left=s[:i+1]
            right=s[i+1:]
            if right:   
                sum_=left.count('0')+right.count('1')
            if max_num<sum_:
                max_num=sum_
        return max_num

