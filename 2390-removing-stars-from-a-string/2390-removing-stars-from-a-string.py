class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        queue=[]
        for i in s:
            if i!="*":
                queue.append(i)
            else:
                queue.pop()
        return "".join(queue)