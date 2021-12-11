#  Implement Stack using Queues
"""
Stack : 1 -> 2 -> 3
Queue : 1 -> 2 -> 3
push : add to right O(1)
pop : s -> right ; q -> left O(N)
Remove the element from left,add it to right again and pop it 
Top : Rightmost element
Empty : len != 0

"""
from collections import deque
class MyStack:
    
    def __init__(self):
        self.q = deque()
        
    def push(self, x: int) -> None:
        self.q.append(x)

    def pop(self) -> int:
        for i in range(len(self.q)-1):
            self.push(self.q.popleft())
        return self.q.popleft()
    
    def top(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return len(self.q) == 0 
