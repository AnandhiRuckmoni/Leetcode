# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.head=None
        self.tail=None

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        tail=head
        if head is None:
            return head
        if head.next is None:
            return head
        while tail.next:
            tail=tail.next
        if head.next is tail:
            head.next=None
            tail.next=head
            head=tail
            return head
        else:
            while head!=tail:
                if tail.next:
                    t=head
                    head=head.next
                    t.next=tail.next
                    tail.next=t
                else:
                    t=head
                    tail.next=head
                    head=head.next
                    t.next=None    
        return head    

    def reorderList(self, head: Optional[ListNode]) -> None:
        if head.next is None:
            return head
        if head is None:
            return head
        curr=head
        head1=head
        nextp=curr
        while nextp: 
            prev=curr           
            curr=curr.next
            if nextp.next:
                nextp=nextp.next.next
            else:
                break
        prev.next=None
        head2=curr
        t=head
        h3=self.reverseList(curr)
        t1=h3
        print(h3 is None)
        while t and t1:
            print(t.val,t1.val)
            if t.next:
                if t1 and t1.next:
                    x=t1.next
                else:
                    x=None
                t1.next=t.next
                t.next=t1
                t=t.next.next
                t1=x
            else:
                t.next=t1
                t=None
                t1=None


        
        