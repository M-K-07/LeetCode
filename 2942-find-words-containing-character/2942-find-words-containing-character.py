class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        s=[]
        for i,w in enumerate(words):
            if x in w:
                s.append(i)
        return s