class MyQueue:

    def __init__(self):
        self.stack = []
        self.rev = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        if self.rev:
            return self.rev.pop()
        for _ in range(len(self.stack)):
            self.rev.append(self.stack.pop())
        return self.rev.pop()
        
    def peek(self) -> int:
        if self.rev:
            return self.rev[-1]
        return self.stack[0]

    def empty(self) -> bool:
        return len(self.stack) == 0 and len(self.rev) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()