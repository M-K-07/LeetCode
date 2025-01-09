class Solution(object):
    def minOperations(self, logs):
        """
        :type logs: List[str]
        :rtype: int
        """
        lst=[]
        for i in logs:
            if i == '../':
                if len(lst)>0:
                    lst.pop()
                else:
                    continue
            elif i == './':
                continue
            else:
                lst.append(i)
        return len(lst)