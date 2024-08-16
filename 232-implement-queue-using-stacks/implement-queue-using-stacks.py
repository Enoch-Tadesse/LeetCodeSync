class MyQueue:

    def __init__(self):
        self.stack = []
        self.temp = []
        
    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        for _ in range(len(self.stack)):
            self.temp.append(self.stack.pop())
        result = self.temp.pop()
        for _ in range(len(self.temp)):
            self.stack.append(self.temp.pop())
        return result
    def peek(self) -> int:
        return self.stack[0]

    def empty(self) -> bool:
        print(self.stack, len(self.stack))
        return len(self.stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()