import math
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        for point in points:
            distance = (point[0]**2 + point[1]**2)**(1/2)

            heapq.heappush(maxHeap, [-distance, point])

            
            
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)

        return [x[1] for x in maxHeap]

