class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x = defaultdict()
        for i in range(len(nums)):
            x[nums[i]] = i
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in x and x[diff] != i:
                return [i, x[diff]]
        
