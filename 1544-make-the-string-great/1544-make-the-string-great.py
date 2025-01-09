class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        a=[]
        for i in s:
            if len(a)>0 and (abs(ord(i)-ord(a[-1])))==32:
                a.pop()
            else:
                a.append(i)
        return("".join(a))
