class MinHeap:
    def __init__(self):
        self.heap = [0]

    def push(self, val):
        self.heap.append(val)
        self._bubble_up(len(self.heap)-1)
    
    def pop(self):
        if len(self.heap) == 1:
            return -1
        
        if len(self.heap) == 2:
            return self.heap.pop()
        
        val = self.heap[1]
        self.heap[1] = self.heap.pop()
        self._bubble_down(1)
        return val
    
    def top(self):
        if len(self.heap) == 1:
            return -1
        
        return self.heap[1]
    
    def heapify(self, nums):
        self.heap = [0] + nums
        for i in range((len(self.heap)-1)//2 , 0, -1):
            self._bubble_down(i)

    def _bubble_up(self, index):
        child = index
        parent = child//2

        while parent > 0:
            if self.heap[child] < self.heap[parent]:
                self.heap[child], self.heap[parent] = self.heap[parent], self.heap[child]
                child = parent
                parent = child//2
            else:
                return

    def _bubble_down(self, index):
        parent = index

        while parent * 2 < len(self.heap):
            leftChild = parent * 2
            rightChild = parent * 2 + 1

            # find the smallest child
            smallest = leftChild
            if rightChild < len(self.heap) and self.heap[rightChild] < self.heap[leftChild]:
                smallest = rightChild

            # swap if needed, otherwise we're done
            if self.heap[smallest] < self.heap[parent]:
                self.heap[parent], self.heap[smallest] = self.heap[smallest], self.heap[parent]
                parent = smallest
            else:
                return
    # def _bubble_down(self, index):
        
    #     parent = index
    #     leftChild = parent * 2
    #     rightChild = parent * 2 + 1


    #     while leftChild < len(self.heap):
            

    #         smallest = leftChild
    #         if rightChild < len(self.heap) and self.heap[rightChild] < self.heap[leftChild]:
    #             smallest = rightChild
                

    #         if self.heap[smallest] < self.heap[parent]:
    #             self.heap[smallest], self.heap[parent] = self.heap[parent], self.heap[smallest]
    #             parent = smallest
    #         else:
    #             return
    #         leftChild = parent * 2
    #         rightChild = parent * 2 + 1


        
    #     # while leftChild < len(self.heap):
    #     #     if rightChild < len(self.heap) and self.heap[rightChild] < self.heap[leftChild]:
    #     #         self.heap[parent], self.heap[rightChild] = self.heap[rightChild], self.heap[parent]
    #     #         parent = rightChild

    #     #     elif self.heap[leftChild] < self.heap[parent]:
    #     #         self.heap[parent], self.heap[leftChild] = self.heap[leftChild], self.heap[parent]
    #     #         parent = leftChild
    #     #     else:
    #     #         return

    #     #     leftChild = parent * 2
    #     #     rightChild = parent * 2 + 1


