# remove all val
# return size nums as k

# 2 pointer

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        
        for i in range(len(nums)):
            if nums[i] != val:
                nums[i], nums[count] = nums[count] , nums[i]
                count += 1
        
        return count