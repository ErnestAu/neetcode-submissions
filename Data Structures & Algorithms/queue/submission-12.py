class Node:
    def __init__(self,val):
        self.val = val
        self.prev = None
        self.next = None

class Deque:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next, self.tail.prev = self.tail, self.head

    def isEmpty(self):
        return self.head.next == self.tail

    def append(self, val):
        newTail = Node(val)
        oldTail = self.tail.prev

        self.tail.prev, oldTail.next = newTail, newTail
        newTail.prev, newTail.next = oldTail, self.tail

    def appendleft(self, val):
        newHead = Node(val)
        oldHead = self.head.next

        self.head.next, oldHead.prev = newHead, newHead
        newHead.prev, newHead.next = self.head, oldHead
    
    def pop(self):
        if self.isEmpty():
            return -1
        
        oldTail = self.tail.prev
        newTail = self.tail.prev.prev

        newTail.next, self.tail.prev = self.tail, newTail

        return oldTail.val
    
    def popleft(self):
        if self.isEmpty():
            return -1
        

        oldHead = self.head.next
        newHead = self.head.next.next

        self.head.next, newHead.prev = newHead, self.head

        return oldHead.val
