






class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        negcnt = [0] * 27
        for task in tasks:
            negcnt[ord(task)-ord("A")] -= 1
        
        heapq.heapify(negcnt)

        time = 0

        queue = deque() 

        while negcnt[0] != 0 or queue:
            if queue:
                if queue[0][1] == time:
                    heapq.heappush(negcnt, queue.popleft()[0])
            
            if negcnt[0] != 0:
                val = heapq.heappop(negcnt) + 1
                if val != 0:
                    queue.append([val, time + n + 1])

            time += 1
        
        return time


