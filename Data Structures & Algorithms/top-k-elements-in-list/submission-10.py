# class Solution:
#     def topKFrequent(self, nums: List[int], k: int) -> List[int]:
#         hashMap = Counter(nums)
#         topKvalue = []
#         topKmap = {}
#         smallest = 0
#         for key, value in hashMap.items():
                


#             if len(topKvalue) >= k and value < smallest:
#                 continue

#             if len(topKvalue) >= k and value > smallest: 
#                 # come back to value > smallest if necessary
#                 heapq.heappop(topKvalue)
#                 # topKmap.pop(removed)

#             heapq.heappush(topKvalue, value)
#             smallest = topKvalue[0]
#             # topKmap[value] = key

        
#         return [topKmap[i] for i in topKmap]



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        heap = []
        
        for num, freq in count.items():
            heapq.heappush(heap, (freq, num))
            if len(heap) > k:
                heapq.heappop(heap)   # remove least frequent
        
        return [num for freq, num in heap]

    