# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        l=[]
        if not self:
            return None        
        if val==root.val:
            return root            
        elif val < root.val:
            if root.left:
                return self.searchBST(root.left,val)
        elif val > root.val:
            if root.right:
                return self.searchBST(root.right,val)
        