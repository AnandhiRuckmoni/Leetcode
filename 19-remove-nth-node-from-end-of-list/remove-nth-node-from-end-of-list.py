# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.head=None
        self.tail=None
    def countofitems(self,head):
        count=0
        curr=head
        while curr:
            count+=1
            curr=curr.next
        return count
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count=self.countofitems(head)
        pos=count-n
        print(count,pos)
        if count==1 and n==1:
            head=None
            return head
        if pos==0:
            print(head.val)
            curr=head
            head=head.next
            curr.next=None

            return head
        curr=head
        j=0
        prev=curr
        while j<pos and curr.next:
            j+=1
            prev=curr
            curr=curr.next
        prev.next=curr.next
        curr.next=None
        return head
        