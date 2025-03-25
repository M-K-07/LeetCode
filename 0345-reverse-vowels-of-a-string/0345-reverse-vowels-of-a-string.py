class Solution:
    def reverseVowels(self, s: str) -> str:
        f=0
        l=len(s)-1
        a=list(s)
        while f<l:
            if a[f] in 'aeiouAEIOU' and a[l] in 'aeiouAEIOU':
                a[f],a[l]=a[l],a[f]
                f+=1
                l-=1
            elif a[f] not in 'aeiouAEIOU':
                f+=1
            else:
                l-=1
        return ''.join(a)