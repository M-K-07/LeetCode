class Solution(object):
    def maxScore(self, s):
        """
        :type s: str
        :rtype: int
        """
        lst=[]
        for i in range (len(s)):
            left=s[:i+1]
            right=s[i+1:]
            if right:   
                sum_=left.count('0')+right.count('1')
            lst.append(sum_)
        return sorted(lst)[-1]

