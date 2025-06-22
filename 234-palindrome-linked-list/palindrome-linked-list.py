# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self,head):
        if not head or not head.next:
            return head
        p=self.reverseList(head.next)
        head.next.next=head
        head.next=None
        return p

    def getdata(self,head):
        l=[]
        root=head
        while root:
            l.append(root.val)
            root=root.next
        return l
    def comparelists(self,head1,head2):
        root1=head1
        root2=head2
        print(root1.val,root2.val,root1.next,root2.next)
        while root1 and root2:
            
            if root1.val == root2.val:
                root1=root1.next
                root2=root2.next
            else:
                return False
        return True
    def printlist(self,head):
        root=head
        while root:
            print(root.val)
            root=root.next
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        
        l=self.getdata(head)
        self.head=self.reverseList(head)
        l1=self.getdata(self.head)
        if l == l1:
            return True
        else:
            return False