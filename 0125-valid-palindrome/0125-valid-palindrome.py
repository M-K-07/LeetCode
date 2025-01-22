class Solution:
    def isPalindrome(self, s: str) -> bool:
        lst=[]
        for i in s:
            if i.lower() in 'abcdefghijklmnopqrstuvwxyz1234567890':
                lst.append(i.lower())
        if lst==lst[::-1]:
            return True
        return False