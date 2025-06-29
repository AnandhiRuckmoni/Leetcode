# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addnode(self,val,head):
        
        if not head:
            head=ListNode(val)
            return head
        curr=head
        while curr.next:
            curr=curr.next
        curr.next=ListNode(val)
        return head
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        l3=[]
        curr=l1
        while curr:
            l.append(curr.val)
            curr=curr.next
        curr=l2
        while curr:
            l3.append(curr.val)
            curr=curr.next
        #print(l,l3)
        s1="".join(str(i) for i in l[::-1])
        s2="".join(str(i) for i in l3[::-1])
        res=int(s1)+int(s2)
        
        l=[]
        for i in str(res)[::-1]:
            l.append(int(i))
        print(l)
        t=Solution()
        head=None
        for i in l:
            head=t.addnode(i,head)
            
        #t.printlist(head)
        print(type(head))
        return head