class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)

        heap = []

        for key, value in cnt.items():
            
            

            if len(heap) < k:
                heapq.heappush(heap, [value, key])

            elif value > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, [value, key])
        
        return [i[1] for i in heap]

        