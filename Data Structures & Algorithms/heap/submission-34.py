class MinHeap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap)-1)

    def pop(self):
        if len(self.heap) <= 1:
            return -1
        if len(self.heap) == 2:
            return self.heap.pop()
        
        val = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._bubble_down(1)

        return val
    
    def top(self):
        if len(self.heap) < 2:
            return -1
        else:
            return self.heap[1]
    
    def heapify(self, nums):
        self.heap = [0] + nums
        for i in reversed(range(1,len(self.heap)//2)):
            self._bubble_down(i)


    def _bubble_up(self, index) -> None:
        parent = index // 2

        while index > 1 and self.heap[parent] > self.heap[index]:
            self.heap[parent], self.heap[index] = self.heap[index], self.heap[parent]
            index = parent
            parent = index // 2
    
    def _bubble_down(self, index):
        child = 2 * index
        while child < len(self.heap):
            if child + 1 < len(self.heap) and self.heap[child] > self.heap[child + 1]:
                child += 1
            
            if self.heap[child] >= self.heap[index]:
                break
            
            self.heap[child] , self.heap[index] = self.heap[index], self.heap[child]
            index = child
            child = index * 2

# class MinHeap:
    
#     def __init__(self):
#         self.heap = [-1]
#         self.size = 0

#     def push(self, val: int) -> None:
        
#         self.heap.append(val)
#         self.size += 1
#         child = self.size 
#         parent = self.size//2

#         while parent > 0:
            
#             if self.heap[parent] > self.heap[child]:
#                 self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
#                 child = parent
#                 parent = child // 2
#             else:
#                 return
            
        

#     def pop(self) -> int:
#         if not self.size > 0:
#             return -1
        
#         val = self.top()


#         parent = 1
#         leftChild = parent * 2
#         rightChild = parent * 2 + 1
        
#         self.heap[parent] = float('-inf')


#         while leftChild <= self.size:
#             if rightChild <= self.size:
#                 if self.heap[leftChild] < self.heap[rightChild]:
#                     self.heap[parent], self.heap[leftChild] = self.heap[leftChild], self.heap[parent]
#                     parent = leftChild
                    
#                 else:
#                     self.heap[parent], self.heap[rightChild] = self.heap[rightChild], self.heap[parent]
#                     parent = rightChild

#             else:
#                 self.heap[parent], self.heap[leftChild] = self.heap[leftChild], self.heap[parent]
#                 parent = leftChild
            
#             leftChild = parent * 2
#             rightChild = parent * 2 + 1
            

#         i = self.size
#         while self.heap[i] != float('-inf'):
#             i -= 1
#             if self.heap[i] == float('-inf'):
#                 self.heap[i], self.heap[self.size] = self.heap[self.size], self.heap[i]
                

        
#         self.size -= 1
        

#         return val

#     def top(self) -> int:
#         if self.size ==0:
#             return -1
#         else:
#             return self.heap[1]

#     def heapify(self, nums: List[int]) -> None:
#         MinHeap()
#         for num in nums:
#             self.push(num)
#         self.size = len(nums)
        