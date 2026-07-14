# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        prev=None
        if head is None:
            return
        succ=curr.next
        while curr!=None:
            curr.next=prev
            prev=curr
            curr=succ
            if curr!=None:
                succ=curr.next
        head=prev
        return head