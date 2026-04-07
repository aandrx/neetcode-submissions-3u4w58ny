class Node:
    # DLL 
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    #map and DLL 
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {} # map key to node

        # mapping
        self.left, self.right = Node(0, 0), Node(0, 0)
        self.left.next, self.right.prev = self.right ,self.left

    def remove(self, node):
        prev, next = node.prev, node.next
        prev.next, next.prev = next, prev
        
    def insert(self, node):
        prev, next = self.right.prev, self.right
        prev.next = next.prev = node
        node.next, node.prev = next, prev

    def get(self, key: int) -> int:
        # ret value of key if key 
        # else ret -1  
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        # update value of key if key 
        # else add pair to cache 
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        # if new pair causes cache to exceed capacity, remove least recently used key 
        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
