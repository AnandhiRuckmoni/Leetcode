# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        curr=head
        prev=None
        succ=curr.next
        while curr!=None:
            curr.next=prev
            prev=curr
            curr=succ
            if curr!=None:
                succ=curr.next
        head=prev
        return head
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow=head
        fast=head
        l=[]
        l.append(slow)
        while fast!=None and fast.next!=None:            
            slow=slow.next
            fast=fast.next.next
            l.append(slow)
        ll2=self.reverseList(slow.next)
        slow.next=None        
        head2=ll2
        head1=head        
        while head2!=None:
            t=head1.next
            t2=head2.next
            head1.next=head2
            head2.next=t
            head2=t2
            head1=t
            