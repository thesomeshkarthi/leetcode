# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        self.subtree = False
        self.subtreeFlag = 0

        def sameTree(curr1, curr2):
            if not curr1 and not curr2:
                return True
            elif curr1 and curr2 and curr1.val == curr2.val:
                return sameTree(curr1.left, curr2.left) and sameTree(curr1.right, curr2.right)
            else:
                return False
        
        def dfs(curr1):
            if curr1 is None:
                return 
            
            if curr1.val == subRoot.val:
                self.subtree = sameTree(curr1, subRoot)
                if self.subtree:
                    self.subtreeFlag += 1

            
            dfs(curr1.right)
            dfs(curr1.left)
        
        dfs(root)
        if self.subtreeFlag > 0:
            return True
        
        return False

        