class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self._search(nums, 0, len(nums)-1, target)
        
    def _search(self, nums, s, e, target):
        if s == e:
            if nums[s]==target:
                return s
            else:
                return -1
        
        m = (s+e)//2
        if nums[m] < target:
            return self._search(nums, m+1, e, target)
        elif nums[m] > target:
            return self._search(nums, s, m, target)
        else:
            return m