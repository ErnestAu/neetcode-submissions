class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def isEmpty(self):
        return self.head.next == self.tail
    
    def append(self, value):
        newtail = Node(value)
        oldtail = self.tail.prev

        newtail.prev, newtail.next = oldtail, self.tail
        oldtail.next = self.tail.prev = newtail

    def appendleft(self, value):
        newhead = Node(value)
        oldhead = self.head.next

        newhead.prev, newhead.next = self.head, oldhead
        self.head.next = oldhead.prev = newhead

    def pop(self):
        if self.isEmpty():
            return -1
        
        oldtail = self.tail.prev
        newtail = self.tail.prev.prev

        newtail.next = self.tail
        self.tail.prev = newtail

        return oldtail.val

    def popleft(self):
        if self.isEmpty():
            return -1
        
        oldhead = self.head.next
        newhead = self.head.next.next

        self.head.next = newhead
        newhead.prev = self.head

        return oldhead.val
