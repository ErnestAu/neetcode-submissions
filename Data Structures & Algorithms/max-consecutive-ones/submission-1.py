class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = maxCnt = 0
        for num in nums:
            if num:
                cnt +=1
            else:
                cnt = 0
            
            
            maxCnt = max(maxCnt, cnt)
        return maxCnt