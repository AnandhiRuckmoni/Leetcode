class Solution:
    def __init__(self):
        self.head=None
        self.tail=None
    def insertatend(self,data):
        if self.head is None:
            self.head=ListNode(data)            
            return self.head
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=ListNode(data)
        return self.head
    
    def createList(self,data_list):
        for i in data_list:
            llist=self.insertatend(i)
        return llist
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=[]  
        if list1 is None and list2 is None:
            return None  
        while list1:
            l1.append(list1.val)
            list1=list1.next
        while list2:
            l1.append(list2.val)
            list2=list2.next
        l1.sort()
        
        head3=self.createList(l1)
        return head3
