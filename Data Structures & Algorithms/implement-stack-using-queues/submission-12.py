



# 1
# 2 1
# 3 2 1
# 4 3 2 1


class MyStack:
    def __init__(self):
        self.deque = []

    
    def push(self,x):
        self.deque = deque([x,self.deque])

    def pop(self):
        res = self.deque.popleft()
        self.deque = self.deque.popleft()
        return res

    def top(self):
        return self.deque[0]
    
    def empty(self):
        return not bool(self.deque)