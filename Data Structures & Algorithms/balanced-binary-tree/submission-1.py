# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def height(node):
            if not node:
                return 0
    
            return 1 + max(height(node.left), height(node.right))

        def recur(node):
            if not node:
                return True

            left = height(node.left)
            right = height(node.right)
            if abs(left - right) > 1:
                return False

            return recur(node.left) and recur(node.right)

        return recur(root)