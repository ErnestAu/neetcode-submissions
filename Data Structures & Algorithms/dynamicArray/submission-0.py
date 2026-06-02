class DynamicArray:
    def __init__(self, capacity: int):
        self.arr = [0] * capacity
        self.size = 0
        self.capacity = capacity
    
    def get(self, i):
        return self.arr[i]
    
    def set(self, i, n):
        # if self.size == self.capacity:
        #     self.resize()
        # for j in range(self.size, i, -1):
        #     self.arr[j] = self.arr[j-1]
        if i >= self.size:
            self.size += 1
        self.arr[i] = n
        
    
    def pushback(self, n):
        if self.size == self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1
    
    def popback(self):

        self.size -= 1
        return(self.arr[self.size])
    
    def resize(self):
        self.capacity *= 2
        newarr = [0] * self.capacity
        newarr[:self.size] = self.arr[:self.size]
        self.arr = newarr
    
    def getSize(self):
        return self.size
    
    def getCapacity(self):
        return self.capacity