class ListNode:
    def __init__(self,data):
        self.data=data
        self.prev=None
        self.next=None

class BrowserHistory:
    def print(self):
        curr=self.head
        while curr:
            print(curr.data)
            curr=curr.next
    def addtobeginning(self,data):
        n=ListNode(data)
        self.head=n
        self.currentnode=n
    def addtocurrentnode(self,data):
        curr=self.head
        end=self.currentnode
        while curr!=end:
            curr=curr.next
        n=ListNode(data)
        n.prev=curr
        curr.next=n
        self.currentnode=n
        
        
    def __init__(self, homepage: str):
        self.addtobeginning(homepage)
        
    def visit(self, url: str) -> None:
        curr=self.head
        
        if curr:
            print(curr.data,url)
            self.addtocurrentnode(url)
        else:
            n=ListNode(url)
            self.head=n
            self.currentnode=n


    def back(self, steps: int) -> str:
        curr=self.currentnode
        
        i=0
        while curr and i < steps:
            if curr.prev:
                curr=curr.prev
                i+=1
            else:
                break
        
        if curr:
            self.currentnode=curr
            return curr.data         
        
            

    def forward(self, steps: int) -> str:
        curr=self.currentnode
        i=0
        while curr and i < steps:
            if curr.next:
                curr=curr.next
                i+=1
            else:
                break
        if curr:
            self.currentnode=curr
            return curr.data
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)