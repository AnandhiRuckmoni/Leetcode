# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        lo=[]
        le=[]
        curr=head
        curr1=head
        start=1
        while curr:
            if start%2!=0:
                lo.append(curr)
            else:
                le.append(curr)
            start+=1

            curr=curr.next
        
        head=lo[0]
        curr=head
        for i in range(1,len(lo)):            
            curr.next=lo[i]
            curr=lo[i]  
        if le !=[] :      
            curr.next=le[0]        
            for i in range(len(le)):
                curr.next=le[i]
                curr=le[i]
        curr.next=None
        return curr1

            
            
        

                