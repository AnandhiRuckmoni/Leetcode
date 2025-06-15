# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def getSubtree(self,root):
        l=[]
        curr=root
        if curr.val not in l:
            l.append(curr.val)
        if curr.left:
            l+=self.getSubtree(curr.left)
        if curr.right:
            l+=self.getSubtree(curr.right)
        return l
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        l=[]
        if not self:
            return None
        
        if val==root.val:
            print(val)
            #l=self.getSubtree(root)
            return root
            print(l)
        elif val < root.val:
            if root.left:
                print(root.val,'root.left')
                return self.searchBST(root.left,val)
        elif val > root.val:
            if root.right:
                return self.searchBST(root.right,val)
        