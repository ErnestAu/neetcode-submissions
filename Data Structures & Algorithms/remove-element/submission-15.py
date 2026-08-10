

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # if len(nums) ==1:
        #     if nums[0] == val:
        #         return 0
        #     else:
        #         return 1
        if len(nums) == 0:
            return 0


        
        l = 0
        r = len(nums)-1
        while l<r:
            if nums[l] == val:
                nums[l], nums[r] = nums[r], nums[l]
                r-=1
                l-=1
            l+=1
        if nums[l]==val:
            return l
        else:
            return l+1
