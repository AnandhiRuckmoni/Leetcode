# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not self:
            root=TreeNode(val)
            return root
        curr=root
        if not root:
            root=TreeNode(val)
            return root
        if val < root.val:
            if root.left:
                root.left= self.insertIntoBST(root.left,val)
                return root
            else:
                root.left=TreeNode(val)
                return root
        if val > root.val:
            if root.right:
                root.right= self.insertIntoBST(root.right,val)
                return root
            else:
                root.right=TreeNode(val)
                return root
        return root