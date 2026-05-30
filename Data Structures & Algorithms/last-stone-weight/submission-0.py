class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        negated = [-x for x in stones]
        heapq.heapify(negated)
        while len(negated) > 1:
            one = heapq.heappop(negated)
            two = heapq.heappop(negated)
            remaining = one - two
            if remaining != 0:
                heapq.heappush(negated, remaining)
        revert = [-x for x in negated]
        if revert:
            return revert[0]
        else:
            return 0