class DataStream:

    def __init__(self, value: int, k: int):
        self.value = value
        self.k = k
        self.stack = 0

    def consec(self, num: int) -> bool:
        if num != self.value:
            self.stack = 0
            return False
        self.stack += 1
        return self.stack >= self.k
        


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)