# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


# traverse the entire tree
# find the kth smallest

# do a maxheap with size k

# how do u traverse the entire tree?
# traverse the left tree
# traverse the right tree

# base case: return 



# 2nd smallest
# -1
# -2,0
# if 

# -3 -2 -1

# from heapq import heappush, heappop

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        arr = []

        def dfs(root):
            nonlocal arr
            if not root:
                return
            
            dfs(root.left)
            arr.append(root.val)
            dfs(root.right)

        dfs(root)

        return arr[k-1]
