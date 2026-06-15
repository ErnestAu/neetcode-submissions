






class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = [0] * 26
        for task in tasks:
            count[ord(task) - ord('A')] += 1
        
        neg = [-x for x in count]


        heapq.heapify(neg)
        
        result = 0
        i = 0
        neg2 = []
        # while neg[0] != 0:
        while neg and neg[0] != 0:
            while neg and neg[0] != 0 and i <= n:
                heapq.heappush(neg2, heapq.heappop(neg)+1)
                result += 1
                i += 1
            while neg and neg[0] != 0:
                heapq.heappush(neg2, heapq.heappop(neg))
            while i <= n and neg2[0]!=0:
                result += 1
                i += 1
            
            
            i = 0
            neg = neg2
            neg2 = []
        return result
        # return neg

        
        # if neg[0] != 0:
        #     while neg:
        #         heapq.heappush(neg2, heapq.heappop(neg)+1)
        #         result += 1
        #         i += 1
        #     while i < n:
        #         result += 1
        #         i += 1
        #     i = 0
        #     neg = neg2
        #     neg2 = []
        # return result

        # return result

        # c = Counter(tasks)
        # sorted_items = sorted(c.items(), key=lambda x: x[1], reverse=True)
        # sorted_list = []
        # for key,value in sorted_items:
        #     for _ in range(value):
        #         sorted_list.append(key)
        
        # l = 0
        # r = len(sorted_list) - 1
        # result = 0
        # while l < r:
            

        
        # return cnt

        # cnt = Counter()

        # highest = max(counter, key=counter.get)

        # cntlist = list(cnt.items())

        # i = 0

        # while i < len(items):
        #     key, value = items[i]
        #     print(f"{key}: {value}")
        #     i += 1

        # seq = ""

        # # for key, value in cnt.items():

        # for i in range(cnt[highest]):
        #     seq + highest
        #     for _ in range(n):
        #         while cnt[i][0]
                
        #             seq + 


