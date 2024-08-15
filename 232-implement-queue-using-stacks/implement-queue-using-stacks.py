class MyQueue:

    def __init__(self):
        self.q = []
        self.len = 0
        
    def push(self, x: int) -> None:
        self.len+=1
        return self.q.append(x)

    def pop(self) -> int:
        self.len-=1
        return self.q.pop(0)

    def peek(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return self.len == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()