# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        path = []
        res = 0

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            path.append(node.val)

            if node.left is None and node.right is None:
                num = 0
                for digit in path:
                    num = num * 10 + digit 
                res+=num
            else:
                dfs(node.left)
                dfs(node.right)
            path.pop()

        dfs(root)
        return res
        