# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right





# height of a tree?
# - 1 + max(left subtree, right subtree)

# base case?
# - if not root: height 0

# a balanced tree
# - left and right subtree balanced
# - left and right subtrees of every node differ in height by no more than 1.


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = True

        def height(root):
            nonlocal balanced
            if not root:
                return 0
            
            left, right = height(root.left), height(root.right)

            if abs(left-right) > 1:
                balanced = False

            return 1 + max(left, right)

        height(root)

        return balanced
        