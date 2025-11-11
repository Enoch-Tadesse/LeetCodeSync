class DataStream:

    def __init__(self, value: int, k: int):
        self.counter = 0
        self.last = value
        self.k = k

    def consec(self, num: int) -> bool:
        if self.last != num:
            self.counter = 0
            return False
        self.counter += 1
        return self.counter >= self.k


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)