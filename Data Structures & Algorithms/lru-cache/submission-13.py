# linked list
# [1,10] > [2,20] > [3,30]
# need to take from anywhere at O(1) (hash)
# [2,20] > [3,30] > [1,10]



class Node:
    def __init__(self, val):
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.cache = {}

        # create 2 dummy nodes as the head and tail
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next, self.tail.prev = self.tail, self.head

        self.capacity = capacity 
    def get(self, key):
        if key not in self.cache:
            return -1
        self.remove(key)
        self.add(key)
        return self.cache[key].val[1]
    
    def put(self, key, value):
        if key in self.cache:
            self.remove(key)
        self.cache[key] = Node([key,value])
        self.add(key)
        if len(self.cache)>self.capacity:
            
            lru = self.head.next
            self.remove(lru.val[0])
            self.cache.pop(lru.val[0])
            


    def remove(self, key):
        curr = self.cache[key]
        left=curr.prev 
        right = curr.next
        left.next, right.prev = right, left

    def add(self, key):
        curr = self.cache[key]
        left = self.tail.prev
        right = self.tail
        left.next, right.prev = curr, curr
        curr.prev, curr.next = left, right
        