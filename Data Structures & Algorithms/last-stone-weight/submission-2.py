from heapq import heapify, heappop, heappush

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapify(stones)
        while len(stones) > 1:
            first = heappop(stones)
            second = heappop(stones)
            if first-second!=0:
                heappush(stones, first-second)
        if stones:
            return abs(stones[0])
        else:
            return 0
