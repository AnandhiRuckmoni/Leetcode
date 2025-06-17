# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_min(self,root):
        curr=root
        
        if curr.left:
            return self.find_min(curr.left)
        else:
            return curr.val

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key == root.val:
            if not root.left and not root.right:
                root=None
                return root
            elif root.right and root.left:
                minnodeval=self.find_min(root.right)
                root.val=minnodeval
                root.right=self.deleteNode(root.right,minnodeval)
                return root
            elif root.left or root.right:
                if root.left:
                    return root.left
                if root.right:
                    return root.right
        if key < root.val:
            root.left=self.deleteNode(root.left,key)
            return root
        if key > root.val:
            root.right=self.deleteNode(root.right,key)
            return root
        return root