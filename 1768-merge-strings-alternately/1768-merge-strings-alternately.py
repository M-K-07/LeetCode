class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i,j=0,0
        result=''
        while i<len(word1) and j<len(word2):
            result+=word1[i]
            result+=word2[j]
            i+=1
            j+=1
        while j<len(word2):
            result+=word2[j]
            j+=1
        while i<len(word1):
            result+=word1[i]
            i+=1
        return result