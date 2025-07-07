# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        if not curr:
            return None
        
        l=[]
        i=0
        indx=None
        while curr:
            i+=1
            if curr in l:
                indx=curr
                break
            l.append(curr)
            curr=curr.next
        return indx