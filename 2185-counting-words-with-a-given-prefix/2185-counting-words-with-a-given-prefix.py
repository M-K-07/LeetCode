class Solution(object):
    def prefixCount(self, words, pref):
        """
        :type words: List[str]
        :type pref: str
        :rtype: int
        """
        l=[]
        for i in words:
            if pref in i:
                l.append(i)
        c=0
        for i in l:
            if pref==i[:len(pref)]:
                c+=1
        return c
        