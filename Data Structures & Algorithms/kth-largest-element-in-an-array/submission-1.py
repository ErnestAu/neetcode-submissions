class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # maxheap
        # heappop k times
        negative = [-num for num in nums]
        heapq.heapify(negative)
        for _ in range(k):
            val = heapq.heappop(negative)
        return -val