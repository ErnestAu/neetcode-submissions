
# option 1: iterate through every possible combination and find the max product 

# time complexity O(n^2)
# memory: O(1)


#  [1,7,2,5,4,7,3,6]



class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxAmount = 0
        i = 0
        j = len(heights)-1
        while i != j:
            amount = min(heights[i], heights[j]) * (j-i)
            maxAmount = max(amount, maxAmount)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return maxAmount
        for j in range(i+1, len(heights)):
                amount = min(heights[i], heights[j]) * (j-i)
                maxAmount = max(amount, maxAmount)
        return maxAmount
