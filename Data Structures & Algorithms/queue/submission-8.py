class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self):
        return self.head.next.val == -1
    
    def append(self, value):
        newTail = Node(value)
        oldTail = self.tail.prev
        
        newTail.prev, newTail.next = oldTail, self.tail
        oldTail.next = newTail
        self.tail.prev = newTail


    def appendleft(self, val):
        newHead = Node(val)
        oldHead = self.head.next

        newHead.prev, newHead.next = self.head, oldHead
        self.head.next = newHead
        oldHead.prev = newHead


    def pop(self):
        if self.head.next.val == -1:
            return -1
        
        oldTailVal = self.tail.prev.val
        newTail = self.tail.prev.prev
        
        newTail.next = self.tail
        self.tail.prev = newTail

        return oldTailVal

    def popleft(self):
        if self.head.next.val == -1:
            return -1
        
        oldHeadVal = self.head.next.val
        newHead = self.head.next.next
        self.head.next = newHead
        newHead.prev = self.head

        return oldHeadVal

# class dequeNode:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#         self.prev = None

# class Deque:
#     def __init__(self):
#         self.first = dequeNode(0)
#         self.last = None

#     def isEmpty(self):
#         return not self.first.next
    
#     def append(self, value):
#         newLast = dequeNode(value)
#         if self.first.next:
            
#             newLast.prev = self.first
#             self.first.next = newLast
            
#         else:
            
#             self.last = newLast
#             newLast.prev = self.last
            
#         self.last = newLast

#     def appendleft(self, val):
#         newFirst = dequeNode(val)

#         newFirst.prev, newFirst.next = self.first, self.first.next
#         self.first.next.prev = newFirst
#         self.first.next = newFirst


#         # self.first.next, newFirst.next = newFirst, self.first.next

#     def pop(self):
#         if not self.first.next:
#             return -1
        
#         lastval = self.last.val
#         self.last = self.last.prev
#         return lastval
    
#     def popleft(self):
#         if not self.first.next:
#             return -1
#         oldFirstVal = self.first.next.val
#         newFirst = self.first.next.next
#         self.first.next, newFirst.prev = newFirst, self.first
#         return oldFirstVal
