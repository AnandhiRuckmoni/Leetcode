# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invert(self,root):
        x=None
        y=None
        curr=root
        if not curr:
            return
        if not curr.left and not curr.right:
            return curr
        if curr.left:
            x=self.invert(curr.left)
        if curr.right:
            y=self.invert(curr.right)
        
        curr.left=y
        curr.right=x
        return curr

    def bfs(self,root):
        l=[]
        q=[]
        if not root:
            return l

        q.append((root))
        while q!=[]:
            curr=q[0]
            del q[0]
            l.append(curr)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        while q!=[]:
            curr=q[0]
            del q[0]
            l.append(curr)
        return l
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        root=self.invert(root)
        return root