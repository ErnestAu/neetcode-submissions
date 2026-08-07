




class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 2
        res = 0

        if n == 1:
            return 1
        if n == 2:
            return 2

        for _ in range(2,n):
            res = one + two
            one = two
            two = res
        return res