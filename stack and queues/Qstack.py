## Implement Queue using Stacks

"""
Push : Use two stacks S1 and S2. Push element to S1, pop from S1 and add to S2.
Now pop from S2 and add to S1.
Pop : Pop from S1.
Top : Rightmost element
Empty : len != 0

"""
class MyQueue:
    
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        while self.s1:
            a = self.s1.pop()
            self.s2.append(a)
            
        self.s1.append(x)
        
        while self.s2:
            b = self.s2.pop()
            self.s1.append(b)

    def pop(self) -> int:
        return self.s1.pop()

    def peek(self) -> int:
        return self.s1[-1]

    def empty(self) -> bool:
        return not self.s1