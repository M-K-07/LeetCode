class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s1=[]
        s2=[]
        for i in s:
            if len(s1)!=0 and i=='#':
                s1.pop()
            else:
                s1.append(i)
        for i in t:
            if len(s2)!=0 and i=='#':
                s2.pop()
            else:
                s2.append(i)
        if "".join(s1)=="".join(s2):
            return True
        else:
            return False
