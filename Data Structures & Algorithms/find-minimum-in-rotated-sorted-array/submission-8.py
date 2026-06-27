

# n = 
# time
# space


# 3 4 5 6 1 2 
# 3 2
# 5 (r)
# 6
# 1

# 5 6 1 2 3 4
# 5 4 
# 1

# 6 1 2 3 4 5
# 6 5 (l)
# 2

# 2 3 4 5 6 1
# 2 1 (r)
# 4

# l < r 
# 

class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        res = nums[l]

        while l<=r:
            
            m = (l+r)//2

            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m - 1

            res = min(nums[m], res)
        
        return res

            
# 1. general pattern (H1)
# 2. anti pattern (H0)
# 3. edge case




        