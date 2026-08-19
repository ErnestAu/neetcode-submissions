# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        def _inorderTraversal(root):
            if not root:
                return

            _inorderTraversal(root.left)
            res.append(root.val)
            _inorderTraversal(root.right)
        
        _inorderTraversal(root)

        return res