class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        hmap = {}
        for i in words:
            if i[::-1] in hmap:
                hmap[i[::-1]] += 1
            else:
                hmap[i] = 0
        cnt=0
        for i in hmap.values():
            if i==1:
                cnt+=1
        return cnt
