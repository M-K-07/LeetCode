class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def compare(s):
            st=[]
            for i in s:
                if i=="#" and st:
                    st.pop()
                elif i!='#':
                    st.append(i)
            return st

        return (compare(s)==compare(t))
