# push to back (append())
# peep from front (arr[0])
# size (len())
# is empty (isEmpty)

class MyStack:

    def __init__(self):
        self.q = deque()
    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft()

    def top(self) -> int:
        return self.q[0]


    def empty(self) -> bool:
        return len(self.q) == 0



# class MyStack:

#     def __init__(self):
#         self.q = deque()
#         self.r = deque()
#         self.size = 0        
#     def push(self, x: int) -> None:
#         self.q.append(x)
#         self.size += 1

#     def pop(self) -> int:
#         for _ in range(self.size-1):
#             self.r.append(self.q.popleft())

#         val = self.q.popleft()
#         self.q = self.r
#         self.size -= 1
#         return val

#     def top(self) -> int:
#         for _ in range(self.size-1):
#             self.r.append(self.q.popleft())

#         val = self.q[0]
#         self.r.append(self.q.popleft())
#         self.q = self.r
#         return val


#     def empty(self) -> bool:
#         return self.size == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()