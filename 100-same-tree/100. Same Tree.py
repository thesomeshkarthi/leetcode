# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        self.same = True

        def dfs(curr1, curr2):
            if curr1 is None:
                if curr2 is None:
                    return 0
                if curr2:
                    self.same = False
                    return 0
            if curr2 is None:
                if curr1 is None:
                    return 0
                if curr1:
                    self.same = False
                    return 0
            
            dfs(curr1.right, curr2.right)
            
            if curr1.val != curr2.val:
                self.same = False

            dfs(curr1.left, curr2.left)

            if curr1.val != curr2.val:
                self.same = False

            return 0
        
        dfs(p, q)
        return self.same

        