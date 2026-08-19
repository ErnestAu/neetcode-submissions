# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



# depth first
# go all the way down, left to right, until root none
# find the max height

# whats the height of a tree?
# 1+ max(left height, right height)




class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def height(root):
            if not root:
                return 0

            left = height(root.left)
            right = height(root.right)
            res = 1 + max(left,right)
            return res

        return height(root)

        # return 1+max(maxDepth(root.left), )
        