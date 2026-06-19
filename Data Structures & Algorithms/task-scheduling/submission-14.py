






class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        negcnt = [-cnt for cnt in count.values()]
        heapq.heapify(negcnt)

        time = 0
        queue = deque() 
        while negcnt or queue:
            if queue:
                if queue[0][1] == time:
                    heapq.heappush(negcnt, queue.popleft()[0])
            
            if negcnt:
                val = heapq.heappop(negcnt) + 1
                if val != 0:
                    queue.append([val, time + n + 1])

            time += 1
        
        return time


