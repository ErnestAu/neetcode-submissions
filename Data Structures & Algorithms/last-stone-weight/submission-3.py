from heapq import heapify, heappush, heappop

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-stone for stone in stones]

        heapify(stones)

        while len(stones)>1:
            x = heappop(stones)
            y = heappop(stones)

            dif = x-y

            heappush(stones, dif)
        
        return abs(stones[0]) if stones else 0