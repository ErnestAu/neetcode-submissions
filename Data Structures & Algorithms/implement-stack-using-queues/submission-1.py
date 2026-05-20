# append (add to back), 
# popleft (remove from front), 
# peek/front (view front element without removing), and 
# isEmpty


class MyStack:

    def __init__(self):
        self.q = deque()
        self.r = deque()
        
    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        self.r = deque()
        for i in range(len(self.q)-1):
            self.r.append(self.q[0])
            self.q.popleft()
        final = self.q[0]
        self.q = self.r
        return final

    def top(self) -> int:
        self.r = deque()
        for i in range(len(self.q)):
            final = self.q[0]
            self.r.append(self.q[0])
            self.q.popleft()
        self.q = self.r
        return final


    def empty(self) -> bool:
        return not self.q


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()