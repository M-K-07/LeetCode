class Solution(object):
    def removeDuplicates(self, s):
        """
        :type s: str
        :rtype: str
        """
        lst=[]
        for i in s:
            if len(lst)>0 and i==lst[-1]:
                lst.pop()
            else:
                lst.append(i)
        return "".join(lst)

s = "abbaca"
obj=Solution()
print(obj.removeDuplicates(s))   