# only need kth largest

# this is a min heap

# heappop when i > heap[0]

from heapq import heappush, heappop

class KthLargest:
    # def __init__():

    def __init__(self, k, nums):
        self.heap = []
        self.k = k
        for num in nums:
            heappush(self.heap, num)
            if len(self.heap) > k:
                heappop(self.heap)


    def add(self, val):
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)

        return self.heap[0]