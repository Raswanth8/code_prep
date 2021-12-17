# LRU Cache 
# O(1) for each operation
# Doubly Linked List Implementation
"""
MRU [1,1] -> <-[2,2] LRU

"""
class Node :
    def __init__(self,key,val):
        self.key,self.val = key,val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {} #Hashmap to hold values
        
        # LRU - left ; MRU - right
        self.left,self.right = Node(0,0),Node(0,0)
        self.left.next,self.right.prev = self.right,self.left
        
    def remove(self,node):
        # Remove from list
        prev,nxt = node.prev,node.next
        prev.next,nxt.prev = nxt,prev
        
    def insert(self,node):
        # Insert to the left
        prev,nxt = self.right.prev, self.right
        prev.next = nxt.prev = node
        node.prev,node.next = prev,nxt

    def get(self, key: int) -> int:
        if key in self.cache :
            # Swap it as it will be MRU
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache :
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        
        if(len(self.cache)> self.cap):
            # Finding LRU and removing it when exceeds capacity
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
            
# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)