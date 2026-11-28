# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        ans = 0
        def help(root: Optional[TreeNode]) -> None:
            nonlocal ans
            if not root: return 0

            left =  help(root.left)
            right = help(root.right)
            ans = max(ans, left + right)
            return 1 + max(left, right)
        help(root)
        return ans

        