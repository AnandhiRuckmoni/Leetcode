# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        if not head.next:
            return head
        curr=head
        idx=1
        x=None
        y=None
        while curr.next:
            print(curr.val)
            
            x=curr.next
            if y is not None:
                y.next=x
            y=curr
            y.next=x.next
            x.next=y
            if idx==1:
                head=x
                idx=2
            curr=curr.next
            if not curr:
                break
        return head