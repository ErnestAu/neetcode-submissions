# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        temp = root
        curr = root
        while curr:
            prev = curr
            if curr.val < val:
                curr = curr.right
            elif curr.val > val:
                curr = curr.left
        
        if prev.val < val:
            prev.right = TreeNode(val)
        elif prev.val > val:
            prev.left = TreeNode(val)
        return temp