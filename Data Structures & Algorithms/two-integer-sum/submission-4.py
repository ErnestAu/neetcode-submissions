class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, n in enumerate(nums):
            hashMap[n] = i
        
        for i, n in enumerate(nums):
            diff = target - n
            if diff in hashMap and hashMap[diff] != i:
                return [i, hashMap[diff]]



        # hashset = set(nums)

        # i = 0
        # for num in nums:
        #     if target - num in hashset:
        #         break
        #     i += 1
        
        # j = i + 1
        # for _ in range(j,len(nums)-1):
        #     if nums[j] == target - nums[i]:
        #         return [i,j]
        #     j += 1

        # return [i,j]