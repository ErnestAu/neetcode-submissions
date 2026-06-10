class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        cnt = Counter(nums)
        bucket = [[] for _ in range(len(nums) + 1)]

        for key, value in cnt.items():
            bucket[value].append(key)
        
        result = []
        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
                result.append(j)
                if len(result) >= k:
                    return result

        # return [i[0] for i in heapq.nlargest(k, Counter(nums).items(), lambda x: x[1])]

        # cnt = Counter(nums)
        # heap = []
        # for key, value in cnt.items():


        #     if len(heap) < k:
        #         heapq.heappush(heap, [value, key])

        #     elif value > heap[0][0]:
        #         heapq.heappop(heap)
        #         heapq.heappush(heap, [value, key])
        
        # return [i[1] for i in heap]

        