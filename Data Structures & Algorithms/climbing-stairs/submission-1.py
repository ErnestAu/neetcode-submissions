# 1 or 2 steps at a time
# n steps
# how many distinct ways?

# base case climbStairs(n=1) return 1
# if you climb stairs n = 1
# if n = 0 return 1

class Solution:
    def climbStairs(self, n: int) -> int:
        firstStep = 1
        secondStep = 0
        
        for i in range(n):
            firstStep, secondStep = firstStep + secondStep, firstStep

        return firstStep