# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        l=[]
        cycle=False
        if head is None:
            return cycle
        curr=head
        while curr:
            if curr.next not in l:
                l.append(curr.next)
            else:
                cycle=True
                break
            curr=curr.next
        return cycle