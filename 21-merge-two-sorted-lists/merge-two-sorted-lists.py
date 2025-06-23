class Solution:
    def __init__(self):
        self.head=None
        self.tail=None

    def mergetwosortedlists(self,head1,head2):
        curr=head1
        if not head1:
            return head2
        if not head2:
            return head1
        if head1.val >= head2.val:
            #insert before head1
            t=head2.next
            head2.next=head1
            head1=head2
            head1.next=self.mergetwosortedlists(head1.next,t)
            return head1
        if head1.val < head2.val:
            print("after",head1.val,head2.val)
            head1.next=self.mergetwosortedlists(head1.next,head2)
            #head1.next.next=p
            print("after call",head1.val,head2.val,head1.next.val)
            return head1
            
            #return head1
        return head1
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
        """l1=[]  
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
        return head3"""
        self.head=self.mergetwosortedlists(list1,list2)
        return self.head
