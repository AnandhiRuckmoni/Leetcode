# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxSum(self,root,maxi):
        
        left=0
        right=0
        x=0
        y=0
        sum=0
        
        
        if not root:
            #return 0
            return 0
        #print(root.val)
        
        left=self.maxSum(root.left,maxi)
        
        right=self.maxSum(root.right,maxi)
        if left == 0 and right != 0:
            x=max(root.val+right,root.val)
            #return x
            if x > maxi[0]:
                maxi[0]=x
        elif left != 0 and right==0:
            x= max(root.val + left,root.val)
            print(x,'value')
            if x > maxi[0]:
                maxi[0]=x
            #return x
        elif left==0 and right == 0:
            x=root.val
            #return x
        else:
            y=max(left,right,0)
            x=root.val+y
            #print(left,right,root.val,maxi)
        #print(left+right+root.val,root.val,sum,maxi)
        y=max(left+right+root.val, left+root.val, right+root.val,root.val)
        if y > maxi[0]:
            print('maxi',maxi)
            maxi[0] = y
            
            

            #return x
        #y=max(root.val,left,right,left+root.val,right+root.val)
        #print(x,y)
        
        
        sum+=x
        print(left+right+root.val,root.val,sum,maxi)
        
        return sum

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        l=[-float('inf')]
        print(self.maxSum(root,l))
        return l[0]