# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        q = deque()
        res = []
        q.append(root)

        if not root:
            return []

        while q:
            _res = []
            for i in range(len(q)):
                curr = q.popleft()
                if curr.right:
                    q.append(curr.right)
                if curr.left:
                    q.append(curr.left)
                if i == 0:
                    res.append(curr.val)
        
        return res