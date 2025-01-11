class Solution(object):
    def minLength(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack=[]
        for i in s:
            if len(stack)!=0 and ((stack[-1]=="A" and i=="B") or (stack[-1]=="C" and i=="D")):
                stack.pop()
            else:
                stack.append(i)
        return len(stack)