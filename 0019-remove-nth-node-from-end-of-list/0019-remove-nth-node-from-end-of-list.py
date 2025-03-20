# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp=head
        count=1
        while temp.next!=None:
            count+=1
            temp=temp.next
        if count-n==0:
            return head.next
        t=head
        for i in range(1,count-n):
            t=t.next
        t.next=t.next.next
        return head