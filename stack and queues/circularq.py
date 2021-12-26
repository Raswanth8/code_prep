# Circular Queue
# Each operation -> O(N)

class MyCircularQueue:
    
    def __init__(self, k: int):
        self.k = k
        self.size = 0
        self.head = 0
        self.tail = 0
        self.q = [None]*k
        

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        self.q[self.tail] = value
        self.tail = (self.tail+1)%self.k # circular condition
        self.size +=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.size -= 1
        self.head = (self.head+1)%self.k # circular condition
        return True
    
    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.q[self.head]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.q[self.tail-1] # -1 is to point the last element

    def isEmpty(self) -> bool:
        if self.size == 0 :
            return True
        return False
        
    def isFull(self) -> bool:
        if self.size == self.k: 
            return True
        return False
