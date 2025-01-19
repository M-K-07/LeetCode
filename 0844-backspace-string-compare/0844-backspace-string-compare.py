class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def rev(s):
            st=[]
            for i in s:
                if i=="#" and st:
                    st.pop()
                elif i!='#':
                    st.append(i)
            return st

        return (rev(s)==rev(t))
