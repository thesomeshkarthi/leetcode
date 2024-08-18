# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxDiameter = 0

        def maxDepthOfBinaryTree(node):
            if not node:
                return 0
            left = maxDepthOfBinaryTree(node.left)
            right = maxDepthOfBinaryTree(node.right)

            # Update the diameter at this node
            self.maxDiameter = max(self.maxDiameter, left + right)

            # Return the height of the current node
            return 1 + max(left, right)

        maxDepthOfBinaryTree(root)
        return self.maxDiameter



        