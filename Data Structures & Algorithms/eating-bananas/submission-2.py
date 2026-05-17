# piles[i] = number of bananas in that pile
# h = no of horus to eat all the bananas

# k = banana eat / hr

# if piles[i] < k

# whats the minimum rate to finish all bananas within h hours



class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        while l<r:
            k = (l + r) // 2
            if self.eatBananasTime(piles, k) <= h:
                r = k 
            else:
                l = k + 1
        return l

    def eatBananasTime(self,piles, k):
        h = 0
        for pile in piles:
            eatTime = pile // k
            if pile % k != 0:
                eatTime += 1
            h += eatTime
        return h


