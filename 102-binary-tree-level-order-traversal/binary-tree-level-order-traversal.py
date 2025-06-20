# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q=[]
        
        values=[]   
        l=[]
        l1=[]
        if not root:
            return values
        level=1
        q.append((root,level))        
        while q!=[]:
            curr=q[0]
            del q[0]
            values.append((curr[0].val,curr[1]))
            if curr[0].left:
                q.append((curr[0].left,curr[1]+1))
            if curr[0].right:
                q.append((curr[0].right,curr[1]+1))
        
        level=1
        for i in values:
            print(i[0],level)
            if i[1]==level:
                l.append(i[0])
            if i[1] > level:
                level=i[1]
                l1.append(l)
                l=[]
                l.append(i[0])
            
        #print(l1)
        if len(l)>0:
            l1.append(l)
            
        return l1
