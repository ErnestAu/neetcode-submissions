class Node:
    def __init__(self, key, value):
        self.cache = [key, value]
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}

        self.left = self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    
    def insert(self, node):
        Prev = self.right.prev
        
        node.prev, node.next = Prev, self.right
        Prev.next = self.right.prev = node
        
    def remove(self, node):
        Prev = node.prev
        Nxt = node.next

        Prev.next = Nxt
        Nxt.prev = Prev
        


    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].cache[1]
        else:
            return -1
        
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        else:
            self.cache[key] = Node(key, value)
            self.insert(self.cache[key])
        
            if len(self.cache) > self.capacity:
                lru = self.left.next
                self.remove(lru)
                self.cache.pop(lru.cache[0])



