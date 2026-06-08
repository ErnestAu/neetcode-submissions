class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = cnt = 0
        for num in nums:
            cnt = (cnt + 1 if num else 0)
            maxOnes = max(maxOnes, cnt)

        return maxOnes