# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def countofitems(self,head:ListNode)->int:
        cnt=0
        curr=head
        while curr:
            cnt+=1
            curr=curr.next
        return cnt
    def insertatfront(self,llist:ListNode,data:int):
        newNode=ListNode(data)
        if llist is None:
            newNode.next=None
        else:
            newNode.next = llist
        llist=newNode
        
        return llist
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        llist_count=self.countofitems(head)
    
        if head is None:
            return head
        curr=head
        if llist_count==1:
            return head
        
        head=curr.next
        curr.next=head.next
        head.next=curr
        
        if llist_count > 2:
            curr=head
            prev=None
            index=0
            pos=2
            while pos < llist_count:
                

                while index < pos and curr.next:
                    prev=curr
                    curr=curr.next
                    index+=1
                prev.next=curr.next
                head=self.insertatfront(head,curr.val)
                #print_singly_linked_list(llist, ' ', fptr)
                pos=pos+1
                
                curr=head
                
                index=0
            
            
            
            
        return head