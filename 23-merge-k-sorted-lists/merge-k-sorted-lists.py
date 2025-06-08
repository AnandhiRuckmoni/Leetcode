# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution: 
    def insertatend(self,head:ListNode,data):
        if head is None:
            newNode=ListNode(data)
            head=newNode
            newNode.next=None
        else:
            curr=head
            while curr.next:
                curr=curr.next
            curr.next=ListNode(data)
            curr.next.next=None
        return head
    def createlist(self, data_list)->ListNode:
        head=None
        for i in data_list:
            head=self.insertatend(head,i)   
        return head
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists)==0:
            return None
        if len(lists)==1:
            if lists[0] is None:
                return None
        l=[]
        for head in lists:
            curr=head
            while curr:
                l.append(curr.val)
                curr=curr.next
        l.sort()
        print(l)
        head=self.createlist(l)
        return head
