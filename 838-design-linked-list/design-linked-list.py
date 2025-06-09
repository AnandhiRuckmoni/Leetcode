class MyListNode:
    def __init__(self,data,next=None):
        self.val=data
        self.next=None

class MyLinkedList:

    def __init__(self):
        self.head=None
        self.tail=None

    def get(self, index: int) -> int:
        i=0
        if index < 0:
            return -1
        curr=self.head
        #print(index,curr.val)
        
        prev=None
       
        while i < index and curr:
            i+=1
            prev=curr
            curr=curr.next
            #print(prev.val,curr.val,"get")
        #print(prev.val)
        if curr:
            return curr.val
        else:
            return -1        

    def addAtHead(self, val: int) -> None:
        
        if self.head is None:
            n=MyListNode(val)
            n.next=None
            self.head=n
            self.tail=n
        else:
            n=MyListNode(val)
            n.next=self.head
            self.head=n
        
        
        

    def addAtTail(self, val: int) -> None:
        curr=self.head
        if curr is None:
            n=MyListNode(val)
            n.next=None
            self.tail=n
            self.head=n
        else:
            while curr.next:
                curr=curr.next
            n=MyListNode(val)
            curr.next=n
            self.tail=n
        return self
        
        

    def addAtIndex(self, index: int, val: int) -> None:
        i=0
        curr=self.head
        if index==0:
            self.addAtHead(val)
        else:
            prev=None
            while i < index and curr:
                i+=1
                prev=curr
                curr=curr.next
            n=MyListNode(val)
            n.next=curr
            print(curr)
            if prev:
                prev.next=n
        return self

    def countofitems(self):
        count=0
        curr=self.head
        while curr:
            count+=1
            curr=curr.next
        return count

    def deleteAtIndex(self, index: int) -> None:
        i=0
        curr=self.head
        count=self.countofitems()
        if index > count - 1:
            return None
        prev=None
        while i < index:
            i+=1
            prev=curr
            curr=curr.next
        if index==0:
            if curr.next:
                self.head=curr.next
            else:
                self.head=None
        else:
            prev.next=curr.next
            curr.next=None


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)