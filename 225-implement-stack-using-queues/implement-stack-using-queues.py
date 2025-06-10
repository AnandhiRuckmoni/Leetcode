class StackNode:
    def  __init__(self,data):
        self.data=data
        self.next=None

class MyStack:

    def __init__(self):
        self.head=None
        

    def push(self, x: int) -> None:
        curr=self.head
        if curr:
            n=StackNode(x)
            n.next=curr
            
        else:
            n=StackNode(x)
            
        self.head=n

    def pop(self) -> int:
        if self.head:
            curr=self.head
            x=curr.data
            self.head=curr.next
            return x

    def top(self) -> int:
        if self.head:
            return self.head.data
        

    def empty(self) -> bool:
        if self.head is None:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()