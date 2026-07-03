class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashMap = {}
        for key, val in enumerate(nums):
            hashMap[val] = key
        
        for i in range(len(nums)):
            if target - nums[i] in hashMap and hashMap[target - nums[i]]!= i:
                return [i, hashMap[target-nums[i]]]

