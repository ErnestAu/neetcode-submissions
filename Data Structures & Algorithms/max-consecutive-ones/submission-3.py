class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = maxCnt = 0
        for num in nums:
            cnt = cnt + 1 if num else 0
            
            
            maxCnt = max(maxCnt, cnt)
        return maxCnt