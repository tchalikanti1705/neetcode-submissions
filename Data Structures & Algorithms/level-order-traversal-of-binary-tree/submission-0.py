# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        while q:
            curr_level = len(q)
            curr_elems = []
            for _ in range(curr_level):
                ele = q.popleft()
                curr_elems.append(ele.val)
                if ele.left:
                    q.append(ele.left)
                if ele.right:
                    q.append(ele.right)
            res.append(curr_elems)
        return res


        