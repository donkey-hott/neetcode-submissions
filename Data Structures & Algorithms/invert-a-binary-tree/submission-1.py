# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: return None

        st = [root]

        while len(st) > 0:
            cur = st.pop()

            cur.left, cur.right = cur.right, cur.left

            if cur.right: st.append(cur.right)
            if cur.left: st.append(cur.left)
        return root