# Design Front Middle Back Queue
from collections import  deque
class FrontMiddleBackQueue:
    
    def __init__(self):
        self.q = deque()

    def pushFront(self, val: int) -> None:
        self.q.appendleft(val)

    def pushMiddle(self, val: int) -> None:
        n = len(self.q)
        m = n // 2
        self.q.insert(m,val)

    def pushBack(self, val: int) -> None:
        self.q.append(val)

    def popFront(self) -> int:
        if len(self.q):
            return self.q.popleft()
        return -1

    def popMiddle(self) -> int:
        n=len(self.q)
        middle=n//2
        if n:
            if (n%2==0):
                self.q.rotate(-(middle-1)) # right to left rotation
                b=self.q.popleft() 
                self.q.rotate(-(n-(middle-1)-1)) # right to left rotation
            else:
                self.q.rotate(-(middle)) # right to left rotation
                b=self.q.popleft()
                self.q.rotate(-(n-middle-1)) # right to left rotation
            return b
        return -1
    def popBack(self) -> int:
        if len(self.q):
            return self.q.pop()
        return -1