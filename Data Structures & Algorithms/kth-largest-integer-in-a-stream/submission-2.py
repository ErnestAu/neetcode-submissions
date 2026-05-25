# question
# neetcode says the first index is 1, so the math works out
# but in the code you have [0]?

from heapq import heapify, heappop, heappush

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums, self.k = nums, k 
        heapify(self.nums)

        while len(self.nums) > k:
            heappop(self.nums)


    def add(self, val: int) -> int:
        heappush(self.nums, val)
        while len(self.nums) > self.k:
            heappop(self.nums)

        return self.nums[0]









 