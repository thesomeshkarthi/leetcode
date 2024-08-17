# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if root is None:
            return 0
        
        rightValue = self.maxDepth(root.right)
        rightValue += 1
        leftValue = self.maxDepth(root.left)
        leftValue += 1

        if rightValue >= leftValue:
            return rightValue
        else:
            return leftValue
        


        

        
    
            

        


        