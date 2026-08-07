class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = cnt = 0
        for num in nums:
            if num:
                cnt += 1
                maxOnes = max(maxOnes, cnt)
            else:
                cnt = 0
        return maxOnes