# if len(piles) == h:
#     return max(piles)

# if sum(piles) == h
# return 1
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        e = max(piles)
        s = 1
        
        k = e

        while s < e:
            m = (e+s)//2
            hours = self.eatBananas(piles, m)
            
            if hours > h:
                # taking too long
                # i need m to increase
                s = m + 1
            else:
                # under time limit
                # store m as smallest so far
                k = m
                e = m 

        return k

    def eatBananas(self, piles, k):
        hours = 0
        for pile in piles:
            hours += pile//k
            if pile%k!=0:
                hours += 1
        return hours
