

# 1
# 1 2
# 2 1

# 2 1 3

# 3 2 1

# d1 = 3 2 1
# d2 = 4

# d2 = 4 3 2 1




class MyStack:
    def __init__(self):
        self.d1 = deque()
        # self.d2 = deque()

    
    def push(self,x):
        self.d2 = deque([x])
        while self.d1:
            self.d2.append(self.d1.popleft())
        self.d1 = self.d2
    
    def pop(self):
        return self.d1.popleft()
    
    def top(self):
        return self.d1[0]
    
    def empty(self):
        return not bool(self.d1)

