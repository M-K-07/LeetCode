class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k%=n
        self.rev_(nums,0,n-1)
        self.rev_(nums,0,k-1) 
        self.rev_(nums,k,n-1) 
    
    def rev_(self,arr,start,end):
        while start<end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1



