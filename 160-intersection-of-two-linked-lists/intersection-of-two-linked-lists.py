# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        l=[]
        x=None
        curr=headA
        while curr:
            l.append(curr)
            curr=curr.next
        curr=headB
        while curr:
            if curr in l:
                x=curr
                break
            curr=curr.next
            
        return x