# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1,temp2=list1,list2
        lst=[]
        while (temp1 != None and temp2 != None):
            if temp1.val<temp2.val:
                lst.append(temp1.val)
                temp1=temp1.next
            else:
                lst.append(temp2.val)
                temp2=temp2.next
        while(temp1!=None):
            lst.append(temp1.val)
            temp1=temp1.next
        while(temp2!=None):
            lst.append(temp2.val)
            temp2=temp2.next
        new_lst=ListNode(0)
        temp=new_lst
        for i in lst:
            temp.next=ListNode(i)
            temp=temp.next
        return new_lst.next